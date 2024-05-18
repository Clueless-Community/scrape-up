import requests


# All the prices returned from this class are in INR
class NSE:
    """
    Handles all data request for nse stock.
    """

    autocomplete_url = "https://www.nseindia.com/api/search/autocomplete?q={}"
    latest_price_url = "https://www.nseindia.com/api/quote-equity?symbol={symbol}"
    chart_data_url = "https://www.nseindia.com/api/chart-databyindex?index={symbol}"
    historical_data_url = 'https://www.nseindia.com/api/historical/cm/equity?symbol={symbol}&series=["EQ"]&from={from_date}&to={to_date}'
    currency_type = "INR"

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

    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.stock_symbol = self.get_data()["symbol"]
        self.latest_price_url = self.latest_price_url.format(symbol=self.stock_symbol)
        self.chart_data_url = self.chart_data_url.format(symbol=self.stock_symbol)

    # gets closest matching name and symbol of stock based given stock_name
    def get_data(self):
        try:
            """
            The line below is necessary as nseindia.com does no give access to its
            api unless you have cookies of visiting main page.
            Hence visiting mainpage would imitate behaviour of a human user and let us
            access all the nseindia APIs.
            """
            main_page = self.fetcher.get("https://www.nseindia.com")
            data = self.fetcher.get(
                self.autocomplete_url.format(self.stock_name)
            ).json()["symbols"][0]
        except IndexError:
            raise Exception("Invalid Stock Name.")
        except TypeError:
            raise Exception("Invalid Stock Name")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error, Please try again.")
        else:
            self.stock_name = data["symbol_info"]
            return {"symbol": data["symbol"], "symbol_info": data["symbol_info"]}

    # please use this return format for other classes (like bse, nasdaq) too if they are created in future
    def get_latest_price(self):
        """
        Gets Latest stock price info of given nse stock.
        """
        price_info = self.fetcher.get(self.latest_price_url).json()["priceInfo"]
        return {
            "latestPrice": price_info["lastPrice"],
            "rateChange": price_info["change"],
            "pChange": price_info["pChange"],
            "open": price_info["open"],
            "close": price_info["close"],
            "vwap": price_info["vwap"],
        }

    # Please give dates in DD-MM-YYYY format
    def get_historical_data(self, from_date, to_date):
        """
        Gets historical stock price (vwap) in range from_date to to_date
        """
        historical_price_data_raw = self.fetcher.get(
            self.historical_data_url.format(
                symbol=self.stock_symbol, from_date=from_date, to_date=to_date
            )
        ).json()["data"]
        historical_price_data = {}
        for i in historical_price_data_raw:
            historical_price_data[i["mTIMESTAMP"]] = i["VWAP"]
        return historical_price_data
