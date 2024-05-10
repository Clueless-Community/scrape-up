from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class TopGainers:
    """
    Create an instance of `TopGainers` class
    ```python
    topgainers = TopGainers()
    ```

    | Methods            | Details                                               |
    | -------------------|-------------------------------------------------------|
    | `.high()`          | Returns the highest value the top gainer was sold for |
    | `.low()`           | Returns the lowest value the top gainer was sold for  |
    | `.last_price()`    | Returns the last price top gainer was sold for        |
    | `.prev_close()`    | Returns the prev close value of the top gainer        |
    | `.change()`        | Returns the change and gain % of top gainer stocks    |


    """

    def __init__(self):
        self.__scrape_page()
        self.__stock_names()

    def __scrape_page(self):
        try:
            url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
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
        Create an instance of `TopGainers` class.\n
        ```python
        topgainers = TopGainers()
        topgainers.high()
        ```
        Return\n
        ```js
        {
            "Cipla": "1,238.70",
            "IndusInd Bank": "1,414.90",
            "Tech Mahindra": "1,181.85",
            "Wipro": "410.00",
            "Bharti Airtel": "892.95",
            "Axis Bank": "954.85"
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
        Create an instance of `TopGainers` class.\n
        ```python
        topgainers = TopGainers()
        topgainers.low()
        ```

        Return\n
        ```js
        {
            "Cipla": "1,171.00",
            "IndusInd Bank": "1,366.30",
            "Tech Mahindra": "1,142.80",
            "Wipro": "400.30",
            "Bharti Airtel": "866.20",
            "Axis Bank": "934.65"
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
        Create an instance of `TopGainers` class.\n
        ```python
        topgainers = TopGainers()
        topgainers.last_price()
        ```

        Return\n
        ```js
        {
            "Cipla": "1,209.75",
            "IndusInd Bank": "1,409.60",
            "Tech Mahindra": "1,175.20",
            "Wipro": "408.85",
            "Bharti Airtel": "889.65",
            "Axis Bank": "952.25"
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
        Create an instance of `TopGainers` class.\n
        ```python
        topgainers = TopGainers()
        topgainers.prev_close()
        ```

        Return\n
        ```js
        {
            "Cipla": "1,165.85",
            "IndusInd Bank": "1,364.50",
            "Tech Mahindra": "1,142.80",
            "Wipro": "399.65",
            "Bharti Airtel": "871.70",
            "Axis Bank": "935.55"
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
        Create an instance of `TopGainers` class.\n
        ```python
        topgainers = TopGainers()
        topgainers.change()
        ```

        Return\n
        ```js
        {
            "Cipla": {"Change": "43.90", "Gain": "3.77"},
            "IndusInd Bank": {"Change": "45.10", "Gain": "3.31"},
            "Tech Mahindra": {"Change": "32.40", "Gain": "2.84"},
            "Wipro": {"Change": "9.20", "Gain": "2.30"},
            "Bharti Airtel": {"Change": "17.95", "Gain": "2.06"},
            "Axis Bank": {"Change": "16.70", "Gain": "1.79"}
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
