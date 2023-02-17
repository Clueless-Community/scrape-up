import requests
from bs4 import BeautifulSoup


class Repository:

    def __init__(self, username: str, repository_name:str):
        self.username = username
        self.repository = repository_name

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}")
        data = BeautifulSoup(data.text,"html.parser")
        return data

    def languagesUsed(self):

        """
        Fetch list of languages used in repository
        """
        data = self.__scrape_page()

        try:
            languages = data.find_all(class_="color-fg-default text-bold mr-1")
            allLanguages = []
            for item in languages:
                allLanguages.append(item.text)
            return allLanguages  # return list of languages
        except:
            message = "No languages found"
            return message