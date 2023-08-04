from bs4 import BeautifulSoup
import requests

class HeathGrades:
    """
    Create an instance of the `HeathGrades` class to fetch information about the best hospitals in a specific state.

    | Method                         | Details                                                               |
    | ------------------------------ | --------------------------------------------------------------------- |
    | `get_best_hospitals(state)`    | Fetches and returns information about the best hospitals in a state.

    """
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"}

    def get_best_hospitals(self,state):
        """
        Fetches and returns information about the best hospitals in a specific state.

        :param state: The name of the state for which to fetch hospital information.
        :type state: str
        :return: A list of dictionaries containing details of the best hospitals.
        :rtype: list

        Each dictionary in the list contains the following information:
        - "Name": The name of the hospital.
        - "Location": The location of the hospital.
        - "Link": The link to the hospital's profile.
        - "Awards": A list of awards received by the hospital.

        Example output:
        ```python
        [
            {
                "Name": "ABC Hospital",
                "Location": "123 Main St, Philadelphia, PA",
                "Link": "https://www.healthgrades.com/hospital/abc-hospital",
                "Awards": ["America's 100 Best Hospitals", "Patient Safety Excellence Award"]
            },
            ...
        ]
        ```
        """
        try:
            state = state.replace(" ","-")
            url = f"https://www.healthgrades.com/quality/americas-best-hospitals/{state}"
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            hospitals = []
            container = soup.find("ul",{"class":"quality-results-group"})

            for items in container.find_all("div",{"class":"quality-card"}):
                award = []
                title = items.find("h3")
                location = items.find("div",{"class":"location-info"})
                link = "https://www.healthgrades.com"+ items.find("div",{"class":"hospital-info__hospital-link"}).find("a",href=True)['href']
                awards = items.find("ul",{"class":"awards-list__quality-award"})
                for item in awards.find_all("li"):
                    award.append(item.text)
                data = {
                    "Name":title.text,
                    "Location":location.text,
                    "Link":link,
                    "Awards":award[:-2]
                }
                hospitals.append(data)
            return hospitals
        except:
            return None

