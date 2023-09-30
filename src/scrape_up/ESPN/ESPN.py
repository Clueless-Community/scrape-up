from bs4 import BeautifulSoup
import requests


class ESPN:
    """
    Create an instance of `ESPN` class
    ```python
    espn = espn.ESPN()
    ```
    
    | Method              | Details                                                           |
    | ------------------- | ----------------------------------------------------------------- |
    | `get_scoreboard()`  | Fetches and returns the football scoreboards for a given date.   |
    | `get_tournaments()` | Fetches and returns information about ongoing football tournaments. |
    | `get_teams()`       | Fetches and returns information about football teams.            |
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def get_scoreboard(self, date):
        """
        Create an instance of the `ESPN` class to fetch football scoreboards.\n
        Example:
        ```python
        espn = ESPN()
        scores = espn.get_scoreboard(date="20230721")
        ```
        Example output:
        ```python
        [
            {
                "Game":"Mexican Liga de Expansión MX",
                "Game Link":"https://www.espn.in/football/scoreboard/_/league/mex.2",
                "Teams":[
                    {
                        "Name":"Venados FC",
                        "Score":"3"
                    },
                    {
                        "Name":"Tlaxcala FC",
                        "Score":"1"
                    }
                ],
                "Location":"Estadio Carlos Iturralde Rivero,Mérida, Mexico"
            },
            ...
        ]
        ```
        """
        try:
            url = f"https://www.espn.in/football/scoreboard/_/date/{date}"
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            scores = []
            container = soup.find("div", {"class": "PageLayout__Main"})
            for items in container.find_all("section", {"class": "Card gameModules"}):
                title = items.find(
                    "h3", {"class": "Card__Header__Title Card__Header__Title--no-theme"}
                )
                link = (
                    "https://www.espn.in"
                    + items.find(
                        "a", {"class": "AnchorLink Card__Header__Link"}, href=True
                    )["href"]
                )
                for item in items.find_all(
                    "section",
                    {"class": "Scoreboard bg-clr-white flex flex-auto justify-between"},
                ):
                    teams = []
                    for team in item.find(
                        "ul", {"class": "ScoreboardScoreCell__Competitors"}
                    ).find_all("li"):
                        name = team.find(
                            "div",
                            {
                                "class": "ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"
                            },
                        )
                        score = team.find(
                            "div",
                            {
                                "class": "ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"
                            },
                        )
                        if score:
                            score = score.text
                        teams.append({"Name": name.text, "Score": score})
                    place = item.find(
                        "div",
                        {
                            "class": "LocationDetail__Item LocationDetail__Item--headline"
                        },
                    )
                    if place:
                        country = place.next_sibling
                        location = place.text + "," + country.text
                        data = {
                            "Game": title.text,
                            "Game Link": link,
                            "Teams": teams,
                            "Location": location,
                        }
                    else:
                        data = {
                            "Game": title.text,
                            "Game Link": link,
                            "Teams": teams,
                        }
                    scores.append(data)
            return scores
        except:
            return None

    def get_tournaments(self):
        """
        Fetches and returns information about ongoing football tournaments.
        ```py
        espn = ESPN()
        tournaments = espn.get_tournaments()
        ```
        Example output:
        ```python
        [
            {
                "Premier League": [
                    ["https://www.espn.in/football/competition/_/id/eng.1", "English Premier League"]
                ]
            },
            ...
        ]
        ```
        """
        try:
            url = "https://www.espn.in/football/competitions"
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            container = soup.find("div", {"class": "Wrapper bg-clr-white br-5 mb3 pa5"})
            data = []
            for items in container.find_all("h3"):
                heading = items.text
                div = items.next_sibling
                li = []
                for item in div.find_all("div", {"class": "ContentList__Item"}):
                    link = item.find("a", href=True)["href"]
                    title = item.find("h2")
                    li.append([link, title.text])
                data.append({heading: li})
            return data
        except:
            return None

    def get_teams(self):
        """
        Fetches and returns information about football teams.
        ```py
        espn = ESPN()
        teams = espn.get_teams()
        ```

        Example output:
        ```python
        [
            {
                "Name": "Manchester United",
                "Link": "https://www.espn.in/football/team/_/id/360/manchester-united"
            },
            ...
        ]
        ```
        """
        try:
            url = "https://www.espn.in/football/teams"
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            container = soup.find("div", {"class": "Wrapper TeamsWrapper br-5 mb3 pa5"})
            teams = []
            for items in container.find_all("div", {"class": "ContentList__Item"}):
                title = items.find("h2")
                link = items.find("a", href=True)["href"]
                data = {"Name": title.text, "Link": "https://www.espn.in" + link}
                teams.append(data)
            return teams
        except:
            return None
