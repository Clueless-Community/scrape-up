from bs4 import BeautifulSoup
import requests

class Hackerearth:
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
        Get the details of ongoing challenges on Hackerearth.

        Returns:
        A dictionary containing the list of ongoing challenges:
        {
            "data": list[dict],
            "message": str
        }
        Each dictionary in the list contains the following keys:
        - "Title": str (The title of the challenge)
        - "No of Registrations": str (The number of registrations for the challenge)
        - "Link": str (The link to the challenge page on Hackerearth)
        """
        try:
            challenge = []
            ongoing = self.container.find("div", {"class": "ongoing challenge-list"})
            for items in ongoing.find_all("div", {"class": "challenge-card-modern"}):
                title = items.find("span", {"class": "challenge-list-title challenge-card-wrapper"}).text
                registrations = items.find("div", {"class": "registrations tool-tip align-left"}).text.strip()
                link = items.find("a", href=True)['href']
                if link[:5] != "https":
                    link = "https://www.hackerearth.com" + link
                data = {
                    "Title": title,
                    "No of Registrations": registrations,
                    "Link": link
                }
                challenge.append(data)
            return {"data": challenge, "message": "Information fetched"}
        except:
            return {"data": None, "message": "Error occurred"}

    def get_upcoming(self):
        """
        Get the details of upcoming challenges on Hackerearth.

        Returns:
        A dictionary containing the list of upcoming challenges:
        {
            "data": list[dict],
            "message": str
        }
        Each dictionary in the list contains the following keys:
        - "Title": str (The title of the challenge)
        - "No of Registrations": str (The number of registrations for the challenge)
        - "Link": str (The link to the challenge page on Hackerearth)
        """
        try:
            challenge = []
            upcoming = self.container.find("div", {"class": "upcoming challenge-list"})
            for items in upcoming.find_all("div", {"class": "challenge-card-modern"}):
                title = items.find("span", {"class": "challenge-list-title challenge-card-wrapper"}).text
                registrations = items.find("div", {"class": "registrations tool-tip align-left"}).text.strip()
                link = items.find("a", href=True)['href']
                if link[:5] != "https":
                    link = "https://www.hackerearth.com" + link
                data = {
                    "Title": title,
                    "No of Registrations": registrations,
                    "Link": link
                }
                challenge.append(data)
            return {"data": challenge, "message": "Information fetched"}
        except:
            return {"data": None, "message": "Error occurred"}


