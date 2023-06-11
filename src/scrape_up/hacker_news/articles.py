import requests
from bs4 import BeautifulSoup

class HackerNews:
    """
    Class - `HackerNews` \n
    Creates a scraper for https://news.ycombinator.com/
    Example - \n
    ```python
    hacker_news = HackerNews()
    """
    def __init__(self):
        self.help = "This scrapes articles"

    def __scrap_page(self):
        data = requests.get("https://news.ycombinator.com/")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def articles_list(self):
        """
        Class - `HackerNews` \n
        Example - \n
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.articles_list()
        ```
        Return \n
        ```python
        return 
        {
            "data": [
                {
                    "Article": "Article 1's title/text",
                    "Link": "https://www.article1.com"
                },
                {
                    "Article": "Article 2's title/text",
                    "Link": "https://www.article2.com/"
                },
                ...
                {
                {
                    "Article": "Article 30's title/text",
                    "Link": "https://www.article30.com/"
                }
                }
            ],
            "message": "Successfully fetched data."
        }
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

