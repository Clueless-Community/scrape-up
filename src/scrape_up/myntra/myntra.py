from selenium import webdriver
from selenium.webdriver.common.by import By

# Path to the chromedriver executable
chromedriver_path = 'PATH_TO_CHROMEDRIVER'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)


class Product:
    def __init__(self, product_name: str):
        self.product_name =product_name
    
    def get_product(self):
        try:
            product_name = self.product_name
            url = f"https://www.myntra.com/search/?q={product_name}"
            driver.get(url)
            lst=[]
            results_ul = driver.find_element(By.CSS_SELECTOR, 'ul.results-base')
            product_li_list = results_ul.find_elements(By.CSS_SELECTOR, 'li.product-base')

            # Extract brand and price information from each <li> element
            for product_li in product_li_list:
                brand = product_li.find_element(By.CSS_SELECTOR, 'h3.product-brand').text
                price = product_li.find_element(By.CSS_SELECTOR, 'div.product-price').text
                lst.append({
                    "product_name": product_name,
                    "price": price,
                    "brand": brand
                })
            driver.quit()

            return lst
        except:
            return "No product found"

    def get_description(self, product_link):
        try:
            driver.get(product_link)
            description_element = driver.find_element(By.CSS_SELECTOR, 'h1.pdp-name')
            description = description_element.text
            return description

        except:
            return "No description found"