from bs4 import BeautifulSoup
from scrape_up.config.request_config import RequestConfig, get

class WalmartScraper:
    """
    Create an object of class `WalmartScraper`\n
    ```python
    scraper = WalmartScraper()
    ```
    | Methods            | Details                                                   |
    | ------------------ | --------------------------------------------------------- |
    | `.get_products()`  | Returns a list of Walmart products and their details      |
    | `.get_specials()`  | Returns a list of special deals and discounts at Walmart  |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.base_url = "https://www.walmart.com"
        self.products_url = self.base_url + "/search/?query="
        self.specials_url = self.base_url + "/specials"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_products(self, query):
        """
        Fetches information about products available on Walmart.\n
        Args:
        - query: The search query for products (e.g., "electronics", "clothing", etc.)
        
        Returns:
        A list of dictionaries, each containing details about a product.
        Example: [{'name': 'Product 1', 'price': '$XX.XX', 'link': 'https://www.walmart.com/product1'}, ...]
        """
        try:
            response = get(self.products_url + query, self.config)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        except Exception as e:
            print(f"Error fetching products: {e}")
            return None

        soup = BeautifulSoup(response.content, "html.parser")
        product_elements = soup.find_all("div", class_="search-result-gridview-item-wrapper")
        products = []

        for product in product_elements:
            name = product.find("a", class_="product-title-link").get_text(strip=True)
            link = self.base_url + product.find("a", class_="product-title-link")['href']
            price = product.find("span", class_="price-main").get_text(strip=True)
            products.append({"name": name, "price": price, "link": link})

        return products

    def get_specials(self):
        """
        Fetches special deals and discounts at Walmart.\n
        Returns:
        A list of dictionaries, each containing details about a special deal.
        Example: [{'title': 'Special Deal 1', 'discount': 'XX%', 'link': 'https://www.walmart.com/special1'}, ...]
        """
        try:
            response = get(self.specials_url, self.config)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        except Exception as e:
            print(f"Error fetching specials: {e}")
            return None

        soup = BeautifulSoup(response.content, "html.parser")
        special_elements = soup.find_all("div", class_="special-deal")
        specials = []

        for special in special_elements:
            title = special.find("h2", class_="special-deal-title").get_text(strip=True)
            link = self.base_url + special.find("a", class_="special-deal-link")['href']
            discount = special.find("span", class_="special-deal-discount").get_text(strip=True)
            specials.append({"title": title, "discount": discount, "link": link})

        return specials
