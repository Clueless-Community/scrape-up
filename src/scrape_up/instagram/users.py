import requests
from bs4 import BeautifulSoup

class Users:
    def __init__(self, username: str):
        self.username = username

    def __scrape_page(self):
        username = self.username
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        }
        response = requests.get(f"https://www.instagram.com/{username}/", headers=headers)
        if response.status_code == 200:
            data = BeautifulSoup(response.text, "html.parser")
            return data
        else:
            response.raise_for_status()

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
        return
        {
            "data": followers_count,
            "message":f"Followers found for user {self.username}"
        }
        ```
        """
        try:
            page = self.__scrape_page()
            followers = page.findAll("meta", attrs={"name": "description"})
            followers_count = followers[0]["content"].split(",")[0].split(" ")[0]
            return {
                "data": followers_count,
                "message": f"Followers found for user {self.username}",
            }
        except IndexError:
            message = f"Failed to retrieve followers count for user {self.username}"
            return {"data": None, "message": message}
        except requests.exceptions.HTTPError as e:
            message = f"Failed to retrieve page for user {self.username}. Error: {str(e)}"
            return {"data": None, "message": message}

# Test
user = Users(username="nikhil_raj803")
print(user.followers())
