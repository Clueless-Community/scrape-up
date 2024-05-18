from bs4 import BeautifulSoup as b

from scrape_up.config.request_config import RequestConfig, get


class FlipkartLaptops:
    """
    Create an instance of `FlipkartLaptops` class.
    ```python
    item = FlipkartLaptops()
    ```
    | Methods               | Details                                                            |
    | --------------------- | ------------------------------------------------------------------ |
    | `.laptops()`          | Returns the list of Laptops on flipkart with all the details       |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def laptops(self):
        """
        Get the list of laptops\n
        Class - `flipkart_laptops`\n
        Example -\n
        ```python
        item = FlipkartLaptops()
        item.laptops()
        ```
        Return
        ```js
        [
            {
                'Item_Name': 'CHUWI Core i3 10th Gen - (8 GB/512 GB SSD/Windows 11 Home) CoreBook X Grey Laptop',
                'rating': '4.3',
                'Description': 'Intel Core i3 Processor (10th Gen)8 GB DDR4 RAM64 bit Windows 11 Operating System512 GB SSD35.56 cm (14 inch) DisplayWPS Office, Operating System Software1 Year Onsite Warranty',
                'price': '₹24,990'
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            page = get(link, self.config)
            soup = b(page.content, "html.parser")

            details = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                rating = data.find("div", class_="_3LWZlK")
                description = data.find("ul", class_="_1xgFaf")
                if description:
                    Processor = description.find_all("li")[0]
                    RAM = description.find_all("li")[1]
                    OS = description.find_all("li")[2]
                    Storage = description.find_all("li")[3]
                    Screen = description.find_all("li")[4]
                    Warranty = description.find_all("li")[-1]
                else:
                    Processor = None
                    RAM = None
                    OS = None
                    Storage = None
                    Screen = None
                    Warranty = None

                price = data.find("div", class_="_30jeq3 _1_WHN1")
                EMI = data.find("div", class_="_2Tpdn3 _18hQoS")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "rating": rating.text if rating else None,
                    "Processor": Processor.text if Processor else None,
                    "RAM": RAM.text if RAM else None,
                    "Operating system": OS.text if OS else None,
                    "Storage": Storage.text if Storage else None,
                    "Screen Size": Screen.text if Screen else None,
                    "Warranty": Warranty.text if Warranty else None,
                    "Price": price.text if price else None,
                    "EMI": EMI.text if EMI else None,
                }

                details.append(item_details)

            return details

        except:
            return None
