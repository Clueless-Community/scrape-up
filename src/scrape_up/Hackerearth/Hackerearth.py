from bs4 import BeautifulSoup
import requests


class Hackerearth:
    """
    First, create an object of class `Hackerearth`
    ```python
    hackerearth = Hackerearth()
    ```
    | Methods          | Details                                                |
    | ---------------- | ------------------------------------------------------ |
    | `get_upcoming()` | Get the details of upcoming challenges on Hackerearth. |
    | `get_ongoing()`  | Get the details of ongoing challenges on Hackerearth.  |
    """

    def __init__(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        url = "https://www.hackerearth.com/challenges/"
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, "lxml")
        self.container = soup.find("div", {"class": "left border-right"})

    def get_ongoing(self):
        """
        Get the details of ongoing challenges on Hackerearth.\n
        Example
        ```python
        hacker = Hackerearth()
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
            challenge = []
            ongoing = self.container.find("div", {"class": "ongoing challenge-list"})
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
        hacker = Hackerearth()
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
            challenge = []
            upcoming = self.container.find("div", {"class": "upcoming challenge-list"})
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
