from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class GoldPrice:
    """
    Create an instance of `GoldPrice` class
    ```python
    goldprice = GoldPrice()
    ```

    | Methods      | Details                                       |
    | -------------| ----------------------------------------------|
    | `.price_22_carat()`| Returns the price of 22k gold prices citywise |
    | `.price_24_carat()`| Returns the price of 22k gold prices citywise |

    """

    def __init__(self):
        self.__scrape_page()
        self.__get_values()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/news/gold-rates-today/"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def __get_values(self):
        y = self.page_soup.find_all("td")
        y = y[25:-33]
        L = []

        for x in y:
            L.append(x.get_text())

        self.vals = []
        for i in range(0, len(y), 5):
            self.vals.append(L[i : i + 5])

    def price_22_carat(self):
        """
        Create an instance of GoldPrice class
        ```python
        goldprice = GoldPrice()
        goldprice.price_22_carat()
        ```
        Return\n
        ```js
        {
            "Agra": "₹ 5,610",
            "Ahmedabad": "₹ 5,614",
            "Andhra pradesh": "₹ 5,550",
            "Assam": "₹ 5,655",
            "Bangalore": "₹ 5,615",
            "Bhilai": "₹ 5,603"
        }
        ```
        """
        try:
            cities = [x[0] for x in self.vals]
            prices = [x[1] for x in self.vals]
            return dict(zip(cities, prices))
        except:
            return None

    def price_24_carat(self):
        """
        Create an instance of GoldPrice class
        ```python
        goldprice = GoldPrice()
        goldprice.price_24_carat()
        ```
        Return\n
        ```js
        {
            'Agra': '₹ 5,891',
            'Ahmedabad': '₹ 5,895',
            'Andhra pradesh': '₹ 5,828',
            'Assam': '₹ 5,938',
            'Bangalore': '₹ 5,896',
            'Bhilai': '₹ 5,883'
        }
        ```
        """
        try:
            cities = [x[0] for x in self.vals]
            prices = [x[3] for x in self.vals]
            return dict(zip(cities, prices))
        except:
            return None
