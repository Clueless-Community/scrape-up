import unittest
from scrape_up import codeforces

class CodeforcesTest(unittest.TestCase):
    """
    Codeforces module test.\n
    | Methods                       | Details                                                          |
    | ----------------------------- | ---------------------------------------------------------------- |
    | `get_user_data(username)`     | Fetches user data from CodeForces. |
    | `get_contests()`              | Returns information on active and past contests like title, start, and duration |
    """

    def test_get_user_data(self):
        instance = codeforces.Users(username="tourist")
        method_response = instance.get_user_data()

        self.assertEqual(
            list(method_response.keys()),
            [
            "rank",
            "handle",
            "firstname",
            "lastname",
            "city",
            "country",
            "organization",
            "rating",
            "contribution",
            "friendsofcount",
            "lastvisit",
            "registered",
            "titlephoto",
            "avatar"
            ],
            "Codeforces:get_user_data - keys mismatch",
        )
    def test_get_contests(self):
        instance = codeforces.Contest()
        method_response = instance.get_contests()

        self.assertEqual(
            list(method_response.keys()),
            [
            "upcoming_contest",
            "ended_contest"
            ],
            "Codeforces:get_contests - keys mismatch",
        )


