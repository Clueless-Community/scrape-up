import json

import requests
from bs4 import BeautifulSoup


class Robu:
    def __init__(self):
        """
        Create an instance of the `Robu` class.

        Methods:
            search(keyword): Returns all the search items from the Robu site.
        """
        self.base_url = "https://www.robo.in"
        self.outputs = []

    def __get_html_content(self, url, headers=None):
        """
        Fetches the HTML content of the given URL.

        Args:
            url (str): The URL to fetch the content from.
            headers (dict, optional): Headers to be included in the request. Defaults to None.

        Returns:
            bytes: The HTML content of the URL.
        """
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }

        session = requests.Session()
        session.headers.update(headers)
        response = session.get(url)
        response.raise_for_status()
        return response.content

    def __get_soup(self, url):
        """
        Parses the HTML content of the given URL using BeautifulSoup.

        Args:
            url (str): The URL to parse the content from.

        Returns:
            BeautifulSoup: Parsed HTML content.
        """
        request_content = self.__get_html_content(url)
        soup = BeautifulSoup(request_content, 'html.parser')
        return soup

    def __is_matching_title(self, title, search_item):
        """
        Checks if the title matches the search item.

        Args:
            title (str): The title to check.
            search_item (str): The search item to match.

        Returns:
            bool: True if the title matches the search item, False otherwise.
        """
        search_words = search_item.lower().split()
        return all(word in title.lower() for word in search_words)

    def __scrape_results(self, soup, search_item):
        """
        Scrapes the search results with the total amount of items from the soup object.

        Args:
            soup (BeautifulSoup): Parsed HTML content.
            search_item (str): The search item to match.
        """
        results_container = soup.find("ul", {"class": 'products'})
        results = results_container.find_all("li")

        for result in results:
            try:
                title_element = result.find("h2", class_="woocommerce-loop-product__title")
                title = title_element.text.strip() if title_element else None

                if title and self.__is_matching_title(title, search_item):
                    price_element = result.find("span", class_="woocommerce-Price-amount amount")
                    price = price_element.text.strip().split('\u20b9\u00a0')[-1] if price_element else None

                    link_element = result.find("a",
                                               class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")
                    link = link_element["href"] if link_element else None

                    img_element = result.find("img",
                                              class_="attachment-woocommerce_thumbnail size-woocommerce_thumbnail")
                    img = img_element["src"] if img_element else None

                    rating_element = result.find("div", class_="product-rating")
                    rating = rating_element.text.strip() if rating_element else None

                    short_description_element = result.find("div", class_="product-short-description")
                    short_description = short_description_element.text.strip().split(
                        '\n') if short_description_element else None

                    product_id_element = result.find("div", class_="product-sku")
                    product_id = product_id_element.text.strip() if product_id_element else None

                    self.outputs.append({
                        "title": title,
                        "price": "Rs. " + price,
                        "link": link,
                        "img": img,
                        "rating": rating,
                        "short_description": short_description,
                        "product_id": product_id
                    })
            except Exception as e:
                print(f"Exception occurred during Robu scraping: {e}")
                continue

    def search(self, search_item, number=-1, orderby="relevance"):
        """
        Class - `RobuSearch`\n
        Example -\n
        ```python\n
        robu = Robu()\n
        print(robu.search("arduino"))
        ```
        Return\n
        ```python
        return
        [
            {
            "Total Items": 368,
            "Result": [
                {
                    "title": "Arduino Uno R3 with Cable",
                    "price": "Rs. 631.68",
                    "link": "https://robu.in/product/arduino-uno-r3/",
                    "img": "https://robu.in/wp-content/uploads/2015/11/SKU-6337-314x252.png",
                    "rating": "Rated 5.00 out of 5 (25)",
                    "short_description": [
                        "Micro-controller : ATmega328.",
                        "Operating Voltage : 5V.",
                        "Input Voltage (recommended) : 7-12V.",
                        "Digital I/O Pins : 14 (of which 6 provide PWM output).",
                        "Analog Input Pins : 6."
                    ],
                    "product_id": "SKU: 6337"
                },
            }
        ]


        Args:
            search_item (str): The search item to match.
            number (int): The number of the items to search [ Options : 20 | 40 | 80 | 160 | 320 | -1 ] Default -1 (all)
            orderby (str): The order by which the items will be returned [ Options : "relevance" | "popularity" | "rating" | "date" | "price" | "price-desc" ] Default : "relevance"
        """
        if number not in [20, 40, 80, 160, 320, -1]:
            raise ValueError("Number must be from 20 | 40 | 80 | 160 | 320 | -1")
        if orderby not in ["relevance", "popularity", "rating", "date", "price", "price-desc"]:
            raise ValueError("Order by must be one of 'relevance','popularity','rating','date','price','price-desc'")
        try:
            url = f"https://robu.in/?s={search_item}&product_cat=0&post_type=product&ppp={number}&orderby={orderby}"
            soup = self.__get_soup(url)
            self.__scrape_results(soup, search_item)
        except requests.exceptions.RequestException as e:
            print(f"Request error: {str(e)}")

        except AttributeError as e:
            print(f"Attribute error: {str(e)}")

        except Exception as e:
            print(f"Error occurred: {str(e)}")

        result = [{'Total Items': len(self.outputs), "Result": self.outputs}]

        return json.dumps(result, indent=4)
