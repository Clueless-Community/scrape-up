import requests
from bs4 import BeautifulSoup


class Issue:
    def __init__(self, username, repository, issue_number):
        self.username = username
        self.repository = repository
        self.issue_number = issue_number

    def __scrape_page(self):
        url = f"https://gitlab.com/{self.username}/{self.repository}/-/issues/{self.issue_number}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_title(self):
        try:
            data = self.__scrape_page()
            title = data.find("h1", class_="title").text.strip()
            return {"data": title, "message": "Retrieved issue title"}
        except Exception as e:
            return {"data": None, "message": f"Error retrieving issue title: {str(e)}"}

    def get_description(self):
        try:
            data = self.__scrape_page()
            description = data.find("div", class_="description").text.strip()
            return {"data": description, "message": "Retrieved issue description"}
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving issue description: {str(e)}",
            }

    def get_author(self):
        try:
            data = self.__scrape_page()
            author = data.find("span", class_="author").text.strip()
            return {"data": author, "message": "Retrieved issue author"}
        except Exception as e:
            return {"data": None, "message": f"Error retrieving issue author: {str(e)}"}
