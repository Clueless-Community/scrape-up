import requests
from bs4 import BeautifulSoup


class PullRequest:

    def __init__(self, username: str, repository_name:str, pull_request_number:int):
        self.username = username
        self.repository = repository_name
        self.pr_number = pull_request_number

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}")
        data = BeautifulSoup(data.text,"html.parser")
        return data

    def commits(self):
        """
        Fetch the number of commits made in a pull request
        """
        data = self.__scrape_page()
        commits_count = data.find('span', id='commits_tab_counter').text.strip()
        return commits_count
    
    def title(self):
        """
        Fetch the title of a pull request
        """
        data = self.__scrape_page()
        try:
            title_body = data.find('bdi', class_='js-issue-title markdown-title')
            title = title_body.text.strip()
            return title
        except:
            Message = "No title found"
            return Message
