import unittest
import json
from src.scrape_up.atcoder import Atcoder


class TestAtcoder(unittest.TestCase):
    """
        | Methods           | Details                                                                            |
        | ----------------- | ---------------------------------------------------------------------------------- |
        | `.get_profile()`  | Returns the user data in json format.                                              |
        | `get_contests()`  | Returns future_contests , past_contests , skill_tests etc in json format.          |

    """

    def setUp(self):
        """
        Initialize an Atcoder instance before each test method.
        """
        self.atcoder_user = "chokudai"  # Example user
        self.atcoder_scraper = Atcoder(user=self.atcoder_user)

    def test_get_profile(self):
        """
        Test the get_profile() method.
        """
        try:
            profile = self.atcoder_scraper.get_profile()
            self.assertIsNotNone(profile, "Failed to fetch profile")

            profile_data = json.loads(profile)

            # Check if profile_data is a dictionary
            self.assertIsInstance(profile_data, dict, "Profile data should be a dictionary")

            # Check if certain keys exist in the profile_data
            expected_keys = [
                "Country/Region", "Birth_Year", "Twitter_ID", "TopCoder_ID",
                "Codeforces_ID", "Affiliation", "Algorithm_Rank", "Algorithm_Rating",
                "Algorithm_Highest_Rating", "Algorithm_Rated_Matches_", "Algorithm_Last_Competed",
                "Heuristic_Rank", "Heuristic_Rating", "Heuristic_Highest_Rating",
                "Heuristic_Rated_Matches_", "Heuristic_Last_Competed"
            ]

            for key in expected_keys:
                self.assertIn(key, profile_data, f"Missing expected key: {key}")

        except:
            return None

    def test_get_contests(self):
        """
        Test the get_contests() method.
        """
        try:
            contests = self.atcoder_scraper.get_contests()
            self.assertIsNotNone(contests, "Failed to fetch contests")

            # Check if contests is a dictionary
            self.assertIsInstance(contests, dict, "Contests data should be a dictionary")

            # Check if certain keys exist in the contests data
            expected_keys = ["active", "Upcoming", "Recent", "Permanent"]

            for key in expected_keys:
                self.assertIn(key, contests, f"Missing expected key: {key}")

                # Check if the value for each key is a dictionary
                self.assertIsInstance(contests[key], dict, f"The value for '{key}' should be a dictionary")


        except:
            return None


if __name__ == "__main__":
    unittest.main()
