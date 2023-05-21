import requests
from bs4 import BeautifulSoup


class Users:
    def __init__(self, username: str):
        self.username = username

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://www.instagram.com/{username}/")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self) -> dict:
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = Users(username="nikhil25803")
        followers = user.followers()
        ```
        Return\n
        ```python
        return {
            "data": followers_count,
            "message": f"Followers found for user {self.username}"
        }
        ```
        """
        page = self.__scrape_page()
        try:
            followers = page.findAll("meta", attrs={"name": "description"})
            followers_count = followers[0]["content"].split(",")[0].split(" ")[0]
            return {
                "data": followers_count,
                "message": f"Followers found for user {self.username}",
            }
        except:
            message = f"{self.username} not found!"
            return {"data": None, "message": message}

    def following(self) -> dict:
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = Users(username="nikhil25803")
        following = user.following()
        ```
        Return\n
        ```python
        return {
            "data": following_count,
            "message": f"User {self.username} is following {following_count} people"
        }
        ```
        """
        page = self.__scrape_page()
        try:
            following = page.findAll("meta", attrs={"name": "description"})
            following_count = (
                following[0]["content"].split(",")[1].strip().split(" ")[0]
            )
            return {
                "data": following_count,
                "message": f"User {self.username} is following {following_count} people.",
            }
        except:
            message = f"{self.username} not found!"
            return {"data": None, "message": message}

    def posts(self) -> dict:
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = Users(username="nikhil25803")
        posts = user.posts()
        ```
        Return\n
        ```python
        return {
            "data": posts_count,
            "message": f"User {self.username} has {posts_count} posts."
        }
        ```
        """
        page = self.__scrape_page()
        try:
            posts = page.findAll("span", class_="g47SY")
            posts_count = posts[0].text
            return {
                "data": posts_count,
                "message": f"User {self.username} has {posts_count} posts.",
            }
        except:
            message = f"{self.username} not found!"
            return {"data": None, "message": message}


# Test
user = Users(username="nikhil_raj803")
print(user.followers())
print(user.following())
print(user.posts())
