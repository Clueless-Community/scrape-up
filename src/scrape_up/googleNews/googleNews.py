import requests
from bs4 import BeautifulSoup
import json
import time


class GoogleNews:
    """
    Class - `GoogleNews`
    Example:
    ```
    articles = GoogleNews(topic = "topic")
    ```\n
    Methods :\n
    1. `.get_articles()` | Response - Articles with title, descriptions, news source, date and link.
    2. `.top_stories()` | Response - Top stories listed regarding the mentioned topic.
    """

    def __init__(self, topic):
        self.topic = topic

    def get_articles(self):
        """
        Class - `GoogleNews`
        Example:
        ```
        articles = GoogleNews("github")
        articles.get_articles()
        ```
        Returns:
        {
            "title": Tile of the article
            "description": Description of the article
            "news_source": News Source of the Article
            "date": Date the article was posted
            "link": Link to the article
        }
        """
        url = "https://www.google.com/search?q=" + self.topic + "&tbm=nws"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            articles_data = {"articles": []}

            articles = soup.find_all("a", jsname="ACyKwe")
            for a in articles:
                title = a.find("div", class_="BNeawe vvjwJb AP7Wnd").getText()
                date = a.find("span", class_="r0bn4c rQMQod").getText()
                desc = (
                    a.find("div", class_="BNeawe s3v9rd AP7Wnd")
                    .getText()
                    .replace(date, "")
                )
                news_source = a.find(
                    "div", class_="BNeawe UPmit AP7Wnd lRVwie"
                ).getText()
                link = a["href"].replace("/url?q=", "")
                articles_data["articles"].append(
                    {
                        "title": title,
                        "description": desc,
                        "news_source": news_source,
                        "date": date,
                        "link": link,
                    }
                )
            return articles_data
        except:
            return None

    def top_stories(self):
        """
        Class - `GoogleNews`
        Example:

        articles = GoogleNews("github")
        articles.top_stories()

        Returns:
        [
            {
                "title": Title of the top story,
                "date": Date of the top story
            },
            ...
        ]
        """
        url = "https://news.google.com/news/rss"
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, features="xml")
            titles = soup.find_all("title")

            top_stories_data = {"top_stories": []}

            if len(titles) > 0:
                for title in titles:
                    top_stories_data["top_stories"].append(
                        {"title": title.text.upper(), "date": time.ctime()}
                    )
                top_stories_data
            else:
                return None
        except requests.exceptions.RequestException as e:
            return None
