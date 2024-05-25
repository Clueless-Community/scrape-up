import requests
import datetime as dt
from bs4 import BeautifulSoup


class Indiatodayweather:
    """
    A class to scrape weather data from Indian today

    Create an instance of `Indiatodayweather` class

    ```python
    weather=Indiatodayweather("Mumbai")
    ```

    | Method                        | Details                                                                                            |
    | ---------------------------   | ------------------------------------------------------------------------                           |
    |`info_about_weather()`         |  return the temperature, wind speed, description(windy, cloudy, clear) and humidity  of the place. |                                                    |

    ---
    """

    def __init__(self, place):
        try:
            self.place = place
            url = (
                "https://www.indiatoday.in/weather/"
                + self.place
                + "-weather-forecast-today"
            )
            response = requests.get(url, headers={"User-Agent": "XY"})
            self.soup = BeautifulSoup(response.content, "lxml")

        except:
            return None

    def info_about_weather(self):
        try:
            temp = self.soup.find("div", class_="wtr_tmp_rhs").text
            humid = self.soup.find("span", class_="wtr_crd_ttl").text + " %"
            description = self.soup.find("span", class_="wtr_tmp_txt").text
            speed = (
                self.soup.find("div", class_="wtr_wid_sec crd_three")
                .find("span", class_="wtr_crd_ttl")
                .text
            ) + " km/h"

            weather_info = {
                "temperature": temp,
                "humidity": humid,
                "description": description,
                "wind_speed": speed,
            }
            return weather_info
        except:
            return None
