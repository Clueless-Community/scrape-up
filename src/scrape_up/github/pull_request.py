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
    
    def __files_changed_body(self):
        '''
        scrape the data of files changed in a pull request
        '''
        link = f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}/files"
        data = requests.get(link)
        data = BeautifulSoup(data.text,"html.parser")
        return data
        
    def files_changed(self):
        """
        Fetch the number of files changed in a pull request
        """
        data = self.__files_changed_body()
        try:
            files_changed_body = data.find('span', id='files_tab_counter')
            files_changed = files_changed_body.text.strip()
            return files_changed
        except:
            Message = "No files changed found"
            return Message
