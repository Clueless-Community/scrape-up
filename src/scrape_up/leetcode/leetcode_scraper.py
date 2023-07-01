from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json


class LeetCodeScraper:
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

    def scrape_rank(self, username):
        url = f"https://leetcode.com/{username}"
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        try:
            rank_element = soup.find(
                "span", {"class": "ttext-label-1 dark:text-dark-label-1 font-medium"}
            )
            rank = rank_element.text.strip() if rank_element else "Not Ranked"

            return {
                "rank": rank,
                "message": f"Successfully scraped rank for user '{username}'",
            }
        except:
            return {
                "rank": None,
                "message": f"Failed to scrape rank for user '{username}'",
            }

    def scrape_rating(self, username):
        url = f"https://leetcode.com/{username}"
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        try:
            rating_element = soup.find(
                "span",
                {
                    "class": "text-label-1 dark:text-dark-label-1 flex items-center text-2xl"
                },
            )
            rating = rating_element.text.strip() if rating_element else "No Rating"

            return {
                "rating": rating,
                "message": f"Successfully scraped rating for user '{username}'",
            }
        except:
            return {
                "rating": None,
                "message": f"Failed to scrape rating for user '{username}'",
            }

    def scrape_solved_count(self, username):
        url = f"https://leetcode.com/{username}"
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        try:
            solved_element = soup.find(
                "div", {"data-cy": "header__side__progress__solved-question-count"}
            )
            solved_count = solved_element.text.strip() if solved_element else "Unknown"

            return {
                "solved_count": solved_count,
                "message": f"Successfully scraped solved count for user '{username}'",
            }
        except:
            return {
                "solved_count": None,
                "message": f"Failed to scrape solved count for user '{username}'",
            }

    def scrape_submissions_count(self, username):
        url = f"https://leetcode.com/{username}"
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        try:
            submissions_element = soup.find(
                "div",
                {"data-cy": "header__side__progress__total-submission-count"},
            )
            submissions_count = (
                submissions_element.text.strip() if submissions_element else "Unknown"
            )

            return {
                "submissions_count": submissions_count,
                "message": f"Successfully scraped submissions count for user '{username}'",
            }
        except:
            return {
                "submissions_count": None,
                "message": f"Failed to scrape submissions count for user '{username}'",
            }