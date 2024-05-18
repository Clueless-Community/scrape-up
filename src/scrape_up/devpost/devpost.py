from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from scrape_up.config.request_config import RequestConfig, get
import undetected_chromedriver as uc
import json


class Devpost:
    """
    Create an instance of `Devpost` class.
    ```py
    posts = Devpost()
    ```
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.get_projects()` | Returns the latest projects along with their decription, like and commment count, image and member details. |
    | `.search(topic)` | Returns the searched projects along with their decription, like and commment count, image and member details. |
    | `.get_hackathons()` | Returns the latest hackathons along with their title, participants, prizes, deadlines.          |
    | `.get_featured()` | Returns the latest featured projects along with their decription, like and commment count, image and member details. |
    | `.get_winner()` | Returns the latest winning projects along with their decription, like and commment count, image and member details. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def get_projects(self):
        """
        Class - `Devpost`
        Example -
        ```python
        devpost = Devpost()
        posts = devpost.get_projects()
        ```
        Return
        ```js
        [
            {
                'title': 'Multiple templates - Quarkus quickstarts & sample 3-tier app',
                'description': 'Learning a new technology requires lot of research & development. There are templates spanning multiple middleware and databases for learning Quarkus with hot reloading & bunnyshell rdev feature.',
                'like_count': '31',
                'comment_count': '9',
                'img_url': 'https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/002/532/156/datas/medium.png',
                'members': [
                    {
                        'name': 'Himanshu Gupta',
                        'avatar_url': 'https://lh3.googleusercontent.com/a-/AOh14GjwWZyRHT67sf0URtiep3OjOzNV1lpLcxHvbHs7?type=square',
                        'link': 'https://devpost.com/himanshu_mps'
                    }
                ]
            }
            ...
        ]
        ```
        """
        url = "https://devpost.com/software"
        projects_data = {"projects": []}
        try:
            page = get(url, self.config)
            soup = BeautifulSoup(page.content, "html.parser")
            heads = soup.find_all("div", class_="large-3 small-12 columns gallery-item")
            for h in heads:
                members_list = []
                title = h.find("h5").getText().strip()
                desc = h.find("p", class_="small tagline").getText().strip()
                like = h.find("span", class_="count like-count").getText().strip()
                comment_count = (
                    h.find("span", class_="count comment-count").getText().strip()
                )
                try:
                    img = h.find("img", alt=title)["src"]
                except:
                    img = ""
                members = h.find_all("span", class_="user-profile-link")
                for m in members:
                    name = m.find("img")["alt"]
                    avatar = m.find("img")["src"]
                    link = m["data-url"]
                    members_list.append(
                        {"name": name, "avatar_url": avatar, "link": link}
                    )
                projects_data["projects"].append(
                    {
                        "title": title,
                        "description": desc,
                        "like_count": like,
                        "comment_count": comment_count,
                        "img_url": img,
                        "members": members_list,
                    }
                )
            return projects_data["projects"]
        except:
            return None

    def search(self, topic):
        """
        Class - `Devpost`
        Example -
        ```python
        devpost = Devpost()
        hackathons = devpost.search()
        ```
        """
        url = f"https://devpost.com/software/search?query={topic}"
        try:
            page = get(url, self.config)
            soup = BeautifulSoup(page.content, "html.parser")
            data = str(soup)
            projects = json.loads(data)
            return projects["software"]
        except:
            return None

    def get_hackathons(self):
        """
        Class - `Devpost`
        Example -
        ```python
        devpost = Devpost()
        hackathons = devpost.get_hackathons()
        ```
        Return
        ```js
        [
            {

                'class_name': 'Software',
                'name': 'Electron-Cash-SLP',
                'tagline': 'Electron Cash for SLP Tokens',
                'slug': 'electron-cash-slp',
                'url': 'https://devpost.com/software/electron-cash-slp',
                'members': None,
                'tags': ['python', 'objective-c', 'c', 'kotlin', 'shell', 'java', 'nsis', 'dockerfile', 'ruby'],
                'winner': False,
                'photo': 'https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/002/558/403/datas/small.jpg',
                'has_video': True,
                'like_count': 1,
                'comment_count': 0}
                'title': 'Ripple CBDC Innovate',
                'status': '9 days left',
                'prize': '200,000',
                'total participants': '1061',
                'host': 'Ripple',
                'submission-period': 'May 15 - Aug 18, 2023',
                'labels': 'Blockchain, Fintech, Social Good, ',
                'hackathon-image': 'https://d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/002/459/630/datas/medium_square.png'
            }
            ...
        ]
        ```
        """
        url = "https://devpost.com/hackathons"

        try:
            chrome_options = uc.ChromeOptions()
            chrome_options.add_argument("--headless")
            driver = uc.Chrome(options=chrome_options)

            driver.get(url)
            wait = WebDriverWait(driver, 5)
        except:
            return None

        head_tags = wait.until(
            lambda d: driver.find_elements(By.CLASS_NAME, "hackathon-tile")
        )
        hackathons_data = {"hackathons": []}
        try:
            for tag in head_tags:
                main_content = tag.find_element(By.CLASS_NAME, "main-content")
                side_content = tag.find_element(By.CLASS_NAME, "side-info")

                img = main_content.find_element(By.TAG_NAME, "img").get_attribute("src")

                title = main_content.find_element(By.CSS_SELECTOR, ".content h3").text

                status = main_content.find_element(
                    By.CLASS_NAME, "hackathon-status"
                ).text

                prize = main_content.find_element(
                    By.CSS_SELECTOR, ".prize-amount span"
                ).text

                participants = main_content.find_element(
                    By.CSS_SELECTOR, ".participants strong"
                ).text

                host = side_content.find_element(By.CLASS_NAME, "host-label").text
                submission = side_content.find_element(
                    By.CLASS_NAME, "submission-period"
                ).text

                theme_labels = side_content.find_elements(By.CLASS_NAME, "theme-label")
                theme = ""
                for label in theme_labels:
                    theme = theme + label.text + ", "

                hackathon = {
                    "title": title,
                    "status": status,
                    "prize": prize,
                    "total participants": participants,
                    "host": host,
                    "submission-period": submission,
                    "labels": theme,
                    "hackathon-image": img,
                }

                hackathons_data["hackathons"].append(hackathon)
        except:
            return None
        return hackathons_data

    def get_featured(self):
        """
        Class - `Devpost`
        Example -
        ```python
        devpost = Devpost()
        posts = devpost.get_featured()
        ```
        """
        url = "https://devpost.com/software/search?query=is%3Afeatured"
        try:
            page = get(url, self.config)
            soup = BeautifulSoup(page.content, "html.parser")
            str_data = str(soup)
            data = json.loads(str_data)
            return data["software"]
        except:
            return None

    def get_winner(self):
        """
        Class - `Devpost`
        Example -
        ```python
        devpost = Devpost()
        posts = devpost.get_winner()
        ```
        Return
        ```js
        [
            {
                'class_name': 'Software',
                'name': 'Smart Fridge',
                'tagline': 'A Smart Fridge that uses Computer Vision to log in food, keeps user updated by SMS, and provide recommendations. ',
                'slug': 'smart-fridge-9d8qyv',
                'url': 'https://devpost.com/software/smart-fridge-9d8qyv',
                'members': ['yeling7', 'jjpprrrr', 'yuelunyang', 'cloudwaysx'],
                'tags': ['python', 'c++', 'google-cloud-vision', 'google-ml', 'google-app-engine', 'google-cloud', 'google-cloud-datastore', 'google-knowledgegraph', 'twilio', 'kinect', 'arduino', 'wolfram-technologies'],
                'winner': True,
                'photo': 'https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/000/485/920/datas/small.jpg',
                'has_video': True,
                'like_count': 67,
                'comment_count': 9
            }
            ...
        ]
        ```
        """
        url = "https://devpost.com/software/search?query=is%3Awinner"
        try:
            page = get(url, self.config)
            soup = BeautifulSoup(page.content, "html.parser")
            str_data = str(soup)
            data = json.loads(str_data)
            return data["software"]
        except:
            return None
