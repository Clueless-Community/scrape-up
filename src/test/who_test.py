import unittest
from src.scrape_up.who import WHO


class TestWHO(unittest.TestCase):

    def setUp(self):
        """
        Initialize a WHO instance before each test method.
        """
        self.who_scraper = WHO()

    def test_get_disease_outbreak(self):
    """
    | Methods                        | Details                                     |
    | ------------------------------ | ------------------------------------------- |
    |    `get_disease_outbreak()`    | Get Disease Outbreak News from WHO website. |
    """
        try:
            # Test with a valid number of items (assuming each page contains 10 items)
            number_of_items = 10
            disease_outbreaks = self.who_scraper.get_disease_outbreak(number_of_items)

            # Check if disease_outbreaks is a list
            self.assertIsNotNone(disease_outbreaks, "Failed to fetch disease outbreaks")
            self.assertIsInstance(disease_outbreaks, list, "Disease outbreaks data should be a list")

            if disease_outbreaks:
                # Check if each item in the list is a dictionary with the required keys
                for outbreak in disease_outbreaks:
                    self.assertIsInstance(outbreak, dict, "Each outbreak should be a dictionary")
                    self.assertIn("Title", outbreak, "Missing expected key: 'Title'")
                    self.assertIn("Date", outbreak, "Missing expected key: 'Date'")
                    self.assertIn("Link", outbreak, "Missing expected key: 'Link'")

                    # Check if the values are of the correct type
                    self.assertIsInstance(outbreak["Title"], str, "'Title' should be a string")
                    self.assertIsInstance(outbreak["Date"], str, "'Date' should be a string")
                    self.assertIsInstance(outbreak["Link"], str, "'Link' should be a string")

        except:
            return None

    def test_invalid_number(self):
        """
        Test the get_disease_outbreak() method with an invalid number.
        """
        try:
            invalid_number = -10
            disease_outbreaks = self.who_scraper.get_disease_outbreak(invalid_number)

            # Check if the function handles invalid numbers gracefully
            self.assertIsNone(disease_outbreaks, "Function should return None for invalid input")
        except:
            return None


if __name__ == "__main__":
    unittest.main()

