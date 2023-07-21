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

    def articles_list(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.articles_list()
        ```
        """
        url = "https://news.ycombinator.com/"

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = "0" if not comments_link else comments_link.text.split()[0]
        
        except:
            return None
