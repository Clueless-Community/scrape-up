# Amazon Scraper
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from genricHtmlib import SeleniumScraper
from lxml import html
import re
import requests
import pandas as pd

SeleniumScraper = SeleniumScraper()

class AmazonScraper:
    def __init__(self, product_category=str, number_of_threads=1, use_selenium=False, storage_format="csv", max_page=False):
        self.stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
        self.product_category = product_category
        self.number_of_threads = number_of_threads
        self.use_selenium = use_selenium
        self.storage_format = storage_format
        self.max_page = max_page
        self.df_list = []
        self.storagePath = os.getcwd()

        self.url = "https://www.amazon.in/s?k={}&page={}&ref=sr_pg_{}"
        self.website = "https://www.amazon.in"
        self.productUrlXpath = '//*[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]//@href'
        self.paginationXpath = '//*[@class="a-section a-spacing-small a-spacing-top-small"]//span[1]//text()'
        self.pagination = 1

    def getProducts(self, keyword, page):
        try:
            url = self.url.format(keyword, page, page)

            response = SeleniumScraper.fetch_request_normal(url)

            if response == None and self.use_selenium == True:
                print("Normal request failed, trying selenium")
                doc = SeleniumScraper.fetch_request_selenium(url)
            else:
                doc = html.fromstring(response)

            productUrls = SeleniumScraper.get_xpath_link(doc, self.productUrlXpath, self.website)
            print(f"Found {len(productUrls)} products for product {keyword} on page {page}")

            pagination = SeleniumScraper.get_xpath_link(doc, self.paginationXpath, self.website)

            pagination = re.findall(r'\d+', pagination[0])
            self.pagination = int(pagination[1])

            if self.max_page == False:
                self.pagination = 1

            return productUrls

        except Exception as e:
            print(f"maybe blocked by amazon try use_selenium=True")
            return []        

    def getProductDetails(self, productUrl): 
        print(f"Scraping product {productUrl}")

        if self.use_selenium == False:
            try:
                response = SeleniumScraper.fetch_request_normal(productUrl)
                doc = html.fromstring(response)

            except Exception as e:
                print(f"Error while scraping product try Selenium)")
                return

        try:
            if self.use_selenium == True:
                doc = SeleniumScraper.fetch_request_selenium(productUrl)
            
        except Exception as e:
            print(e)
            return

        productDetails = {}

        try:
            sku = productUrl.split("dp%2F")[1].split("%2F")[0]
        except:
            try:
                sku = productUrl.split("dp/")[1].split("/")[0]
            except:
                sku = []
            
        
        name = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@id="productTitle"]//text()'))    
        
        try:
            description = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@id="productDescription"]//span//text()'))
            description = " ".join(description)
        except Exception as e:
            try:
                description = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@id="feature-bullets"]//span//text()'))
                description = " ".join(description)
            except:
                print(f"Error while scraping product description for product {productUrl}: {e}")

        try:
            image_path = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@id="landingImage"]//@src'))
            image_path = image_path[0]
        except Exception as e:
            try:
                image_path = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@id="imgTagWrapperId"]//@src'))
                image_path = ''.join(image_path)
            except:
                print(f"Error while scraping product image for product {productUrl}: {e}")

        category = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@class="a-link-normal a-color-tertiary"]//text()'))
        try:
            category = category[-1]
        except Exception as e:
            category = []
            print(f"Error while scraping product category for product {productUrl}: {e}")

        try:
            price = SeleniumScraper.cleanData(SeleniumScraper.get_xpath_data(doc, '//*[@class="a-price-whole"]//text()'))[0]
            price = price.replace(",", "")
            price = int(price)
        except Exception as e:
            print(f"Error while scraping product price for product {productUrl}: {e}")
            price = []

        if price == []:
            price = "None"

        if description == []:
            description = "None"
        
        if image_path == []:
            image_path = "None"
        
        if category == []:
            category = "None"
        
        if name == []:
            name = "None"
        
        if sku == []:
            sku = "None"

        if category == []:
            category = "None"


        productDetails["sku"] = str(sku)
        productDetails["name"] = str(name[0])
        productDetails["description"] = str(description)
        productDetails["image_path"] = str(image_path)
        productDetails["category"] = str(category)
        productDetails["timestamp"] = str(self.stamp)
        productDetails["URL"] = str(productUrl)
        productDetails['price'] = price

        df = pd.DataFrame.from_dict(productDetails, orient='index').T
        self.df_list.append(df)        
        return productDetails

    def main(self):
        keyword = self.product_category

        # get products
        products = []
        for page in range(1, self.pagination+1):
            products.extend(self.getProducts(keyword, page))


        if self.pagination > 1:
            for page in range(2, self.pagination+1):
                products.extend(self.getProducts(keyword, page))


        # get product details
        with ThreadPoolExecutor(max_workers=self.number_of_threads) as executor:
            results = executor.map(self.getProductDetails, products)

            # save to db
            for result in results:
                print(f"Saving product id {result['sku']} to {self.storage_format}")
        
                SeleniumScraper.data_storage(df_list=self.df_list, unique_id='sku', name='amazon', storageFormat=self.storage_format)
