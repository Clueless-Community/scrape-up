from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class IndianCity:
    """
    Create an instance of `IndianCity` class with the name of the city
    ```python
    indiancity = IndianCity("bengaluru")
    ```

    | Methods              | Details                                         |
    | ---------------------|-------------------------------------------------|
    | `.state()`           | Returns the state of the c                      |
    | `.lat_long()`        | Returns the latitude and longitude of the city  |
    | `.elevation()`       | Returns the elevation of the city from sea level|
    | `.language()`        | Returns the language spoken in the city         |
    | `.weather()`         | Returns the weather in the city                 |
    | `.local_time()`      | Returns the local time in the city              |
    | `.nearby_airports()` | Returns a list of nearby airports in the city   |


    """

    def __init__(self, city):
        city = "-".join(city.split())
        self.city = city.lower()
        self.__scrape_page()
        self.__get_details()

    def __scrape_page(self):
        try:
            url = "https://www.timeanddate.com/worldclock/india/" + self.city
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def __get_details(self):
        try:
            x = self.page_soup.find_all("td")
            x = x[:6]
            self.details = []
            for y in x:
                self.details.append(y.get_text())
        except:
            return None

    def state(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.state()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'State': 'Karnataka'
        }
        ```
        """
        obj_keys = ["City", "State"]
        try:
            return dict(zip(obj_keys, [self.city, self.details[1]]))
        except:
            return None

    def lat_long(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.lat_long()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'Latitude and Longitude': "12°58'N / 77°34'E"
        }
        ```
        """

        obj_keys = ["City", "Latitude and Longitude"]
        try:
            return dict(zip(obj_keys, [self.city, self.details[2]]))
        except:
            return None

    def elevation(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.elevation()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'Elevation': '876 m'
        }
        ```
        """

        obj_keys = ["City", "Elevation"]
        try:
            return dict(zip(obj_keys, [self.city, self.details[3]]))
        except:
            return None

    def language(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.language()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'Language': 'Kannada'
        }
        ```
        """

        obj_keys = ["City", "Language"]
        try:
            return dict(zip(obj_keys, [self.city, self.details[5]]))
        except:
            return None

    def weather(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.weather()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'Weather': '30 °C'
        }
        ```
        """

        obj_keys = ["City", "Weather"]
        try:
            temp = self.page_soup.find("div", {"id": "wt-tp"})
            temp = " ".join(temp.get_text().split("\xa0"))
            return dict(zip(obj_keys, [self.city, temp]))
        except:
            return None

    def local_time(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.local_time()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'Time': '15:46:05'
        }
        ```
        """

        obj_keys = ["City", "Time"]
        try:
            temp = self.page_soup.find("span", {"id": "ct"})
            temp = temp.get_text()
            return dict(zip(obj_keys, [self.city, temp]))
        except:
            return None

    def nearby_airports(self):
        """
        Create an instance of `IndianCity` class with the name of the city
        ```python
        indiancity = IndianCity("bengaluru")
        indianciy.nearby_airports()
        ```

        Return\n
        ```js
        {
            'City': 'bengaluru',
            'Airports': ['Kempegowda International Airport, BLR',
                        'Calicut International Airport, CCJ',
                        'Chennai International Airport, MAA']
        }
        ```
        """

        obj_keys = ["City", "Airports"]
        try:
            temp = self.page_soup.find_all("div", {"class": "four columns"})
            temp = temp[4:]
            temp = str(temp[0]).split("<li>")
            temp_list = []
            for x in temp[1:]:
                temp_list.append((x.split("<br/>"))[0])

            return dict(zip(obj_keys, [self.city, temp_list]))
        except:
            return None
