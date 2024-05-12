import requests
from bs4 import BeautifulSoup


class Product:
    def __init__(self, product_name: str):
        self.product_name = product_name

    def fetch_product_page(self):
        try:
            product_name = self.product_name.replace(" ", "+")
            url = f"https://www.amazon.in/s?k={product_name}"
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(url, headers=headers)
            return BeautifulSoup(r.content, "html.parser")
        except Exception as e:
            raise e

    def get_product(self):
        try:
            soup = self.fetch_product_page()
            product = soup.find("div", {"class": "s-product-image-container"})
            product_link = product.find("a", {"class": "a-link-normal"})["href"]
            product_link = "https://www.amazon.in" + product_link
            return {
                "data": product_link,
                "message": "Product data has been fetched",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Unable to fetch product's data: {str(e)}",
            }

    def get_product_details(self):
        try:
            soup = self.fetch_product_page()
            product_link = self.get_product()["data"]
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            product_name = soup.find("span", {"id": "productTitle"}).text.strip()
            product_price = soup.find("span", {"class": "a-price-whole"}).text.strip()
            product_rating = soup.find("span", {"class": "a-size-base a-color-base"}).text.strip()
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
            return {
                "data": None,
                "message": f"Unable to fetch product detail: {str(e)}",
            }

    def get_product_image(self):
        try:
            soup = self.fetch_product_page()
            product_link = self.get_product()["data"]
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            product_image = soup.find("img", {"class": "a-dynamic-image a-stretch-horizontal"})["src"]
            return {
                "data": product_image,
                "message": "Product image has been fetched",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Unable to fetch product image: {str(e)}",
            }

    def customer_review(self):
        try:
            soup = self.fetch_product_page()
            product_link = self.get_product()["data"]
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            review_elements = soup.find_all("div", {"data-hook": "review"})
            reviews = []
            for review_element in review_elements:
                reviewer_name = review_element.find("span", {"class": "a-profile-name"}).text
                rating = review_element.find("i", {"class": "a-icon-star"}).find("span", {"class": "a-icon-alt"}).text
                review_title = review_element.find("a", {"data-hook": "review-title"}).text.strip()
                review_date = review_element.find("span", {"data-hook": "review-date"}).text
                review_text = review_element.find("span", {"data-hook": "review-body"}).text.strip()
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
            return {
                "data": None,
                "message": f"Unable to fetch product reviews: {str(e)}",
            }
