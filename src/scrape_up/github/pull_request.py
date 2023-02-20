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
    def labels(self):
        labels_found=[]
        data=self.__scrape_page()
        label_raw=data.find_all("a",class_="IssueLabel hx_IssueLabel width-fit mb-1 mr-1")
        for d in label_raw:
            pass
            labels_found.append(d.get_text().strip())   
        return labels_found
        

    def commits(self):
        """
        Fetch the number of commits made in a pull request
        """
        data = self.__scrape_page()
        commits_count = data.find('span', id='commits_tab_counter').text.strip()
        return commits_count
