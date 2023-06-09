try:
    from nse import NSE
except ModuleNotFoundError:
    from scrape_up.finance.nse import NSE


class StockPrice:
    """
    This is entry point for users to scrape data.
    Usage:
        Create an instance of Stock price class for Infosys
        >>> infosys_stock = StockPrice('infosys','nse')
        >>> infosys_stock = StockPrice('infosys')

        # the stock_index option is optional as it is set to 'nse' by default for now

        To get latest price info of Infosys's Stock
        >>> latest_price_info = infosys_stock.get_latest_price()

        To get stock price of Infosys from 02-05-2023 to 31-05-2023
        >>> historical_price_info = infosys_stock.get_historical_data('02-05-2023', '31-05-2023')

    """

    def __init__(self, stock_name, stock_index="nse"):
        self.stock_name = stock_name.strip()
        self.stock_index = stock_index.strip().lower()
        if self.stock_index == "nse":
            print(f"Searching for {self.stock_name} nse stock...")
            try:
                self.stock = NSE(stock_name)
                self.stock_name = self.stock.stock_name
                print(
                    f"Found stock based on provided name: {self.stock_name}\nStock instance created"
                )
            except:
                self.stock = None
                print(f"No stock found based on provided name: {self.stock_name}")
        else:
            print(
                f"{self.stock_index} stock scraping code under development.\nPlease wait for Update."
            )

    # these two functions could potentially be modified to
    # also return data as pandas format
    def get_latest_price(self):
        """
        Gets Latest stock price info of given stock
        """
        try:
            data = self.stock.get_latest_price()
            message = f"Found latest stock price for {self.stock_name}"
        except:
            data = None
            message = f"No latest stock price found for {self.stock_name}"
        finally:
            return {
                "data": data,
                "message": message,
            }

    def get_historical_data(self, from_date, to_date):
        """
        Gets historical stock price (vwap) in range from_date to to_date
        """
        try:
            data = self.stock.get_historical_data(from_date, to_date)
            message = f"Historical stock price found for {self.stock_name} in range {from_date} to {to_date}"
        except:
            data = None
            message = f"No historial stock price found for {self.stock_name}"
        finally:
            return {
                "data": data,
                "message": message,
            }
