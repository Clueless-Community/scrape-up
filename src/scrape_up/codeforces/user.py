import requests
from bs4 import BeautifulSoup


class USER:
    """
    Fetches user data from CodeForces Competitive Platform
    """

    api_base_url = "https://codeforces.com/api/"

    def __init__(self, username):
        self.username = username
        self.userdata = self.user_get_data()

    def user_get_data(self):
        """
        Gets all information of a username from codeforces.

        Class - `codeforces.user()`\n
        Example -\n
        ```python
        user = USER("benq")
        print(user.user_get_data())
        ```
        Return\n
        ```python
        return
        lastName → Qi
        country → United States
        lastOnlineTimeSeconds → 1686275190
        city → Princeton
        rating → 3783
        friendOfCount → 12513
        titlePhoto → https://userpic.codeforces.org/312472/title/7cf0a442d4071e87.jpg
        handle → Benq
        avatar → https://userpic.codeforces.org/312472/avatar/5716ac69aea8159a.jpg
        firstName → Benjamin
        contribution → 50
        organization → MIT
        rank → legendary grandmaster
        maxRating → 3813
        registrationTimeSeconds → 1435099979
        maxRank → legendary grandmaster
        lastName → Qi
        country → United States
        lastOnlineTimeSeconds → 1686275190
        city → Princeton
        rating → 3783
        friendOfCount → 12513
        titlePhoto → https://userpic.codeforces.org/312472/title/7cf0a442d4071e87.jpg
        handle → Benq
        avatar → https://userpic.codeforces.org/312472/avatar/5716ac69aea8159a.jpg
        firstName → Benjamin
        contribution → 50
        organization → MIT
        rank → legendary grandmaster
        maxRating → 3813
        registrationTimeSeconds → 1435099979
        maxRank → legendary grandmaster
        Data Fetching Successful
        ```
        """
        try:
            # Defining the API method and parameters
            method = "user.info"
            params = {"handles": self.username}

            # Making the API request
            response = requests.get(f"{self.api_base_url}{method}", params=params)
            data = response.json()

            if data["status"] == "OK":
                user_info = data["result"][0]
                
                # Extracting and printing the detailed user information
                for key, value in user_info.items():
                    print(f"{key} → {value}")

                return "Data Fetching Successful"
            else:
                raise Exception(f"API Request Failed: {data.get('comment', 'No comment')}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request Error: {e}")
        except Exception as e:
            raise Exception(f"Error: {e}")


if __name__ == "__main__":
    user = USER("benq")
    print(user.user_get_data())
