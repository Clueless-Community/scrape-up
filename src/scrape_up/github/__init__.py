import requests
from bs4 import BeautifulSoup


class Users:

    def __init__(self, username: str):
        self.username = username

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://github.com/{username}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self):
        """
        Fetch the number of followers of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            followers = page.find(class_="text-bold color-fg-default")
            return followers.text
        except:
            message = f"{self.username} not found !"
            return message

    def get_avatar(self):
        """
        Fetch the avatar URL of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            avatar = page.find(
                class_="avatar avatar-user width-full border color-bg-default")
            return avatar["src"]
        except:
            message = f"Avatart not found for username {self.username}"
            return message

    def get_bio(self):
        """
        Fetch the bio of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            bio = page.find(class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
            return bio.text
        except:
            message = f"Bio not found for username {self.username}"
            return message
