try:
    from nse import NSE
    from nasdaq import NASDAQ
    from bse import BSE
except ModuleNotFoundError:
    from scrape_up.finance.nse import NSE
    from scrape_up.finance.nasdaq import NASDAQ
    from scrape_up.finance.bse import BSE


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

    def __init__(self, stock_name: str, stock_index: str):
        self.stock_name = stock_name.strip()
        self.stock_index = stock_index.strip().lower()
        stock_class = None
        if self.stock_index == "nse":
            stock_class = NSE
        elif self.stock_index == "nasdaq":
            stock_class = NASDAQ
        elif self.stock_index == "bse":
            stock_class = BSE
        if stock_class:
            print(f"Searching for {self.stock_name} {self.stock_index} stock...")
            try:
                self.stock = stock_class(stock_name)
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
        Gets Latest stock price info of given nse stock.
        Class - `finance.StockPrice()`\n
        Example -\n
        ```python
        infosys_stock = StockPrice("infosys", "nse")
        print(infosys_stock.get_latest_price())
        ```
        Return\n
        ```python
        return
        {
            "data": data,
            "message": f"No latest stock price found for {self.stock_name}"
        }
        ```
        """
        try:
            data = self.stock.get_latest_price()
            message = f"Found latest stock price(in {self.stock.currency_type}) for {self.stock_name}"
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
        Class - `finance.StockPrice()`\n
        Example -\n
        ```python
        infosys_stock = StockPrice("infosys", "nse")
        print(infosys_stock.get_historical_data('02-05-2023', '31-05-2023'))
        ```
        Return\n
        ```python
        return
        {
            "data": data,
            "message": f"No historial stock price found for {self.stock_name}"
        }
        ```
        """
        try:
            data = self.stock.get_historical_data(from_date, to_date)
            message = f"Historical stock price(in {self.stock.currency_type}) found for {self.stock_name} in range {from_date} to {to_date}"
        except:
            data = None
            message = f"No historial stock price found for {self.stock_name}"
        finally:
            return {
                "data": data,
                "message": message,
            }
