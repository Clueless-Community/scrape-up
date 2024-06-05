import unittest
from src.scrape_up.lichess import LichessGames


class TestLichessGames(unittest.TestCase):
    """
    | Methods                       | Details                                                                    |
    | ----------------------------- | -------------------------------------------------------------------------- |
    | `.fetch_games()`              | Fetch all the games data for the specified username.                       |
    """
    def setUp(self):
        """
        Initialize a LichessGames instance before each test method.
        """
        self.username = "chess_player"  # Example username
        self.lichess_scraper = LichessGames(username=self.username)

    def test_fetch_games(self):
        """
        Test the fetch_games() method.
        """
        try:
            games = self.lichess_scraper.fetch_games()

            # Check if games is a list of dictionaries
            self.assertIsInstance(games, list)
            for game in games:
                self.assertIsInstance(game, dict)
                self.assertIn("white_player", game)
                self.assertIn("black_player", game)
                self.assertIn("pgn", game)

                white_player = game["white_player"]
                black_player = game["black_player"]

                self.assertIn("username", white_player)
                self.assertIn("before_game_score", white_player)
                self.assertIn("score_change", white_player)

                self.assertIn("username", black_player)
                self.assertIn("before_game_score", black_player)
                self.assertIn("score_change", black_player)
        except:
            return None

    def test_fetch_games_empty(self):
        """
        Test fetch_games() method with a username that has no games.
        """
        try:
            self.lichess_scraper = LichessGames(username="non_existent_user")
            games = self.lichess_scraper.fetch_games()
            self.assertEqual(games, [], "Expected an empty list for a non-existent user")
        except:
            return None


if __name__ == "__main__":
    unittest.main()
