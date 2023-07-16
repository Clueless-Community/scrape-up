import requests
from bs4 import BeautifulSoup
import json
import time
import pprint


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
            "link": Link to the article,
            "title": Tile of the article
            "date": Date the article was posted         
        }
        """
        url="https://news.google.com/rss/search?q="+self.topic
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, features="xml")
             # find all li tags
            lis = soup.find_all("item")
            sub_articles = []
            for li in lis:
                sub_articles.append({   "link": li.link.text,
                                         "title": li.title.text,
                                         "Date & Time": li.pubDate.text
                                    })
            return sub_articles[:8]
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
                "link": Link of the news,
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
            lis = soup.find_all("item")
            sub_articles = []
            for li in lis:
                sub_articles.append({   "link": li.link.text,
                                         "title": li.title.text,
                                         "Date & Time": li.pubDate.text
                                    })
            return sub_articles
        except:
            return None

    def timed_articles(self, time=""):
        """
        Class - `GoogleNews`
        Example:

        articles = GoogleNews("github")
        articles.timed_articles(time)
        time format:
        1h - within 1 hour
        1d - within 24 hours
        7d - within a week
        1y - within a year


        Returns:
        [
            {
                "link": Link of the news,
                "title": Title of the top story,
                "date": Date of the top story
            },
            ...
        ]
        """
        if time!="":
            time=" when:"+time
        url = "https://news.google.com/news/rss/search?q="+self.topic+time
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, features="xml")
            lis = soup.find_all("item")
            sub_articles = []
            for li in lis:
                sub_articles.append({   "link": li.link.text,
                                         "title": li.title.text,
                                         "Date & Time": li.pubDate.text
                                    })
            return sub_articles
        except:
            return None
        