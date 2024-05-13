import unittest
from scrape_up.espncricinfo import Espncricinfo


class ESPNTest(unittest.TestCase):
    """
    Tests for the Cricbuzz class in the cricbuzz module.
    | Methods                      | Details                                                                |
    | ---------------------------- | ---------------------------------------------------------------------- |
    | `.get_live_matches()`        | Returns a list of live matches from Cricbuzz.                          |
    | `.get_recent_matches()`      | Returns a list of recent matches from Cricbuzz.                        |
    | `.get_upcoming_matches()`    | Returns a list of upcoming matches from Cricbuzz.                      |
    | `.get_series()`              | Returns a dictionary of series in month and year format from Cricbuzz. |
    | `.get_series_from_archive()` | Returns a list of series from archive from Cricbuzz.                   |
    | `.get_matches_by_day()`      | Returns a dictionary of matches by day from Cricbuzz.                  |
    | `.get_series_matches()`      | Returns a list of matches in a series from Cricbuzz.                   |
    | `.get_series_stats()`        | Returns a list of stats of players in a series from Cricbuzz.          |
    | `.get_teams_list()`          | Returns a list of teams from Cricbuzz.                                 |
    | `.get_team_schedule()`       | Returns a list of matches of a team from Cricbuzz.                     |
    | `.get_team_players()`        | Returns a list of players of a team from Cricbuzz.                     |
    | `.get_team_results()`        | Returns a list of past results of a team from Cricbuzz.                |
    | `.get_team_stats()`          | Returns a list of player stats of a team from Cricbuzz.                |
    """

    def test_connection(self):
        instance = Espncricinfo()
        self.assertTrue(
            instance,
            "ESPN:__init__ - connection failed",
        )

    def test_get_news(self):
        instance = Espncricinfo()
        method_response = instance.get_news()

        self.assertIsInstance(
            method_response,
            list,
            "ESPN:get_news - invalid response",
        )

    def test_get_livescores(self):
        instance = Espncricinfo()
        method_response = instance.get_livescores()

        self.assertIsInstance(
            method_response,
            list,
            "ESPN:get_livescores - invalid response",
        )


if __name__ == "__main__":
    unittest.main()
