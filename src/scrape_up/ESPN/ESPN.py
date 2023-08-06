from bs4 import BeautifulSoup
import requests


class ESPN:
    """
    Create an instance of the `ESPN` class to fetch football scoreboards.

    Example:
    ```python
    espn = ESPN()
    ```

    | Method              | Details                                                       |
    | ------------------- | ------------------------------------------------------------  |
    | `get_scoreboard()`  | Fetches and returns the football scoreboards for a given date.|

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
        print(scores)
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