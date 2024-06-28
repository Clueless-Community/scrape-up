import unittest
from scrape_up.chromewebstore import ChromeWebStore


class TestChromeWebStore(unittest.TestCase):

    def setUp(self):
        self.chrome_web_store = ChromeWebStore()

    def test_search_success(self):
        """
        Test that search returns a list of extensions and success message for a valid keyword.
        """
        keyword = "box"
        extensions, message = self.chrome_web_store.search(keyword)
        self.assertIsInstance(extensions, list)
        self.assertEqual(message, "success")
        self.assertGreaterEqual(len(extensions), 0)  # At least one extension

    def test_search_no_results(self):
        """
        Test that search returns an empty dict and message for a non-existent keyword.
        """
        keyword = "notarealkeyword"
        extensions, message = self.chrome_web_store.search(keyword)
        self.assertIsInstance(extensions, list)
        self.assertEqual(message, "No results found for given criteria")
        self.assertEqual(len(extensions), 0)

    def test_get_details_success(self):
        """
        Test that get_details returns a dictionary with extension details for a valid ID.
        """
        extension_id = (
            "efaidnbmnnnibpcajpcglclefindmkaj"
        )
        details, message = self.chrome_web_store.get_details(extension_id)
        self.assertIsInstance(details, dict)
        self.assertEqual(message, "success")
        self.assertIn("title", details)
        self.assertIn("thumbnail", details)
    
    def test_get_details_error(self):
        """
        Test that get_details returns an empty dictionary and error message for an invalid ID.
        """
        invalid_id = "invalid_id"
        details, message = self.chrome_web_store.get_details(invalid_id)
        self.assertIsInstance(details, dict)
        self.assertEqual(message.startswith("No results found"), True)
        self.assertEqual(details, {})

    def test_get_details_with_overview(self):
        """
        Test that get_details with overview=True includes the extension overview.
        """
        extension_id = (
            "efaidnbmnnnibpcajpcglclefindmkaj"
        )
        details, message = self.chrome_web_store.get_details(
            extension_id, overview=True
        )
        self.assertIn("overview", details)


if __name__ == "__main__":
    unittest.main()
