import requests
import time
from datetime import datetime, timedelta
import json

def get_unix_timestamp(date=None):
    if date:
        start_of_day = date.replace(hour=0, minute=0, second=0)
        return int(start_of_day.timestamp())
    else:
        time.time()

class CRYPTO:
    price_url = "https://price-api.crypto.com/price/v1/token-price/{crypto_name}?_t={timestamp}"

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    # Creating request.Session object so cookies persist among requests
    fetcher = requests.Session()
    fetcher.headers.update(headers)

    def __init__(self,crypto_name):
        self.crypto_name = crypto_name
        self.currency_type = "USD"
        try:
            """
            The line below is necessary as crypto.com does no give access to its
            api unless you have cookies of visiting main page.
            Hence visiting mainpage would imitate behaviour of a human user and let us
            access all the crypto.com APIs.
            """
            main_page = self.fetcher.get("https://crypto.com")

        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error, Please try again.")            
    
    def get_latest_price(self):
        try:
            price_info = self.fetcher.get(
                self.price_url.format(
                    crypto_name = self.crypto_name,
                    timestamp = get_unix_timestamp()
                )
            ).json()
        except json.decoder.JSONDecodeError:
            raise Exception("Invalid Currency Name")
        else:
            return {
                "latestPrice": float(price_info["usd_price"]),
                "usdPriceChange": float(price_info["usd_price_change_24h"]),
                "btcPriceChange": float(price_info["btc_price_change_24h"])
            }
            
    
    def get_historical_data(self,from_date,to_date):
        from_date_obj = datetime.strptime(from_date,"%d-%m-%Y")
        to_date_obj = datetime.strptime(to_date,"%d-%m-%Y")
        curr_date_obj = from_date_obj
        one_day = timedelta(days=1)
        historical_price_data = {}
        while(curr_date_obj != to_date_obj):
            date_str = curr_date_obj.strftime("%d-%m-%Y")
            historical_price_data[date_str] = self.fetcher.get(
                self.price_url.format(
                    crypto_name = self.crypto_name,
                    timestamp = get_unix_timestamp(curr_date_obj)
                )
            ).json()["usd_price"]
            curr_date_obj += one_day
        return historical_price_data

if __name__=="__main__":
    solana = CRYPTO("bitcoin")
    print(solana.get_latest_price())
    print(solana.get_historical_data("05-06-2023","10-06-2023"))
        
    