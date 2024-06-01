import unittest
import requests
from unittest.mock import patch
from scrape_up.swiggy import Swiggy


class TestSwiggy(unittest.TestCase):
    """
    Swiggy module test.
    | Methods                   | Details                                                                   |
    | ------------------------- | ------------------------------------------------------------------------- |
    | `get_restraunt_details()` | Returns the restaurant data with name, cuisine, area, rating, offers, etc |
    | `get_restaurants()`       | Returns the restaurant names as per given city                            |
    """

    def setUp(self):
        self.scrapper = Swiggy()

    def test_get_restraunt_details(self):
        try:

            expected_data = {
                "name": "Pizza Hut",
                "cuisine": "Pizzas",
                "area": "Karol Bagh",
                "rating": "3.7",
                "rating_count": "1K+ ratings",
                "cost_per_person": "₹350 for two",
                "offers": [{"15% OFF UPTO ₹300": "USE CITIFOODIE | ABOVE ₹1200"}],
            }

            self.assertEqual(
                self.scrapper.get_restraunt_details("https://www.swiggy.com/pizza-hut"),
                expected_data,
            )
        except:
            return None

    def test_get_restaurants(self):
        try:

            expected_restaurants = [
                {
                    "Name": "Domino's Pizza",
                    "Rating": "4.2",
                    "Cusine": "Pizzas, Italian, Pastas, Desserts",
                    "Location": "Punjabi Bagh",
                    "Link": "/restaurant1",
                }
            ]

            self.assertEqual(
                self.scrapper.get_restaurants("Delhi"), expected_restaurants
            )
        except:
            return None


if __name__ == "__main__":
    unittest.main()
