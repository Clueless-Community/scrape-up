from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


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
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

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
            'Nippon India Small Cap Fund', 
            'WhiteOak Capital Mid Cap Fund', 
            'Bank of India Manufacturing & Infrastructure Fund', 
            'Nippon India Multicap Fund', 'JM Flexi Cap Fund', 
            'DSP Equity Opportunities Fund', 
            'ICICI Prudential Large & Mid Cap Fund- Direct Plan', 
            'DSP India T.I.G.E.R. Fund', 
            'ICICI Prudential Large & Mid Cap Fund- GrowthLarge & Mid Cap Fund', 
            'UTI S&P BSE Low Volatility Index Fund', 
            'UTI Value Opportunities Fund', 
            'WhiteOak Capital Tax Saver Fund', 
            'DSP Tax Saver Fund', 
            'WhiteOak Capital Flexi Cap Fund', 
            'Parag Parikh Tax Saver Fund',
            'Bandhan Tax Advantage (ELSS) Fund',
            'Invesco India Infrastructure Fund', 
            'DSP Focus Fund', 
            'HDFC Large and Mid Cap Fund'
        ]

        ```
        """

        try:
            L = []
            for x in self.page_soup.find_all("a",{"class":"robo_medium"}):
                temp = x.get_text().split(' - ')[0]
                if temp not in L:
                    L.append(temp)

            return L
        
        except:

            return None
