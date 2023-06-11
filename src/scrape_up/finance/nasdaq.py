import requests
from datetime import datetime


# All prices returned form this class are in USD
class NASDAQ:
    """
    Handles all requests for nasdaq stock
    """

    autocomplete_url = "https://api.nasdaq.com/api/search/result?query={}&order=relevence&offset=0&lang=en"
    latest_price_url = (
        "https://api.nasdaq.com/api/quote/{symbol}/info?assetclass=stocks"
    )
    chart_data_url = "https://api.nasdaq.com/api/quote/{symbol}/chart?assetclass=stocks"
    historical_data_url = "https://api.nasdaq.com/api/quote/{symbol}/historical?assetclass=stocks&fromdate={from_date}&limit=0&todate={to_date}"  # date in yyyy-mm-dd format
    currency_type = "USD"

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "Sec-Fetch-User": "?1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    }

    # Creating request.Session object so cookies persist among requests
    fetcher = requests.Session()
    fetcher.headers.update(headers)

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.stock_symbol = self.get_data()["symbol"]
        self.latest_price_url = self.latest_price_url.format(symbol=self.stock_symbol)
        self.chart_data_url = self.chart_data_url.format(symbol=self.stock_symbol)

    def get_data(self):
        try:
            data = self.fetcher.get(
                self.autocomplete_url.format(self.stock_name)
            ).json()["data"]["results"][0]
        except IndexError:
            raise Exception("Invalid Stock Name.")
        except TypeError:
            raise Exception("Invalid Stock Name")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error, Please try again.")
        else:
            self.stock_name = data["name"][0]
            return {"symbol": data["symbol"][0], "symbol_info": data["name"][0]}

    def get_latest_price(self):
        """
        Gets Latest stock price info of given nse stock.
        Class - `finance.NASDAQ()`\n
        Example -\n
        ```python
        google = NASDAQ("alphabet")
        print(google.get_latest_price())
        ```
        Return\n
        ```python
        return
        {
            "data": data,
            "message": f"Latest price of the stock has been fetched",
        }
        ```
        """
        try:
            price_info = self.fetcher.get(self.latest_price_url).json()["data"][
                "primaryData"
            ]
            data = {
                "latestPrice": float(price_info["lastSalePrice"][1:]),
                "rateChange": float(price_info["netChange"]),
                "pChange": float(price_info["percentageChange"][:-1]),
            }
            return {
                "data": data,
                "message": f"Latest price of the stock has been fetched",
            }
        except:
            return {
                "data": None,
                "message": f"Not able to fetch latest price of the stock",
            }

    # Please give dates in DD-MM-YYYY format
    def get_historical_data(self, from_date, to_date):
        """
        Gets Latest stock price info of given nse stock.
        Class - `finance.NASDAQ()`\n
        Example -\n
        ```python
        google = NASDAQ("alphabet")
        print(google.get_historical_data("05-06-2023", "09-06-2023"))
        ```
        Return\n
        ```python
        return
        {
            "data": historical_price_data,
            "message": f"Sucessfylly scrapped the historic data of the stock.",
        }
        ```
        """
        try:
            from_date = datetime.strptime(from_date, "%d-%m-%Y").strftime("%Y-%m-%d")
            to_date = datetime.strptime(to_date, "%d-%m-%Y").strftime("%Y-%m-%d")
            historical_price_data_raw = self.fetcher.get(
                self.historical_data_url.format(
                    symbol=self.stock_symbol, from_date=from_date, to_date=to_date
                )
            ).json()["data"]["tradesTable"]["rows"]
            historical_price_data = {}
            for i in historical_price_data_raw:
                date_formatted = datetime.strptime(i["date"], "%m/%d/%Y").strftime(
                    "%d-%m-%Y"
                )
                historical_price_data[date_formatted] = float(i["open"][1:])
            return {
                "data": historical_price_data,
                "message": f"Sucessfylly scrapped the historic data of the stock.",
            }
        except:
            return {
                "data": None,
                "message": f"Not able to fetch historical data of the stock.",
            }


if __name__ == "__main__":
    google = NASDAQ("alphabet")
    print(google.get_latest_price())
    print(google.get_historical_data("05-06-2023", "09-06-2023"))
