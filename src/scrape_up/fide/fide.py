import requests
from bs4 import BeautifulSoup


class FIDE:
    """
    Create an instance of `FIDE` class.
    ```python
    obj = fide.FIDE()
    ```
    | Methods                   | Details                                            |
    | ------------------------- | -------------------------------------------------- |
    | `.get_events()`           | Returns all the major chess events of 2024.        |
    | `.get_open_ratings()`     | Returns a list of top 100 open category players.   |
    | `.get_women_ratings()`    | Returns a list of top 100 women category players.  |
    | `.get_juniors_ratings()`  | Returns a list of top 100 juniors category players.|
    | `.get_girls_ratings()`    | Returns a list of top 100 girls category players.  |
    | `.get_news()`             | Returns a list of top chess/fide news.             |
    """

    def __init__(self):
        self.session = requests.Session()
        self.BASE_URL = ""

    def get_events(self):
        events = []
        try:
            EVENTS_URL = "https://fide.com/calendar?filter=filter%5Bdate_start_years%5D%3D2024%26filter%5Bworld_champion%5D%3Dfalse%26filter%5Bclosest_events%5D%3Dfalse%26"
            res = self.session.get(EVENTS_URL)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            event_domains = soup.find_all(
                "div", attrs={"class": "block-calendar-table-one no-padding col-12"}
            )
            for event_domain in event_domains:
                table_div = event_domain.find("div", attrs={"class": "ant-table-body"})
                events_table = table_div.find("table")
                events_table_body = events_table.find(
                    "tbody", attrs={"class": "ant-table-tbody"}
                )
                table_rows = events_table_body.find_all("tr")
                for event in table_rows:
                    try:
                        table_datas = event.find_all("td")
                        name = table_datas[0].text
                        place = table_datas[1].text
                        start = table_datas[2].text
                        end = table_datas[3].text
                        event = {
                            "name": name,
                            "place": place,
                            "start": start,
                            "end": end,
                        }
                        events.append(event)
                    except:
                        pass
            return events
        except:
            return events

    def get_open_ratings(self):
        ratings = []
        try:
            OPEN_URL = "https://ratings.fide.com/a_top.php?list=open"
            res = self.session.get(OPEN_URL)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            table = soup.find("table")
            player_list = table.find_all("tr")
            for player in player_list[1:]:
                table_datas = player.find_all("td")
                rank = table_datas[0].text
                name = table_datas[1].text
                country = table_datas[2].text.lstrip().rstrip()
                rating = table_datas[3].text.lstrip()
                player_details = {
                    "rank": rank,
                    "name": name,
                    "country": country,
                    "ratings": rating,
                }
                ratings.append(player_details)
            return ratings
        except:
            return ratings

    def get_women_ratings(self):
        ratings = []
        try:
            WOMEN_URL = "https://ratings.fide.com/a_top.php?list=women"
            res = self.session.get(WOMEN_URL)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            table = soup.find("table")
            player_list = table.find_all("tr")
            for player in player_list[1:]:
                table_datas = player.find_all("td")
                rank = table_datas[0].text
                name = table_datas[1].text
                country = table_datas[2].text.lstrip().rstrip()
                rating = table_datas[3].text.lstrip()
                player_details = {
                    "rank": rank,
                    "name": name,
                    "country": country,
                    "ratings": rating,
                }
                ratings.append(player_details)
            return ratings
        except:
            return ratings

    def get_juniors_ratings(self):
        ratings = []
        try:
            JUNIORS_URL = "https://ratings.fide.com/a_top.php?list=juniors"
            res = self.session.get(JUNIORS_URL)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            table = soup.find("table")
            player_list = table.find_all("tr")
            for player in player_list[1:]:
                table_datas = player.find_all("td")
                rank = table_datas[0].text
                name = table_datas[1].text
                country = table_datas[2].text.lstrip().rstrip()
                rating = table_datas[3].text.lstrip()
                player_details = {
                    "rank": rank,
                    "name": name,
                    "country": country,
                    "ratings": rating,
                }
                ratings.append(player_details)
            return ratings
        except:
            return ratings

    def get_girls_ratings(self):
        ratings = []
        try:
            GIRLS_URL = "https://ratings.fide.com/a_top.php?list=girls"
            res = self.session.get(GIRLS_URL)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            table = soup.find("table")
            player_list = table.find_all("tr")
            for player in player_list[1:]:
                table_datas = player.find_all("td")
                rank = table_datas[0].text
                name = table_datas[1].text
                country = table_datas[2].text.lstrip().rstrip()
                rating = table_datas[3].text.lstrip()
                player_details = {
                    "rank": rank,
                    "name": name,
                    "country": country,
                    "ratings": rating,
                }
                ratings.append(player_details)
            return ratings
        except:
            return ratings

    def get_news(self):
        news = []
        try:
            NEWS_URL = "https://100.fide.com/fide-100-years-anniversary-news/"
            res = self.session.get(NEWS_URL)
            if res.status_code != 200:
                return [{"error": "Unable to fetch data from ESPN"}]
            soup = BeautifulSoup(res.text, "html.parser")
            articles_div = soup.find(
                "div", attrs={"class": "wppm wppm-grid s1 columns-3"}
            )
            articles = articles_div.find_all("article")
            for article in articles:
                headline = article.find("div", attrs={"class": "entry-content"}).text
                date = article.find("aside", attrs={"class": "meta-row row-3"}).text
                post_url_div = article.find("div", attrs={"class": "post-img"})
                url = post_url_div.find("a")
                news_details = {"headline": headline, "date": date, "url": url["href"]}
                news.append(news_details)
            return news
        except:
            return news
