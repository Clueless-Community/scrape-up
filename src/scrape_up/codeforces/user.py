import requests
import json

class Users:
    """
    Create an object of class `LeetCodeScraper`

    ```python
    from scrape_up import codeforces
    ```

    Methods
    ```md
    | Methods                    | Details                                       |
    | -------------------------- | --------------------------------------------- |
    | `.get_user_data(username)` | Fetches user data from CodeForces. |
    ```
    """

    user_url = "https://codeforces.com/profile/{}"

    def __init__(self, username):
        self.username = username

    def get_user_data(self):
        """
        Fetches user data from CodeForces.\n
        Example

        ```python
        codeforces_user = codeforces.Users(username="tourist")
        codeforces_user.get_user_data()
        ```
        Response
        ```js
        {
            "rank":"Legendary Grandmaster",
            "handle":"tourist",
            "firstname":"Gennady",
            "lastname":"Korotkevich",
            "city":" Gomel",
            "country":"Belarus",
            "organization":" ITMO University",
            "rating":"3775",
            "contribution":"+127",
            "friendsofcount":"59,071",
            "lastvisit":"14400",
            "registered":"441806400.0",
            "titlephoto":"https://userpic.codeforces.org/422/title/50a270ed4a722867.jpg",
            "avatar":"https://userpic.codeforces.org/422/title/50a270ed4a722867.jpg"
        }
        ```
        """
        # API Method to get user information
        api_url = f"https://codeforces.com/api/user.info?handles={self.username}"
        request = requests.get(api_url)
        
        # Incase of invalid handle or other error return empty dictionary
        if not request.ok:
            return {}

        # Extracting data from response
        response = json.loads(request.text)
        data = response["result"][0]

        # Creating a dictionary
        result = {
            "rank": data.get("rank", None),
            "handle": data.get("handle", None),
            "firstname": data.get("firstName", "NA"),
            "lastname": data.get("lastName", "NA"),
            "city": data.get("city", "NA"),
            "country": data.get("country", "NA"),
            "organization": data.get("organization", "NA"),
            "rating": data.get("rating", None),
            "contribution": f'+{data.get("maxRating", 0)}',
            "friendsofcount": data.get("friendOfCount", 0),
            "lastvisit": data.get("lastOnlineTimeSeconds", 0),
            "registered": data.get("registrationTimeSeconds", 0),
            "titlephoto": data.get("titlePhoto", None),
            "avatar": data.get("avatar", None),
        }

        return result # Return the dictionary object