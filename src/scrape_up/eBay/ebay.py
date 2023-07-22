from bs4 import BeautifulSoup
import requests

class eBay:
    def __init__(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"}
        url = "https://www.ebay.com/globaldeals"
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, "lxml")

        self.container = soup.find("div", {"class": "sections-container"})

    def spotlights(self):
        """
        Get the spotlight deal information.

        Example:
        ```python
        ebay = eBay()
        spotlight_data = ebay.spotlights()
        print(spotlight_data)
        ```

        Returns:
        A dictionary containing the spotlight deal information.
        """
        try:
            deals = []
            spotlight_deal = self.container.find("div", {"class": "ebayui-dne-summary-card card ebayui-dne-item-featured-card--topDeals"}).find("div", {"class": "dne-itemtile-detail"})
            title = spotlight_deal.find("h3").text
            price = spotlight_deal.find("span", {"class": "first"}).text
            url = spotlight_deal.find("a", href=True)
            spotlight = {
                "Description": "Spotlight Deal",
                "Product": title,
                "Price": price,
                "Link": url['href']
            }
            deals.append(spotlight)
            return {"data": deals, "message": "Information is now fetched"}
        except:
            return "Unable to fetch data"

    def featured(self):
        """
        Get the featured deals information.

        Example:
        ```python
        ebay = eBay()
        featured_data = ebay.featured()
        print(featured_data)
        ```

        Returns:
        A dictionary containing the featured deals information.
        """
        try:
            deals = []
            featured_deal = self.container.find("div", {"class": "ebayui-dne-banner-text"}).next_sibling
            Featured_deal = []
            for cols in featured_deal.find_all("div", {"class", "col"}):
                cols = cols.find("div", {"class": "dne-itemtile-detail"})
                title = cols.find("h3").text
                url = cols.find("a", href=True)['href']
                price = cols.find("span", {"class": "first"}).text
                featured = {
                    "Product": title,
                    "Price": price,
                    "Link": url
                }
                Featured_deal.append(featured)
            deals.append({"Featured_deal": Featured_deal})
            return {"data": deals, "message": "Information is now fetched"}
        except:
            return "Unable to fetch data"

    def specific_deals(self):
        """
        Get the specific deals information.

        Example:
        ```python
        ebay = eBay()
        specific_deals_data = ebay.specific_deals()
        print(specific_deals_data)
        ```

        Returns:
        A dictionary containing the specific deals information.
        """
        try:
            deals = []
            for items in self.container.find_all("div", {"class": "ebayui-dne-item-pattern-card ebayui-dne-item-pattern-card-no-padding ebayui-dne-item-pattern-card--desktop"}):
                description = items.find("h2").text
                specific = []
                i = 0
                for cols in items.find("div", {"class": "row"}).find_all("div", {"class": "col"}):
                    for item in cols.find_all("div", {"class": "item"}):
                        if i == 4:
                            break
                        i += 1
                        title = item.find("h3").text
                        price = item.find("span", {"class": "first"}).text
                        url = item.find("a", href=True)['href']
                        deal = {
                            "Product": title,
                            "Price": price,
                            "Link": url
                        }
                        specific.append(deal)
                deals.append({description: specific})
            return {"data": deals, "message": "Information is now fetched"}
        except:
            return "Unable to fetch data"


