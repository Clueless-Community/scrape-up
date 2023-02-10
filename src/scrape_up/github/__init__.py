import requests
from bs4 import BeautifulSoup

class User:
    """An python wrapper to scrape any github profile"""
    def __init__(self, username):
        self.uname = username
        try:
            response = requests.get(f"https://github.com/{username}")
            self.soup = BeautifulSoup(response.text, "html.parser")
        except:
            print("Username not found")

    @property
    def username(self):
        """Return username of the user"""
        return self.uname

    @property
    def fullname(self):
        """Returns the fullname of the user"""
        fullname = self.soup.select_one("[class*='p-name vcard-fullname d-block']")
        return fullname.text.strip()

    @property
    def followers(self):
        """Returns total number of followers of the user"""
        followers = self.soup.select("[class*='text-bold color-fg-default']")
        return followers[0].text

    @property
    def following(self):
        """Returns the number of accounts user had followed"""
        following = self.soup.select("[class*='text-bold color-fg-default']")
        return following[1].text

    @property
    def bio(self):
        """Returns the bio of the user"""
        bio = self.soup.select_one("[class*='p-note user-profile-bio']")
        if bio:
            return bio.text.strip()
        return None

    @property
    def location(self):
        """Returns the location of the user"""
        location = self.soup.select_one("[itemprop='homeLocation']")
        if location:
            return location.text.strip()
        return None