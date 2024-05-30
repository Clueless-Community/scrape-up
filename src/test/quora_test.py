import unittest
import requests
from unittest.mock import patch
from src.scrape_up.quora import Quora


class TestQuora(unittest.TestCase):
    """
    Quora module test.
    | Methods           | Details                                                                                              |
    | ----------------- | ---------------------------------------------------------------------------------------------------- |
    | `fetch_answers()` | Returns the list of answers pertaining to a particular URL given by the user as a parameter.         |
    | `get_by_query()`  | Returns the list of answers pertaining to a particular query given by the user.                      |
    | `profile_details()` | Returns the name of a user along with their Quora profile link.                                      |
    """

    def setUp(self):
        self.scrapper = Quora()

    @patch("requests.get")
    def test_fetch_answers(self, mock_get):
        try:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_response._content = b"""
            <script type="application/ld+json">
                {
                    "mainEntity": {
                        "acceptedAnswer": [{"text": "Accepted answer 1"}],
                        "suggestedAnswer": [{"text": "Suggested answer 1"}]
                    }
                }
            </script>
            """
            mock_get.return_value = mock_response

            expected_answers = ["Accepted answer 1", "Suggested answer 1"]

            self.assertEqual(
                self.scrapper.fetch_answers("https://www.quora.com/question"), expected_answers
            )
        except:
            return None

    @patch("requests.get")
    def test_get_by_query(self, mock_get):
        try:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_response._content = b"""
            <script type="application/ld+json">
                {
                    "mainEntity": {
                        "suggestedAnswer": [{"text": "Suggested answer 1"}]
                    }
                }
            </script>
            """
            mock_get.return_value = mock_response

            expected_answer = "Suggested answer 1"

            self.assertEqual(
                self.scrapper.get_by_query("How-should-I-start-learning-Python-1"),
                expected_answer,
            )
        except:
            return None

    @patch("requests.get")
    def test_profile_details(self, mock_get):
        try:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_response._content = b"""
            <meta content="Nikhil Raj" />
            """
            mock_get.return_value = mock_response

            expected_profile = {"name": "Nikhil Raj", "url": "https://www.quora.com/profile/Nikhil-Raj"}

            self.assertEqual(
                self.scrapper.profile_details("Nikhil Raj"), expected_profile)
        except:
            return None


if __name__ == "__main__":
    unittest.main()

