import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class Users:
    def __init__(self, username: str):
        self.username = username
        self.cache = {}  # Cache to store scraped data
        self.cache_expiry = timedelta(minutes=10)  # Cache expiry time

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://www.instagram.com/{username}/")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __check_cache(self, key):
        if key in self.cache:
            cached_data, expiry_time = self.cache[key]
            if datetime.now() < expiry_time:
                return cached_data
            else:
                del self.cache[key]
        return None

    def __update_cache(self, key, data):
        expiry_time = datetime.now() + self.cache_expiry
        self.cache[key] = (data, expiry_time)

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
        cache_key = f"followers_{self.username}"
        cached_data = self.__check_cache(cache_key)
        if cached_data:
            return cached_data

        page = self.__scrape_page()
        try:
            followers = page.findAll("meta", attrs={"name": "description"})
            followers_count = followers[0]["content"].split(",")[0].split(" ")[0]
            data = {
                "data": followers_count,
                "message": f"Followers found for user {self.username}",
            }
            self.__update_cache(cache_key, data)
            return data
        except:
            message = f"{self.username} not found!"
            data = {"data": None, "message": message}
            self.__update_cache(cache_key, data)
            return data

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
        cache_key = f"following_{self.username}"
        cached_data = self.__check_cache(cache_key)
        if cached_data:
            return cached_data

        page = self.__scrape_page()
        try:
            following = page.findAll("meta", attrs={"name": "description"})
            following_count = (
                following[0]["content"].split(",")[1].strip().split(" ")[0]
            )
            data = {
                "data": following_count,
                "message": f"User {self.username} is following {following_count} people.",
            }
            self.__update_cache(cache_key, data)
            return data
        except:
            message = f"{self.username} not found!"
            data = {"data": None, "message": message}
            self.__update_cache(cache_key, data)
            return data

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
        cache_key = f"posts_{self.username}"
        cached_data = self.__check_cache(cache_key)
        if cached_data:
            return cached_data

        page = self.__scrape_page()
        try:
            posts = page.findAll("span", class_="g47SY")
            posts_count = posts[0].text
            data = {
                "data": posts_count,
                "message": f"User {self.username} has {posts_count} posts.",
            }
            self.__update_cache(cache_key, data)
            return data
        except:
            message = f"{self.username} not found!"
            data = {"data": None, "message": message}
            self.__update_cache(cache_key, data)
            return data


# Test
user = Users(username="nikhil_raj803")
print(user.followers())
print(user.following())
print(user.posts())
