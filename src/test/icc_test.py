import unittest
from scrape_up import icc

class ICCTest(unittest.TestCase):
    """
    ICC module test.\n
    | Method                               | Details                                                             |
    | ----------------------------         | ------------------------------------------------------------------- |
    | `.team_rankings(format)`             | Returns the list of rankings of teams of desired format             |
    | `.player_ranking(type,format)`       | Returns the list of player ranking of desired type and format       |
    | `.team_rankings_women(format)`       | Returns the list of rankings of teams of desired format             |
    | `.player_ranking_women(type,format)` | Returns the list of player ranking of desired type and format       |
    """

    def test_team_rankings(self):
        instance = icc.ICC()
        response = instance.team_rankings("ODI")
        self.assertGreater(len(response), 0, "Team rankings is empty")
        self.assertTrue(isinstance(response, list), "Team rankings is not a list")
        self.assertTrue(all(isinstance(team, dict) and "rank" in team and "team" in team for team in response), "Incorrect format for team rankings")

    def test_player_ranking(self):
        instance = icc.ICC()
        response = instance.player_ranking("batting", "TEST")
        self.assertGreater(len(response), 0, "Player ranking is empty")
        self.assertTrue(isinstance(response, list), "Player ranking is not a list")
        self.assertTrue(all(isinstance(player, dict) and "rank" in player and "name" in player for player in response), "Incorrect format for player rankings")
    
    def test_team_rankings_women(self):
        instance = icc.ICC()
        response = instance.team_rankings_women("T20")
        self.assertGreater(len(response), 0, "Team rankings for women is empty")
        self.assertTrue(isinstance(response, list), "Team rankings for women is not a list")
        self.assertTrue(all(isinstance(team, dict) and "rank" in team and "team" in team for team in response), "Incorrect format for team rankings for women")

    def test_player_ranking_women(self):
        instance = icc.ICC()
        response = instance.player_ranking("bowling", "ODI")
        self.assertGreater(len(response), 0, "Player ranking for women is empty")
        self.assertTrue(isinstance(response, list), "Player ranking for women is not a list")
        self.assertTrue(all(isinstance(player, dict) and "rank" in player and "name" in player for player in response), "Incorrect format for player rankings for women")

if __name__ == "__main__":
    unittest.main()