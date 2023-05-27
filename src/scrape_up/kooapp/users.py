import requests
import json
from bs4 import BeautifulSoup

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
    def __init__(self, username: str) -> None:
        self.username = username

    def __str__(self) -> str:
        return f"The username is: {self.username}"

    @property
    def profile_url(self) -> str:
        return f"https://www.kooapp.com/profile/{self.username}"

    def __scrape_page(self) -> requests.Response:
        try:
            res = requests.get(self.profile_url)
            if res.status_code == 404:
                raise Exception(f"User not found with username: {self.username}")
            return res
        except Exception as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")
    
    def __parse_page(self) -> dict:
        res = self.__scrape_page()
        try:
            page = BeautifulSoup(res.text, "html.parser")
            data = json.loads(page.find('script', attrs={'id': '__NEXT_DATA__'}).text)
            return data
        except Exception as e:
            raise Exception(f"An error occurred while parsing the page: {str(e)}")

    def __parse_profile_data(self) -> dict:
        data = self.__parse_page()
        userdata = data.get('props').get('pageProps').get('initialState').get('profileReducers').get('profileItems')
        return userdata

    def get_name(self) -> str:
        """
        Fetch the name of the user.
        """
        userdata = self.__parse_profile_data()
        name = userdata.get('name')
        return name

    def get_bio(self) -> str:
        """
        Fetch the bio dsecription of the user.
        """
        userdata = self.__parse_profile_data()
        bio = userdata.get('description')
        return bio or f"Bio not found for username: {self.username}"
    
    def get_avatar_url(self) -> str:
        """
        Fetch the avatar url of the user.
        """
        userdata = self.__parse_profile_data()
        avatar = userdata.get("profileImage")
        return avatar or f"Avatar not found for username {self.username}"
    
    def followers(self) -> int:
        """
        Fetch the number of followers of the Koo user.
        """
        userdata = self.__parse_profile_data()
        return userdata.get("followerCount")
    
    def following(self) -> int:
        """
        Fetch the number of following of the Koo user.
        """
        userdata = self.__parse_profile_data()
        return userdata.get("followingCount")
    
    def get_social_profiles(self) -> dict[str, str]:
        """
        Fetch all the listed social media profiles of user.
        """
        userdata = self.__parse_profile_data()
        return {s_media: handle for s_media, handle in userdata.get('socialProfile').items() if handle }

    def get_profession(self) -> str:
        """
        Fetch the profession of the user.
        """
        userdata = self.__parse_profile_data()
        return userdata.get('title')
