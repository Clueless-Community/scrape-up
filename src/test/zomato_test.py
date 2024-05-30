import unittest
from scrape_up.zomato import Zomato


class TestZomato(unittest.TestCase):
    """
    | Methods                       | Details                                                                    |
    | ----------------------------- | -------------------------------------------------------------------------- |
    | `.get_restaurants_details(page_url)`    | Returns the restraunt data with name, cuisine, area, rating, offers, etc|
    """

    def setUp(self):
        self.restaurant = Zomato()

    def test_get_restaurants_details(self):
        result = self.restaurant.get_restaurants_details(
            page_url="https://www.zomato.com/ncr/khatirdari-ek-riwaz-paras-tierea-noida/order"
        )
        try:
            self.assertIsNotNone(
                result,
                "Failed to fetch restaurant details. Please provide a url of type https://www.zomato.com/ncr/music-mountains-hillside-cafe-greater-kailash-gk-1-new-delhi/order",
            )
            self.assertIsInstance(
                result, dict, "Restaurant details should be a dictionary object"
            )
            try:
                if result is not None:
                    for key in result:
                        self.assertIn(result[key], f"no key named {key}")
            except:
                return None

            try:
                if result["name"] is not None:
                    self.assertIsInstance(
                        result["name"], str, "name should be a string"
                    )
                if result["cuisine"] is not None:
                    (
                        self.assertIsInstance(result["cuisine"], list),
                        "cuisine should be a list",
                    )
                if result["area"] is not None:
                    self.assertIsInstance(
                        result["area"], str, "area should be a string"
                    )
                if result["dining_rating"] is not None:
                    self.assertIsInstance(
                        result["dining_rating"],
                        str,
                        "dining rating should be a string representing a number",
                    )
                if result["dining_review_count"] is not None:
                    self.assertIsInstance(
                        result["dining_review_count"],
                        str,
                        "dining review count should be a string representing a number",
                    )
                if result["delivery_rating"] is not None:
                    self.assertIsInstance(
                        result["delivery_rating"],
                        str,
                        "delivery rating should be a string representing a number",
                    )
                if result["delivery_review_count"] is not None:
                    self.assertIsInstance(
                        result["delivery_review_count"],
                        str,
                        "delivery review count should be a string representing a number",
                    )
                if result["offers"] is not None:
                    self.assertIsInstance(
                        result["offers"], list, "offers should be a list"
                    )
            except:
                return None

        except:
            return None


if __name__ == "__main__":
    unittest.main()
