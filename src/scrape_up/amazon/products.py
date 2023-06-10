import requests
from bs4 import BeautifulSoup


#scraping amazon product page
class Product:
    def __init__(self, product_name: str):
        self.product_name = product_name
        
    def get_product(self):
        # try:
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
        return product_link
        
#Get product details    
    def get_product_details(self):
        try:
            product_link = self.get_product()
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
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
                "product_link": product_link    
            }
            return product_details
        except:
            return "Product details not found."
    
 #Get product image   
    def get_product_image(self):
        try:
            product_link = self.get_product()
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            product_image = soup.find("img", {"class": "a-dynamic-image a-stretch-horizontal"})["src"]
            return product_image
        except:
            return "Product image not found."
        
#Get customer reviews      
    def customer_review(self):
        try: 
            product_link = self.get_product()
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
            r = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            
            review_elements = soup.find_all('div', {'data-hook': 'review'})

            for review_element in review_elements:
                reviewer_name = review_element.find('span', {'class': 'a-profile-name'}).text
                rating = review_element.find('i', {'class': 'a-icon-star'}).find('span', {'class': 'a-icon-alt'}).text
                review_title = review_element.find('a', {'data-hook': 'review-title'}).text.strip()
                review_date = review_element.find('span', {'data-hook': 'review-date'}).text
                review_text = review_element.find('span', {'data-hook': 'review-body'}).text.strip()
                review=[reviewer_name, rating, review_title, review_date, review_text]
            return review
        except:
            return "Customer review not found."    
    
