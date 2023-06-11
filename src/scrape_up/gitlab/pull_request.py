import requests
from bs4 import BeautifulSoup


class PullRequest:
    def __init__(self, username, repository, pull_request_number):
        self.username = username
        self.repository = repository
        self.pull_request_number = pull_request_number

    def __scrape_page(self):
    url = f"https://gitlab.com/{self.username}/{self.repository}/-/merge_requests/{self.pull_request_number}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP errors
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def get_title(self):
    try:
        data = self.__scrape_page()
        title = data.find("h1", class_="title").text.strip()
        return {
            "data": title,
            "message": "Retrieved pull request title"
        }
    except Exception as e:
        return {
            "data": None,
            "message": f"Error retrieving pull request title: {str(e)}"
        }

def get_description(self):
    try:
        data = self.__scrape_page()
        description = data.find("div", class_="description").text.strip()
        return {
            "data": description,
            "message": "Retrieved pull request description"
        }
    except Exception as e:
        return {
            "data": None,
            "message": f"Error retrieving pull request description: {str(e)}"
        }

def get_author(self):
    try:
        data = self.__scrape_page()
        author = data.find("span", class_="author").text.strip()
        return {
            "data": author,
            "message": "Retrieved pull request author"
        }
    except Exception as e:
        return {
            "data": None,
            "message": f"Error retrieving pull request author: {str(e)}"
        }

