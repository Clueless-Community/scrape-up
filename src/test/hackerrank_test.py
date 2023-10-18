import unittest
from scrape_up import hackerrank


class HackerrankTest(unittest.TestCase):
    """
    CodeChef module test.\n
    | Methods                       | Details                                                          |
    | ----------------------------- | ---------------------------------------------------------------- |
    | `get_profile(id="username")`  | Returns name, username, country, user_type, details, badges, verified_skills, social etc. |
    | `get_skills()`                | Returns information on active contests like title, status, and link |
    | `active_contests()`           | Returns a list of verified skills and their links |
    | `archived_contests()`         | Returns information regarding archived contests |
    """

    def test_get_profile(self):
        instance = hackerrank.User()
        method_response = instance.get_profile(id="inclinedadarsh")

        self.assertEqual(
            list(method_response.keys()),
            [
                "name",
                "username",
                "country",
                "user_type",
                "details",
                "badges",
                "verified_skills",
                "social",
            ],
            "Hackerrank:get_profile - keys mismatch",
        )

    def test_get_skills(self):
        instance = hackerrank.User()
        method_response = instance.get_skills()

        self.assertIsInstance(
            method_response, list, "Hackerrank:get_skills - return type mismatch"
        )
        self.assertTrue(
            all(isinstance(skill, dict) for skill in method_response),
            "Hackerrank:get_skills - return type mismatch",
        )

        for skill in method_response:
            self.assertIn("Name", skill)
            self.assertIn("Link", skill)

    def test_active_contests(self):
        instance = hackerrank.Contest()
        method_response = instance.active_contests()

        self.assertIsInstance(
            method_response, list, "Hackerrank:active_contests - return type mismatch"
        )
        self.assertTrue(
            all(isinstance(contest, dict) for contest in method_response),
            "Hackerrank:active_contests - return type mismatch",
        )
        for contest in method_response:
            self.assertIn("Title", contest)
            self.assertIn("Status", contest)
            self.assertIn("Link", contest)

    def test_archived_contests(self):
        instance = hackerrank.Contest()
        method_response = instance.archived_contests()

        self.assertIsInstance(
            method_response, list, "Hackerrank:archived_contests - return type mismatch"
        )

        for contest in method_response:
            self.assertIn("title", contest)


if __name__ == "__main__":
    unittest.main()
