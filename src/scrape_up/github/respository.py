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
            allTopics = list(map(lambda s: s.strip(), allTopics))
            return allLanguages  # return list of languages
        except:
            message = "No languages found"
            return message

    def about(self):

        """
        Fetch details in about section of repository
        """
        data = self.__scrape_page()

        try:
            tag = data.find(class_="f4 mb-3")
            about = tag.get_text()
            return about  # return string about
        except:
            message = "No details found in the about section"
            return message

    
    def fork_count(self):

        """
        Returns the number of forks of the repository
        """
        data = self.__scrape_page()
        try:
            stats_body = data.find("ul", class_ = "pagehead-actions flex-shrink-0 d-none d-md-inline")
            forks = stats_body.find('span', id = 'repo-network-counter')
            fork_count = forks.text.strip()
            return fork_count
        except:
            message = f"Repository Stats are not found for username {self.username}"
            return message


    def topics(self):
        """
        Fetch topics of repository
        """
        data = self.__scrape_page()
    
        try:
            topics = data.find_all(class_="topic-tag topic-tag-link")
            allTopics = []
            for item in topics:
                allTopics.append(item.text)
            return allTopics  # return list of topics
        except:
            message = "No topics found"
            return message
        

    def star_count(self):
        """
        Fetch star count of a repository
        """
        try:
            data = self.__scrape_page()
            starCount = data.find('a', href=f"/{self.username}/{self.repository}/stargazers").find('span').text.strip()
            return starCount
        except:
            message = "Oops! No Stars found"
            return message

