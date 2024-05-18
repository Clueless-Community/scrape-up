import json
from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class KooUser:
    """
    class - `KooUser`

    Example:
    ```py
    user = KooUser('krvishal')
    avatar = user.get_avatar_url()
    ```
    Returns:
    ```
    >>> 'https://images.kooapp.com/transcode_input/8074390/profile16851706949505ew9y8.jpg'
    """

    def __init__(self, username: str, *, config: RequestConfig = RequestConfig()):
        self.username = username
        self.config = config

    def __str__(self) -> str:
        return f"The username is: {self.username}"

    @property
    def profile_url(self) -> str:
        return f"https://www.kooapp.com/profile/{self.username}"

    def __scrape_page(self):
        try:
            res = get(self.profile_url, self.config)
            if res.status_code == 404:
                raise Exception(f"User not found with username: {self.username}")
            return res
        except Exception as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def __parse_page(self) -> dict:
        res = self.__scrape_page()
        try:
            page = BeautifulSoup(res.text, "html.parser")
            data = json.loads(page.find("script", attrs={"id": "__NEXT_DATA__"}).text)
            return data
        except Exception as e:
            raise Exception(f"An error occurred while parsing the page: {str(e)}")

    def __parse_profile_data(self) -> dict:
        data = self.__parse_page()
        try:
            userdata = (
                data.get("props")
                .get("pageProps")
                .get("initialState")
                .get("profileReducers")
                .get("profileItems")
            )
            return userdata
        except Exception as e:
            raise Exception(f"An error occured while parsing the data: {e}")

    def get_name(self) -> str:
        """
        Fetch the name of the user.
        """
        userdata = self.__parse_profile_data()
        name = userdata.get("name")
        return {
            "data": name or None,
            "message": (
                f"Name of the user {self.username} is {name}"
                if name
                else f"No name found for the user {self.username}"
            ),
        }

    def get_bio(self) -> str:
        """
        Fetch the bio dsecription of the user.
        """
        userdata = self.__parse_profile_data()
        bio = userdata.get("description")
        return {
            "data": bio or None,
            "message": (
                f"Bio found for the user {self.username}"
                if bio
                else f"No bio found for the user {self.username}"
            ),
        }

    def get_avatar_url(self) -> str:
        """
        Fetch the avatar url of the user.
        """
        userdata = self.__parse_profile_data()
        avatar = userdata.get("profileImage")
        return {
            "data": avatar or None,
            "message": (
                f"Avatar found for the user {self.username}"
                if avatar
                else f"Avatar not found for the user {self.username}"
            ),
        }

    def followers(self) -> int:
        """
        Fetch the number of followers of the Koo user.
        """
        userdata = self.__parse_profile_data()
        followers = userdata.get("followerCount")
        return {
            "data": followers,
            "message": f"There are {followers} follower(s) of the user {self.username}",
        }

    def following(self) -> int:
        """
        Fetch the number of following of the Koo user.
        """
        userdata = self.__parse_profile_data()
        following = userdata.get("followingCount")
        return {
            "data": following,
            "message": f"There are {following} user(s) followed by {self.username}",
        }

    def get_social_profiles(self) -> dict[str, str]:
        """
        Fetch all the listed social media profiles of user.
        """
        userdata = self.__parse_profile_data()
        profiles = {
            s_media: handle
            for s_media, handle in userdata.get("socialProfile").items()
            if handle
        }
        return {
            "data": profiles or None,
            "message": (
                f"Found {len(profiles)} social profiles for the user {self.username}"
                if profiles
                else f"No social profiles found for the user {self.username}"
            ),
        }

    def get_profession(self) -> str:
        """
        Fetch the profession of the user.
        """
        userdata = self.__parse_profile_data()
        profession = userdata.get("title")
        return {
            "data": profession or None,
            "message": (
                f"Profession found for the user {self.username}"
                if profession
                else f"No profession found for the user {self.username}"
            ),
        }
