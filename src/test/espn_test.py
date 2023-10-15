import unittest
from scrape_up.espn import ESPN

class ESPNScraperTest(unittest.TestCase):
    """
    ESPN class test.\n
    | Methods              | Details                                              |
    | -------------------  | ---------------------------------------------------- |
    | `.get_scoreboard()`  | Tests the get_scoreboard() method of the ESPN class  |
    | `.get_tournaments()` | Tests the get_tournaments() method of the ESPN class |
    | `.get_teams()`       | Tests the get_teams() method of the ESPN class       |
    """

    def test_get_scoreboard(self):
        espn = ESPN()
        date = "20230721"  # Replace with a valid date
        scoreboard = espn.get_scoreboard(date)
        self.assertIsInstance(scoreboard, list)

    def test_get_tournaments(self):
        espn = ESPN()
        tournaments = espn.get_tournaments()
        self.assertIsInstance(tournaments, list)

    def test_get_teams(self):
        espn = ESPN()
        teams = espn.get_teams()
        self.assertIsInstance(teams, list)

if __name__ == "__main__":
    unittest.main()
