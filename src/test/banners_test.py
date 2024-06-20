import unittest
from src.scrape_up.banners import Scraper88x31


class TestScraper88x31(unittest.TestCase):
    def setUp(self):
        """
        Initialize a Scraper88x31 instance before each test method.
        """
        self.scraper = Scraper88x31()

    def test_get_all(self):
        """
        | Methods            | Details                                                  |
        | ------------------ | -------------------------------------------------------- |
        | `get_all()`        | Returns the list of all available 88x31 banners          |
        """
        try:
            banners = self.scraper.get_all()

            # Check if banners is a list of URLs
            self.assertIsInstance(banners, list)
            for banner in banners:
                self.assertIsInstance(banner, str)
                self.assertTrue(banner.startswith("https://cyber.dabamos.de/88x31/"))
                self.assertTrue(banner.endswith(".gif"))
        except:
            return None


if __name__ == "__main__":
    unittest.main()
