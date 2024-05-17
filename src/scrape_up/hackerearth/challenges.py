from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Challenges:
    """
    First, create an object of class `Challenges`
    ```python
    hackerearth = Challenges()
    ```
    | Methods          | Details                                                |
    | ---------------- | ------------------------------------------------------ |
    | `get_upcoming()` | Get the details of upcoming challenges on Hackerearth. |
    | `get_ongoing()`  | Get the details of ongoing challenges on Hackerearth.  |
    | `get_hiring()`  | Get the details of hiring challenges on Hackerearth.  |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_ongoing(self):
        """
        Get the details of ongoing challenges on Hackerearth.\n
        Example
        ```python
        hacker = Challenges()
        hacker.get_ongoing()
        ```
        Returns:
        ```js
        [
            {
                "Title":"Koinos Supercharger Event (Calling All Coders!)",
                "No of Registrations":"970",
                "Link":"https://koinos.hackerearth.com/"
            }
            ...
        ]
        ```
        """
        try:
            url = "https://www.hackerearth.com/challenges/"
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")
            container = soup.find("div", {"class": "left border-right"})
            challenge = []
            ongoing = container.find("div", {"class": "ongoing challenge-list"})
            for items in ongoing.find_all("div", {"class": "challenge-card-modern"}):
                title = items.find(
                    "span", {"class": "challenge-list-title challenge-card-wrapper"}
                ).text
                registrations = items.find(
                    "div", {"class": "registrations tool-tip align-left"}
                ).text.strip()
                link = items.find("a", href=True)["href"]
                if link[:5] != "https":
                    link = "https://www.hackerearth.com" + link
                data = {
                    "Title": title,
                    "No of Registrations": registrations,
                    "Link": link,
                }
                challenge.append(data)
            return challenge
        except:
            return None

    def get_upcoming(self):
        """
        Get the details of ongoing challenges on Hackerearth.\n
        Example
        ```python
        hacker = Challenges()
        hacker.get_upcoming()
        ```
        Returns:
        ```js
        [
            {
                "Title":"Cepheid Automation Engineer Hiring Challenge 2023",
                "No of Registrations":"Best in Class",
                "Link":"https://www.hackerearth.com/challenges/hiring/cepheid-automation-engineer-hiring-challenge-2023-2/"
            }
            ...
        ]
        ```
        """
        try:
            url = "https://www.hackerearth.com/challenges/"
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")
            container = soup.find("div", {"class": "left border-right"})
            challenge = []
            upcoming = container.find("div", {"class": "upcoming challenge-list"})
            for items in upcoming.find_all("div", {"class": "challenge-card-modern"}):
                title = items.find(
                    "span", {"class": "challenge-list-title challenge-card-wrapper"}
                ).text
                registrations = items.find(
                    "div", {"class": "registrations tool-tip align-left"}
                ).text.strip()
                link = items.find("a", href=True)["href"]
                if link[:5] != "https":
                    link = "https://www.hackerearth.com" + link
                data = {
                    "Title": title,
                    "No of Registrations": registrations,
                    "Link": link,
                }
                challenge.append(data)
            return challenge
        except:
            return None

    def get_hiring(self):
        """
        Fetches and returns information about ongoing job opportunities from HackerEarth's jobs page.\n
        Example
        ```python
        hacker = Challenges()
        hacker.get_hiring()
        ```
        Example output:
        ```python
        {
            "data": [
                {
                    "Title": "Software Engineer",
                    "Description": "50 registrations",
                    "Link": "https://www.hackerearth.com/job/software-engineer/"
                },
                ...
            ],
            "message": "Information fetched"
        }
        ```
        """

        try:
            url = "https://www.hackerearth.com/jobs/"
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")
            container = soup.find("div", {"class": "left border-right"})
            challenge = []
            upcoming = container.find("div", {"class": "ongoing challenge-list"})
            for items in upcoming.find_all("div", {"class": "challenge-card-modern"}):
                title = items.find(
                    "span", {"class": "challenge-list-title challenge-card-wrapper"}
                ).text
                registrations = items.find(
                    "div", {"class": "registrations tool-tip align-left"}
                ).text.strip()
                link = items.find("a", href=True)["href"]
                if link[:5] != "https":
                    link = "https://www.hackerearth.com" + link
                data = {"Title": title, "Description": registrations, "Link": link}
                challenge.append(data)
            return challenge
        except:
            return None
