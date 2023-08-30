from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
USER_AGENT = {
    "User-Agent": "Mozilla/5.0"
}

class EquityMutualFunds:

    """
    Create an instance of `EquityMutualFunds` class.
    ```python
    equitymutualfunds = EquityMutualFunds()
    ```
    | Methods                  | Details                                         |
    | -------------------------|-------------------------------------------------|
    | `.historical_returns`    | Returns mutual funds based on historic returns  |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/mutual-funds/best-funds/equity.html"
            req = Request(url, headers= USER_AGENT)

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def historical_returns(self):
        """
        Create an instance of `EquityMutualFunds` class.

        ```python
        equitymutualfunds = EquityMutualFunds()
        equitymutualfunds.historical_returns()

        ```
        Return\n
        ```js
        [
            'Motilal Oswal Midcap Fund',
            'Quant Small Cap Fund',
            'UTI Flexi Cap Fund',
            ....
        ]
        ```
        """

        try:
            L = []
            for x in self.page_soup.find_all("a", {"class": "robo_medium"}):
                temp = x.get_text().split(" - ")[0]
                if temp not in L:
                    L.append(temp)

            return L

        except:
            return None
