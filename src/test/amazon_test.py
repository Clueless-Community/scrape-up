import unittest
import sys 
sys.path.insert(1,"C:/Users/KIIT0001/OneDrive/Documents/Coding and shizzz/Scrape-U (GSSOC 24)/scrape-up/src/scrape_up/amazon")
from products import Product 

class AmazonTest(unittest.TestCase):
    def setUp(self):
        self.product = Product("Watch")

    def test_get_product(self):
        result = self.product.get_product_details()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        if result is not None:
            self.assertIn("data", result)
            self.assertIn("message", result)
        self.assertIsNotNone(result["data"], str)
        if result["data"] is not None:
            self.assertIsInstance(result["data"], str)
        if result["message"] is not None:
            self.assertIsInstance(result["message"], str)

    def test_get_product_details(self):
        result = self.product.get_product_details()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        if result is not None:
            self.assertIn("data", result)
            self.assertIn("message", result)
        self.assertIsNotNone(result["data"], str)
        if result["data"] is not None:
            self.assertIsInstance(result["data"], str)
        if result["message"] is not None:
            self.assertIsInstance(result["message"], str)

    def test_get_product_image(self):
        result = self.product.get_product_details()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        if result is not None:
            self.assertIn("data", result)
            self.assertIn("message", result)
        self.assertIsNotNone(result["data"], str)
        if result["data"] is not None:
            self.assertIsInstance(result["data"], str)
        if result["message"] is not None:
            self.assertIsInstance(result["message"], str)

    def test_customer_review(self):
        result = self.product.get_product_details()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        if result is not None:
            self.assertIn("data", result)
            self.assertIn("message", result)
        self.assertIsNotNone(result["data"], str)
        if result["data"] is not None:
            self.assertIsInstance(result["data"], str)
        if result["message"] is not None:
            self.assertIsInstance(result["message"], str)

if __name__ == "__main__":
    unittest.main()

