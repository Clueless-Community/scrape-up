import requests
from bs4 import BeautifulSoup


class Repository:
    def __init__(self, username, repository_name):
        self.username = username
        self.repository_name = repository_name

    def __scrape_page(self):
        url = f"https://gitlab.com/{self.username}/{self.repository_name}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_name(self):
        try:
            data = self.__scrape_page()
            name = data.find("h1", class_="project-title").text.strip()
            return {
                "data": name,
                "message": f"Retrieved name for repository {self.repository_name}",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving name for repository {self.repository_name}: {str(e)}",
            }

    def get_description(self):
        try:
            data = self.__scrape_page()
            description = data.find("div", class_="project-description").text.strip()
            return {
                "data": description,
                "message": f"Retrieved description for repository {self.repository_name}",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving description for repository {self.repository_name}: {str(e)}",
            }
