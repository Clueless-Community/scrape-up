import requests
from bs4 import BeautifulSoup


class HackerNews:

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
            return {
                "data": article_list,
                "message": "Successfylly fetched data."
            }

        except:
            message = "An Error Occurred!"
            return {
                "data": article_list,
                "message": message
            }
news = HackerNews()
print(news.articles_list())

