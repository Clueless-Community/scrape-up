import unittest
from scrape_up.healthgrades import HealthGrades

class HealthGradesTest(unittest.TestCase):
    """
    HealthGrades class test.\n
    | Methods                  | Details                                                         |
    | ------------------------- | --------------------------------------------------------------- |
    | `.get_best_hospitals()`   | Tests the get_best_hospitals() method of the HealthGrades class |
    """

    def test_healthgrades_query(self):
        healthgrades = HealthGrades()

        # Test get_best_hospitals() method
        state = "bihar"  # Replace with an appropriate state
        best_hospitals = healthgrades.get_best_hospitals(state)
        self.assertIsInstance(best_hospitals, list)
        for hospital_data in best_hospitals:
            self.assertIsInstance(hospital_data, dict)
            self.assertIn("Name", hospital_data)
            self.assertIn("Location", hospital_data)
            self.assertIn("Link", hospital_data)
            self.assertIn("Awards", hospital_data)

if __name__ == "__main__":
    unittest.main()
