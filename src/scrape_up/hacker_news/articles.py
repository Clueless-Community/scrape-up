import requests
from bs4 import BeautifulSoup
import json

class Article:

    def __init__(self):
        self.help = "This scrapes articles"

    def __scrap_page(self):
        data = requests.get(
            "https://news.ycombinator.com/"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def articles_list(self):
        page = self.__scrap_page()
        try:
            articles = page.find_all('span', class_="titleline")
            article_list = []
            for article in articles:
                article_list.append(article.text)
                link = article.find('a')
                article_list.append(link['href'])

            return json.dumps(article_list)
        except:
            message = "An Error Occured!"
            return message


