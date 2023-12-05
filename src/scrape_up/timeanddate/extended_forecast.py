from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class Forecast:
    """
    Create an instance of `Forecast` class with the name of the city
    ```python
    forecast = Forecast(city="bengaluru")
    ```
    | Methods            | Details                                                                                                                   |
    | -------------------|---------------------------------------------------------------------------------------------------------------------------|
    | `.full_forecast(city)` | Returns datewise the Temperature, Weather, Wind, Humidity, Precipitation chance and Amount, UV, Sunrise, Sunset of a city.|

    """

    def __init__(self, city):
        self.city = city
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = (
                "https://www.timeanddate.com/weather/india/"
                + "-".join(self.city.lower().split(" "))
                + "/ext"
            )
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def full_forecast(self):
        """
        Return the list of forecast details of next few days of a city.\n
        ```python
        forecast = Forecast(city="bengaluru")
        forecast.full_forecast()
        ```

        Return\n
        ```js
        [
            {
                "Temperature":"29 / 21°C",
                "Weather":"Passing showers. Overcast.",
                "Feels like":"30°C",
                "Wind":"12 km/h",
                "Humidity":"53%",
                "Precipitation chance":"58%",
                "Precipitation Amount":"5.3  mm",
                "UV":"3 (Moderate)",
                "Sunrise":"06.06",
                "Sunset":"18.43",
                "Date":"10"
            }
            ...
        ]
        ```
        """
        try:
            x = self.page_soup.find("tbody")
            response = []

            for y in x.find_all("tr"):
                date = "".join(w for w in y.find("th").get_text() if w.isnumeric())
                params = []
                for z in y.find_all("td"):
                    params.append(z.get_text())
                params.pop(0)
                params.pop(4)
                params[0] = "".join(params[0].split("\xa0"))
                params[2] = "".join(params[2].split("\xa0"))
                params_list = [
                    "Temperature",
                    "Weather",
                    "Feels like",
                    "Wind",
                    "Humidity",
                    "Precipitation chance",
                    "Precipitation Amount",
                    "UV",
                    "Sunrise",
                    "Sunset",
                    "Date",
                ]
                params.append(date)
                response.append(dict(zip(params_list, params)))

            return response
        except:
            return None
