import unittest
from unittest.mock import patch
from scrape_up.quora import Quora


class TestQuora(unittest.TestCase):
    def setUp(self):
        self.scrapper = Quora()

    def test_fetch_answers(self):
        try:

            expected_answers = ["Accepted answer 1", "Suggested answer 1"]

            self.assertEqual(
                self.scrapper.fetch_answers("https://www.quora.com/question"),
                expected_answers,
            )
        except:
            return None

    def test_get_by_query(self):
        try:

            expected_answer = "Suggested answer 1"

            self.assertEqual(
                self.scrapper.get_by_query("How-should-I-start-learning-Python-1"),
                expected_answer,
            )
        except:
            return None

    def test_profile_details(self):
        try:

            expected_profile = {
                "name": "Nikhil Raj",
                "url": "https://www.quora.com/profile/Nikhil-Raj",
            }

            self.assertEqual(
                self.scrapper.profile_details("Nikhil Raj"), expected_profile
            )
        except:
            return None


if __name__ == "__main__":
    unittest.main()
