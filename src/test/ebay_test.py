import unittest
from scrape_up.ebay import EBAY


class eBayTest(unittest.TestCase):
    """
    eBay module test.\n
    | Methods             | Details                             |
    | ------------------- | ----------------------------------- |
    | `spotlights()`      | Returns spotlight deals on EBAY.    |
    | `featured()`        | Returns the featured deals on EBAY. |
    | `specific_deals()`  | Returns the specific deals on EBAY. |
    """

    def setUp(self):
        self.instance = EBAY()

    def test_spotlights(self):
        spotlights = self.instance.spotlights()

        self.assertIsNotNone(spotlights)
        self.assertIsInstance(spotlights, dict)
        self.assertEqual(list(spotlights.keys()), ['Description', 'Product', 'Price', 'Link'])

        for value in spotlights.values():
            self.assertIsInstance(value, str)

    def test_featured(self):
        featured = self.instance.featured()

        self.assertIsNotNone(featured)
        self.assertIsInstance(featured, list)

        for item in featured:
            self.assertIsInstance(item, dict)
            self.assertEqual(list(item.keys()), ['Product', 'Price', 'Link'])

            for value in item.values():
                self.assertIsInstance(value, str)

    def test_specific_deals(self):
        specific_deals = self.instance.specific_deals()

        self.assertIsNotNone(specific_deals)
        self.assertIsInstance(specific_deals, list)

        for item in specific_deals:
            self.assertIsInstance(item, dict)
            self.assertEqual(list(item.keys()), ['Product', 'Price', 'Link'])

            for value in item.values():
                self.assertIsInstance(value, str)
        

if __name__ == "__main__":
    unittest.main()
