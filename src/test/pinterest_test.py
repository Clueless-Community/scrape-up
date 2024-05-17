import unittest
from scrape_up.pinterest import Pinterest


class TestPinterest(unittest.TestCase):
    def setUp(self):
        self.pinterest = Pinterest()

    def test_get_today(self):
        today_topics = self.pinterest.get_today()
        self.assertIsInstance(today_topics, list, "Expected get_today to return a list")
        if today_topics:
            for topic in today_topics:
                self.assertIn("link", topic)
                self.assertIn("title", topic)
                self.assertIn("subtitle", topic)
                self.assertIn("image", topic)

    def test_get_photo(self):
        url = "https://www.pinterest.com/pin/1234567890/"
        photo = self.pinterest.get_photo(url)
        if photo:
            self.assertIn("alt", photo)
            self.assertIn("image", photo)

    def test_search_pins(self):
        keyword = "nature"
        pins = self.pinterest.search_pins(keyword=keyword)
        self.assertIsInstance(pins, list, "Expected search_pins to return a list")
        if pins:
            for pin in pins:
                self.assertIn("link", pin)
                self.assertIn("image", pin)

    def test_get_pin_details(self):
        pin_url = "https://www.pinterest.com/pin/1234567890/"
        details = self.pinterest.get_pin_details(pin_url)
        if details:
            self.assertIn("title", details)
            self.assertIn("description", details)
            self.assertIn("saves", details)
            self.assertIn("comments", details)


if __name__ == "__main__":
    unittest.main()
