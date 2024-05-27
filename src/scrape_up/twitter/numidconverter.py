from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json


class TwitterScraper:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-logging")
        self.chrome_options.add_argument("--log-level=3")
        self.chrome_options.add_argument("--silent")
        self.chrome_options.add_argument("--blink-settings=imagesEnabled=false")

    def unametoid(self, username):
        url = "https://twitter.com/{}".format(username)
        # print(url)
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        try:
            user_id = soup.find("script", {"data-testid": "UserProfileSchema-test"})
            data = json.loads(user_id.string)
            # driver.quit()
            return {
                "data": data["author"]["identifier"],
                "message": f"Numerical id found for username {username}",
            }
        except:
            return {
                "data": None,
                "message": f"Numerical id not found for username {username}",
            }

    def idtouname(self, numid):
        url = "https://twitter.com/i/user/{}".format(numid)
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        try:
            user_id = soup.find("script", {"data-testid": "UserProfileSchema-test"})
            data = json.loads(user_id.string)
            # driver.quit()
            return {
                "data": data["author"]["additionalName"],
                "message": f"Username found for numerical id {numid}",
            }
        except:
            return {
                "data": None,
                "message": f"Username not found for numerical id {numid}",
            }
