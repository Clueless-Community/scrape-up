import requests
from bs4 import BeautifulSoup


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
        article_list = []
        try:
            articles = page.find_all('span', class_="titleline")
            for article in articles:
                link = article.find('a')
                article_list.append({"Article": article.text, "Link": link['href']})
            return article_list

        except:
            message = "An Error Occurred!"
            return {
                "data": article_list,
                "message": message
            }


