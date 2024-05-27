import requests
from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Cricbuzz:
    """
    Create an instance of `Cricubzz` class.
    ```python
    cricbuzz = Cricubzz()
    ```
    Methods\n
    | Methods                      | Details                                                                |
    | ---------------------------- | ---------------------------------------------------------------------- |
    | `.get_live_matches()`        | Returns a list of live matches from Cricbuzz.                          |
    | `.get_recent_matches()`      | Returns a list of recent matches from Cricbuzz.                        |
    | `.get_upcoming_matches()`    | Returns a list of upcoming matches from Cricbuzz.                      |
    | `.get_series()`              | Returns a dictionary of series in month and year format from Cricbuzz. |
    | `.get_series_from_archive()` | Returns a list of series from archive from Cricbuzz.                   |
    | `.get_matches_by_day()`      | Returns a dictionary of matches by day from Cricbuzz.                  |
    | `.get_series_matches()`      | Returns a list of matches in a series from Cricbuzz.                   |
    | `.get_series_stats()`        | Returns a list of stats of players in a series from Cricbuzz.          |
    | `.get_teams_list()`          | Returns a list of teams from Cricbuzz.                                 |
    | `.get_team_schedule()`       | Returns a list of matches of a team from Cricbuzz.                     |
    | `.get_team_players()`        | Returns a list of players of a team from Cricbuzz.                     |
    | `.get_team_results()`        | Returns a list of past results of a team from Cricbuzz.                |
    | `.get_team_stats()`          | Returns a list of player stats of a team from Cricbuzz.                |
    """

    BASE_URL = "https://www.cricbuzz.com/"
    TYPES = ["all", "international", "domestic", "league", "women"]
    FORMATS = ["Test", "ODI", "T20I"]
    STATS = [
        "most-runs",
        "highest-score",
        "highest-avg",
        "highest-sr",
        "most-hundreds",
        "most-fifties",
        "most-fours",
        "most-sixes",
        "most-nineties",
        "most-wickets",
        "lowest-avg",
        "best-bowling-innnings",
        "most-five-wickets",
        "lowest-econ",
        "lowest-sr",
    ]

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def __timestamp_to_date(self, timestamp):
        """
        Converts timestamp to date
        """
        from datetime import datetime

        dt_obj = datetime.fromtimestamp(timestamp / 1000)
        return dt_obj.strftime("%d-%m-%Y %H:%M:%S")

    def __scrape_match(self, url, type, isUpcoming=False):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            search_paras = {
                "class": "cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main"
            }
            if type.lower() not in self.TYPES:
                return [{"error": "Invalid type"}]
            elif type.lower() != "all":
                search_paras["ng-show"] = f"active_match_type == '{type.lower()}-tab'"
            series = soup.find_all(
                "div",
                attrs=search_paras,
            )
            if len(series) == 0:
                return [{"error": "No live matches"}]
            matches = []
            for s in series:
                series_name = s.find("h2").text.strip()
                series_matches = s.find_all(
                    "div", attrs={"class": "cb-mtch-lst cb-col cb-col-100 cb-tms-itm"}
                )
                for m in series_matches:
                    match_data = {}
                    match_data["series_name"] = series_name
                    match_data["match_name"] = (
                        m.find(
                            "h3", class_="cb-lv-scr-mtch-hdr inline-block"
                        ).text.strip()
                        + " "
                        + m.find("span", class_="text-gray").text.strip()
                    )
                    match_data["start_date_time"] = (
                        self.__timestamp_to_date(
                            int(
                                m.find("div", class_="text-gray")
                                .find("span")["ng-if"]
                                .split("|")[0]
                                .strip()[1:]
                            )
                        )
                        + " GMT"
                    )
                    match_data["location"] = "at".join(
                        m.find("div", class_="text-gray")
                        .find_all("span")[-1]
                        .text.split("at")[1:]
                    ).strip()
                    match_data_id = m.find("a")["href"].split("/")
                    match_id = match_data_id[
                        match_data_id.index("live-cricket-scores") + 1
                    ]
                    match_data["match_id"] = match_id
                    if not isUpcoming:
                        match_data["status"] = m.find("div", class_="cb-text-live")
                        if match_data["status"] == None:
                            match_data["status"] = m.find(
                                "div", class_="cb-text-complete"
                            )
                        if match_data["status"] == None:
                            match_data["status"] = m.find(
                                "div", class_="cb-text-preview"
                            )
                        if match_data["status"] != None:
                            match_data["status"] = match_data["status"].text.strip()
                        else:
                            del match_data["status"]
                        match_score = []
                        score_div = m.find(
                            "div", class_="cb-scr-wll-chvrn cb-lv-scrs-col"
                        )
                        if score_div == None:
                            matches.append(match_data)
                            continue
                        bat_scores_div = score_div.find(
                            "div", class_="cb-hmscg-bat-txt"
                        )
                        bowl_scores_div = score_div.find(
                            "div", class_="cb-hmscg-bwl-txt"
                        )
                        if bat_scores_div == None and bowl_scores_div == None:
                            matches.append(match_data)
                            continue
                        elif bat_scores_div == None:
                            bat_scores_div = score_div.find_all(
                                "div", class_="cb-hmscg-bwl-txt"
                            )[1]
                        elif bowl_scores_div == None:
                            bowl_scores_div = score_div.find_all(
                                "div", class_="cb-hmscg-bat-txt"
                            )[1]
                        bat_team_names = bat_scores_div.find(
                            "div", class_="cb-hmscg-tm-nm"
                        ).text.strip()
                        bowl_team_names = bowl_scores_div.find(
                            "div", class_="cb-hmscg-tm-nm"
                        ).text.strip()
                        bat_scores = bat_scores_div.find_all(
                            "div", class_="cb-ovr-flo"
                        )[-1].text.strip()
                        bowl_scores = bowl_scores_div.find_all(
                            "div", class_="cb-ovr-flo"
                        )[-1].text.strip()
                        bat_team_scores = {
                            "team_name": bat_team_names,
                            "scores": [i.strip() for i in bat_scores.split("&")],
                        }
                        bowl_team_scores = {
                            "team_name": bowl_team_names,
                            "scores": [i.strip() for i in bowl_scores.split("&")],
                        }
                        match_score.append(bat_team_scores)
                        match_score.append(bowl_team_scores)
                        match_data["score"] = match_score
                    matches.append(match_data)
            return matches

        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_live_matches(self, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - TYPES = ["all", "international", "domestic", "league", "women"]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_live_matches(type="all")
        ```
        """
        try:
            URL = self.BASE_URL + "cricket-match/live-scores"
            response = self.__scrape_match(url=URL, type=type)
            return response
        except:
            return None

    def get_recent_matches(self, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - TYPES = ["all", "international", "domestic", "league", "women"]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_recent_matches(type="all")
        ```
        """
        try:
            URL = self.BASE_URL + "cricket-match/live-scores/recent-matches"
            response = self.__scrape_match(url=URL, type=type)
            return response
        except:
            return None

    def get_upcoming_matches(self, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - TYPES = ["all", "international", "domestic", "league", "women"]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_upcoming_matches(type="all")
        ```
        """
        try:
            URL = self.BASE_URL + "cricket-match/live-scores/upcoming-matches"
            response = self.__scrape_match(url=URL, type=type, isUpcoming=True)
            return response
        except:
            return None

    def __scrape_series(self, url, type="all"):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            series = soup.find_all(
                "div",
                class_="cb-col-100 cb-col",
            )
            international_series = [
                i
                for i in series
                if i["ng-if"] == "((filtered_category == 0 || filtered_category == 9))"
            ]
            domestic_series = [
                i
                for i in series
                if i["ng-if"] == "((filtered_category == 1 || filtered_category == 9))"
            ]
            league_series = [
                i
                for i in series
                if i["ng-if"] == "((filtered_category == 2 || filtered_category == 9))"
            ]
            womens_series = [
                i
                for i in series
                if i["ng-if"] == "((filtered_category == 3 || filtered_category == 9))"
            ]
            diff_series = [
                international_series,
                domestic_series,
                league_series,
                womens_series,
            ]
            if type.lower() not in self.TYPES:
                return [{"error": "Invalid type"}]
            elif type.lower() != "all":
                series = diff_series[self.TYPES.index(type.lower()) - 1]
            series_data = {}
            for s in series:
                series_month = s.find(
                    "div", class_="cb-col-16 cb-col text-bold cb-mnth"
                )
                monthly_series_data = []
                series_div = s.find_all("div", class_="cb-sch-lst-itm")
                for i in series_div:
                    series_data_id = i.find("a")["href"].split("/")
                    series_id = series_data_id[
                        series_data_id.index("cricket-series") + 1
                    ]
                    monthly_series_data.append(
                        {
                            "series_name": i.find("a").text.strip(),
                            "series_id": series_id,
                            "series_dates": i.find(
                                "div", class_="text-gray cb-font-12"
                            ).text.strip(),
                        }
                    )
                if series_data.get(series_month.text.strip()) == None:
                    series_data[series_month.text.strip()] = monthly_series_data
                else:
                    series_data[series_month.text.strip()].extend(monthly_series_data)
            return series_data
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_series(self, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - TYPES = ["all", "international", "domestic", "league", "women"]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_series(type="all")
        ```
        """
        try:
            URL = self.BASE_URL + "cricket-schedule/series"
            response = self.__scrape_series(url=URL, type=type)
            return response
        except:
            return None

    def __scrape_series_from_archive(self, url, type="all"):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            data = soup.select_one(
                "#page-wrapper > div:nth-child(5) > div.cb-left.cb-col-67.cb-col.cb-schdl"
            )
            data_elements = [
                i.text.lower()
                for i in data.find_all(
                    "h2",
                    class_="cb-col-16 cb-col text-bold cb-srs-cat cb-lv-scr-mtch-hdr",
                )
            ]
            data_divs = data.find_all("div", class_="cb-col-84 cb-col")
            divs = data_divs
            if type.lower() != "all":
                if type.lower() == "league":
                    divs = [data_divs[data_elements.index("t20 league")]]
                else:
                    divs = [data_divs[data_elements.index(type.lower())]]
            series = []
            for d in divs:
                data = []
                series_data = d.find_all("div", class_="cb-srs-lst-itm")
                for s in series_data:
                    series_data_id = s.find("a")["href"].split("/")
                    series_id = series_data_id[
                        series_data_id.index("cricket-series") + 1
                    ]
                    data.append(
                        {
                            "series_name": s.find("a").text.strip(),
                            "series_id": series_id,
                            "series_dates": s.find(
                                "span", class_="text-gray cb-font-12"
                            ).text.strip(),
                        }
                    )
                series.extend(data)
            return series
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_series_from_archive(self, year, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - TYPES = ["all", "international", "domestic", "league", "women"]
        - Year\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_series_from_archive(year, type="all")
        ```
        """
        try:
            URL = self.BASE_URL + f"cricket-scorecard-archives/{year}"
            if type.lower() not in self.TYPES:
                return [{"error": "Invalid type"}]
            response = self.__scrape_series_from_archive(url=URL, type=type)
            return response
        except:
            return None

    def __scarpe_matches_by_day(self, url, type):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            data = soup.find("div", id=f"{type.lower()}-list")
            days_data = data.select(f"#{type.lower()}-list > div:nth-child(n)")
            matches_data = {}
            for i in days_data:
                day = i.find("div", class_="cb-lv-grn-strip text-bold").text.strip()
                match_data = i.find_all("div", class_="cb-col-100 cb-col")
                matches = []
                for m in match_data:
                    match_data = {}
                    match_series = m.find("a")
                    match_series_data_id = match_series["href"].split("/")
                    match_data["series_name"] = match_series.text.strip()
                    match_data["series_id"] = match_series_data_id[
                        match_series_data_id.index("cricket-series") + 1
                    ]
                    match_elem = m.find("div", class_="cb-col-67 cb-col").find("a")
                    match_data_id = match_elem["href"].split("/")
                    match_data["match_name"] = match_elem.text.strip()
                    match_data["match_id"] = match_data_id[
                        match_data_id.index("live-cricket-scores") + 1
                    ]
                    match_data["location"] = m.find(
                        "div", attrs={"itemprop": "location"}
                    ).text.strip()
                    match_data["start_date_time"] = (
                        self.__timestamp_to_date(
                            int(m.find("span", class_="schedule-date")["timestamp"])
                        )
                        + " GMT"
                    )
                    matches.append(match_data)
                matches_data[day] = matches
            return matches_data

        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_matches_by_day(self, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - TYPES = ["all", "international", "domestic", "league", "women"]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_matches_by_day(type="all")
        ```
        """
        try:
            URL = self.BASE_URL + "cricket-schedule/upcoming-series"
            if type.lower() not in self.TYPES:
                return [{"error": "Invalid type"}]
            else:
                URL += f"/{type.lower()}"
            response = self.__scarpe_matches_by_day(url=URL, type=type)
            return response
        except:
            return None

    def __scrape_series_matches(self, url):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")

            data = soup.find_all("div", class_="cb-series-matches")
            matches = []
            for m in data:
                match_data = {}
                match_data["match_start_data_time"] = (
                    self.__timestamp_to_date(
                        int(
                            m.find("div", class_="schedule-date")
                            .find("span")["ng-bind"]
                            .split("|")[0]
                            .strip()
                        )
                    )
                    + " GMT"
                )
                match_data["match_title"] = (
                    m.find("div", class_="cb-col-60 cb-col cb-srs-mtchs-tm")
                    .find("span")
                    .text.strip()
                )
                match_data["match_location"] = (
                    m.find("div", class_="cb-col-60 cb-col cb-srs-mtchs-tm")
                    .find("div", class_="text-gray")
                    .text.strip()
                )
                if (
                    m.find("div", class_="cb-col-60 cb-col cb-srs-mtchs-tm")
                    .find("div", class_="text-gray")
                    .find_next_sibling("a")
                    is not None
                ):
                    match_data["match_status"] = (
                        m.find("div", class_="cb-col-60 cb-col cb-srs-mtchs-tm")
                        .find("div", class_="text-gray")
                        .find_next_sibling("a")
                        .text.strip()
                    )
                match_id_data = m.find("a")["href"].split("/")
                try:
                    match_data["match_id"] = match_id_data[
                        match_id_data.index("cricket-scores") + 1
                    ]
                except:
                    match_data["match_id"] = match_id_data[
                        match_id_data.index("live-cricket-scores") + 1
                    ]

                matches.append(match_data)
            return matches
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_series_matches(self, series_id):
        """
        Class - Cricbuzz\n
        Params required
        - `series_id` = Cricket match series Id(can be found on Cricbuzz Website)\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_series_matches(series_id="abc")
        ```
        """
        try:
            URL = self.BASE_URL + f"cricket-series/{series_id}/series/matches"
            return self.__scrape_series_matches(url=URL)
        except:
            return None

    def __scrape_series_stats(self, series_id, match_format="Test", stat="most-runs"):
        try:
            format_index = self.FORMATS.index(match_format) + 1
            URL = f"https://www.cricbuzz.com/api/html/series/{series_id}/{stat}/{format_index}/0/0"
            res = get(URL, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            if soup.find("tbody") == None:
                return {"error": "No data found"}
            keys = [i.text.strip() for i in soup.find("thead").find_all("th")]
            players_data = soup.find("tbody").find_all("tr")
            players = []
            for i in players_data:
                player_data_id = i.find("a")["href"].split("/")
                player_id = player_data_id[player_data_id.index("profiles") + 1]
                player_data = [i.text.strip() for i in i.find_all("td")]
                player_data_dict = dict(zip(keys, player_data))
                player_data_dict["PLAYER ID"] = player_id
                players.append(player_data_dict)
            return players
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_series_stats(self, series_id, match_format="Test", stat="most-runs"):
        """
        Class - Cricbuzz\n
        Params required
        - `series_id` = Cricket match series Id(can be found on Cricbuzz Website)\n
        - `match_format` = ["Test", "ODI", "T20I"]\n
        - `stat` = [
            "most-runs",
            "highest-score",
            "highest-avg",
            "highest-sr",
            "most-hundreds",
            "most-fifties",
            "most-fours",
            "most-sixes",
            "most-nineties",
            "most-wickets",
            "lowest-avg",
            "best-bowling-innnings",
            "most-five-wickets",
            "lowest-econ",
            "lowest-sr",
        ]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_series_stats(series_id, match_format="Test", stat="most-runs")
        ```
        """
        try:
            if match_format not in self.FORMATS:
                return [
                    {"error": "Invalid match format", "valid_formats": self.FORMATS}
                ]
            if stat not in self.STATS:
                return [{"error": "Invalid stat", "valid_stats": self.STATS}]
            return self.__scrape_series_stats(
                series_id=series_id, match_format=match_format, stat=stat
            )
        except:
            return None

    def __scrape_team_data(self, url: str):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            data = soup.select_one(
                "#page-wrapper > div:nth-child(6) > div.cb-col.cb-col-67.cb-nws-lft-col > div.cb-col.cb-col-100"
            )
            teams = []
            teams_data = data.find_all("div", class_="cb-team-item")
            for t in teams_data:
                team_name = t.find("a")["title"].strip().title()
                team_code = t.find("a")["href"].split("/")[-1].strip()
                teams.append({"team_name": team_name, "team_code": team_code})
            return teams
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_teams_list(self, type="all"):
        """
        Class - Cricbuzz\n
        Params required
        - `type` = ["all", "international", "domestic", "league", "women"]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_teams_list(type="all")
        ```
        """
        URL = self.BASE_URL + "cricket-team"
        if type.lower() not in self.TYPES:
            return [{"error": "Invalid type"}]
        elif type.lower() != "all" and type.lower() != "international":
            URL += f"/{type.lower()}"
        if type.lower() == "all":
            return {
                "international": self.__scrape_team_data(url=URL),
                "domestic": self.__scrape_team_data(url=URL + "/domestic"),
                "league": self.__scrape_team_data(url=URL + "/league"),
                "women": self.__scrape_team_data(url=URL + "/women"),
            }
        return self.__scrape_team_data(url=URL)

    def __scrape_team_schedule(self, url: str):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")

            data = soup.find_all("div", class_="cb-series-matches")
            matches = []
            for m in data:
                match_data = {}
                match_data["match_start_data_time"] = (
                    self.__timestamp_to_date(
                        int(
                            m.find("div", class_="schedule-date")
                            .find("span")["ng-bind"]
                            .split("|")[0]
                            .strip()
                        )
                    )
                    + " GMT"
                )
                match_data["match_title"] = (
                    m.find("div", class_="cb-srs-mtchs-tm").find("span").text.strip()
                )
                match_data["match_location"] = (
                    m.find("div", class_="cb-srs-mtchs-tm")
                    .find("div", class_="text-gray cb-ovr-flo")
                    .text.strip()
                )
                match_data["match_series_name"] = (
                    m.find("div", class_="cb-srs-mtchs-tm")
                    .find("div", class_="text-gray")
                    .text.strip()
                )
                if (
                    m.find("div", class_="cb-srs-mtchs-tm")
                    .find("div", class_="text-gray")
                    .find_next_sibling("a")
                    is not None
                ):
                    match_data["match_status"] = (
                        m.find("div", class_="cb-srs-mtchs-tm")
                        .find("div", class_="text-gray")
                        .find_next_sibling("a")
                        .text.strip()
                    )
                match_id_data = m.find("a")["href"].split("/")
                try:
                    match_data["match_id"] = match_id_data[
                        match_id_data.index("cricket-scores") + 1
                    ]
                except:
                    match_data["match_id"] = match_id_data[
                        match_id_data.index("live-cricket-scores") + 1
                    ]

                matches.append(match_data)
            return matches
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_team_schedule(self, team_id):
        """
        Class - Cricbuzz\n
        Params required
        - `team_id` = Can be extracted from Cricbuzz\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_team_schedule(team_id=" ")
        """
        URL = self.BASE_URL + f"cricket-team/team/{team_id}/schedule"
        return self.__scrape_team_schedule(url=URL)

    def __scrape_team_players(self, url: str):
        # try:
        res = get(url, self.config)
        if res.status_code != 200:
            return [{"error": "Unable to fetch data from cricbuzz"}]
        soup = BeautifulSoup(res.text, "html.parser")
        players_data = soup.find("div", class_="cb-top-zero").find_all(
            "a", class_="cb-col cb-col-50"
        )
        players = []
        for player in players_data:
            player_data_id = player["href"].split("/")
            player_id = player_data_id[player_data_id.index("profiles") + 1]
            players.append(
                {
                    "player_name": player.text.strip(),
                    "player_id": player_id,
                }
            )
        return players

    def get_team_players(self, team_id):
        """
        Class - Cricbuzz\n
        Params required
        - `team_id` = Can be extracted from Cricbuzz\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_team_players(team_id=" ")
        ```
        """
        try:
            URL = self.BASE_URL + f"cricket-team/team/{team_id}/players"
            return self.__scrape_team_players(url=URL)
        except:
            return None

    def __scrape_team_results(self, url: str):
        try:
            res = get(url, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")

            data = soup.find("div", id="series-matches").find_all(
                "div", class_="cb-col-100 cb-col cb-brdr-thin-btm"
            )
            matches = []
            for m in data:
                match_data = {}
                match_data["match_start_data_time"] = (
                    self.__timestamp_to_date(
                        int(m.find("span")["ng-bind"].split("|")[0].strip())
                    )
                    + " GMT"
                )
                match_data["match_title"] = (
                    m.find("div", class_="cb-srs-mtchs-tm").find("a").text.strip()
                )
                match_data["match_series_name"] = (
                    m.find("div", class_="cb-srs-mtchs-tm")
                    .find("div", class_="text-gray")
                    .text.strip()
                )
                if (
                    len(
                        m.find("div", class_="cb-srs-mtchs-tm").find_all(
                            "div", class_="text-gray"
                        )
                    )
                    > 1
                ):
                    match_data["match_location"] = (
                        m.find("div", class_="cb-srs-mtchs-tm")
                        .find_all("div", class_="text-gray")[1]
                        .text.strip()
                    )
                if (
                    m.find("div", class_="cb-srs-mtchs-tm")
                    .find("div", class_="text-gray")
                    .find_next_sibling("a")
                    is not None
                ):
                    match_data["match_status"] = (
                        m.find("div", class_="cb-srs-mtchs-tm")
                        .find("div", class_="text-gray")
                        .find_next_sibling("a")
                        .text.strip()
                    )
                match_id_data = m.find("a")["href"].split("/")
                try:
                    match_data["match_id"] = match_id_data[
                        match_id_data.index("cricket-scores") + 1
                    ]
                except:
                    match_data["match_id"] = match_id_data[
                        match_id_data.index("live-cricket-scores") + 1
                    ]

                matches.append(match_data)
            return matches
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_team_results(self, team_id):
        """
        Class - Cricbuzz\n
        Params required
        - `team_id` = Can be extracted from Cricbuzz\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_team_results(team_id=" ")
        ```
        """
        try:
            URL = self.BASE_URL + f"cricket-team/team/{team_id}/results"
            return self.__scrape_team_results(url=URL)
        except:
            return None

    def __scrape_team_stats(self, team_id, year, match_format="Test", stat="most-runs"):
        try:
            format_index = self.FORMATS.index(match_format) + 1
            URL = f"https://www.cricbuzz.com/cricket-team/team/{team_id}/stats-table/{stat}/{format_index}/{year}/all"
            res = get(URL, self.config)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from cricbuzz"}]
            soup = BeautifulSoup(res.text, "html.parser")
            if soup.find("tbody") == None:
                return {"error": "No data found"}
            keys = [i.text.strip() for i in soup.find("thead").find_all("th")]
            players_data = soup.find("tbody").find_all("tr")
            players = []
            for i in players_data:
                player_data_id = i.find("a")["href"].split("/")
                player_id = player_data_id[player_data_id.index("profiles") + 1]
                player_data = [i.text.strip() for i in i.find_all("td")]
                player_data_dict = dict(zip(keys, player_data))
                player_data_dict["PLAYER ID"] = player_id
                players.append(player_data_dict)
            return players
        except Exception as e:
            return [{"error": f"Something Went Wrong: {e}"}]

    def get_team_stats(
        self, team_id, year="all", match_format="Test", stat="most-runs"
    ):
        """
        Class - Cricbuzz\n
        Params required
        - `team_id` = Team Id(can be found on Cricbuzz Website)\n
        - `match_format` = ["Test", "ODI", "T20I"]\n
        - `stat` = [
            "most-runs",
            "highest-score",
            "highest-avg",
            "highest-sr",
            "most-hundreds",
            "most-fifties",
            "most-fours",
            "most-sixes",
            "most-nineties",
            "most-wickets",
            "lowest-avg",
            "best-bowling-innnings",
            "most-five-wickets",
            "lowest-econ",
            "lowest-sr",
        ]\n
        ```python
        cricbuzz = Cricubzz()
        cricbuzz.get_team_stats(team_id, match_format="Test", stat="most-runs")
        ```
        """
        try:
            if match_format not in self.FORMATS:
                return [
                    {"error": "Invalid match format", "valid_formats": self.FORMATS}
                ]
            if stat not in self.STATS:
                return [{"error": "Invalid stat", "valid_stats": self.STATS}]
            return self.__scrape_team_stats(
                team_id=team_id, year=year, match_format=match_format, stat=stat
            )
        except:
            return None
