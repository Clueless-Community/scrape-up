from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class IndianIndex:
    """
    Create an instance of `IndianIndex` class

    ```python
    indianindex = IndianIndex()
    ```

    | Methods      | Details                                                 |
    | ------------ | ------------------------------------------------------- |
    | `.current()` | Returns the Indian Indices and their current value      |
    | `.change()`  | Returns the Indian Indices and their change and %change |
    """

    def __init__(self):
        self.__scrape_page()
        self.__find_index_names()
        self.__index_values()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/technicals/gapup/nse/index.html/markets/indian-indices/?classic=true"

            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def __find_index_names(self):
        try:
            self.keys = []
            x = self.page_soup.find_all("a", {"class": "bl_12"})
            for y in x:
                self.keys.append(y.get_text())
        except:
            return None

    def __index_values(self):
        try:
            self.points = self.page_soup.find_all("td", {"align": "right"})
            self.points = [x.get_text() for x in self.points]

        except:
            return None

    def current(self):
        """
        Create an instance of `IndianIndex` class
        ```python
        indianindex = IndianIndex()
        indianindex.current()
        ```
        Return\n
        ```js
        {
            'S&P BSE Sensex': '66,156.39',
            'NIFTY 50': '19,666.35',
            'S&P BSE SENSEX 50 Index': '20,615.15',
            'S&P BSE Smallcap': '34,669.80',
            'S&P BSE Midcap': '30,170.69',
            'S&P BSE SmallCap Select Index': '5,502.69',
            'S&P BSE MidCap Select Index': '10,907.52'
        }
        ```
        """
        try:
            self.current_values = []

            for i in range(0, len(self.points), 6):
                self.current_values.append(self.points[i])

            return dict(zip(self.keys, self.current_values))
        except:
            return None

    def change(self):
        """
        Create an instance of `IndianIndex` class
        ```python
        indianindex = IndianIndex()
        indianindex.change()
        ```
        Return\n
        ```js
        {
            'S&P BSE Sensex': {'Change': '-3.81', '% Change': '-0.01'},
            'NIFTY 50': {'Change': '20.30', '% Change': '0.10'},
            'S&P BSE SENSEX 50 Index': {'Change': '-0.22', '% Change': '-0.00'},
            'S&P BSE Smallcap': {'Change': '121.34', '% Change': '0.35'},
            'S&P BSE Midcap': {'Change': '10.87', '% Change': '0.04'},
            'S&P BSE SmallCap Select Index': {'Change': '15.23', '% Change': '0.28'},
            'S&P BSE MidCap Select Index': {'Change': '-19.09', '% Change': '-0.18'}
        }
        ```
        """

        try:
            self.points_keys = ["Change", "% Change"]
            self.change_values = []
            for i in range(0, len(self.points), 6):
                self.change_values.append(
                    dict(zip(self.points_keys, self.points[i + 1 : i + 3]))
                )
            return dict(zip(self.keys, self.change_values))
        except:
            return None
