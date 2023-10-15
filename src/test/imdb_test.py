import unittest
from src.scrape_up.imdb.actor import Actor
from src.scrape_up.imdb.box_office import BoxOffice
from src.scrape_up.imdb.celeb import Celeb
from src.scrape_up.imdb.imdb import IMDB
from src.scrape_up.imdb.indian_movies import IndianMovies
from src.scrape_up.imdb.movie import Movie

class TestActorClass(unittest.TestCase):

    def test_actor_creation(self):
        actor = Actor("Tom Holland")
        self.assertIsNotNone(actor)

    def test_popular_movies(self):
        actor = Actor("Tom Holland")
        result = actor.popular_movies()
        self.assertIsNotNone(result)
        self.assertIn("title", result)
        self.assertIn("popular_movies", result)

    def test_all_movies(self):
        actor = Actor("Tom Holland")
        result = actor.all_movies()
        self.assertIsNotNone(result)
        self.assertIn("title", result)
        self.assertIn("all_movies", result)

    def test_awards(self):
        actor = Actor("Tom Holland")
        result = actor.awards()
        self.assertIsNotNone(result)
        self.assertIn("title", result)
        self.assertIn("awards", result)

class TestBoxOffice(unittest.TestCase):

    def test_boxoffice_creation(self):
        boxoffice = BoxOffice()
        self.assertIsNotNone(boxoffice)

    def test_top_movies(self):
        boxoffice = BoxOffice()
        result = boxoffice.top_movies()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for movie in result:
                self.assertIn("Movie Name", movie)
                self.assertIn("Weekend Gross", movie)
                self.assertIn("Total Gross", movie)
                self.assertIn("Weeks released", movie)

                self.assertIsInstance(movie["Movie Name"], str)
                self.assertIsInstance(movie["Weekend Gross"], str)
                self.assertIsInstance(movie["Total Gross"], str)
                self.assertIsInstance(movie["Weeks released"], str)

class TestCeleb(unittest.TestCase):

    def test_celeb_creation(self):
        celeb = Celeb()
        self.assertIsNotNone(celeb)

    def test_top_celebs(self):
        celeb = Celeb()
        result = celeb.top_celebs()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for celebrity in result:
                self.assertIn("Name", celebrity)
                self.assertIn("Roles", celebrity)
                self.assertIn("Famous Movie", celebrity)

                self.assertIsInstance(celebrity["Name"], str)
                self.assertIsInstance(celebrity["Roles"], list)
                self.assertIsInstance(celebrity["Famous Movie"], str)

                # Additional checks for Roles list
                for role in celebrity["Roles"]:
                    self.assertIsInstance(role, str)

class TestIMDBClass(unittest.TestCase):

    def test_imdb_creation(self):
        imdb = IMDB()
        self.assertIsNotNone(imdb)

    def test_top_rated_movies(self):
        imdb = IMDB()
        result = imdb.top_rated()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for movie in result:
                self.assertIn("title", movie)
                self.assertIn("year", movie)
                self.assertIn("duration", movie)
                self.assertIn("rating", movie)

                self.assertIsInstance(movie["title"], str)
                self.assertIsInstance(movie["year"], str)
                self.assertIsInstance(movie["duration"], str)
                self.assertIsInstance(movie["rating"], str)

    def test_scrape_genre_movies(self):
        imdb = IMDB()
        genre = "Adventure"
        result = imdb.scrape_genre_movies(genre)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for movie in result:
                self.assertIn("title", movie)
                self.assertIn("year", movie)
                self.assertIn("certificate", movie)
                self.assertIn("time", movie)
                self.assertIn("genre", movie)
                self.assertIn("rating", movie)
                self.assertIn("simple_desc", movie)
                self.assertIn("votes", movie)

                self.assertIsInstance(movie["title"], str)
                self.assertIsInstance(movie["year"], str)
                self.assertIsInstance(movie["certificate"], str)
                self.assertIsInstance(movie["time"], str)
                self.assertIsInstance(movie["genre"], str)
                self.assertIsInstance(movie["rating"], str)
                self.assertIsInstance(movie["simple_desc"], str)
                self.assertIsInstance(movie["votes"], str)

    def test_top_rated_shows(self):
        imdb = IMDB()
        result = imdb.top_rated_shows()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for show in result:
                self.assertIn("title", show)
                self.assertIn("year", show)
                self.assertIn("episode", show)
                self.assertIn("rating", show)

                self.assertIsInstance(show["title"], str)
                self.assertIsInstance(show["year"], str)
                self.assertIsInstance(show["episode"], str)
                self.assertIsInstance(show["rating"], str)

class TestIndianMovies(unittest.TestCase):

    def test_indian_movies_creation(self):
        indianmovies = IndianMovies()
        self.assertIsNotNone(indianmovies)

    def test_top_movies(self):
        indianmovies = IndianMovies()
        result = indianmovies.top_movies()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        if result is not None:
            for movie in result:
                self.assertIsInstance(movie, str)

class TestMovie(unittest.TestCase):

    def test_movie_creation(self):
        movie = Movie("Avengers: Endgame")
        self.assertIsNotNone(movie)

    def test_rating(self):
        movie = Movie("Avengers: Endgame")
        result = movie.rating()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

        if result is not None:
            self.assertIn("title", result)
            self.assertIn("rating", result)

            self.assertIsInstance(result["title"], str)
            self.assertIsInstance(result["rating"], str)

    def test_description(self):
        movie = Movie("Avengers: Endgame")
        result = movie.description()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

        if result is not None:
            self.assertIn("title", result)
            self.assertIn("description", result)

            self.assertIsInstance(result["title"], str)
            self.assertIsInstance(result["description"], str)

    def test_such_movies(self):
        movie = Movie("Avengers: Endgame")
        result = movie.such_movies()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

        if result is not None:
            self.assertIn("title", result)
            self.assertIn("more_like_this", result)

            self.assertIsInstance(result["title"], str)
            self.assertIsInstance(result["more_like_this"], list)

            # Additional checks for more_like_this list
            for movie_name in result["more_like_this"]:
                self.assertIsInstance(movie_name, str)

    def test_box_office(self):
        movie = Movie("Avengers: Endgame")
        result = movie.box_office()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

        if result is not None:
            self.assertIn("title", result)
            self.assertIn("box_office", result)

            self.assertIsInstance(result["title"], str)
            self.assertIsInstance(result["box_office"], dict)

            # Additional checks for box_office dictionary
            box_office_data = result["box_office"]
            self.assertIn("Budget", box_office_data)
            self.assertIn("Gross worldwide", box_office_data)

            self.assertIsInstance(box_office_data["Budget"], str)
            self.assertIsInstance(box_office_data["Gross worldwide"], str)


if __name__ == '__main__':
    unittest.main()
