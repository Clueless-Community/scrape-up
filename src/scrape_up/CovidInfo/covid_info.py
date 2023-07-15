import pandas as pd
import requests
from bs4 import BeautifulSoup


class CovidInfo:
    """
    Class - `CovidInfo`\n
    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.scrape()`                 | Returns the scraped data from the target website of all the countries in the form of a list          |
    | `.findCountry()`            | Returns the data related to the specific country passed as a parameter into the function             |
    | `.sortbycases()`            | Returns the list of datas of all the country, sorted according to the number of cases                |
    | `.sortbydeaths()`           | Returns the list of datas of all the country, sorted according to the number of deaths               |
    | `.totalcases()`             | Returns the total number of covid cases as of yet in the form of a string of numbers                 |
    | `.totaldeaths()`            | Returns the total number of covid deaths as of yet in the form of a string of numbers                |
    """

    def __init__(self):
        pass

    def covid_data(self):
        """
        Class - `CovidInfo`\n
        ```python
        response = CovidInfo()
        response.covid_data()
        ```
        Returns\n
        ```js
        {'Country': 'United States', 'Number of Cases': 107365548, 'Deaths': 1168558, 'Continent': 'North America'}
        ```
        """

        url = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        keys_data = ["Country", "Number of Cases", "Deaths", "Continent"]
        response_data = []
        data_iterator = iter(soup.find_all("td"))
        while True:
            try:
                country = next(data_iterator).text
                confirmed = str(
                    next(data_iterator).text.replace(",", "").replace(" ", "")
                )
                deaths = str(next(data_iterator).text.replace(",", "").replace(" ", ""))
                continent = next(data_iterator).text

                values_data = [country, int(confirmed), int(deaths), continent]
                zipped_data = dict(zip(keys_data, values_data))
                response_data.append(zipped_data)

            except StopIteration:
                break
        if len(response_data) == 1:
            return None
        else:
            return response_data

    def total_cases(self):
        """
        Get the total number of COVID cases in the world\n
        Class - `CovidInfo`\n
        ```python
        response = CovidInfo()
        response.total_cases()
        ```
        """
        try:
            url = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            req = soup.find_all("span", {"class": "bold_number"})

            z = req[0].find_all("a")
            fin = ""
            for i in z:
                fin = fin + i.contents[0]
            sol = fin.split(" ")
            return sol[0]
        except:
            return None

    def total_deaths(self):
        """
        Get the total number of COVID-deaths in the world\n
        Class - `CovidInfo`\n
        ```python
        response = CovidInfo()
        response.total_cases()
        ```
        """
        try:
            url = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            req = soup.find_all("a", {"href": "/coronavirus/coronavirus-death-toll/"})
            k = req[0].find("strong").contents[0].split(" ")
            return k[0]
        except:
            return None
