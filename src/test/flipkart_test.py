import unittest
from scrape_up import flipkart

class FlipKartTest(unittest.TestCase):
    """
    FlipKart module test.\n
    | Methods                        | Details                                                                 |
    | ------------------------------ | ----------------------------------------------------------------------- |
    | `.test_get_tvs()`              | Returns Item_Name, Price, Rating, Specifications.                       |
    | `.test_get_bestseller_books()` | Returns Item_Name, Price, Rating, Specifications.                       |
    | `.test_get_mobiles()`          | Returns Item_Name, Price, Description, Review.                          |
    | `.test_get_sport_shoes()`      | Returns Item_Name, Image_URL, Details.                                  |
    | `.test_get_laptops()`          | Returns Item_Name, Price, Description, Review.                          |
    | `.test_get_headphones()`       | Returns Item_Name, Price, Description, Review.                          |
    | `.test_get_camera()`           | Returns Item_Name, Price, Description, Review.                          |
    | `.test_get_computer()`         | Returns Item_Name, Price, Delivery, Review.                             |
    | `.test_get_tablets()`          | Returns Item_Name, Price, Description, Review, Offer_Price.             |
    | `.test_get_cycle()`            | Returns Item_Name, Price, Description, Review, Deals.                   |
    | `.test_get_printers()`         | Returns Item_Name, Price, Description, Review, Delivery, Exchange_Upto. |
    | `.test_get_monitor()`          | Returns Item_Name, Price, Description, Review, Deals.                   |
    | `.test_get_ac()`               | Returns Item_Name, Price, Description, Review, Deals.                   |
    | `.test_get_refrigerator()`     | Returns Item_Name, Price, Description, Review, Deals.                   |
    | `.test_get_vrbox()`            | Returns Item_Name, Price, Review, Delivery.                             |
    | `.test_get_speakers()`         | Returns Item_Name, Price, Color, Review, Delivery, Off_Percentage.      |
    """

    def test_get_tvs(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.tvs()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Rating","Specifications"]
        )
    
    def test_get_bestseller_books(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.bestseller_books()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Rating","Specifications"]
        )

    def test_get_mobiles(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.mobiles()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Review"]
        )

    def test_get_sport_shoes(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.sport_shoes()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Image_URL","Details"]
        )

    def test_get_laptops(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.laptops()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Review"]
        )
    
    def test_get_headphones(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.headphones()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Review"]
        )

    def test_get_camera(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.camera()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Review"]
        )

    def test_get_computer(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.computer()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Delivery","Review"]
        )

    def test_get_tablets(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.tablets()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Descripion","Review", "Offer_Price"]
        )

    def test_get_cycle(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.cycle()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Review", "Deals"]
        )

    def test_get_printers(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.printers()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Delivery", "Exchange_Upto"]
        )

    def test_get_monitor(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.monitor()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Review", "Deals"]
        )

    def test_get_ac(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.ac()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Reviews", "Deals"]
        )

    def test_get_refrigerator(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.refrigerator()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Description","Reviews", "Deals"]
        )

    def test_get_vrbox(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.vrbox()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Reviews","Delivery"]
        )

    def test_get_speakers(self):
        instance = flipkart.flipkart_file.Flipkart()
        method_response = instance.speakers()
        self.assertEqual(
            list(method_response.keys()),
            ["Item_Name","Price","Color","Reviews","Delivery", "Off_Percentage"]
        )

if __name__ == "__main__":
   unittest.main() 