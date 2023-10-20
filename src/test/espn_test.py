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

        # Ensure that the returned data is a list
        self.assertIsInstance(scoreboard, list)

        if scoreboard:
            for game in scoreboard:
                # Validate keys in each game dictionary
                self.assertCountEqual(
                    game.keys(),
                    ["Game", "Game Link", "Teams", "Location"],
                    "ESPN:get_scoreboard - keys mismatch",
                )

    def test_get_tournaments(self):
        espn = ESPN()
        tournaments = espn.get_tournaments()

        # Ensure that the returned data is a list
        self.assertIsInstance(tournaments, list)

        if tournaments:
            for tournament in tournaments:
                for tournament_name, links in tournament.items():
                    for link, name in links:
                        # Validate keys in each tournament dictionary
                        self.assertCountEqual(
                            links[0].keys(),
                            ["Link", "Name"],
                            f"ESPN:get_tournaments - keys mismatch for {tournament_name}",
                        )

    def test_get_teams(self):
        espn = ESPN()
        teams = espn.get_teams()

        # Ensure that the returned data is a list
        self.assertIsInstance(teams, list)

        if teams:
            for team in teams:
                # Validate keys in each team dictionary
                self.assertCountEqual(
                    team.keys(),
                    ["Name", "Link"],
                    "ESPN:get_teams - keys mismatch",
                )

if __name__ == "__main__":
    unittest.main()
