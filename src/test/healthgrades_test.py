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

    def test_get_best_hospitals(self):
        best_hospitals = self.instance.get_best_hospitals('bihar')

        # assert statements
        self.assertIsInstance(best_hospitals, list)


if __name__ == "__main__":
    unittest.main()
