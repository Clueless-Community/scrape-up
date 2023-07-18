import json
import time

import requests
from bs4 import BeautifulSoup


class Flyrobu:
    def __init__(self):
        """
        Create an instance of the `FlyRobu` class.

        Methods:
            search(keyword): Returns all the search items from the FlyRobu site.
        """
        self.base_url = "https://www.flyrobo.in"
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
        results_container = soup.find("div", class_="product-grid")
        results = results_container.find_all("div", class_="product-layout")

        for result in results:
            try:
                title_element = result.select_one(".name a")
                if title_element:
                    title = title_element.text.strip()
                    if not self.__is_matching_title(title, search_item):
                        continue

                    price_new_element = result.select_one(".price-new")
                    price_element = price_new_element or result.select_one(".price-normal")
                    price = price_element.text.strip().replace("₹", "Rs. ") if price_element else None

                    brand_name = result.select_one(".stat-1 a").text.strip() if result.select_one(".stat-1 a") else None
                    image = result.select_one(".image img")["src"] if result.select_one(".image img") else None
                    description = result.select_one(".description").text.strip() if result.select_one(
                        ".description") else None
                    rating_stars = result.select(".rating-stars .fa-star")
                    rating = len(rating_stars)
                    model_id = result.select_one(".stat-2 span:nth-of-type(2)").text.strip() if result.select_one(
                        ".stat-2 span:nth-of-type(2)") else None
                    link = title_element["href"] if title_element else None

                    self.outputs.append({
                        "title": title,
                        "price": price,
                        "brand_name": brand_name,
                        "image": image,
                        "description": description,
                        "rating": rating,
                        "model_id": model_id,
                        "link": link,
                    })

            except Exception as e:
                print(f"Error scraping result: {str(e)}")

    def search(self, keyword):
        """
        Class - `Flyrobu`\n
        Example -\n
        ```python
        from flyrobu import Flyrobu

        flyrobu = Flyrobu()
        results = flyrobu.search("arduino")
        print(results)
        ```
        Return\n
        ```python
        return
        [
            {
                "Total Items": 107,
                "Result": [
                {
                    "title": "Arduino Uno R3 Compatible board + Cable for Arduino Uno",
                    "price": "Rs. 777",
                    "brand_name": "Arduino",
                    "image": "https://www.flyrobo.in/image/cache/catalog/product/arduino-uno-r3-+-cable-for-arduino-uno-250x250.jpg",
                    "description": "The Arduino Uno R3 Compatible board is an electronic hardware device used to build and program electronic circuits and projects. The board is based on the ATmega3:
                    "rating": 4,
                    "model_id": "FRC-01-401",
                    "link": "https://www.flyrobo.io/productsn/arduino-uno-r3-compatible-board-plus-cable-for-arduino-uno-1?search-arduino&description=true"
                },
            }
        ]
        """
        url = f"{self.base_url}/index.php?route=product/search&search={keyword}&description=true&limit=100"

        while True:
            try:
                soup = self.__get_soup(url)
                self.__scrape_results(soup, keyword)

                next_page = soup.find("ul", class_="pagination").find("a", class_="next")
                if next_page:
                    url = next_page['href']
                    time.sleep(2)
                else:
                    break

            except requests.exceptions.RequestException as e:
                print(f"Request error: {str(e)}")
            except AttributeError as e:
                print(f"Attribute error: {str(e)}")
            except Exception as e:
                print(f"Error occurred: {str(e)}")

        result = [{'Total Items': len(self.outputs), "Result": self.outputs}]

        return json.dumps(result, indent=4)
