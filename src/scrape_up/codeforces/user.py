+import requests
from bs4 import BeautifulSoup


class USER:
    """
    Fetches user data from CodeForces Competitive Platform
    """

    user_url = "https://codeforces.com/profile/{}"

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
            url = self.user_url.format(self.username)
            info = requests.get(url)
            soup = BeautifulSoup(info.content)
            user_info_set = info.json()
            user_info_data = user_info_set["result"][0]
            for data in user_info_data:
                print(f"{data} → {user_info_data[data]}")
            return (
                "Data Fetching Successful"
                if user_info_set["status"] == "OK"
                else "Failed"
            )
        except IndexError:
            raise Exception("Invalid User Name.")
        except TypeError:
            raise Exception("Invalid User Name")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error, Please try again.")


if __name__ == "__main__":
    user = USER("benq")
    print(user.user_get_data())
