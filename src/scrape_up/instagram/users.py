import requests
from bs4 import BeautifulSoup


class Users:
    def __init__(self, username: str):
        self.username = username

    def __scrape_page(self):
        username = self.username
        try:
            data = requests.get(f"https://www.instagram.com/{username}/")
            data.raise_for_status()
            return data.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def __parse_page(self, html):
        try:
            page = BeautifulSoup(html, "html.parser")
            return page
        except Exception as e:
            raise Exception(f"An error occurred while parsing the page: {str(e)}")

    def followers(self):
        """
        Class - `Users`
        Example:
        ```
        scraper = Users(username="nikhil25803")
        followers = scraper.followers()
        ```
        Returns:
        {
            "data": followers_count,
            "message": f"Followers found for user {self.username}"
        }
        """
        try:
            html = self.__scrape_page()
            page = self.__parse_page(html)
            followers = page.find_all("meta", attrs={"name": "description"})
            followers_count = followers[0]["content"].split(",")[0].split(" ")[0]
            return {
                "data": followers_count,
                "message": f"Followers found for user {self.username}",
            }
        except Exception as e:
            message = f"{self.username} not found!"
            return {"data": None, "message": message}

    def following(self):
        """
        Class - `Users`
        Example:
        ```
        scraper = Users(username="nikhil25803")
        following = scraper.following()
        ```
        Returns:
        {
            "data": following_count,
            "message": f"User {self.username} is following {following_count} people"
        }
        """
        try:
            html = self.__scrape_page()
            page = self.__parse_page(html)
            following = page.find_all("meta", attrs={"name": "description"})
            following_count = following[0]["content"].split(",")[1].strip().split(" ")[0]
            return {
                "data": following_count,
                "message": f"User {self.username} is following {following_count} people.",
            }
        except Exception as e:
            message = f"{self.username} not found!"
            return {"data": None, "message": message}
          
    
    def posts(self):
        """
        Returns post count of the user.
        """

        page = self.__scrape_page()
        page = self.__parse_page(page)
        try:
            post = page.select("meta", attrs={"name": "description"})
            meta = post[11]
            meta = [x for x in meta["content"].split()]
            iterator_meta = iter(meta)
            for i in range(len(meta)):
                if next(iterator_meta, 0) == 'Posts':
                    post_count = meta[i-1]
                   
            return {
                "data": post_count,
                "message": f"User {self.username} has {post_count} posts.",
            }
        except:
            message = f"{self.username} not found !"
            return {"data": None, "message": message}
        

# Test
# user = Users(username="nikhil_raj803")
# print(user.followers())
# print(user.following())
# print(user.posts())