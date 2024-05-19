from bs4 import BeautifulSoup
import re
import requests


class Indiantrekking:
    """
    A class to scrape data from Indian trekking

    Create an instance of `Indiantrekking` class

    ```python
    trek=Indiantrekking("hidden-lakes-of-kashmir")
    ```

    | Method                        | Details                                                                              |
    | ---------------------------   | --------------------------------------------------------------------                 |
    |`destination()`                |  return name of the place.                                                           |
    |'trip_fact()'                  |  returns the trip duration, destination, altitude and the season good for trekking   |
    |'outline_day_to_day_itinerary' |  returns the ouline of the day to day itinerary                                      |
    ---
    """

    def __init__(self, place):
        self.place = place
        try:
            url = f"https://www.indiantrekking.com/{self.place}.html"
            response = requests.get(url, headers={"User-Agent": "XY"})
            self.soup = BeautifulSoup(response.content, "lxml")
        except:
            return None

    def destination_name(self):
        try:
            place = self.soup.find("div", class_="main-title").text
            return place
        except:
            return None

    def trip_fact(self):
        try:
            trip_duration = self.soup.findAll("div", class_="inner-wrap")[0].b.text
            trip_destination = self.soup.findAll("div", class_="inner-wrap")[1].b.text
            trip_season = self.soup.findAll("div", class_="inner-wrap")[3].b.text
            trip_altitude = self.soup.findAll("div", class_="inner-wrap")[4].b.text

            tripfact = {
                "trip_duration": re.sub(" +", " ", trip_duration.strip()),
                "trip_destination": re.sub(" +", " ", trip_destination.strip()),
                "trip_season": re.sub(" +", " ", trip_season.strip()),
                "trip_altitude": re.sub(" +", " ", trip_altitude.strip()),
            }
            return tripfact
        except:
            return None

    def outline_day_to_day_itinerary(self):
        try:
            outline = self.soup.find("div", class_="itinerary").text
            return outline
        except:
            return None
