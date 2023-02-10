import requests
from bs4 import BeautifulSoup

class User:
    """A python wrapper to scrape any github profile"""
    def __init__(self, username:str=None, url:str=None):
        if username:
            self.url = f"https://github.com/{username}"
        elif url:
            self.url = url
        else:
            raise AttributeError("Github username or profile url required.")

        try:
            response = requests.get(self.url)
            self.soup = BeautifulSoup(response.text, "html.parser")
        except:
            print("Username not found")

    def __str__(self) -> str:
        return f"User({self.fullname})"

    @property
    def username(self) -> str:
        """Return username of the user"""
        fullname = self.soup.select_one("[class*='p-nickname vcard-username']")
        return fullname.text.strip()

    @property
    def fullname(self) -> str:
        """Returns the fullname of the user"""
        fullname = self.soup.select_one("[class*='p-name vcard-fullname d-block']")
        return fullname.text.strip()

    @property
    def followers(self) -> str:
        """Returns total number of followers of the user"""
        followers = self.soup.select("[class*='text-bold color-fg-default']")
        return followers[0].text

    @property
    def following(self) -> str:
        """Returns the number of accounts user had followed"""
        following = self.soup.select("[class*='text-bold color-fg-default']")
        return following[1].text

    @property
    def bio(self) -> [str, None]:
        """Returns the bio of the user"""
        bio = self.soup.select_one("[class*='p-note user-profile-bio']")
        if bio:
            return bio.text.strip()
        return None

    @property
    def location(self) -> [str, None]:
        """Returns the location of the user"""
        location = self.soup.select_one("[itemprop='homeLocation']")
        if location:
            return location.text.strip()
        return None

    @property
    def repositories(self) -> str:
        """Returns the total number of repositories of the user"""
        repos = self.soup.select("[class*='UnderlineNav-item']")[1].text.strip()
        return repos.split("\n")[1].strip()

    @property
    def readme(self) -> [str, None]:
        """Returns the readme article of the profile"""
        try:
            readme = self.soup.select_one("[class*='markdown-body entry-content']").text
            return "".join(filter(lambda ele: ele != '', readme.splitlines()))
        except AttributeError:
            return None

    @property
    def contributions(self) -> str:
        """Returns total number of contributions this year"""
        contributions = self.soup.select_one("[class*='js-yearly-contributions']")
        return contributions.find('h2').text.split()[0]

    def get_pinned_repos(self) -> [list, None]:
        """Return all the pinned repos of the user"""
        repos = self.soup.find_all("span", class_="repo")
        if repos:
            return [repo.text for repo in repos]
        return None