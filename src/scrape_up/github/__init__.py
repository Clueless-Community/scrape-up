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

    def repo_count(self):
        """
        Fetch the number of repositories of Github user.
        """
        page = self.__scrape_page()
        try:
            count_repo = page.find_all(class_="Counter")
            count_repo_list=[]
            for word in count_repo:
                find_all_example=word.get_text()
                count_repo_list.append(find_all_example)
            return(count_repo_list[0])
        except:        
            message = f"No. of Repos not found for username {self.username}"
            return message

    def star_count(self):
        """
        Fetch the number of stars of Github user.
        """
        page = self.__scrape_page()
        try:           
            count_star = page.find_all(class_="Counter")
            count_star_list=[]
            for words in count_star:
                find_all_example=words.get_text()
                count_star_list.append(find_all_example)
            return(count_star_list[3])
        except:        
            message = f"Starred repo not found for username {self.username}"
            return message

    