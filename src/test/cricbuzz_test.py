import unittest
from scrape_up.cricbuzz import Cricbuzz

class CricbuzzTest(unittest.TestCase):
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
		instance = Cricbuzz()
		self.assertTrue(
			instance,
			"Cricbuzz:__init__ - connection failed",
		)
	
	def test_get_live_matches(self):
		instance = Cricbuzz()
		method_response = instance.get_live_matches()

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_live_matches - invalid response",
		)

	def test_get_recent_matches(self):
		instance = Cricbuzz()
		method_response = instance.get_recent_matches()

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_recent_matches - invalid response",
		)

	def test_get_upcoming_matches(self):
		instance = Cricbuzz()
		method_response = instance.get_upcoming_matches()

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_upcoming_matches - invalid response",
		)

	def test_get_series(self):
		instance = Cricbuzz()
		method_response = instance.get_series()

		self.assertIsInstance(
			method_response,
			dict,
			"Cricbuzz:get_series - invalid response",
		)

	def test_get_series_from_archive(self):
		instance = Cricbuzz()
		method_response = instance.get_series_from_archive(2023)

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_series_from_archive - invalid response",
		)

	def test_get_matches_by_day(self):
		instance = Cricbuzz()
		response = instance.get_matches_by_day(type="all")
		self.assertIsInstance(response, dict)

		response = instance.get_matches_by_day(type="invalid_type")
		self.assertEqual(response, [{"error": "Invalid type"}])

		response = instance.get_matches_by_day(type=None)
		self.assertIsNone(response)

	def test_get_series_matches(self):
		instance = Cricbuzz()
		method_response = instance.get_series_matches(7607)

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_series_matches - invalid response",
		)
	
	def test_get_series_stats(self):
		instance = Cricbuzz()
		method_response = instance.get_series_stats(7607)

		self.assertIsInstance(
			method_response,
			dict,
			"Cricbuzz:get_series_stats - invalid response",
		)

		# invalid series id
		method_response = instance.get_series_stats(0)
		self.assertEqual(
			method_response,
			{"error": "No data found"},
			"Cricbuzz:get_series_stats - invalid series id"
		)

	def test_get_teams_list(self):
		instance = Cricbuzz()
		method_response = instance.get_teams_list()

		self.assertIsInstance(
			method_response,
			dict,
			"Cricbuzz:get_teams_list - invalid response",
		)

	def test_get_team_schedule(self):
		instance = Cricbuzz()
		method_response = instance.get_team_schedule("india")

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_team_schedule - invalid response",
		)

	def test_get_team_players(self):
		instance = Cricbuzz()
		method_response = instance.get_team_players("india")

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_team_players - invalid response",
		)

	def test_get_team_results(self):
		instance = Cricbuzz()
		method_response = instance.get_team_results("india")

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_team_results - invalid response",
		)

	def test_get_team_stats(self):
		instance = Cricbuzz()
		method_response = instance.get_team_stats("india")

		self.assertIsInstance(
			method_response,
			list,
			"Cricbuzz:get_team_stats - invalid response",
		)


if __name__ == "__main__":
	unittest.main()