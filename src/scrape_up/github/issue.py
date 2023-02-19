import requests
from bs4 import BeautifulSoup


class Issue:

    def __init__(self, username: str, repository_name:str, issue_number:int):
        self.username = username
        self.repository = repository_name
        self.issue_number = issue_number

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}/issues/{self.issue_number}")
        data = BeautifulSoup(data.text,"html.parser")
        return data