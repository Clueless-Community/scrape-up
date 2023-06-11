import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json


# All the prices returned from this class are in INR
class BSE:
    """
    Handles all data request for bse stock.
    """

    autocomplete_url = "https://api.bseindia.com/Msource/90D/getQouteSearch.aspx?Type=EQ&text={}&flag=gq"
    latest_price_url = "https://api.bseindia.com/BseIndiaAPI/api/getScripHeaderData/w?Debtflag=&scripcode={code}&seriesid="
    historical_data_url = "https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w?scripcode={code}&flag=1&fromdate={from_date}&todate={to_date}&seriesid="  # date format yyyymmdd
    chart_data_url = "https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w?scripcode={code}&flag=0&fromdate=&todate=&seriesid="
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

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.stock_code = self.get_data()["code"]
        self.latest_price_url = self.latest_price_url.format(code=self.stock_code)
        self.chart_data_url = self.chart_data_url.format(code=self.stock_code)

    # gets closest matching name and symbol of stock based given stock_name
    def get_data(self):
        try:
            data_html = self.fetcher.get(self.autocomplete_url.format(self.stock_name))
            soup = BeautifulSoup(data_html.text, "html.parser")
            li_element = soup.find("li", class_="quotemenu")
            stock_code = li_element.find("span").text.split()[-1]
            stock_name = li_element.find("strong").text
            if li_element.find("strong").next_sibling.strip:
                stock_name += str(li_element.find("strong").next_sibling.strip())

        except IndexError:
            raise Exception("Invalid Stock Name.")
        except TypeError:
            raise Exception("Invalid Stock Name")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error, Please try again.")
        else:
            self.stock_name = stock_name
            return {"code": stock_code, "symbol_info": stock_name}

    def get_latest_price(self):
        """
        Gets Latest stock price info of given bse stock.
        """
        price_info = self.fetcher.get(self.latest_price_url).json()["CurrRate"]
        return {
            "latestPrice": float(price_info["LTP"]),
            "rateChange": float(price_info["Chg"]),
            "pChange": float(price_info["PcChg"]),
        }

    # Please give dates in DD-MM-YYYY format
    def get_historical_data(self, from_date, to_date):
        """
        Gets historical stock price (vwap) in range from_date to to_date
        """

        from_date = datetime.strptime(from_date, "%d-%m-%Y").strftime("%Y%m%d")
        to_date = datetime.strptime(to_date, "%d-%m-%Y").strftime("%Y%m%d")

        historical_price_data_raw = self.fetcher.get(
            self.historical_data_url.format(
                code=self.stock_code, from_date=from_date, to_date=to_date
            )
        ).json()["Data"]

        historical_price_data_raw = json.loads(historical_price_data_raw)
        historical_price_data = {}

        for item in historical_price_data_raw:
            dttm = datetime.strptime(item["dttm"], "%a %b %d %Y %H:%M:%S").strftime(
                "%d-%m-%Y"
            )
            vale1 = float(item["vale1"])
            historical_price_data[dttm] = vale1

        return historical_price_data


if __name__ == "__main__":
    infosys = BSE(stock_name="infosys ltd")
    print(infosys.get_latest_price())
    print(infosys.get_historical_data("05-06-2023", "10-06-2023"))
