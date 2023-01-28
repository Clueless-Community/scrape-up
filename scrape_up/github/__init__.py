import requests
from bs4 import BeautifulSoup


class Users:

    def __init__(self, username):
        self.username = username

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://github.com/{username}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self):
        page = self.__scrape_page()
        try:
            followers = page.find(class_ = "text-bold color-fg-default")
            return followers.text
        except:
            message = f"{self.username} not found !"
            return message

