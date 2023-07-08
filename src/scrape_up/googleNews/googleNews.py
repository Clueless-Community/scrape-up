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
    1. ``.getArticles() | Response - Articles with title, descriptions, news source, date and link.
    """
    
    def __init__(self, topic):
        self.topic = topic

    def getArticles(self):
        """
        Class - `GoogleNews`
        Example:
        ```
        articles = GoogleNews("github")
        articles.getArticles()
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
        url = (
            "https://www.google.com/search?q=" + self.topic + "&tbm=nws"
        )
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            articles_data = {"articles": []}

            articles = soup.find_all(
                "a", jsname="ACyKwe"
            )
            for a in articles:
                title = (
                    a.find("div", class_="BNeawe vvjwJb AP7Wnd")
                    .getText()
                )
                date = (
                    a.find("span", class_="r0bn4c rQMQod")
                    .getText()
                )
                desc = (
                    a.find("div", class_="BNeawe s3v9rd AP7Wnd")
                    .getText()
                    .replace(date, '')
                )
                news_source = (
                    a.find("div", class_="BNeawe UPmit AP7Wnd lRVwie")
                    .getText()
                )
                link = (
                    a["href"]
                    .replace("/url?q=", '')
                )
                articles_data["articles"].append(
                    {
                        "title": title,
                        "description": desc,
                        "news_source": news_source,
                        "date": date,
                        "link": link,
                    }
                )
            res_json = json.dumps(articles_data)
            return res_json
        except:
            error_message = {
                "message": "Can't fetch any articles from the topic provided."
            }
            ejson = json.dumps(error_message)
            return ejson
    def Top_stories(self):
        """
        Class - `GoogleNews`
        Example:
        ```
        # articles = GoogleNews("github")

        ```
        Prints the top stories from Google News RSS feed.
        """
        url = "https://news.google.com/news/rss"
        page = requests.get(url)
        soup = BeautifulSoup(page.content,features="xml")
        titles = soup.find_all("title")
        for title in titles:
            print(title.text.upper())
            print(time.ctime())
            print("-" * 70)
