import requests
from bs4 import BeautifulSoup
import json


class TechCrunch:
    """
    Class - `TechCrunch`
    Example:
    ```
    articles = TechCrunch(category = "topic")
    ```\n
    Methods :\n
    1. ``.getArticles() | Response - Articles with title, descriptions, images, date and link.
    """

    def __init__(self, category):
        self.category = category

    def getArticles(self):
        """
        Class - `TechCrunch`
        Example:
        ```
        articles = TechCrunch("artificial-intelligence")
        articles.getArticles()
        ```
        Returns:
        {
            "title": Tile of the article
            "description": Description of the article
            "image": Image of the article
            "author": Author of the Article
            "date": Date the article was posted
            "link": Link to the article
        }
        """
        url = (
            "https://techcrunch.com/category/" + self.category.replace(" ", "-").lower()
        )
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            articles_data = {"articles": []}

            articles = soup.find_all(
                "div", class_="post-block post-block--image post-block--unread"
            )
            for n in articles:
                title = (
                    n.select_one(".post-block__title__link")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                description = (
                    n.select_one(".post-block__content")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                img = n.find_all("img", src=True)
                image = img[0]["src"]
                author = (
                    n.select_one(".river-byline__authors")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                time = n.find_all("div", class_="river-byline")
                date = (
                    time[0]
                    .select_one(".river-byline__time")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                links = n.find_all("a", class_="post-block__title__link", href=True)
                link = links[0]["href"]
                articles_data["articles"].append(
                    {
                        "title": title,
                        "description": description,
                        "image": image,
                        "author": author,
                        "date": date,
                        "link": link,
                    }
                )
            result_json = json.dumps(articles_data)
            return result_json
        except:
            error_message = {
                "message": "Can't fetch any articles from the topic provided."
            }
            error_json = json.dumps(error_message)
            return error_json
