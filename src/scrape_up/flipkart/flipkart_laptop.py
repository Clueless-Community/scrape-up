import requests
import bs4
from bs4 import BeautifulSoup as b


class flipkart_laptop:
    """
    Create an instance of `flipkart_laptop` class.
    ```python
    item = flipkart_laptops
    ```
    | Methods               | Details                                                            |
    | --------------------- | ------------------------------------------------------------------ |
    | `.laptops()`          | Returns the list of Laptops on flipkart with all the details       |
    """

    def __init__(self):
        pass

    def laptops(self):
        """
        Get the list of laptops\n
        Class - `flipkart_laptops`\n
        Example -\n
        ```python
        item = flipkart_laptop()
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
            page = requests.get(link)
            soup = b(page.content, "html.parser")

            details = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                rating = data.find("div", class_="_3LWZlK")
                description = data.find("ul", class_="_1xgFaf")
                price = data.find("div", class_="_30jeq3 _1_WHN1")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "rating": rating.text if rating else None,
                    "Description": description.text if description else None,
                    "price": price.text if price else None,
                }

                details.append(item_details)

            return details
            
        except Exception as e:
            return None