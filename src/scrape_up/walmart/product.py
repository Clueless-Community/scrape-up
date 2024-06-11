from bs4 import BeautifulSoup
import requests
from scrape_up.config.request_config import RequestConfig, get

class WalmartProduct:
    """
    Class for fetching and retrieving product details from Walmart.
        Create an instance of 'WalmartProduct' class
        product = WalmartProduct("example-product-name") 
        
        | Method                         | Details                                                                           |
        | ------------------------------ | --------------------------------------------------------------------------------- |
        | `get_product()`                | Get the link to the product from the search page.                                 |
        | `get_product_details()`        | Get details of the product from the product page.                                 |
        | `get_product_image()`          | Get the URL of the product image from the product page.                           |
        | `customer_review()`            | Get customer reviews of the product from the product page.                        |

    """


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
        Fetch the HTML content of the Walmart search page for the product.

        Returns:
            BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the search page.

        Raises:
            Exception: If there is an error fetching the page.
        """
        try:
            product_name = self.product_name.replace(" ", "+")
            url = f"https://www.walmart.com/search/?query={product_name}"
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
            product = soup.find("div", {"data-tl-id": "ProductTileGridView"})
            if product:
                product_link = product.find("a", {"class": "product-title-link"})["href"]
                product_link = "https://www.walmart.com" + product_link
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
        product_link = self.fetch_product_page()
        if product_link is None:
            raise Exception("Product link could not be fetched")
        try:
            r = get(product_link, self.config)
            r.raise_for_status()  # Raise HTTPError for bad responses
            soup = BeautifulSoup(r.content, "html.parser")
            product_name = soup.find("h1", {"class": "prod-ProductTitle"}).text.strip()
            product_price = soup.find("span", {"class": "price-group"}).text.strip()
            product_rating = soup.find("span", {"class": "ReviewsHeader-ratingPrefix"}).text.strip()
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
            product_image = soup.find("img", {"class": "hover-zoom-hero-image"})["src"]
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
            review_elements = soup.find_all("div", {"class": "review"})
            reviews = []
            for review_element in review_elements:
                reviewer_name = review_element.find(
                    "span", {"class": "review-footer-userNickname"}
                ).text
                rating = (
                    review_element.find("span", {"class": "seo-avg-rating"}).text
                )
                review_title = review_element.find(
                    "h3", {"class": "review-title"}
                ).text.strip()
                review_date = review_element.find(
                    "span", {"class": "review-date-submissionTime"}
                ).text
                review_text = review_element.find(
                    "div", {"class": "review-text"}
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
