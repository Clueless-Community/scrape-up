from bs4 import BeautifulSoup as bs

from scrape_up.config.request_config import RequestConfig, get


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
    | `.headphones()`       | Returns the list of headphone from flipkart.                       |
    | `.camera()`           | Returns the list of camera from flipkart.                          |
    | `.computer()`         | Returns the list of computer from flipkart.                        |
    | `.tablets()`          | Returns the list of tablets from flipkart.                         |
    | `.cycle()`            | Returns the list of bicycles from flipkart.                        |
    | `.printers()`         | Returns the list of printers from flipkart.                        |
    | `.monitor()`          | Returns the list of monitors from flipkart.                        |
    | `.ac()`               | Returns the list of acs from flipkart.                             |
    | `.refrigerator()`     | Returns the list of refrigerators from flipkart.                   |
    | `.vrbox()`            | Returns the list of vrbox from flipkart.                           |
    | `.speakers()`         | Returns the list of speakers from flipkart.                        |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()) -> None:
        self.config = config

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
            page = get(link, self.config)
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

        except:
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
            page = get(link, self.config)
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

        except:
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
            page = get(link, self.config)
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

        except:
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
            response = get(url, self.config)
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
                    "Item_Name": name,
                    "Image_URL": image_url,
                    "Details": details,
                }

                all_items.append(item_details)

            return all_items

        except:
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
            page = get(link, self.config)
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

        except:
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
            page = get(link, self.config)
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

        except:
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
            page = get(link, self.config)
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

        except:
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
            page = get(link, self.config)
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
                    "Delivery": delivery.text if delivery else None,
                    "Review": review.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except:
            return None

    def tablets(self):
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
            page = get(link, self.config)
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

        except:
            return None

    def cycle(self):
        try:
            """
            Get the list of mobiles under 50K\n
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.cycle()
            """

            link = "https://www.flipkart.com/search?q=bicycle&sid=abc%2Culv%2Cixt&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=bicycle%7CCycles&requestId=05fd446d-fd05-4abe-8bcc-445937cc6fb1&as-searchtext=bicy&page=1"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_25b18c")
                description = data.find("div", class_="_3Djpdu")
                review = data.find("div", class_="gUuXy- _2D5lwg")
                deals = data.find("div", class_="_3xFhiH")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                    "Deals": deals.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except:
            return None

    def printers(self):
        """
        Get the list of printers\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.printers()
        ```
        Return
        ```js
        [
            {
                "item_name":"Canon ImageCLASS MF3010 Multi-function Monochrome Laser...",
                "price":"₹17,680",
                "description":"Black, Toner Cartridge",
                "review":"4.3",
                "delivery":"Free delivery",
                "exchange_upto":"Upto ₹400 Off on Exchange"
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=printer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_13oc-S"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_30jeq3")
                description = data.find("div", class_="_3Djpdu")
                review = data.find("div", class_="_3LWZlK")
                delivery = data.find("div", class_="_3tcB5a _2hu4Aw")
                Exchange_Up_To = data.find("div", class_="_3xFhiH")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                    "Delivery": delivery.text if review else None,
                    "Exchange_Upto": Exchange_Up_To.text if Exchange_Up_To else None,
                }

                all_items.append(item_details)

            return all_items

        except:
            return None

    def monitor(self):
        """
        Get the list of mobiles under 50K\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.monitor()
        ```
        Return
        ```js
        [
            {
                "Item_Name":"Acer 27 inch Full HD LED Backlit IPS Panel White Colour Monitor (HA270)",
                "Price":"₹10,550",
                "Description":"Panel Type: IPS PanelScreen Resolution Type: Full HDBrightness: 250 nitsResponse Time: 4 ms | Refresh Rate: 75 HzHDMI Ports - 13 Years on Site",
                "Review":"4.48,788 Ratings\\xa0&\\xa01,484 Reviews",
                "Deals":"44% off"
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=monitors&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="gUuXy-")
                deals = data.find("div", class_="_3Ay6Sb")

                if names and price and description and review and deals:
                    item_details = {
                        "Item_Name": names.text if names else None,
                        "Price": price.text if price else None,
                        "Description": description.text if description else None,
                        "Review": review.text if review else None,
                        "Deals": deals.text if deals else None,
                    }

                    all_items.append(item_details)

            return all_items

        except:
            return None

    def ac(self):
        """
        Get the list of mobiles under 50K\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.ac()
        ```
        Return
        ```js
        [
            {
                "name":"Voltas 1.5 Ton 3 Star Split Inverter AC...",
                "price":"₹31,990",
                "description":"Annual Electricity Consumption: ....",
                "reviews":"218,092",
                "deals":"49% off"
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=ac&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="gUuXy-")
                deals = data.find("div", class_="_3Ay6Sb")

                if names and price and description and review and deals:
                    item_details = {
                        "Item_Name": names.text if names else None,
                        "Price": price.text if price else None,
                        "Description": description.text if description else None,
                        "Reviews": (
                            "".join(list(str(review.text).split(" ")[0])[2:])
                            if review
                            else None
                        ),
                        "Deals": deals.text if deals else None,
                    }

                    all_items.append(item_details)

            return all_items

        except:
            return None

    def refrigerator(self):
        """
        Get the list of mobiles under 50K\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.refrigerator()
        ```
        Return
        ```js
        [
            {
                "name":"realme TechLife 564 L Frost Free Side by Side Refrigerator",
                "price":"₹47,990",
                "description":"Advanced Inverter CompressorBuilt-in ...",
                "reviews":"3229",
                "deals":"46% off"
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=refrigerator&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="gUuXy-")
                deals = data.find("div", class_="_3Ay6Sb")

                if names and price and description and review and deals:
                    item_details = {
                        "Item_Name": names.text if names else None,
                        "Price": price.text if price else None,
                        "Description": description.text if description else None,
                        "Review": (
                            "".join(list(str(review.text).split(" ")[0])[2:])
                            if review
                            else None
                        ),
                        "Deals": deals.text if deals else None,
                    }

                    all_items.append(item_details)

            return all_items

        except:
            return None

    def vrbox(self):
        """
        Get the list of mobiles under `VRbox`\n
        Class - `Flipkart`\n
        Example -\n
        ```python
        item = Flipkart()
        item.vrbox()
        ```
        Return
        ```js
        [
            {
                "name":"'Cyphon CYPHON VR Glasses Box Set, Virtual Reality Sets",
                "price":"₹₹1,799",
                "reviews":"2",
                "delivery":"Free delivery"
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=vr+box&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_30jeq3")
                review = data.find("div", class_="_3LWZlK")
                delivery = data.find("div", class_="_2Tpdn3")

                if names and price and review and delivery:
                    item_details = {
                        "Item_Name": names.text if names else None,
                        "Price": price.text if price else None,
                        "Review": (
                            "".join(list(str(review.text).split(" ")[0])[2:])
                            if review
                            else None
                        ),
                        "Delivery": delivery.text if delivery else None,
                    }

                    all_items.append(item_details)

            return all_items

        except:
            return None

    def speakers():
        """
        Get the list of speakers.\n
        Class - `Flipkart`\n
        Example
        ```python
        item = Flipkart()
        item.speakers()
        ```
        Return
        ```js
        [
            {
                "name":"Intex IT-2616 BT 55 W Bluetooth Home Theatre",
                "price":"₹1,599",
                "color":"Black, 4.1 Channel"
                "reviews":"2",
                "delivery":"Free delivery",
                "offpercentage":"46%off"
            }
            ...
        ]
        ```
        """
        try:
            link = "https://www.flipkart.com/search?q=speaker&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"
            page = get(link, self.config)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_30jeq3")
                color = data.find("div", class_="_3Djpdu")
                review = data.find("div", class_="_3LWZlK")
                delivery = data.find("div", class_="_2Tpdn3")
                offpercentage = data.find("div", class_="_3Ay6Sb")

                if names and price and review and delivery:
                    item_details = {
                        "Item_Name": names.text if names else None,
                        "Price": price.text if price else None,
                        "Color": color.text if color else None,
                        "Review": (
                            "".join(list(str(review.text).split(" ")[0])[2:])
                            if review
                            else None
                        ),
                        "Delivery": delivery.text if delivery else None,
                        "Off_Percentage": offpercentage.text if offpercentage else None,
                    }

                    all_items.append(item_details)

            return all_items

        except:
            return None
