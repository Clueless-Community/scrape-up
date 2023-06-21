"""This script serves as an example on how to use Python 
   & Playwright to scrape/extract data from Google Maps"""
   
from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse


@dataclass
class Business:
    """holds business data
    """
    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None
    reviews_count: int = None
    reviews_average: float = None

@dataclass
class BusinessList:
    """holds list of Business objects, 
       and save to both excel and csv
    """
    business_list : list[Business] = field(default_factory=list)
    
    def dataframe(self):
        """transform business_list to pandas dataframe 

        Returns: pandas dataframe
        """
        return pd.json_normalize((asdict(business) for business in self.business_list), sep="_")
    
    def save_to_excel(self, filename):
        """saves pandas dataframe to excel (xlsx) file

        Args:
            filename (str): filename
        """   
        self.dataframe().to_excel(f'{filename}.xlsx', index=False)
    
    def save_to_csv(self, filename):
        """saves pandas dataframe to csv file

        Args:
            filename (str): filename
        """
        self.dataframe().to_csv(f'{filename}.csv', index=False)


def main():
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://www.google.com/maps', timeout=60000)
        # wait is added for dev phase. can remove it in production
        page.wait_for_timeout(5000)
        
        page.locator('//input[@id="searchboxinput"]').fill(search_for)
        page.wait_for_timeout(3000)
        
        page.keyboard.press('Enter')
        page.wait_for_timeout(5000)
        
        # scrolling 
        page.hover('(//div[@role="article"])[1]')

        # this variable is used to detect if the bot
        # scraped the same number of listings in the previous iteration
        previously_counted = 0
        while True:
            page.mouse.wheel(0, 10000)
            page.wait_for_timeout(3000)
            
            if page.locator('//div[@role="article"]').count() >= total:
                listings = page.locator('//div[@role="article"]').all()[:total]
                print(f'Total Scraped: {len(listings)}')
                break
            else:
                # logic to break from loop to not run infinitely 
                # in case arrived at all available listings
                if page.locator('//div[@role="article"]').count() == previously_counted:
                    listings = page.locator('//div[@role="article"]').all()
                    print(f'Arrived at all available\nTotal Scraped: {len(listings)}')
                    break
                else:
                    previously_counted = page.locator('//div[@role="article"]').count()
                    print(f'Currently Scraped: ', page.locator('//div[@role="article"]').count())
        
        business_list = BusinessList()
        
        # scraping
        for listing in listings:
        
            listing.click()
            page.wait_for_timeout(5000)
            
            name_xpath = '//h1[contains(@class, "fontHeadlineLarge")]'
            address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
            website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
            phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
            reviews_span_xpath = '//span[@role="img"]'
            
            business = Business()
            
            if page.locator(name_xpath).count() > 0:
                business.name = page.locator(name_xpath).inner_text()
            else:
                business.name = ''
            if page.locator(address_xpath).count() > 0:
                business.address = page.locator(address_xpath).inner_text()
            else:
                business.address = ''
            if page.locator(website_xpath).count() > 0:
                business.website = page.locator(website_xpath).inner_text()
            else:
                business.website = ''
            if page.locator(phone_number_xpath).count() > 0:
                business.phone_number = page.locator(phone_number_xpath).inner_text()
            else:
                business.phone_number = ''
            if listing.locator(reviews_span_xpath).count() > 0:
                business.reviews_average = float(listing.locator(reviews_span_xpath).get_attribute('aria-label').split()[0].replace(',','.').strip())
                business.reviews_count = int(listing.locator(reviews_span_xpath).get_attribute('aria-label').split()[2].strip())
            else:
                business.reviews_average = ''
                business.reviews_count = ''
                
            business_list.business_list.append(business)
        
        # saving to both excel and csv just to showcase the features.
        business_list.save_to_excel('google_maps_data')
        business_list.save_to_csv('google_maps_data')
        
        browser.close()
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str)
    parser.add_argument("-t", "--total", type=int)
    args = parser.parse_args()
    
    if args.search:
        search_for = args.search
    else:
        # in case no arguments passed
        # the scraper will search by defaukt for:
        search_for = 'dentist new york'
    
    # total number of products to scrape. Default is 10
    if args.total:
        total = args.total
    else:
        total = 10
        
    main()