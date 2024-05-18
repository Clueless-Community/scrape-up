from bs4 import BeautifulSoup
from scrape_up.config.request_config import RequestConfig, get


class Crypto:
    """
    Create an instance of `Crypto` class

    ```python
    crypto = Crypto()
    ```

    | Method                       | Details                                                  |
    | ---------------------------- | -------------------------------------------------------- |
    | `get_top_cryptocurrencies()` | Fetches and returns data about the top cryptocurrencies. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        """
        Initialize the CoinMarketCap class by fetching data from the CoinMarketCap website.
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        url = "https://coinmarketcap.com/"
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)
        html_text = get(url, self.config).text
        self.soup = BeautifulSoup(html_text, "lxml")

    def get_top_cryptocurrencies(self):
        """
        A list of dictionaries containing details of the top cryptocurrencies.\n
        ```python
        crypto = Crypto()
        top_crypto = crypto.get_top_cryptocurrencies()
        ```
        Example output:
        ```python
        [
            {
                "Name": "Bitcoin",
                "Symbol": "BTC",
                "Link": "https://coinmarketcap.com/...",
                "Price": "$65,432.10",
                "1h%": "-1.23% (Down)",
                "24h%": "+0.45% (Up)",
                "7d%": "-2.15% (Down)",
                "MarketCap": "$1.23T",
                "Volume(24h)": "$12.5B",
                "Circulating Supply": "18.7M BTC"
            },
            ...
        ]
        """
        try:
            cryptocurrency = []
            container = self.soup.find("div", {"class": "sc-66133f36-2 cgmess"})
            i = 0
            tbody = container.find("tbody")
            for items in tbody.find_all("tr"):
                i += 1
                if i == 11:
                    break
                j = 0
                for item in items.find_all("td"):
                    j += 1
                    if j == 1 or j == 2:
                        continue
                    elif j == 3:
                        name = item.find("p", {"class": "sc-4984dd93-0 kKpPOn"}).text
                        symbol = item.find(
                            "p", {"class": "sc-4984dd93-0 iqdbQL coin-item-symbol"}
                        ).text
                        link = (
                            "https://coinmarketcap.com"
                            + item.find("a", href=True)["href"]
                        )
                    elif j == 4:
                        price = item.text
                    elif j == 5:
                        if item.find("span", {"class": "icon-Caret-down"}) is not None:
                            market = "Down"
                        else:
                            market = "Up"
                        hour = item.text + f" ({market})"
                    elif j == 6:
                        if item.find("span", {"class": "icon-Caret-down"}) is not None:
                            market = "Down"
                        else:
                            market = "Up"
                        hour_24 = item.text + f" ({market})"
                    elif j == 7:
                        if item.find("span", {"class": "icon-Caret-down"}) is not None:
                            market = "Down"
                        else:
                            market = "Up"
                        day = item.text + f" ({market})"
                    elif j == 8:
                        marketcap = item.find(
                            "span", {"class": "sc-7bc56c81-1 bCdPBp"}
                        ).text
                    elif j == 9:
                        volume = item.find(
                            "p", {"class": "sc-4984dd93-0 jZrMxO font_weight_500"}
                        ).text
                    elif j == 10:
                        supply = item.find("p", {"class": "sc-4984dd93-0 WfVLk"}).text
                data = {
                    "Name": name,
                    "Symbol": symbol,
                    "Link": link,
                    "Price": price,
                    "1h%": hour,
                    "24h%": hour_24,
                    "7d%": day,
                    "MarketCap": marketcap,
                    "Volume(24h)": volume,
                    "Circulating Supply": supply,
                }
                cryptocurrency.append(data)
            return cryptocurrency
        except Exception:
            return None
