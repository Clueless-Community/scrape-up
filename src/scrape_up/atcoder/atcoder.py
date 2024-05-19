import json
import sys
import requests
from bs4 import BeautifulSoup


class Atcoder:
    """
    ```
    atc = Atcoder(user="chokudai")
    atc.get_profile()
    ```
    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_profile()`  | Returns the user data in json format.                                              |
    | `get_contests()`  | Returns future_contests , past_contests , skill_tests etc in json format.          |

    Response
    ```json
    {
        "Country/Region": "Japan",
        "Birth_Year": "1988",
        "Twitter_ID": "@chokudai",
        "TopCoder_ID": "chokudai",
        "Codeforces_ID": "chokudai",
        "Affiliation": "AtCoder Inc. CEO",
        "Algorithm_Rank": "44th",
        "Algorithm_Rating": "3028",
        "Algorithm_Highest_Rating": "3092 ― 6 Dan (+108 to promote)",
        "Algorithm_Rated_Matches_": "35",
        "Algorithm_Last_Competed": "2023/12/17",
        "Heuristic_Rank": "62nd",
        "Heuristic_Rating": "2525 (Provisional)",
        "Heuristic_Highest_Rating": "2525",
        "Heuristic_Rated_Matches_": "8",
        "Heuristic_Last_Competed": "2024/04/07"
    }
    ```
    """

    def __init__(self, user):
        self.user = user

    def get_profile(self):
        try:
            url = f"https://atcoder.jp/users/{self.user}"
            headers = {"User-Agent": "scrapeup"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find_all("table", class_="dl-table")
            user_details = {}

            row = table[0].find_all("tr")
            for r in row:
                user_details[r.find("th").text.replace(" ", "_")] = (
                    r.find("td").text.replace("\n", " ").strip()
                )

            row = table[1].find_all("tr")
            for r in row:
                user_details["Algorithm_" + r.find("th").text.replace(" ", "_")] = (
                    r.find("td").text.replace("\n", " ").strip()
                )

            url = f"https://atcoder.jp/users/{self.user}?contestType=heuristic"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find_all("table", class_="dl-table")
            row = table[1].find_all("tr")
            for r in row:
                user_details["Heuristic_" + r.find("th").text.replace(" ", "_")] = (
                    r.find("td").text.replace("\n", " ").strip()
                )
            return json.dumps(user_details)
        except:
            return None

    def get_contests(self):
        try:
            url = "https://atcoder.jp/contests/"
            headers = {"User-Agent": "scrapeup"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            # print(soup)
            ac = soup.find("div", id="contest-table-action").find("tbody")
            active = {}
            row = ac.find_all("tr")
            i = 1
            for r in row:
                b = r.find_all("td")
                active[i] = {
                    "start_time": b[0].text.strip().replace("\n", " "),
                    "name": b[1].text.strip().replace("\n", " "),
                    "Duration": b[2].text.strip().replace("\n", " "),
                    "Rated_for": b[3].text.strip().replace("\n", " "),
                }
                i = i + 1
            ac = soup.find("div", id="contest-table-upcoming").find("tbody")
            upcoming = {}
            row = ac.find_all("tr")
            i = 1
            for r in row:
                b = r.find_all("td")
                upcoming[i] = {
                    "start_time": b[0].text.strip().replace("\n", " "),
                    "name": b[1].text.strip().replace("\n", " "),
                    "Duration": b[2].text.strip().replace("\n", " "),
                    "Rated_for": b[3].text.strip().replace("\n", " "),
                }
                # print(b[1].text)
                i = i + 1
            ac = soup.find("div", id="contest-table-recent").find("tbody")
            recent = {}
            row = ac.find_all("tr")
            i = 1
            for r in row:
                b = r.find_all("td")
                recent[i] = {
                    "start_time": b[0].text.strip().replace("\n", " "),
                    "name": b[1].text.strip().replace("\n", " "),
                    "Duration": b[2].text.strip().replace("\n", " "),
                    "Rated_for": b[3].text.strip().replace("\n", " "),
                }
                i = i + 1
            ac = soup.find("div", id="contest-table-permanent").find("tbody")
            permanent = {}
            row = ac.find_all("tr")
            i = 1
            for r in row:
                b = r.find_all("td")
                permanent[i] = {
                    "name": b[0].text.strip().replace("\n", " "),
                    "Rated_for": b[1].text.strip().replace("\n", " "),
                }
                i = i + 1

            response = {
                "active": active,
                "Upcoming": upcoming,
                "Recent": recent,
                "Permanent": permanent,
            }

            sys.stdout.reconfigure(encoding="utf-8")
            return response
        except:
            return None
