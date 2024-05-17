from bs4 import BeautifulSoup
import json

from scrape_up.config.request_config import RequestConfig, get


class EazyDiner:
    """
    Create an instance of `EazyDiner` class.\n
    ```python
    restaurants = EazyDiner(location="city-name")
    ```
    | Methods             | Details                                                                               |
    | ------------------- | ------------------------------------------------------------------------------------- |
    | `.get_restaurants()` | Returns the restaurants name, location, rating, cuisine and prices in JSON format.  |
    | `.get_breakfast()`   | Returns the restaurants name, location, rating, cuisine and prices in JSON format for Breakfast.|
    | `.get_lunch()`       | Returns the restaurants name, location, rating, cuisine and prices in JSON format for Lunch. |
    | `.get_dinner()`      | Returns the restaurants name, location, rating, cuisine and prices in JSON format for Dinner.|
    | `.dinner_with_discount()` | Returns list of restaurant from the entered location with 50% offer.|
    | `.get_top10()`      | Returns list of top 10 restaurants from given city|
    """

    def __init__(self, location: str, *, config: RequestConfig = RequestConfig()):
        self.location = location
        self.config = config

    def get_restaurants(self):
        """
        Class - `EazyDiner`
        Example:
        ```
        del = EazyDiner("Delhi NCR") or del = EazyDiner("delhi-ncr")
        del.getRestaurants()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        url = (
            "https://www.eazydiner.com/restaurants?location="
            + self.location.replace(" ", "-").replace(",", "").lower()
        )
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "restaurant": name,
                        "location": location,
                        "rating": rating,
                        "cuisine": cuisine,
                        "price": "Rs. " + price + " for two",
                    }
                )
            res_json = json.dumps(restaurant_data)
            return res_json
        except:
            error_message = {
                "message": "There are no restaurants in the given location."
            }
            ejson = json.dumps(error_message)
            return ejson

    def get_breakfast(self):
        """
        Class - `EazyDiner`
        Example:
        ```
        del = EazyDiner("Delhi NCR") or del = EazyDiner("delhi-ncr")
        del.getBreakfast()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        url = (
            "https://www.eazydiner.com/restaurants?location="
            + self.location.replace(" ", "-").replace(",", "").lower()
            + "&meal_period=breakfast"
        )
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "restaurant": name,
                        "location": location,
                        "rating": rating,
                        "cuisine": cuisine,
                        "price": "Rs. " + price + " for two",
                    }
                )
            res_json = json.dumps(restaurant_data)
            return res_json
        except:
            error_message = {
                "message": "There are no restaurants in the given location."
            }
            ejson = json.dumps(error_message)
            return ejson

    def get_lunch(self):
        """
        Class - `EazyDiner`
        Example:
        ```
        del = EazyDiner("Delhi NCR") or del = EazyDiner("delhi-ncr")
        del.getLunch()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        url = (
            "https://www.eazydiner.com/restaurants?location="
            + self.location.replace(" ", "-").replace(",", "").lower()
            + "&meal_period=lunch"
        )
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "restaurant": name,
                        "location": location,
                        "rating": rating,
                        "cuisine": cuisine,
                        "price": "Rs. " + price + " for two",
                    }
                )
            res_json = json.dumps(restaurant_data)
            return res_json
        except:
            error_message = {
                "message": "There are no restaurants in the given location."
            }
            ejson = json.dumps(error_message)
            return ejson

    def get_dinner(self):
        """
        Class - `EazyDiner`
        Example:
        ```
        del = EazyDiner("Delhi NCR") or del = EazyDiner("delhi-ncr")
        del.getDinner()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        url = (
            "https://www.eazydiner.com/restaurants?location="
            + self.location.replace(" ", "-").replace(",", "").lower()
            + "&meal_period=dinner"
        )
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "restaurant": name,
                        "location": location,
                        "rating": rating,
                        "cuisine": cuisine,
                        "price": "Rs. " + price + " for two",
                    }
                )
            res_json = json.dumps(restaurant_data)
            return res_json
        except:
            error_message = {
                "message": "There are no restaurants in the given location."
            }
            ejson = json.dumps(error_message)
            return ejson

    def dinner_with_discount(self):
        """
        Returns list of resturant from the entered location with 50% offer.\n
        Class - `EazyDiner`
        Example:
        ```
        deldiner = EazyDiner("Delhi NCR")
        deldiner.dinner_with_discount()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        url = (
            "https://www.eazydiner.com/restaurants?location="
            + self.location.replace(" ", "-").replace(",", "").lower()
            + "&meal_period=dinner&buckets%5B%5D=fifty-percent-discounts"
        )
        try:
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "restaurant": name,
                        "location": location,
                        "rating": rating,
                        "cuisine": cuisine,
                        "price": "Rs. " + price + " for two",
                    }
                )
            return restaurant_data["restaurants"]
        except:
            return None

    def get_top10(self):
        """
        Returns list of top 10 restaurants from given city.\n
        Class - `EazyDiner`
        Example:
        ```
        deldiner = EazyDiner("Delhi NCR")
        deldiner.get_top10()
        ```
        Returns:
        {
            "restaurant": restaurant name
            "location": location of restaurant
            "rating": rating
            "cuisine": cuisines provided
            "price": price for two people
        }
        """
        try:
            url = f"https://www.eazydiner.com/{self.location}/restaurants"
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            restaurant_data = {"restaurants": []}

            restaurants = soup.select(".restaurant")
            for r in restaurants:
                name = r.find("h3", class_="res_name").getText().strip()
                location = r.find("h3", class_="res_loc").getText().strip()
                rating = r.find("span", class_="critic").getText().strip()
                cuisine = (
                    r.find("div", class_="res_cuisine").getText().replace(",", ", ")
                )
                price = (
                    r.find("span", class_="cost_for_two")
                    .getText()
                    .encode("ascii", "ignore")
                    .decode()
                    .strip()
                )
                restaurant_data["restaurants"].append(
                    {
                        "Restaurant": name,
                        "Location": location,
                        "Rating": rating,
                        "Cuisine": cuisine,
                        "Price": "Rs. " + price + " for two",
                    }
                )
            return restaurant_data
        except:
            return None
