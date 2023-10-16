import unittest

from scrape_up.healthgrades import HealthGrades


class HealthGradesTest(unittest.TestCase):
    """
    HealthGrades module test.\n
    | Methods         | Details                                                          |
    | --------------- | ---------------------------------------------------------------- |
    | `get_best_hospitals()` | Returns Name, Location, Link, Awards etc.                 |
    """

    def setUp(self):
        """
        setup instance for HealthGrades class
        """
        self.instance = HealthGrades()

    def test_get_best_hospitals(self):
        """
        Test get_best_hospitals for state 'bihar'
        """
        best_hospitals = self.instance.get_best_hospitals("bihar")
        first_hospital = best_hospitals[0]

        # assert statements
        self.assertIsInstance(best_hospitals, list)
        self.assertIsInstance(first_hospital, dict)
        self.assertEqual(
            list(first_hospital.keys()),
            ["Name", "Location", "Link", "Awards"],
            "Healthgrades:get_best_hospitals - keys mismatch",
        )


if __name__ == "__main__":
    unittest.main()
