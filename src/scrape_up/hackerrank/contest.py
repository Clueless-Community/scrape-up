from bs4 import BeautifulSoup as bs

from scrape_up.config.request_config import RequestConfig, get


class Contest:
    """
    First, create an object of class `Contest`

    ```python
    hackerank = Contest()
    ```

    | Methods                      | Details                                                                                   |
    | ---------------------------- | ----------------------------------------------------------------------------------------- |
    | `active_contests()`          | Returns information on active contests like title, status, and link                       |
    | `archived_contests()`        | Returns information regarding archived contests                                           |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def active_contests(self):
        """
        Get the details of active contests on HackerRank.\n
        First, create an object of class `HackerRank`\n
        ```python
        hrank = Contest()
        hrank.active_contests()
        ```
        Returns:
        ```js
        [
            {
                "Title":"ProjectEuler+",
                "Status":"Open Indefinitely",
                "Link":"https://www.hackerrank.com/contests/projecteuler"
            }
        ]
        ```
        """
        try:
            url = "https://www.hackerrank.com/contests"
            html_text = get(url, self.config).text
            soup = bs(html_text, "lxml")
            container = soup.find("div", {"class": "theme-m contest-list left-pane"})
            actives = []
            active_contest = container.find(
                "div", {"class": "active_contests active-contest-container"}
            )
            for items in active_contest.find_all("li"):
                title = items.find("h4").text
                status = items.find("span", {"class": "contest-status"}).text
                link = (
                    "https://www.hackerrank.com"
                    + items.find("a", {"class": "text-link"}, href=True)["href"]
                )
                data = {"Title": title, "Status": status, "Link": link}
                actives.append(data)
            return actives
        except:
            return None

    def archived_contests(self):
        """
        Get the details of active contests on HackerRank.\n
        First, create an object of class `HackerRank`\n
        ```python
        hrank = Contest()
        hrank.archived_contests()
        ```
        Returns:
        ```js
        [
            {
                "title":"Cisco Hack to Secure Challenge 2023"
            }
            ...
        ]
        ```
        """
        try:
            url = "https://www.hackerrank.com/contests"
            html_text = get(url, self.config).text
            soup = bs(html_text, "lxml")
            container = soup.find("div", {"class": "theme-m contest-list left-pane"})
            archives = []
            archived_contest = container.find(
                "div", {"class": "active_contests archived-contest-container"}
            )
            for items in archived_contest.find_all("li"):
                title = items.find("h4").text
                data = {"title": title}
                archives.append(data)
            return archives
        except Exception:
            return None
