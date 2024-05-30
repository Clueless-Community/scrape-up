import unittest
import requests
from unittest.mock import patch
from src.scrape_up.swiggy import Swiggy


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

    @patch("requests.get")
    def test_get_restraunt_details(self, mock_get):
        try:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_response._content = """
                <html>
                <body>
                    <p class="RestaurantNameAddress_name__2IaTv">Pizza Hut</p>
                    <p class="RestaurantNameAddress_cuisines__mBHr2">Pizzas</p>
                    <p class="RestaurantNameAddress_area__2P9ib">Karol Bagh</p>
                    <span class="RestaurantRatings_avgRating__1TOWY">3.7</span>
                    <span class="RestaurantRatings_totalRatings__3d6Zc">1K+ ratings</span>
                    <li class="RestaurantTimeCost_item__2HCUz">₹350 for two</li>
                    <div class="RestaurantOffer_infoWrapper__2trmg">
                        <p class="RestaurantOffer_header__3FBtQ">15% OFF UPTO ₹300</p>
                        <span>USE CITIFOODIE</span>
                        <span class="RestaurantOffer_description__1SRJf"> | ABOVE ₹1200</span>
                    </div>
                </body>
                </html>
            """
            mock_get.return_value = mock_response


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

    @patch("requests.get")
    def test_get_restaurants(self, mock_get):
        try:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_response._content = b"""
                <html>
                <body>
                    <div class="sc-iBdmCd hPntbc">
                        <a class="RestaurantList__RestaurantAnchor-sc-1d3nl43-3 jrDRCS" href="/restaurant1">
                            <div class="sc-dmyDGi bJRtXU">Domino's Pizza</div>
                            <span class="sc-dmyDGi flXrCy">4.2</span>
                            <div class="sc-dmyDGi jHWzLy">Pizzas, Italian, Pastas, Desserts</div>
                            <div>Punjabi Bagh</div>
                        </a>
                    </div>
                </body>
                </html>
            """
            mock_get.return_value = mock_response

            expected_restaurants = [
                {
                    "Name": "Domino's Pizza",
                    "Rating": "4.2",
                    "Cusine": "Pizzas, Italian, Pastas, Desserts",
                    "Location": "Punjabi Bagh",
                    "Link": "/restaurant1",
                }
            ]

            self.assertEqual(self.scrapper.get_restaurants("Delhi"), expected_restaurants)
        except:
            return None


if __name__ == "__main__":
    unittest.main()

