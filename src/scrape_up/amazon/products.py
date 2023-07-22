import requests
from bs4 import BeautifulSoup


# scraping amazon product page
class Product:
    def __init__(self, product_name: str):
        self.product_name = product_name

    def get_product(self):
        """
        Class - `Product`\n
        Example -\n
        ```python
        product = Product(product_name="watch")
        product.get_product()
        ```
        Return\n
        ```python
        return
        {
            "data": product_link,
            "message": f"Product data has been fetched",
        }
        ```
        """
        try:
            product_name = self.product_name
            product_name = product_name.replace(" ", "+")
            url = f"https://www.amazon.in/s?k={product_name}"
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            product = soup.find("div", {"class": "s-product-image-container"})
            product_link = product.find("a", {"class": "a-link-normal"})["href"]
            product_link = "https://www.amazon.in" + product_link
            return {
                "data": product_link,
                "message": f"Product data has been fetched",
            }
        except:
            return {
                "data": None,
                "message": f"Unable to fetch product's data",
            }

    # Get product details
    def get_product_details(self):
        """
        Class - `Product`\n
        Example -\n
        ```python
        product = Product(product_name="watch")
        product.get_product_details()
        ```
        Return\n
        ```python
        return
        {
            "data": product_details,
            "message": f"Product detail has been fetched",
        }
        ```
        """
        try:
            product_link = self.get_product()["data"]
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            product_name = soup.find("span", {"id": "productTitle"}).text.strip()
            product_price = soup.find("span", {"class": "a-price-whole"}).text.strip()
            product_rating = soup.find(
                "span", {"class": "a-size-base a-color-base"}
            ).text.strip()
            product_details = {
                "product_name": product_name,
                "product_price": product_price,
                "product_rating": product_rating,
                "product_link": product_link,
            }
            return {
                "data": product_details,
                "message": f"Product detail has been fetched",
            }
        except:
            return {
                "data": None,
                "message": f"Unable to fetch product detail",
            }

    # Get product image
    def get_product_image(self):
        """
        Class - `Product`\n
        Example -\n
        ```python
        product = Product(product_name="watch")
        product.get_product_image()
        ```
        Return\n
        ```python
        return
        {
            "data": product_image,
            "message": f"Product image has been fetched",
        }
        ```
        """
        try:
            product_link = self.get_product()["data"]
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            product_image = soup.find(
                "img", {"class": "a-dynamic-image a-stretch-horizontal"}
            )["src"]

            return {
                "data": product_image,
                "message": f"Product image has been fetched",
            }
        except:
            return {
                "data": None,
                "message": f"Unable to fetch product image",
            }

    # Get customer reviews
    def customer_review(self):
        """
        Class - `Product`\n
        Example -\n
        ```python
        product = Product(product_name="watch")
        product.customer_review()
        ```
        Return\n
        ```python
        return
        {
            "data": review,
            "message": f"Product review has been fetched",
        }
        ```
        """
        try:
            product_link = self.get_product()["data"]
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")

            review_elements = soup.find_all("div", {"data-hook": "review"})

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
                review = [reviewer_name, rating, review_title, review_date, review_text]
            return {
                "data": review,
                "message": f"Product review has been fetched",
            }
        except:
            return {
                "data": None,
                "message": f"Unable to fetch product review",
            }
    #Get BestSeller Products
    def bestsellers(self):
        """
        Class - `Product`\n
        Example -\n
        ```python
        product = Product(product_type)
        product_type = "baby"
        product.bestsellers()
        product_type = ["baby", "electronics", "luggage", "beauty", "books", "automotive", "computers", "garden", "gift-cards", "grocery".
        "industrial", "jewelry", "musical-instruments", "office", "pet-supplies", "shoes", "sports", "toys", "watches"]   
        ```
        Return\n
        ```python
        return
        {
            "data": bestsellers_list,
            "message": f"Bestsellers data has been fetched",
        }
        ```
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            url = f"https://www.amazon.in/gp/bestsellers/{self.product_name}/ref=zg_bs_nav_0"
            html_text = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html_text, "lxml")

            bestsellers_list = []
            container = soup.find("div", {"class": "p13n-gridRow _cDEzb_grid-row_3Cywl"})


            for items in container.find_all("div", {"id": "gridItemRoot"}):
                title = items.find("div", {"class": "_cDEzb_p13n-sc-css-line-clamp-4_2q2cc"})
                price = items.find("span", {"class": "a-size-base a-color-price"})
                if not title:
                    title = items.find("div", {"class": "_cDEzb_p13n-sc-css-line-clamp-3_g3dy1"})
                    price = items.find("span", {"class": "a-size-base"})
                stars = items.find("span", {"class": "a-icon-alt"})
                if stars is None:
                    stars = "Rating not available"
                else:
                    stars = stars.text.split()[0]
                link = items.find("a", {"class": "a-link-normal"}, href=True)
                url = "https://www.amazon.in/" + link['href']
                if not price:
                    price = "Information not available"
                else:
                    price = price.text
                products = {
                    "Title": title.text,
                    "Rating(out of 5)": stars,
                    "Price(in rupees)": price,
                    "Link": url,
                }
                bestsellers_list.append(products)

            return {
                "data": bestsellers_list,
                "message": f"Bestsellers data has been fetched",
            }
        except:
            return {
                "data": None,
                "message": f"Unable to fetch bestsellers data",
            }
