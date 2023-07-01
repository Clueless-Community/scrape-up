from bs4 import BeautifulSoup

class Amazon:
    def __init__(self, html_file):
        """
        Initialize the Amazon class.
        
        Parameters:
        - html_file: The path to the HTML file to be parsed.
        """
        self.html_file = html_file
        self.soup = None
    
    def read_html_file(self):
        """
        Read the HTML file and parse it using Beautiful Soup.
        """
        try:
            with open(self.html_file, "r", encoding="utf-8") as file:
                html = file.read()
            self.soup = BeautifulSoup(html, "html.parser")
        except FileNotFoundError:
            print("HTML file not found.")
        except Exception as e:
            print("Error occurred while reading the HTML file:", str(e))
    
    def get_product_name(self, div):
        """
        Extract the product name from the given div.
        
        Parameters:
        - div: The div element containing the product information.
        
        Returns:
        - The product name.
        """
        name_span = div.find("span", class_="a-size-medium a-color-base a-text-normal")
        return name_span.text.strip() if name_span else ""
    
    def get_product_price(self, div):
        """
        Extract the product price from the given div.
        
        Parameters:
        - div: The div element containing the product information.
        
        Returns:
        - The product price.
        """
        price_span = div.find("span", class_="a-price-whole")
        return price_span.text.strip() if price_span else ""
    
    def get_product_reviews(self, div):
        """
        Extract the product reviews from the given div.
        
        Parameters:
        - div: The div element containing the product information.
        
        Returns:
        - The product reviews.
        """
        reviews_span = div.find("span", class_="a-size-base")
        return reviews_span.text.strip() if reviews_span else ""
    
    def get_product_availability(self, div):
        """
        Extract the product availability from the given div.
        
        Parameters:
        - div: The div element containing the product information.
        
        Returns:
        - The product availability.
        """
        availability_span = div.find("span", class_="a-color-base a-text-bold")
        return availability_span.text.strip() if availability_span else ""
    
    def get_product_image(self, div):
        """
        Extract the product image URL from the given div.
        
        Parameters:
        - div: The div element containing the product information.
        
        Returns:
        - The product image URL.
        """
        image = div.find("img", class_="s-image")
        return image.get("src") if image else ""
    
    def display_product_details(self):
        """
        Display the product details by iterating over the divs in the HTML.
        """
        if not self.soup:
            self.read_html_file()

        if self.soup:
            # Find all divs with the specified class
            divs = self.soup.find_all("div", class_="sg-row")

            # Iterate over the divs and extract the desired information
            for div in divs:
                product_name = self.get_product_name(div)
                product_price = self.get_product_price(div)
                product_reviews = self.get_product_reviews(div)
                product_availability = self.get_product_availability(div)
                product_image = self.get_product_image(div)

                # Display the product details only if all information is available
                if product_name and product_price and product_reviews:
                    print("Product Name:", product_name)
                    print("Product Price:", product_price)
                    print("Product Reviews:", product_reviews)
                    print("Product Image:", product_image)
                    print("Product Availability:", product_availability)
                    print("-" * 20)
    
    def run(self):
        """
        Run the Amazon class to display the product details.
        """
        self.display_product_details()

