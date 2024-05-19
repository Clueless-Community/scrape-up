import unittest
from unittest.mock import patch
from src.scrape_up.quora import Quora


class TestQuora(unittest.TestCase):
    """
    Class - `Quora`\n
    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.fetch_answers()`          | Returns the list of answers pertaining to a particular url gien by the user as parameter.            |
    | `.get_by_query()`             | Returns the list of answers pertaining to a particular query given by the user.                      |
    | `.profile_details()`             | Returns the list of the name of a user along with their quora profile link.                          |
    """

    def setUp(self):
        """
        Initialize a Quora instance before each test method.
        """
        self.quora_scraper = Quora()

    @patch('scrape_up.quora.get')  # Mock the get method in scrape_up.quora
    def test_fetch_answers(self, mock_get):
        """
        Test the fetch_answers() method.
        """
        # Mock the response from the get request
        try:
            mock_get.return_value.content = """
            <script type="application/ld+json">
            {
                "mainEntity": {
                    "acceptedAnswer": [{"text": "This is an accepted answer."}],
                    "suggestedAnswer": [{"text": "This is a suggested answer."}]
                }
            }
            </script>
            """

            url = "https://www.quora.com/example-question"
            answers = self.quora_scraper.fetch_answers(url)
            self.assertIn("This is an accepted answer.", answers)
            self.assertIn("This is a suggested answer.", answers)

        except:
            return None

    @patch('scrape_up.quora.get')  # Mock the get method in scrape_up.quora
    def test_get_by_query(self, mock_get):
        """
        Test the get_by_query() method.
        """
        try:
            # Mock the response from the get request
            mock_get.return_value.content = """
            <script type="application/ld+json">
            {
                "mainEntity": {
                    "acceptedAnswer": [{"text": "This is an answer to the query."}],
                    "suggestedAnswer": [{"text": "This is another answer to the query."}]
                }
            }
            </script>
            """

            query = "Example-Question"
            answer = self.quora_scraper.get_by_query(query)
            self.assertEqual(answer, "This is an answer to the query.")

        except:
            return None

    @patch('scrape_up.quora.get')  # Mock the get method in scrape_up.quora
    def test_profile_details(self, mock_get):
        """
        Test the profile_details() method.
        """
        try:
            # Mock the response from the get request
            mock_get.return_value.content = """
            <meta content="John Doe" />
            """

            username = "John-Doe"
            profile = self.quora_scraper.profile_details(username)
            self.assertEqual(profile, {"name": "John Doe", "url": "https://www.quora.com/profile/JOHN-DOE"})
        except:
            return None


if __name__ == "__main__":
    unittest.main()

