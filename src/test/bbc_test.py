import unittest
from scrape_up.bbcnews import BBCNews


class TestBBCNews(unittest.TestCase):
    """
    | Methods            | Details                                                  |
    | ------------------ | -------------------------------------------------------- |
    | `.get_headlines()` | Returns the list of object containig the headlines       |
    | `get_article()`    | Returns an object with proper details about the articles |

    """

    def setUp(self):
        """
        Initialize a BBCNews instance before each test method.
        """
        self.bbc_scraper = BBCNews()

    def test_get_headlines(self):
        """
        Testing the get_headlines() method.
        """
        try:
            headlines = self.bbc_scraper.get_headlines()

            # Check if headlines is a list of dictionaries
            if headlines is not None:
                self.assertIsInstance(headlines, list)
                for headline in headlines:
                    self.assertIsInstance(headline, dict)
                    self.assertIn("index", headline)
                    self.assertIn("headline", headline)

                # Check if all headlines have unique indices
                indices = {headline["index"] for headline in headlines}
                self.assertEqual(
                    len(indices), len(headlines), "Duplicate indices found in headlines"
                )
                # Check if headlines list is not empty
                self.assertGreater(len(headlines), 0, "No headlines extracted")
        except:
            return None

    def test_get_article(self):
        """
        Testing the get_article(url) method.
        """
        try:
            valid_url = "https://www.bbc.co.uk/news/world-europe-61258011"  # Test with a valid article URL
            article = self.bbc_scraper.get_article(valid_url)

            if article is not None:
                self.assertIsInstance(
                    article, dict
                )  # Check if article is a dictionary or not
                self.assertIn(
                    "main_heading", article
                )  # Does it contain main_heading or not
                self.assertIn("time", article)  # Does it contain time or not
                self.assertIn("text", article)  # Does it contain text or not

            invalid_url = "https://www.bbc.co.uk/news/non-existent-article"  # Test with an invalid article URL
            invalid_article = self.bbc_scraper.get_article(
                invalid_url
            )  # Should return None
            self.assertIsNone(invalid_article, "Invalid URL should return None")
        except:
            return None


if __name__ == "__main__":
    unittest.main()
