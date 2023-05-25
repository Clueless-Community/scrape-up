import unittest
from datetime import datetime
from scrape_up.Amazon.amazon import AmazonScraper

class AmazonScraperTest(unittest.TestCase):

    def test_getProducts(self):
        scraper = AmazonScraper(product_category="mobiles")
        products = scraper.getProducts("iphone", 1)
        self.assertIsInstance(products, list)
        self.assertTrue(len(products) > 0)

    def test_getProductDetails(self):
        scraper = AmazonScraper(product_category="mobiles")
        product_url = "https://www.amazon.in/dp/B0C2Z95WVS"
        product_details = scraper.getProductDetails(product_url)
        self.assertIsInstance(product_details, dict)
        self.assertTrue("sku" in product_details)
        self.assertTrue("name" in product_details)
        self.assertTrue("description" in product_details)
        self.assertTrue("image_path" in product_details)
        self.assertTrue("category" in product_details)
        self.assertTrue("timestamp" in product_details)
        self.assertTrue("URL" in product_details)
        self.assertTrue("price" in product_details)

    def test_main(self):
        scraper = AmazonScraper(product_category="mobiles", number_of_threads=2)
        scraper.main()
        self.assertIsInstance(scraper.df_list, list)
        self.assertTrue(len(scraper.df_list) > 0)

if __name__ == "__main__":
    unittest.main()
