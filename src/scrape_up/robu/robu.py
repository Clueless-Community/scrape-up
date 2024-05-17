from bs4 import BeautifulSoup
import requests

from scrape_up.config.request_config import RequestConfig, get


class Robu:
    """
    Create a new instance of the `Robu` class\n
    ```python
    robu = Robu()
    ```
    | Methods     | Details                                                                                                         |
    | ----------- | --------------------------------------------------------------------------------------------------------------- |
    | `.search()` | Returns the json data of all the details related to search with informing about the total amount of items found |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.base_url = "https://www.robo.in"
        self.outputs = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def __get_html_content(self, url: str):
        if self.headers is None:
            response = get(url, self.config)
            response.raise_for_status()
            return response.content

    def __get_soup(self, url):
        request_content = self.__get_html_content(url)
        soup = BeautifulSoup(request_content, "html.parser")
        return soup

    def __is_matching_title(self, title, search_item):
        search_words = search_item.lower().split()
        return all(word in title.lower() for word in search_words)

    def __scrape_results(self, soup, search_item):
        results_container = soup.find("ul", {"class": "products"})
        results = results_container.find_all("li")

        for result in results:
            try:
                title_element = result.find(
                    "h2", class_="woocommerce-loop-product__title"
                )
                title = title_element.text.strip() if title_element else None

                if title and self.__is_matching_title(title, search_item):
                    price_element = result.find(
                        "span", class_="woocommerce-Price-amount amount"
                    )
                    price = (
                        price_element.text.strip().split("\u20b9\u00a0")[-1]
                        if price_element
                        else None
                    )

                    link_element = result.find(
                        "a",
                        class_="woocommerce-LoopProduct-link woocommerce-loop-product__link",
                    )
                    link = link_element["href"] if link_element else None

                    img_element = result.find(
                        "img",
                        class_="attachment-woocommerce_thumbnail size-woocommerce_thumbnail",
                    )
                    img = img_element["src"] if img_element else None

                    rating_element = result.find("div", class_="product-rating")
                    rating = rating_element.text.strip() if rating_element else None

                    short_description_element = result.find(
                        "div", class_="product-short-description"
                    )
                    short_description = (
                        short_description_element.text.strip().split("\n")
                        if short_description_element
                        else None
                    )

                    product_id_element = result.find("div", class_="product-sku")
                    product_id = (
                        product_id_element.text.strip() if product_id_element else None
                    )

                    self.outputs.append(
                        {
                            "title": title,
                            "price": "Rs. " + price,
                            "link": link,
                            "img": img,
                            "rating": rating,
                            "short_description": short_description,
                            "product_id": product_id,
                        }
                    )
            except Exception as e:
                print(f"Exception occurred during Robu scraping: {e}")
                continue

    def search(self, search_item, number=-1, orderby="relevance"):
        """
        Class - `RobuSearch`\n
        Args:
        + `search_item` (str): The search item to match.
        + `number` (int): The number of the items to search [ Options : 20 | 40 | 80 | 160 | 320 | -1 ] Default -1 (all)
        + `orderby` (str): The order by which the items will be returned [ Options : "relevance" | "popularity" | "rating" | "date" | "price" | "price-desc" ] Default : "relevance"
        Example -
        ```python
        robu = Robu()
        robu.search("arduino")
        ```
        Return
        ```js
        [
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
        ]
        ```
        """
        if number not in [20, 40, 80, 160, 320, -1]:
            raise ValueError("Number must be from 20 | 40 | 80 | 160 | 320 | -1")
        if orderby not in [
            "relevance",
            "popularity",
            "rating",
            "date",
            "price",
            "price-desc",
        ]:
            raise ValueError(
                "Order by must be one of 'relevance','popularity','rating','date','price','price-desc'"
            )
        try:
            url = f"https://robu.in/?s={search_item}&product_cat=0&post_type=product&ppp={number}&orderby={orderby}"
            soup = self.__get_soup(url)
            self.__scrape_results(soup, search_item)
        except requests.exceptions.RequestException as e:
            return None

        except AttributeError as e:
            return None

        except Exception as e:
            return None

        result = self.outputs

        return result
