import unittest
from walmart_scraper import WalmartScraper

class WalmartScraperTest(unittest.TestCase):
    def setUp(self):
        self.scraper = WalmartScraper()

    """
    WalmartScraper module test.\n
    | Methods           | Details                                                   |
    | ----------------- | --------------------------------------------------------- |
    | `.get_products()` | Returns a list of Walmart products and their details      |
    | `.get_specials()` | Returns a list of special deals and discounts at Walmart  |
    """

    def test_get_products(self):
        query = "laptops"
        products_response = self.scraper.get_products(query)
        self.assertIsInstance(products_response, list)
        if products_response:
            for product in products_response:
                self.assertIsInstance(product, dict)
                self.assertIn("name", product)
                self.assertIn("price", product)
                self.assertIn("link", product)
                self.assertIsInstance(product["name"], str)
                self.assertIsInstance(product["price"], str)
                self.assertIsInstance(product["link"], str)

    def test_get_specials(self):
        specials_response = self.scraper.get_specials()
        self.assertIsInstance(specials_response, list)
        if specials_response:
            for special in specials_response:
                self.assertIsInstance(special, dict)
                self.assertIn("title", special)
                self.assertIn("discount", special)
                self.assertIn("link", special)
                self.assertIsInstance(special["title"], str)
                self.assertIsInstance(special["discount"], str)
                self.assertIsInstance(special["link"], str)

if __name__ == "__main__":
    unittest.main()
