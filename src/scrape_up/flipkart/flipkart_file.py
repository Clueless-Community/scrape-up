import bs4
from bs4 import BeautifulSoup as bs
import requests


class Flipkart:
    """
    Create an instance of `Flipkart` class.
    ```python
    item = Flipkart()
    ```
    | Methods               | Details                                                            |
    | --------------------- | ------------------------------------------------------------------ |
    | `.TVs()`              | Returns the list of TV sets on flipkart                            |
    | `.bestseller_books()` | Returns the list of bestselling books data listed on Flipkart.     |
    | `.mobiles()`          | Returns the list of mobile phones under 50K along with their data. |
    | `.sport_shoes()`      | Returns the list of trendong sport shoes data.                     |
    | `.laptops()`          | Returns the list of laptop from flipkart.                          |
    | `.camera()`           | Returns the list of camera from flipkart.                           |
    | `.computer()`         | Returns the list of computer from flipkart.                       |
    | `.tablets()`          | Returns the list of tablets from flipkart.                         |
    """

    def __init__(self):
        pass

    def tvs(self):
        """
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.tvs()
        """
        try:
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

    def bestseller_books(self):
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.bestseller_books()
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

    def mobiles(self):
        """
        Get the list of mobiles under 50K\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.mobiles()
        """
        try:
            link = "https://www.flipkart.com/search?q=MOBILE+PHONE+UNDER+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=3"
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
            return None

    def sport_shoes(self):
        """
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.BestsellersBooks()
        item.sport_shoes()
        """
        try:
            all_items = []
            url = "https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp,cil,1cu&otracker=nmenu_sub_Men_0_Sports%20Shoes"
            response = requests.get(url)
            html_content = response.content
            soup = bs(html_content, "html.parser")

            all_items = []

            div_elements = soup.find_all("div", class_="_1xHGtK _373qXS")

            for div in div_elements:
                name_element = div.find("a", class_="IRpwTa")
                name = name_element.text.strip() if name_element else ""

                image_element = div.find("img", class_="_2r_T1I")
                image_url = image_element["src"] if image_element else ""

                details_element = div.find("a", class_="_3bPFwb")
                details = details_element.text.strip() if details_element else ""

                item_details = {
                    "Name": name,
                    "Image URL": image_url,
                    "Details": details,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            print("Error:", str(e))
            return None

    def laptops(self):
        """
        Get the list of mobiles under 50K\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.laptops()
        """
        try:
            link = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
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
            return None

    def headphones(self):
        """
        Class - `Flipkart`\n
        ```python
        item = Flipkart()
        item.headphones()
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=headphones+bluetooth&sid=0pm%2Cfcn%2Cgc3%2Cka8&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=headphones+bluetooth%7CWireless+Headphones&requestId=beefc9a9-55a8-4b64-b510-b9bc44ae6680&as-backfill=on&page=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_30jeq3")
                description = data.find("div", class_="_3xFhiH")
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
            return None

    def camera(self):
        """
        Class - `Flipkart`\n
        ```python
        item = Flipkart()
        item.camera()
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                price = data.find("div", class_="_30jeq3")
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
            return None

    def computer(self):
        """
        Class - `Flipkart`\n
        ```python
        item = Flipkart()
        item.computer()
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=computer&sid=6bo%2Cnl4%2Cigk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_na&as-pos=2&as-type=RECENT&suggestionId=computer%7CAll+In+One+PCs&requestId=a640e175-ccac-4757-81de-8580730de6ef&as-backfill=on&page=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_30jeq3")
                delivery = data.find("div", class_="_2Tpdn3")
                review = data.find("div", class_="_3LWZlK")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "delivery": delivery.text if delivery else None,
                    "Review": review.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None

    def tablets():
        """
        Get the list of mobiles under 50K\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.tablets()
        """
        try:
            link = "https://www.flipkart.com/search?q=tablet&sid=tyy%2Chry&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tablet%7CTablets&requestId=07b434d5-21a5-48e0-9170-8d9f4a90928f&as-searchtext=tablet&page=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="gUuXy-")
                offer_price = data.find("div", class_="_2ZdXDB")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                    "Offer_Price": offer_price.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None
