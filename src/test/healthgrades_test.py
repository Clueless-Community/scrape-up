import unittest

from scrape_up import healthgrades


class HealthGradesTest(unittest.TestCase):
    """
    HealthGrades module test.\n
    | Methods         | Details                                                          |
    | --------------- | ---------------------------------------------------------------- |
    | `get_best_hospitals()` | Returns Name, Location, Link, Awards etc.                 |
    """

    def setUp(self):
        self.instance = healthgrades.HealthGrades()


if __name__ == "__main__":
    unittest.main()
