import requests
from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Espncricinfo:
    """
    Create an instance of `Espncricinfo` class.
    ```python
    obj = Espncricinfo()
    ```

    | Methods                      | Details                                           |
    | ---------------------------- | --------------------------------------------------|
    | `.get_news()`                | Returns a latest news from ESPNCricinfo.          |
    | `.get_livescores()`          | Returns a list of live matches from ESPNCricinfo. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config
        self.BASE_URL = "https://www.espncricinfo.com"

    def get_news(self):
        news = []
        URL = self.BASE_URL + "/cricket-news"
        try:
            res = get(URL, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            search_paras = {"class": "ds-flex ds-flex-col"}
            news_list = soup.find_all("div", attrs=search_paras)
            for i in news_list:
                details = {"headlines": i.find("h2").text}
                news.append(details)
            return news
        except:
            return news

    def get_livescores(self):
        live_scores = []
        URL = self.BASE_URL + "/live-cricket-score"
        try:
            res = get(URL, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            search_paras = {"class": "ds-flex ds-flex-wrap"}
            match_box_container = soup.find("div", attrs=search_paras)
            match_boxes1 = soup.find_all(
                "div",
                attrs={"class": "ds-border-b ds-border-line ds-border-r ds-w-1/2"},
            )
            match_boxes2 = soup.find_all(
                "div", attrs={"class": "ds-border-b ds-border-line ds-w-1/2"}
            )
            match_boxes = match_boxes1 + match_boxes2
            for match in match_boxes:
                curr_status = match.find(
                    "span",
                    attrs={
                        "class": "ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5"
                    },
                ).text
                if curr_status == "Live":
                    about = match.find(
                        "div",
                        attrs={
                            "class": "ds-text-tight-xs ds-truncate ds-text-typo-mid3"
                        },
                    ).text
                    teams = match.find_all(
                        "div",
                        attrs={
                            "class": "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1"
                        },
                    )
                    team1_details = teams[0].find_all("div")
                    team2_details = teams[1].find_all("div")

                    team1_name = team1_details[0].text
                    team1_score = team1_details[1].text
                    team2_name = team2_details[0].text
                    team2_score = team2_details[1].text

                    match_status = match.find(
                        "p",
                        attrs={
                            "class": "ds-text-tight-s ds-font-medium ds-truncate ds-text-typo"
                        },
                    ).text
                    match_details = {
                        "current": curr_status,
                        "about": about,
                        "team1": team1_name,
                        "team2": team2_name,
                        "team1_score": team1_score,
                        "team2_score": team2_score,
                        "status": match_status,
                    }
                    live_scores.append(match_details)
            return live_scores
        except:
            return live_scores
