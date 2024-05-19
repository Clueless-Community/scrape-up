import unittest
from scrape_up.geeksforgeeks import Geeksforgeeks
import json

class GeeksforgeeksTest(unittest.TestCase):
    """
    Geeksforgeeks module test.
    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_profile()`  | Returns the user data in json format.                                              |
    """

    def test_get_profile(self):
        instance = Geeksforgeeks(user="nikhil25803")
        method_response = instance.get_profile()

        if isinstance(method_response, str):
            try:
                method_response = json.loads(method_response)
            except json.JSONDecodeError:
                self.fail("get_profile should return a dictionary or a JSON string")

        expected_keys = [
            "username", "collage_name", "collage_rank", "score",
            "languages_used", "current_potd_streak", "total_problem_solved", "campus_ambassader"
        ]

        self.assertEqual(
            list(method_response.keys()),
            expected_keys,
            "Geeksforgeeks:get_profile - keys mismatch"
        )

        self.assertEqual(
            list(method_response['score'].keys()),
            ["overall_coding_score", "monthly_coding_score"],
            "Geeksforgeeks:get_profile - score keys mismatch"
        )

if __name__ == "__main__":
    unittest.main()