import bs4
from bs4 import BeautifulSoup as bs
import requests


class Flipkart:
    """
    Class - `Flipkart`\n
    Instantiate a class\n
    Example -\n
    ```python
    item = Flipkart()
    ```
    \n
    Available Methods\n
    1. TVs - To fetch the list of trending TVs on Flipkart with other details
    2. BestsellersBooks - To fetch the bestselling items listed on FLipkart

    """

    def __init__(self):
        pass

    def TVs(self):
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.TVs()
            ```
            Return\n
            ```python
            return {all_items with details in json}
            ```
            """

            link = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_3pLy-c row"):
                names = data.find("div", attrs={"class": "_4rR01T"})
                price = data.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
                rating = data.find("div", attrs={"class": "_3LWZlK"})
                specification = data.find("div", attrs={"class": "fMghEO"})

                specs = []
                for spec in specification.find_all("li", attrs={"class": "rgWa7D"}):
                    specs.append(spec.text)

                item_details = {
                    "Item_Name": names.text,
                    "Price": price.text,
                    "Rating": rating.text,
                    "Specifications": ", ".join(specs),
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None

    def BestsellersBooks(self):
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.BestsellersBooks()
            ```
            Return\n
            ```python
            return {all_items with details in json}
            ```
            """

            link = "https://www.flipkart.com/search?q=bestsellers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_4ddWXP"):
                names = data.find("a", attrs={"class": "s1Q9rs"})
                price = data.find("div", attrs={"class": "_30jeq3"})
                rating = data.find("div", attrs={"class": "_3LWZlK"})
                specification = data.find("div", attrs={"class": "_3Djpdu"})

                item_details = {
                    "Item_Name": names.text,
                    "Price": price.text,
                    "Rating": rating.text if rating else None,
                    "Specifications": specification.text if specification else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None
        

    def scrapdatamobiles():
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.BestsellersBooks()
            ```
            Return\n
            ```python
            return {all_items with details in json}
            ```
            """
            link = "https://www.flipkart.com/search?q=MOBILE+PHONE+UNDER+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE"):
                names = data.find("a", class_="_1fQZEK")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="_3LWZlK")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            print("Error:", str(e))
            return None
        
