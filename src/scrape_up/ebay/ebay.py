from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class EBAY:
    """
    Create an instance of EBAY class
    ```python
    quora = EBAY()
    ```
    | Methods             | Details                             |
    | ------------------- | ----------------------------------- |
    | `.spotlights()`     | Returns spotlight deals on EBAY.    |
    | `.featured()`       | Returns the featured deals on EBAY. |
    | `.specific_deals()` | Returns the specific deals on EBAY. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        url = "https://www.ebay.com/globaldeals"
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)
        html_text = get(url, self.config).text
        soup = BeautifulSoup(html_text, "lxml")

        self.container = soup.find("div", {"class": "sections-container"})

    def spotlights(self):
        """
        Get the spotlight deal information.
        Example:
        ```python
        ebay = EBAY()
        spotlight_data = EBAY.spotlights()
        ```
        Returns:
        ```js
        {
            "Description":"Spotlight Deal",
            "Product":"Apple iPhone 12 Pro 128GB Unlocked Smartphone - Very Good",
            "Price":"US $524.95",
            "Link":"https://www.ebay.com/itm/363490711983?_trkparms=5373%3A0%7C5374%3AFeatured"
        }
        ```
        """
        try:
            spotlight_deal = self.container.find(
                "div",
                {
                    "class": "ebayui-dne-summary-card card ebayui-dne-item-featured-card--topDeals"
                },
            ).find("div", {"class": "dne-itemtile-detail"})
            title = spotlight_deal.find("h3").text
            price = spotlight_deal.find("span", {"class": "first"}).text
            url = spotlight_deal.find("a", href=True)
            spotlight = {
                "Description": "Spotlight Deal",
                "Product": title,
                "Price": price,
                "Link": url["href"],
            }
            return spotlight
        except:
            return None

    def featured(self):
        """
        Get the featured deals information.
        Example:
        ```python
        ebay = eBay()
        featured_data = ebay.featured()
        ```
        Returns:
        ```
        [
            {
                "Product":"Intel Core i5-13600KF Unlocked Desktop Processor - 14 Cores (6P+8E) & 20 Threads",
                "Price":"US $313.41",
                "Link":"https://www.ebay.com/itm/295247209215?_trkparms=5373%3A0%7C5374%3AFeatured"
            }
            ...
        ]
        ```
        """
        try:
            featured_deal = self.container.find(
                "div", {"class": "ebayui-dne-banner-text"}
            ).next_sibling
            Featured_deal = []
            for cols in featured_deal.find_all("div", {"class", "col"}):
                cols = cols.find("div", {"class": "dne-itemtile-detail"})
                title = cols.find("h3").text
                url = cols.find("a", href=True)["href"]
                price = cols.find("span", {"class": "first"}).text
                featured = {"Product": title, "Price": price, "Link": url}
                Featured_deal.append(featured)
            return Featured_deal
        except:
            return None

    def specific_deals(self):
        """
        Get the specific deals information.
        Example:
        ```python
        ebay = EBAY()
        specific_deals_data = EBAY.specific_deals()
        ```

        Returns:
        ```js
        [
            {
                "Product":"STRAY KIDS MAXIDENT Album GO LIMITED Ver. CD+P.Book+Poster+2 Card+Pre-Order+GIFT",
                "Price":"US $32.50",
                "Link":"https://www.ebay.com/itm/165661661490?_trkparms=5373%3A0%7C5374%3AFeatured%7C5079%3A6000012162"
            }
            ...
        ]
        ``
        """
        try:
            for items in self.container.find_all(
                "div",
                {
                    "class": "ebayui-dne-item-pattern-card ebayui-dne-item-pattern-card-no-padding ebayui-dne-item-pattern-card--desktop"
                },
            ):
                specific = []
                i = 0
                for cols in items.find("div", {"class": "row"}).find_all(
                    "div", {"class": "col"}
                ):
                    for item in cols.find_all("div", {"class": "item"}):
                        if i == 4:
                            break
                        i += 1
                        title = item.find("h3").text
                        price = item.find("span", {"class": "first"}).text
                        url = item.find("a", href=True)["href"]
                        deal = {"Product": title, "Price": price, "Link": url}
                        specific.append(deal)
            return specific
        except:
            return None
