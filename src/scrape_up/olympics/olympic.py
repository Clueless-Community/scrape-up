from bs4 import BeautifulSoup
import requests

from scrape_up.config.request_config import RequestConfig, get


class Olympics:
    """
    Create an object of the 'Olympics' class\n
    ```python
    scraper = Olympics()
    ```
    | Methods                | Details                                                                                    |
    | ---------------------- | ------------------------------------------------------------------------------------------ |
    | `.allcountries()`      |  returns the list of all the countries participated yet in olympics.                       |
    | `.allsports()`         |  returns the list of all the sports being currently played in olympics.                    |
    | `.alldeceased()`       |  Returns the list of all recently deceased olympians along with their death date.          |
    | `.alltimemedals()`     |  Returns list of all countries with their total numbers of medals yet in all categories.   |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config
        # print(self)

    def allcountries(self):
        """
        Create an object of the 'TOlympics' class\n
        ```python
        scraper = Olympics()
        scraper.allcountries()
        ```
        Response
        ```js
        {
            'res': List of all countries which participated in olympics
        }
        ```
        """

        url = "http://www.olympedia.org/countries/best_results"

        try:
            try:
                response = get(url, self.config)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            except requests.RequestException as e:
                print(f"Error fetching headlines: {e}")
                return []

            soup = BeautifulSoup(response.content, "html.parser")

            titles = soup.find_all(
                "select", attrs={"class": "form-control", "name": "country_id"}
            )
            alldata = []
            for i in titles:
                res = i.text.split("\n")
                alldata = res

            return alldata[1:]

        except:
            return None

    def allsports(self):
        """
        Create an object of the 'TOlympics' class\n
        ```python
        scraper = Olympics()
        scraper.allsports()
        ```
        Response
        ```js
        {
            'res': List of all sports which are currently played in olympics
        }
        ```
        """

        url = "http://www.olympedia.org/countries/best_results"

        try:
            try:
                response = get(url, self.config)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            except requests.RequestException as e:
                print(f"Error fetching headlines: {e}")
                return []

            soup = BeautifulSoup(response.content, "html.parser")

            titles = soup.find_all(
                "select", attrs={"class": "form-control", "name": "event_name_id"}
            )
            alldata = []
            for i in titles:
                res = i.text.split("\n")
                alldata = res

            return alldata[1:]

        except:
            return None

    def alldeceased(self):
        """
        Create an object of the 'TOlympics' class\n
        ```python
        scraper = Olympics()
        scraper.alldeceased()
        ```
        Response
        ```js
        {
            'res': List of all recently died olympians along with their death date
        }
        ```
        """

        url = "http://www.olympedia.org/athletes/recent_deaths"

        try:
            try:
                response = get(url, self.config)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            except requests.RequestException as e:
                print(f"Error fetching headlines: {e}")
                return []

            soup = BeautifulSoup(response.content, "html.parser")

            data = soup.find_all("tr")
            ret = []
            for i in data:
                k = i.text.replace("\n", " ").strip()
                ret.append(k)
                # print(i.text)
            return ret[1:]

        except:
            return None

    def alltimemedals(self):
        """
        Create an object of the 'TOlympics' class\n
        ```python
        scraper = Olympics()
        scraper.alltimemedals()
        ```
        Response
        ```js
        {
            'res': List of countries with their medal counts of all types- bronze, silver, and gold
        }
        ```
        """

        url = "http://www.olympedia.org/statistics/medal/country"
        try:
            try:
                response = get(url, self.config)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            except requests.RequestException as e:
                print(f"Error fetching headlines: {e}")
                return []

            soup = BeautifulSoup(response.content, "html.parser")

            data = soup.find_all("tr")
            val = []
            for i in data:
                k = i.text.replace("\n", "    ").strip()
                val.append(k)

            val[0] = "NOC.   Code.   Gold.   Silver.   Bronze.   Total"
            return val
        except:
            return None
