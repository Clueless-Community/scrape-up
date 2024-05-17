import unittest
from scrape_up.fide import FIDE


class FIDETest(unittest.TestCase):
    """
    Tests for the FIDE class in the fide module.
    | Methods                   | Details                                            |
    | ------------------------- | -------------------------------------------------- |
    | `.get_events()`           | Returns all the major chess events of 2024.        |
    | `.get_open_ratings()`     | Returns a list of top 100 open category players.   |
    | `.get_women_ratings()`    | Returns a list of top 100 women category players.  |
    | `.get_juniors_ratings()`  | Returns a list of top 100 juniors category players.|
    | `.get_girls_ratings()`    | Returns a list of top 100 girls category players.  |
    | `.get_news()`             | Returns a list of top chess/fide news.             |
    """

    def test_connection(self):
        instance = FIDE()
        self.assertTrue(
            instance,
            "FIDE:__init__ - connection failed",
        )

    def test_get_events(self):
        instance = FIDE()
        method_response = instance.get_events()

        self.assertIsInstance(
            method_response,
            list,
            "FIDE:get_events - invalid response",
        )

    def test_get_open_ratings(self):
        instance = FIDE()
        method_response = instance.get_open_ratings()

        self.assertIsInstance(
            method_response,
            list,
            "FIDE:get_open_ratings - invalid response",
        )

    def test_get_women_ratings(self):
        instance = FIDE()
        method_response = instance.get_women_ratings()

        self.assertIsInstance(
            method_response,
            list,
            "FIDE:get_women_ratings - invalid response",
        )

    def test_get_juniors_ratings(self):
        instance = FIDE()
        method_response = instance.get_juniors_ratings()

        self.assertIsInstance(
            method_response,
            list,
            "FIDE:get_juniors_ratings - invalid response",
        )

    def test_get_girls_ratings(self):
        instance = FIDE()
        method_response = instance.get_girls_ratings()

        self.assertIsInstance(
            method_response,
            list,
            "FIDE:get_girls_ratings - invalid response",
        )

    def test_get_news(self):
        instance = FIDE()
        method_response = instance.get_news()

        self.assertIsInstance(
            method_response,
            list,
            "FIDE:get_news - invalid response",
        )


if __name__ == "__main__":
    unittest.main()
