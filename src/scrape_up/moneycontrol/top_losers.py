from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class TopLosers:
    """
    Create an instance of `TopLosers` class
    ```python
    toplosers = TopLosers()
    ```

    | Methods            | Details                                              |
    | -------------------|------------------------------------------------------|
    | `.high()`          | Returns the highest value the top loser was sold for |
    | `.low()`           | Returns the lowest value the top loser was sold for  |
    | `.last_price()`    | Returns the last price top loser was sold for        |
    | `.prev_close()`    | Returns the prev close value of the top loser        |
    | `.change()`        | Returns the change and loss % of top loser stocks    |


    """

    def __init__(self):
        self.__scrape_page()
        self.__stock_names()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/stocks/marketstats/nseloser/index.php"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def __stock_names(self):
        try:
            self.keys = []
            x = self.page_soup.find_all("a", {"style": "color:#333"})
            for y in x:
                self.keys.append(y.get_text())
        except:
            return None

    def high(self):
        """
        Create an instance of `TopLosers` class
        ```python
        toplosers = TopLosers()
        toplosers.high()
        ```

        Return\n
        ```js
        {
            "SBI": "598.70",
            "Bajaj Auto": "4,864.20",
            "BPCL": "370.85",
            "NTPC": "222.20",
            "Maruti Suzuki": "9,616.00",
            "Tata Motors": "625.00",
            "Eicher Motors": "3,478.85"
        }
        ```
        """
        try:
            z = self.page_soup.find_all("td", {"width": "75"})
            values = []
            for y in z:
                values.append(y.get_text())
            return dict(zip(self.keys, values))

        except:
            return None

    def low(self):
        """
        Create an instance of `TopLosers` class
        ```python
        toplosers = TopLosers()
        toplosers.low()
        ```

        Return\n
        ```js
        {
            "SBI": "571.40",
            "Bajaj Auto": "4,700.00",
            "BPCL": "360.05",
            "NTPC": "217.60",
            "Maruti Suzuki": "9,427.00",
            "Tata Motors": "613.30",
            "Eicher Motors": "3,350.00"
        }
        ```
        """
        try:
            z = self.page_soup.find_all("td", {"width": "80"})
            values = []
            x = True
            for y in z:
                if x:
                    values.append(y.get_text())
                x = not (x)
            return dict(zip(self.keys, values))

        except:
            return None

    def last_price(self):
        """
        Create an instance of `TopLosers` class
        ```python
        toplosers = TopLosers()
        toplosers.last_price()
        ```

        Return\n
        ```js
        {
            "SBI": "573.30",
            "Bajaj Auto": "4,712.00",
            "BPCL": "360.40",
            "NTPC": "217.95",
            "Maruti Suzuki": "9,470.40",
            "Tata Motors": "615.00",
            "Eicher Motors": "3,359.55"
        }
        ```
        """
        try:
            z = self.page_soup.find_all("td", {"width": "85"})
            values = []
            for y in z:
                values.append(y.get_text())
            return dict(zip(self.keys, values))

        except:
            return None

    def prev_close(self):
        """
        Create an instance of `TopLosers` class
        ```python
        toplosers = TopLosers()
        toplosers.prev_close()
        ```

        Return\n
        ```js
        {
            "SBI": "590.50",
            "Bajaj Auto": "4,826.30",
            "BPCL": "368.00",
            "NTPC": "220.10",
            "Maruti Suzuki": "9,543.70",
            "Tata Motors": "618.95",
            "Eicher Motors": "3,379.70"
        }
        ```
        """
        try:
            z = self.page_soup.find_all("td", {"width": "80"})
            values = []
            x = False
            for y in z:
                if x:
                    values.append(y.get_text())
                x = not (x)
            return dict(zip(self.keys, values))

        except:
            return None

    def change(self):
        """
        Create an instance of `TopLosers` class
        ```python
        toplosers = TopLosers()
        toplosers.change()
        ```

        Return\n
        ```js
        {
            "SBI": {"Change": "-17.20", "Gain": "-2.91"},
            "Bajaj Auto": {"Change": "-114.30", "Gain": "-2.37"},
            "BPCL": {"Change": "-7.60", "Gain": "-2.07"},
            "NTPC": {"Change": "-2.15", "Gain": "-0.98"},
            "Maruti Suzuki": {"Change": "-73.30", "Gain": "-0.77"},
            "Tata Motors": {"Change": "-3.95", "Gain": "-0.64"},
            "Eicher Motors": {"Change": "-20.15", "Gain": "-0.60"}
        }
        ```
        """
        try:
            z = self.page_soup.find_all("td", {"width": "45"})
            z = [y.get_text() for y in z]

            values = []
            for y in range(0, len(z), 2):
                change_dict = {}
                change_dict["Change"] = z[y]
                change_dict["Gain"] = z[y + 1]
                values.append(change_dict)
            return dict(zip(self.keys, values))

        except:
            return None
