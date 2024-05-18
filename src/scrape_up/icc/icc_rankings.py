from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class ICC:
    """
    Create an instance of `ICC` class.
    ```python
    scraper = ICC()
    ```
    | Method                       | Details                                                             |
    | ---------------------------- | ------------------------------------------------------------------- |
    | `.team_rankings(format)`     | Returns the list of rankings of teams of desired format             |
    |`.player_ranking(type,format)`| Returns the list of player ranking of desired type and format       |
    | `.team_rankings_women(format)`     | Returns the list of rankings of teams of desired format             |
    |`.player_ranking_women(type,format)`| Returns the list of player ranking of desired type and format       |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.url = "https://www.icc-cricket.com/rankings/mens/"
        self.url_women = "https://www.icc-cricket.com/rankings/womens/"
        self.config = config

    def team_rankings(self, format):
        """
        Create an instance of `ICC` class.\n
        Required Params - `format` - "ODI","T20" or "TEST"
        ```python
        icc = ICC()
        icc.team_rankings(format="odi")
        ```
        ```js
        [
            {
                "rank":1,
                "team":"Australia"
            }
        ]
        ```
        """
        try:
            format = format.lower()
            if format == "t20":
                format = "t20i"
            obj_keys = ["rank", "team"]
            resposne_list = []
            url = self.url + "team-rankings/" + format
            response = get(url, self.config)
            soup = BeautifulSoup(response.content, "html.parser")
            teams = soup.find_all("span", class_="u-hide-phablet")
            for rank, team in enumerate(teams, 1):
                obj_values = [rank, team.get_text()]
                resposne_list.append(dict(zip(obj_keys, obj_values)))

            return resposne_list
        except:
            return None

    def player_ranking(self, type, format):
        """
        Create an instance of `ICC` class.\n
        Required Params
        - `format` - "ODI","T20" or "TEST"
        - `type` - "batting","bowling" or "all-rounder"\n
        ```python
        icc = ICC()
        icc.team_player(format="test",type="batting")
        ```
        Returns \n
        ```js
        [
            {
                "rank":1,
                "team":"Kane Williamson"
            }
            ...
        ]
        ```
        """
        try:
            format = format.lower()
            type = type.lower()
            response_list = []
            obj_keys = ["rank", "name"]
            url = self.url + f"/player-rankings/{format}/{type}"
            response = get(url, self.config)
            soup = BeautifulSoup(response.content, "html.parser")
            top_player = soup.find(
                "div", class_="rankings-block__banner--name-large"
            ).get_text()
            rest_players = soup.find_all(
                "td", class_="table-body__cell rankings-table__name name"
            )
            response_list.append(dict(zip(obj_keys, [1, top_player])))
            for rank, player in enumerate(rest_players, 2):
                obj_values = [rank, player.get_text().replace("\n", "")]
                response_list.append(dict(zip(obj_keys, obj_values)))

            return response_list
        except:
            return None

    def team_rankings_women(self, format):
        """
        Create an instance of `ICC` class.\n
        Required Params - `format` - "ODI","T20"
        ```python
        icc = ICC()
        icc.team_rankings_women(format="odi")
        ```
        ```js
        [
            {
                "rank":1,
                "team":"Australia"
            }
        ]
        ```
        """
        try:
            format = format.lower()
            if format == "t20":
                format = "t20i"
            obj_keys = ["rank", "team"]
            resposne_list = []
            url = self.url_women + "team-rankings/" + format
            response = get(url, self.config)
            soup = BeautifulSoup(response.content, "html.parser")
            teams = soup.find_all("span", class_="u-hide-phablet")
            for rank, team in enumerate(teams, 1):
                obj_values = [rank, team.get_text()]
                resposne_list.append(dict(zip(obj_keys, obj_values)))

            return resposne_list
        except:
            return None

    def player_ranking_women(self, type, format):
        """
        Create an instance of `ICC` class.\n
        Required Params
        - `format` - "ODI","T20"
        - `type` - "batting","bowling" or "all-rounder"\n
        ```python
        icc = ICC()
        icc.player_ranking_women(type="batting", format="odi")
        ```
        Returns \n
        ```js
        [
            {
                "rank":1,
                "team":"Natalie Sciver-Brunt"
            }
            ...
        ]
        ```
        """
        try:
            format = format.lower()
            type = type.lower()
            type = type.replace(" ", "-")
            if format == "t20":
                format = "t20i"
            response_list = []
            obj_keys = ["rank", "name"]
            url = self.url_women + f"/player-rankings/{format}/{type}"
            response = get(url, self.config)
            soup = BeautifulSoup(response.content, "html.parser")
            top_player = soup.find(
                "div", class_="rankings-block__banner--name-large"
            ).get_text()
            rest_players = soup.find_all(
                "td", class_="table-body__cell rankings-table__name name"
            )
            response_list.append(dict(zip(obj_keys, [1, top_player])))
            for rank, player in enumerate(rest_players, 2):
                obj_values = [rank, player.get_text().replace("\n", "")]
                response_list.append(dict(zip(obj_keys, obj_values)))

            return response_list
        except:
            return None
