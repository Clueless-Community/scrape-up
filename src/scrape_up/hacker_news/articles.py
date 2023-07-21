import requests
from bs4 import BeautifulSoup

class HackerNews:
    """
    Class - `HackerNews`
    Creates a scraper for https://news.ycombinator.com/
    Example -
    ```python
    hacker_news = HackerNews()
    ```
    """

    def __init__(self, url="https://news.ycombinator.com/"):
        self.url = url
        self.help = "This scrapes articles"

    def __scrap_page(self):
        data = requests.get(self.url)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def articles_list(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.articles_list()
        ```
        """
        page = self.__scrap_page()
        article_list = []
        try:
            articles = page.find_all("span", class_="titleline")
            for article in articles:
                link = article.find("a")
                article_list.append({"Article": article.text, "Link": link["href"]})
            return {"data": article_list, "message": "Successfully fetched data."}

        except:
            message = "An Error Occurred!"
            return {"data": article_list, "message": message}
