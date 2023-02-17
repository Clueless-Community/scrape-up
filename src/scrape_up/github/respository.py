import requests
from bs4 import BeautifulSoup


class Repository:

    def __init__(self, username: str, repository_name:str):
        self.username = username
        self.repository = repository_name

    def languagesUsed(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}")
        data = BeautifulSoup(data.text,"html.parser")

        try:
            languages = data.find_all(class_="color-fg-default text-bold mr-1")
            allLanguages = []
            for item in languages:
                allLanguages.append(item.text)
            return allLanguages  # return list of languages
        except:
            message = "No languages found"
            return message