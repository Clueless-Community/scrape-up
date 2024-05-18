from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class SilverPrice:
    """
    Create an instance of `SilverPrice` class
    ```python
    silverprice = SilverPrice()
    ```

    | Methods            | Details                                                             |
    | -------------------|---------------------------------------------------------------------|
    | `.citywise_price()`| Returns the price of  silver citywise in rupees                     |
    | `.last_10_days()`  | Returns the price of 10 grams silver for the last 10 days in rupees |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/news/silver-rates-today/"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def citywise_price(self):
        """
        Create an instance of `SilverPrice` class
        ```python
        silverprice = SilverPrice()
        silverprice.citywise_price()
        ```

        Return\n
        ```js
        {
            'Agra': '81',
            'Ahmedabad': '81',
            'Bangalore': '81',
            'Bhilai': '81',
            'Bhopal': '81'
        }
        ```
        """
        try:
            x = self.page_soup.find_all("tr")
            x = x[7:-12]

            x = [(y.get_text()).split("₹ ")[:-1] for y in x]
            keys = [y[0] for y in x]
            values = [y[1] for y in x]

            return dict(zip(keys, values))

        except:
            return None

    def last_10_days(self):
        """
        Create an instance of `SilverPrice` class
        ```python
        silverprice = SilverPrice()
        silverprice.citywise_price()
        ```

        Return\n
        ```js
        {
            'Aug 01, 2023': '810',
            'Jul 31, 2023': '800',
            'Jul 30, 2023': '800',
            'Jul 29, 2023': '800',
            'Jul 28, 2023': '795',
            'Jul 26, 2023': '804',
            'Jul 25, 2023': '800',
            'Jul 24, 2023': '805',
            'Jul 23, 2023': '805',
            'Jul 22, 2023': '805'
        }
        ```
        """
        try:
            x = self.page_soup.find_all("tr")
            x = x[-10:]

            x = [(y.get_text()).split("₹ ") for y in x]
            keys = [y[0] for y in x]
            values = [y[1] for y in x]

            return dict(zip(keys, values))

        except:
            return None
