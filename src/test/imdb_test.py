import unittest
from scrape_up import imdb

class IMDBTest(unittest.TestCase):
    """
    imdb module test.\n
    | Method               | Details                                                             |
    | ---------------------| ------------------------------------------------------------------- |
    | `.top_rated()`       | Returns the list of top rated movies                                |
    | `.scrape_genre_movies(genre)` | Returns the list of movies of a specific genre             |
    | `.top_rated_shows()` | Returns the list of top rated TV shows                              |
    """

    def setUp(self):
        self.scraper = imdb()

    def test_top_rated(self):
        response = self.scraper.top_rated()
        self.assertGreater(len(response), 0, "Top rated movies list is empty")
        self.assertIsInstance(response, list, "Top rated movies is not a list")
        self.assertTrue(
            all(
                isinstance(movie, dict) and "title" in movie and "year" in movie and "duration" in movie and "rating" in movie
                for movie in response
            ),
            "Incorrect format for top rated movies",
        )

    def test_scrape_genre_movies(self):
        genre = "Adventure"
        response = self.scraper.scrape_genre_movies(genre)

        self.assertIsInstance(response, list, f"{genre} movies is not a list")
        self.assertGreater(len(response), 0, f"{genre} movies list is empty")

        for movie in response:
            self.assertIsInstance(movie, dict)
            self.assertIn("title", movie)
            self.assertIn("year", movie)
            self.assertIn("certificate", movie)
            self.assertIn("time", movie)
            self.assertIn("genre", movie)
            self.assertIn("rating", movie)
            self.assertIn("simple_desc", movie)
            self.assertIn("votes", movie)

    def test_top_rated_shows(self):
        response = self.scraper.top_rated_shows()

        self.assertIsInstance(response, list, "Top rated shows is not a list")
        self.assertGreater(len(response), 0, "Top rated shows list is empty")

        for show in response:
            self.assertIsInstance(show, dict)
            self.assertIn("title", show)
            self.assertIn("year", show)
            self.assertIn("episode", show)
            self.assertIn("rating", show)

if __name__ == '__main__':
    unittest.main()