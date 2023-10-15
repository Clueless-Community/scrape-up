import unittest
from scrape_up.imdb import Actor, BoxOffice, Celeb

class IMDBTest(unittest.TestCase):
    """
    IMDB module test.\n
    | Classes         | Details                              |
    | --------------- | ------------------------------------ |
    | `Actor`         | Tests related to the Actor class     |
    | `BoxOffice`     | Tests related to the BoxOffice class |
    | `Celeb`         | Tests related to the Celeb class     |
    
    """

    def test_actor_query(self):
        actor_name = "Tom Holland"
        actor = Actor(actor_name)

        # Test popular_movies() method
        popular_movies = actor.popular_movies()
        self.assertIsInstance(popular_movies, dict)
        self.assertIn("title", popular_movies)
        self.assertIn("popular_movies", popular_movies["title"])

        # Test all_movies() method
        all_movies = actor.all_movies()
        self.assertIsInstance(all_movies, dict)
        self.assertIn("title", all_movies)
        self.assertIn("all_movies", all_movies["title"])

        # Test awards() method
        awards = actor.awards()
        self.assertIsInstance(awards, dict)
        self.assertIn("title", awards)
        self.assertIn("awards", awards["title"])

    def test_box_office_query(self):
        boxoffice = BoxOffice()

        # Test top_movies() method
        top_movies = boxoffice.top_movies()
        self.assertIsInstance(top_movies, list)
        for movie_data in top_movies:
            self.assertIsInstance(movie_data, dict)
            self.assertIn("Movie Name", movie_data)
            self.assertIn("Weekend Gross", movie_data)
            self.assertIn("Total Gross", movie_data)
            self.assertIn("Weeks released", movie_data)

    def test_celeb_query(self):
        celeb = Celeb()

        # Test top_celebs() method
        top_celebs = celeb.top_celebs()
        self.assertIsInstance(top_celebs, list)
        for celeb_data in top_celebs:
            self.assertIsInstance(celeb_data, dict)
            self.assertIn("Name", celeb_data)
            self.assertIn("Roles", celeb_data)
            self.assertIn("Famous Movie", celeb_data)

    # Add more test methods for specific queries or functionality within each class

if __name__ == "__main__":
    unittest.main()
