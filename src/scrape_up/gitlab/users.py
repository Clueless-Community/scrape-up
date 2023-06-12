import requests
from bs4 import BeautifulSoup


class Users:
    def __init__(self, username):
        self.username = username

    def __scrape_page(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_name(self):
        url = f"https://gitlab.com/{self.username}"
        try:
            data = self.__scrape_page(url)
            name = data.find("h1", class_="user-title").text.strip()
            return {"data": name, "message": f"Retrieved name for user {self.username}"}
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving name for user {self.username}: {str(e)}",
            }

    def get_bio(self):
        url = f"https://gitlab.com/{self.username}"
        try:
            data = self.__scrape_page(url)
            bio = data.find("div", class_="user-info").text.strip()
            return {"data": bio, "message": f"Retrieved bio for user {self.username}"}
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving bio for user {self.username}: {str(e)}",
            }

    def get_avatar_url(self):
        url = f"https://gitlab.com/{self.username}"
        try:
            data = self.__scrape_page(url)
            avatar_url = data.find("img", class_="avatar s40")["src"]
            return {
                "data": avatar_url,
                "message": f"Retrieved avatar URL for user {self.username}",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving avatar URL for user {self.username}: {str(e)}",
            }

    def get_repositories(self):
        url = f"https://gitlab.com/{self.username}?tab=repositories"
        try:
            data = self.__scrape_page(url)
            repositories = []
            repo_elements = data.find_all("li", class_="project-row")
            for repo_element in repo_elements:
                name = repo_element.find("h3", class_="project-title").text.strip()
                description = repo_element.find(
                    "p", class_="project-description"
                ).text.strip()
                repositories.append({"name": name, "description": description})
            return {
                "data": repositories,
                "message": f"Retrieved repositories for user {self.username}",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving repositories for user {self.username}: {str(e)}",
            }

    def get_project_details(self, project_id):
        url = f"https://gitlab.com/{self.username}/{project_id}"
        try:
            data = self.__scrape_page(url)
            name = data.find("h1", class_="project-title").text.strip()
            last_activity = data.find("span", class_="last_activity").text.strip()
            return {
                "data": {"name": name, "last_activity": last_activity},
                "message": f"Retrieved project details for project {project_id}",
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving project details for project {project_id}: {str(e)}",
            }
