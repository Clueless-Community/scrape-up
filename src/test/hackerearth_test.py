import unittest

from scrape_up import hackerearth


class HackerEarthTest(unittest.TestCase):
    """
    HackerEarth module test.\n
    | Methods         | Details                                                          |
    | --------------- | ---------------------------------------------------------------- |
    | `get_ongoing()` | Returns the ongoing challenges.                                  |
    | `get_upcoming()`| Returns the upcoming challenges.                                 |
    | `get_hiring()`  | Returns information about ongoing hiring challenges.             |
    """

    def setUp(self):
        self.instance = hackerearth.challenges.Challenges()

    def test_get_ongoing(self):
        ongoing_challenges = self.instance.get_ongoing()
        self.assertIsInstance(ongoing_challenges, list)

        if len(ongoing_challenges) > 0:
            first_challenge = ongoing_challenges[0]
            self.assertIsInstance(first_challenge, dict)
            self.assertEqual(
                list(first_challenge.keys()),
                ["Title", "No of Registrations", "Link"],
                "HackerEarth-Challenges:get_ongoing - keys mismatch",
            )

    def test_get_upcoming(self):
        upcoming_challenges = self.instance.get_upcoming()
        self.assertIsInstance(upcoming_challenges, list)

        if len(upcoming_challenges) > 0:
            first_challenge = upcoming_challenges[0]
            self.assertIsInstance(first_challenge, dict)
            self.assertEqual(
                list(first_challenge.keys()),
                ["Title", "No of Registrations", "Link"],
                "HackerEarth-Challenges:get_upcoming - keys mismatch",
            )

    def test_get_hiring(self):
        hiring_challenges = self.instance.get_hiring()
        self.assertIsInstance(hiring_challenges, list)

        if len(hiring_challenges) > 0:
            first_challenge = hiring_challenges[0]
            self.assertIsInstance(first_challenge, dict)
            self.assertEqual(
                list(first_challenge.keys()),
                ["Title", "Description", "Link"],
                "HackerEarth-Challenges:get_hiring - keys mismatch",
            )


if __name__ == "__main__":
    unittest.main()
