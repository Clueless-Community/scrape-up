from bs4 import BeautifulSoup
import requests
from scrape_up.config.request_config import RequestConfig, get


class Product:
    """Class for fetching and retrieving product details from Amazon."""

    def __init__(self, product_name: str, *, config: RequestConfig = RequestConfig()):
        """
        Initialize the Product object with a product name.

        Args:
            product_name (str): The name of the product.
        """
        self.product_name = product_name
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def fetch_product_page(self):
        """
        Fetch the HTML content of the Amazon search page for the product.

        Returns:
            BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the search page.

        Raises:
            Exception: If there is an error fetching the page.
        """
        try:
            product_name = self.product_name.replace(" ", "+")
            url = f"https://www.amazon.in/s?k={product_name}"
            r = get(url, self.config)
            r.raise_for_status()  # Raise HTTPError for bad responses
            return BeautifulSoup(r.content, "html.parser")
        except requests.RequestException as e:
            raise Exception(f"Error fetching product page: {str(e)}")

    def get_product(self):
        """
        Get the link to the product from the search page.

        Returns:
            dict: A dictionary containing the product link and a message indicating success.

        Raises:
            Exception: If there is an error fetching the product link.
        """
        try:
            soup = self.fetch_product_page()
            product = soup.find("div", {"class": "s-result-item"})
            if product:
                product_link = product.find("a", {"class": "a-link-normal"})["href"]
                product_link = "https://www.amazon.in" + product_link
                return {
                    "data": product_link,
                    "message": "Product data has been fetched",
                }
            else:
                return {
                    "data": None,
                    "message": "Product not found",
                }
        except Exception as e:
            raise Exception(f"Unable to fetch product's data: {str(e)}")

    def get_product_details(self):
        """
        Get details of the product from the product page.

        Returns:
            dict: A dictionary containing product details and a message indicating success.

        Raises:
            Exception: If there is an error fetching the product details.
        """
        try:
            product_link = self.get_product()["data"]
            r = get(product_link, self.config)
            r.raise_for_status()  # Raise HTTPError for bad responses
            soup = BeautifulSoup(r.content, "html.parser")
            product_name = soup.find("span", {"id": "productTitle"}).text.strip()
            product_price = soup.find("span", {"class": "a-price-whole"}).text.strip()
            product_rating = soup.find("span", {"class": "a-icon-alt"}).text.strip()
            product_details = {
                "product_name": product_name,
                "product_price": product_price,
                "product_rating": product_rating,
                "product_link": product_link,
            }
            return {
                "data": product_details,
                "message": "Product detail has been fetched",
            }
        except Exception as e:
            raise Exception(f"Unable to fetch product detail: {str(e)}")

    def get_product_image(self):
        """
        Get the URL of the product image from the product page.

        Returns:
            dict: A dictionary containing the product image URL and a message indicating success.

        Raises:
            Exception: If there is an error fetching the product image.
        """
        try:
            product_link = self.get_product()["data"]
            r = get(product_link, self.config)
            r.raise_for_status()  # Raise HTTPError for bad responses
            soup = BeautifulSoup(r.content, "html.parser")
            product_image = soup.find("div", {"id": "imgTagWrapperId"}).find("img")[
                "data-old-hires"
            ]
            return {
                "data": product_image,
                "message": "Product image has been fetched",
            }
        except Exception as e:
            raise Exception(f"Unable to fetch product image: {str(e)}")

    def customer_review(self):
        """
        Get customer reviews of the product from the product page.

        Returns:
            dict: A dictionary containing the product reviews and a message indicating success.

        Raises:
            Exception: If there is an error fetching the product reviews.
        """
        try:
            product_link = self.get_product()["data"]
            r = get(product_link, self.config)
            r.raise_for_status()  # Raise HTTPError for bad responses
            soup = BeautifulSoup(r.content, "html.parser")
            review_elements = soup.find_all("div", {"data-hook": "review"})
            reviews = []
            for review_element in review_elements:
                reviewer_name = review_element.find(
                    "span", {"class": "a-profile-name"}
                ).text
                rating = (
                    review_element.find("i", {"class": "a-icon-star"})
                    .find("span", {"class": "a-icon-alt"})
                    .text
                )
                review_title = review_element.find(
                    "a", {"data-hook": "review-title"}
                ).text.strip()
                review_date = review_element.find(
                    "span", {"data-hook": "review-date"}
                ).text
                review_text = review_element.find(
                    "span", {"data-hook": "review-body"}
                ).text.strip()
                review = {
                    "reviewer_name": reviewer_name,
                    "rating": rating,
                    "review_title": review_title,
                    "review_date": review_date,
                    "review_text": review_text,
                }
                reviews.append(review)
            return {
                "data": reviews,
                "message": "Product reviews have been fetched",
            }
        except Exception as e:
            raise Exception(f"Unable to fetch product reviews: {str(e)}")
