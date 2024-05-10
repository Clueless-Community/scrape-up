from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class MoneyControl:
    """
    Create an instance of MoneyControl class
    ```python
    index = MoneyControl()
    ```

    | Methods          | Details                                                                                    |
    | -----------------| -------------------------------------------------------------------------------------------|
    | `.contribution()`| Returns the stocks are driving the Sensex and the Nifty up or down and by how many points. |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/stocks/marketstats/indcontrib.php?optex=NSE&opttopic=indcontrib&index=9"

            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def __company_names(self):
        try:
            self.keys = []
            t = self.page_soup.find_all("td", {"class": "PR"})
            for x in t:
                self.keys.append((x.get_text().split("\n"))[0])
        except:
            return None

    def __contribution_values(self):
        try:
            y = self.page_soup.find_all("td", {"align": "right"})
            i = 0
            count = 0
            self.values = []

            name_keys = [
                "Last_Price",
                "Change (Rs)",
                "Change(%)",
                "Mkt Cap(Rs cr)",
                "Contribution",
            ]
            while i < len(y):
                val = []
                while count < 5:
                    val.append(y[i].get_text())
                    count += 1
                    i += 1
                self.values.append(dict(zip(name_keys, val)))
                count = 0
                i += 18
        except:
            return None

    def contribution(self):
        """
        Create an instance of Index class
        ```python
        index = MoneyControl()
        index.contribution()
        ```
        Return\n
        ```js
        {
            {
                "HDFC Bank ": {"Last_Price": "1,643.50", "Change (Rs)": "-29.65", "Change(%)": "-1.77", "Mkt Cap(Rs cr)": "992,011.37", "Contribution": "84.61"},
                "Bajaj Finserv ": {"Last_Price": "1,584.85", "Change (Rs)": "-29.70", "Change(%)": "-1.84", "Mkt Cap(Rs cr)": "252,437.36", "Contribution": "22.37"},
                "TCS ": {"Last_Price": "3,355.40", "Change (Rs)": "-41.50", "Change(%)": "-1.22", "Mkt Cap(Rs cr)": "368,327.43", "Contribution": "21.54"}
                ...
            }
        }
        ```
        """
        try:
            self.__company_names()
            self.__contribution_values()
            return dict(zip(self.keys, self.values))
        except:
            return None
