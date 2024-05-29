import unittest
from src.scrape_up.zomato import Zomato

class TestZomato(unittest.TestCase):
    def setUp(self):
        self.restaurant = Zomato()
        
    def test_get_restaurants_details(self):
        #restaurant = Zomato()
        result=self.restaurant.get_restaurants_details(page_url="https://www.zomato.com/ncr/music-mountains-hillside-cafe-greater-kailash-gk-1-new-delhi/order")
        print(result)
        self.assertIsNotNone(result)
        self.assertIsInstance(result,dict)
        if result is not None:
            self.assertIn("name",result)
            self.assertIn("cuisine",result)
            self.assertIn("area",result)
            self.assertIn("dining_rating",result)
            self.assertIn("dining_review_count",result)
            self.assertIn("delivery_rating",result)
            self.assertIn("delivery_review_count",result)
            self.assertIn("offers",result)    
        if result["name"] is not None:
            self.assertIsInstance(result["name"],str)
        if result["cuisine"] is not None:
            self.assertIsInstance(result["cuisine"],list)
        if result["area"] is not None:
            self.assertIsInstance(result["area"],str)
        if result["dining_rating"] is not None:
            self.assertIsInstance(result["dining_rating"],str)
        if result["dining_review_count"] is not None:    
            self.assertIsInstance(result["dining_review_count"],str)
        if result["delivery_rating"] is not None:
            self.assertIsInstance(result["dining_rating"],str)
        if result["delivery_review_count"] is not None:    
            self.assertIsInstance(result["dining_review_count"],str)    
        if result["offers"] is not None:
            self.assertIsInstance(result["offers"],list)   
  
      
if __name__ == "__main__":
    unittest.main()
            