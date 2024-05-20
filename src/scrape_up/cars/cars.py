import requests
from bs4 import BeautifulSoup
import json


class Cars:
    """
    Create an instance of the class `Cars`
    ```python
    scraper = Cars()
    cars_data = scraper.fetch_cars(model, page)
    ```
    | Methods                    | Details                                              |
    | ---------------------------| ---------------------------------------------------- |
    | `.fetch_cars(model, page)` | Fetch car listings data based on the model and page. |
    """

    def __init__(self):
        self.base_url = "https://www.cars.com"

    def fetch_cars(self, model, page=1):
        """
        Fetch car listings data based on the model, and page.

        Parameters:
        - `model`: The model of the car.
        - `page` : The page number of the search results (default: 1).

        Example:
        ```python
        scraper = Cars()
        cars_data = scraper.fetch_cars("Toyota", page=1)
        ```
        """
        try:
            url = f"{self.base_url}/shopping/results/?&keyword={model}&page={page}"
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            car_listings = soup.find_all("div", class_="vehicle-card")

            cars = []
            for car in car_listings:
                car_info = self.__extract_car_info(car)
                if car_info:
                    cars.append(car_info)
            return cars
        except Exception:
            return None

    def __extract_car_info(self, car):
        """
        Extract car information from a single car listing.
        """

        car_model = self.__extract_car_model(car)
        car_url = self.__extract_car_url(car)
        dealer_name = self.__extract_dealer_name(car)
        car_price = self.__extract_car_price(car)
        car_discount = self.__extract_car_discount(car)

        return {
            "model": car_model,
            "dealer": dealer_name,
            "price": car_price,
            "discount": car_discount,
            "url": car_url,
        }

    def __extract_car_model(self, car):
        return car.find("h2", class_="title").text.strip()

    def __extract_car_url(self, car):
        return self.base_url + car.find("a")["href"]

    def __extract_car_price(self, car):
        car_price = car.find("span", class_="primary-price").text.strip()
        if car_price == "Not Priced":
            return None
        return car_price

    def __extract_dealer_name(self, car):
        dealer_name = car.find("div", class_="dealer-name")
        return dealer_name.text.strip() if dealer_name else None

    def __extract_car_discount(self, car):
        car_discount = car.find("span", class_="price-drop")
        return car_discount.text.strip() if car_discount else None
