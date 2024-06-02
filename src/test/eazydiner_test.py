import unittest
import json
from scrape_up.eazydiner import EazyDiner


class EazyDinerTest(unittest.TestCase):
    """
    EazyDiner class test.\n
    | Methods                  | Details                                                          |
    | ------------------------ | ---------------------------------------------------------------- |
    | `.get_restaurants()`     | Tests the get_restaurants() method of the EazyDiner class        |
    | `.get_breakfast()`       | Tests the get_breakfast() method of the EazyDiner class          |
    | `.get_lunch()`           | Tests the get_lunch() method of the EazyDiner class              |
    | `.get_dinner()`          | Tests the get_dinner() method of the EazyDiner class             |
    | `.dinner_with_discount()`| Tests the dinner_with_discount() method of the EazyDiner class   |
    | `.get_top10()`           | Tests the get_top10() method of the EazyDiner class              |
    """

    def assert_response_keys(self, response, expected_keys):
        if isinstance(response, str):
            response_dict = json.loads(response)

            for key in expected_keys:
                self.assertTrue(
                    key in response_dict, f"Key '{key}' is missing in the response."
                )

    def test_get_restaurants(self):
        eazydiner = EazyDiner(
            location="AGRA"
        )  # Replace with an appropriate location
        restaurants = eazydiner.get_restaurants()
        self.assertIsInstance(restaurants, str)
        self.assert_response_keys(restaurants, ["restaurants"])

    def test_get_breakfast(self):
        eazydiner = EazyDiner(
            location="AGRA"
        )  # Replace with an appropriate location
        breakfast = eazydiner.get_breakfast()
        self.assertIsInstance(breakfast, str)
        self.assert_response_keys(breakfast, ["restaurants"])

    def test_get_lunch(self):
        eazydiner = EazyDiner(
            location="AGRA"
        )  # Replace with an appropriate location
        lunch = eazydiner.get_lunch()
        self.assertIsInstance(lunch, str)
        self.assert_response_keys(lunch, ["restaurants"])

    def test_get_dinner(self):
        eazydiner = EazyDiner(
            location="AGRA"
        )  # Replace with an appropriate location
        dinner = eazydiner.get_dinner()
        self.assertIsInstance(dinner, str)
        self.assert_response_keys(dinner, ["restaurants"])

    def test_dinner_with_discount(self):
        eazydiner = EazyDiner(
            location="AGRA"
        )  # Replace with an appropriate location
        dinner_discount = eazydiner.dinner_with_discount()
        self.assertIsInstance(dinner_discount, list)

    def test_get_top10(self):
        eazydiner = EazyDiner(
            location="AGRA"
        )  # Replace with an appropriate location
        top10 = eazydiner.get_top10()
        self.assertIsInstance(top10, dict)


if __name__ == "__main__":
    unittest.main()
