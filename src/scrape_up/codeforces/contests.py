from bs4 import BeautifulSoup
import json
from scrape_up.config.request_config import RequestConfig, get


class Contest:
    """
    First, create an object of class `Contest`

    ```python
    codeforces = Contest()
    ```

    | Methods                      | Details                                                                                   |
    | ---------------------------- | ----------------------------------------------------------------------------------------- |
    | `get_contests()`             | Returns information on active and past contests like title, start, and duration           |           |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {"User-Agent": "scrapeup"}
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_contests(self):
        """
        Method to fetch the list of active and past contests on Codeforces using web scraping.

        Example
        -------
        ```python
        codeforces = Contest()
        codeforces.get_contests()
        ```

        Returns
        -------
         {
            "upcoming_contest": [
                {
                    "name": "Codeforces Round #731 (Div. 3)",
                    "start": "Aug/08/2021 17:35",
                    "length": "2 hrs"
                },
                ...
            ],
            "ended_contest": [
                {
                    "name": "Codeforces Round #730 (Div. 2)",
                    "start": "Aug/01/2021 17:35",
                    "length": "2 hrs"
                },
                ...
            ]
        }
        """
        codeforces_url = "https://codeforces.com/contests"
        response = get(codeforces_url, self.config)

        if response.status_code != 200:
            json.dumps({"data": None, "message": "Cannot load Contest"})

        soup = BeautifulSoup(response.text, "html.parser")
        contest_list = []

        try:
            upcoming_list = []
            upcoming_contests = soup.find_all("div", {"class": "datatable"})[
                0
            ].find_all("tr")
            for contest in upcoming_contests:
                columns = contest.find_all("td")
                if len(columns) == 6:
                    name = (
                        columns[0]
                        .text.strip()
                        .replace("Enter", " ")
                        .replace("Virtual participation", " ")
                        .replace("\u00bb", " ")
                    )
                    start_time_str = columns[2].text.strip()
                    duration_str = columns[3].text.strip()
                    name = " ".join(
                        line.strip() for line in name.splitlines() if line.strip()
                    )
                    upcoming_list.append(
                        {
                            "name": name,
                            "start": start_time_str,
                            "length": duration_str,
                        }
                    )
            ended_list = []
            ended_contests = soup.find_all("div", {"class": "datatable"})[1].find_all(
                "tr"
            )
            for contest in ended_contests:
                columns = contest.find_all("td")
                if len(columns) == 6:
                    name = (
                        columns[0]
                        .text.strip()
                        .replace("Enter", " ")
                        .replace("Virtual participation", " ")
                        .replace("\u00bb", " ")
                    )
                    start_time_str = (
                        columns[2].find("span", class_="format-date").text.strip()
                    )
                    duration_str = columns[3].text.strip()
                    name = " ".join(
                        line.strip() for line in name.splitlines() if line.strip()
                    )
                    ended_list.append(
                        {
                            "name": name,
                            "start": start_time_str,
                            "length": duration_str,
                        }
                    )
            contest_list = {
                "upcoming_contest": upcoming_list,
                "ended_contest": ended_list,
            }

            return json.dumps(contest_list)
        except Exception:
            return None
