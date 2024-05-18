from bs4 import BeautifulSoup
import re

from scrape_up.config.request_config import RequestConfig, get


class Flyrobu:
    """
    Create an instance of `Flyrobu` class.

    ```python
    flyrobu = Flyrobu()
    print(flyrobu.search("arduino"))
    ```

    | Methods             | Details                                                                                                         |
    | ------------------- | --------------------------------------------------------------------------------------------------------------- |
    | `.search(keyword)`  | Returns the json data of all the details related to search with informing about the total amount of items found |
    | `.get_product_details(product_name)` | Returns the json data of the product details based on the given `product_name` |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.base_url = "https://www.flyrobo.in"
        self.outputs = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def __get_html_content(self, url: str):
        response = get(url, self.config)
        response.raise_for_status()
        return response.content

    def __get_soup(self, url: str):
        request_content = self.__get_html_content(url)
        soup = BeautifulSoup(request_content, "html.parser")
        return soup

    def __is_matching_title(self, title: str, search_item: str):
        search_words = search_item.lower().split()
        return all(word in title.lower() for word in search_words)

    def __scrape_results(self, soup: BeautifulSoup, search_item: str):
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
                    price_element = price_new_element or result.select_one(
                        ".price-normal"
                    )
                    price = (
                        price_element.text.strip().replace("₹", "Rs. ")
                        if price_element
                        else None
                    )

                    brand_name = (
                        result.select_one(".stat-1 a").text.strip()
                        if result.select_one(".stat-1 a")
                        else None
                    )
                    image = (
                        result.select_one(".image img")["src"]
                        if result.select_one(".image img")
                        else None
                    )
                    description = (
                        result.select_one(".description").text.strip()
                        if result.select_one(".description")
                        else None
                    )
                    rating_stars = result.select(".rating-stars .fa-star")
                    rating = len(rating_stars)
                    model_id = (
                        result.select_one(".stat-2 span:nth-of-type(2)").text.strip()
                        if result.select_one(".stat-2 span:nth-of-type(2)")
                        else None
                    )
                    link = title_element["href"] if title_element else None

                    self.outputs.append(
                        {
                            "title": title,
                            "price": price,
                            "brand_name": brand_name,
                            "image": image,
                            "description": description,
                            "rating": rating,
                            "model_id": model_id,
                            "link": link,
                        }
                    )

            except Exception as e:
                return None

    def search(self, keyword: str):
        """
        Class - `Flyrobu`\n
        Example -\n
        ```python
        flyrobu = Flyrobu()
        results = flyrobu.search("arduino")
        print(results)
        ```
        Return\n
        ```js
        [
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
        ```
        """
        url = f"{self.base_url}/index.php?route=product/search&search={keyword}&description=true&limit=100"
        try:
            while True:
                try:
                    soup = self.__get_soup(url)
                    self.__scrape_results(soup, keyword)

                    next_page = soup.find("ul", class_="pagination").find(
                        "a", class_="next"
                    )
                    if next_page:
                        url = str(next_page["href"])
                    else:
                        break
                except:
                    return None

            result = self.outputs
            return result
        except:
            return None

    def get_product_details(self, product_name):
        """
        Retrieve Detailed Product Description and Specification based on the given `product_name`.

        Parameters required: \n
        `product_name: str`: The name of the product to fetch details for.

        Example:
        ```python
        flyrobu = Flyrobu()
        product_details = flyrobu.get_product_details(product_name)
        ```

        Output:
        ```js
        {
            "Description": "E-Bike Power Lock Ignition Key Switch is brand new and unused and comes with 2 keys. E-Bike Power Lock Ignition Key Switch has 2 Female Pin, Plastic Make.\nIt is Suitable for MY1016 controllers.\n\n \nFeatures:\n     \n\nEasy installation\nProtect the security\nDesigned with a reliable ignition switch locking mechanism\nDurable, convenient to use",
            "Features": [
                "Easy installation",
                "Protect the security",
                "Designed with a reliable ignition switch locking mechanism",
                "Durable, convenient to use"
            ],
            "Technical Details": {
                "Cable Length": "27 cm",
                "Connector": "2 Pin Female"
            },
            "Current Price": 349,
            "Original Price": 399,
            "Image": "https://www.flyrobo.in/image/cache/catalog/e-bile-power-lock-ignition-key-switch/e-bile-power-lock-ignition-key-switch-2-550x550.jpeg",
            "Package Includes": "1 x E-Bike Power Lock Ignition Key Switch"
        }
        ```
        """
        try:
            product_url = f"{self.base_url}/{product_name}"

            soup = self.__get_soup(product_url)
            product_details = {}

            # Extract the product description and features
            description = (
                soup.find("div", class_="product_extra-242").find("div").text.strip()
            )
            features_list = (
                soup.find("div", class_="product_extra-242").find("ul").find_all("li")
            )
            features = [feature.text.strip() for feature in features_list]

            product_details["Description"] = description
            product_details["Features"] = features

            # Extract the technical specifications
            technical_details_table = soup.find("table", class_="table-bordered")
            technical_details = {}
            if technical_details_table:
                rows = technical_details_table.find_all("tr")
                for row in rows[1:]:
                    attribute_name = row.find(
                        "td", class_="attribute_name"
                    ).b.text.strip()
                    attribute_value = row.find(
                        "td", class_="attribute_value"
                    ).p.text.strip()
                    technical_details[attribute_name] = attribute_value

            product_details["Technical Details"] = technical_details

            # Extract the price details
            price_section = soup.find("div", class_="price-group")
            current_price_elem = price_section.find("div", class_="product-price-new")
            original_price_elem = price_section.find("div", class_="product-price-old")

            # Check if both current_price_elem and original_price_elem are None, then try to find the "product-price" element
            if current_price_elem is None and original_price_elem is None:
                fallback_price_elem = price_section.find("div", class_="product-price")
                if fallback_price_elem:
                    current_price = fallback_price_elem.text.strip()
                    original_price = None
                else:
                    current_price = None
                    original_price = None
            else:
                current_price = (
                    current_price_elem.text.strip() if current_price_elem else None
                )
                original_price = (
                    original_price_elem.text.strip() if original_price_elem else None
                )

            # Remove the Rupee symbol and convert the prices to integers
            if current_price:
                current_price = int(current_price.replace("₹", "").replace(",", ""))
                product_details["Current Price"] = current_price

            if original_price:
                original_price = int(original_price.replace("₹", "").replace(",", ""))
                product_details["Original Price"] = original_price

            # Extract the image URL
            image_div = soup.find("div", class_="swiper-wrapper")
            image_url = image_div.find("img")["src"]
            product_details["Image"] = image_url

            # Extract the "Package Includes" details from the description using regular expression
            package_includes_pattern = r"Package Includes:\s*(.*)"
            match = re.search(package_includes_pattern, description)
            if match:
                package_includes_text = match.group(1).strip()
                product_details["Package Includes"] = package_includes_text

                # Remove the "Package Includes" part from the description
                description = re.sub(package_includes_pattern, "", description).strip()
                product_details["Description"] = description

            return product_details
        except:
            return None
