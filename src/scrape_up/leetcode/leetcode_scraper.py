import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


class LeetCodeScraper:
    def __init__(self, username: str = ""):
        self.username = username
        self.user_profile = self.__scrape_user_profile()

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
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 100)

    def __scrape_user_profile(self):
        url = f"https://leetcode.com/{self.username}"
        data = requests.get(url)
        data.raise_for_status()
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def scrape_rank(self):
        if(self.username == ""):
            message = f"username is not given"
            return {
                "data": None,
                "message": message
            }

        soup = self.user_profile
        try:
            rank_element = soup.find(
                "span", {"class": "ttext-label-1 dark:text-dark-label-1 font-medium"}
            )
            rank = rank_element.text.strip() if rank_element else "Not Ranked"

            return {
                "data": rank,
                "message": f"Successfully scraped rank for user '{self.username}'",
            }
        except:
            return {
                "data": None,
                "message": f"Failed to scrape rank for user '{self.username}'",
            }

    def scrape_rating(self):
        if(self.username == ""):
            message = f"username is not given"
            return {
                "data": None,
                "message": message
            }

        soup = self.user_profile
        try:
            rating_element = soup.find(
                "div",
                {
                    "class": "text-label-1 dark:text-dark-label-1 flex items-center text-2xl"
                },
            )
            rating = rating_element.text.strip() if rating_element else "No Rating"

            return {
                "data": rating,
                "message": f"Successfully scraped rating for user '{self.username}'",
            }
        except:
            return {
                "data": None,
                "message": f"Failed to scrape rating for user '{self.username}'",
            }

    def get_problems_solved(self):
        if(self.username == ""):
            message = f"username is not given"
            return {
                "data": None,
                "message": message
            }

        soup = self.user_profile
        try:
            total_problems = soup.find(
                "div",
                {
                    "class": "text-[24px] font-medium text-label-1 dark:text-dark-label-1"
                },
            )
            return {
                "data": total_problems.text,
                "message": f"Found total problems solved for user '{self.username}'"
            }
        except:
            message = f"Failed to scrape total problems for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }

    def get_solved_by_difficulty(self):
        if(self.username == ""):
            message = f"username is not given"
            return {
                "data": None,
                "message": message
            }

        soup = self.user_profile
        try:
            difficulty_wise = soup.find_all(
                "span",
                {
                    "class": "mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1"
                },
            )

            solved = {
                'easy': difficulty_wise[0].text,
                'medium': difficulty_wise[1].text,
                'hard': difficulty_wise[2].text
            }

            return {
                "data": solved,
                "message": f"Found difficulty wise problems solved for user '{self.username}'"
            }
        except:
            message = f"Failed to scrape difficulty wise problems for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }

    def get_github_link(self):
        if(self.username == ""):
            message = f"username is not given"
            return message

        soup = self.user_profile
        try:
            links = soup.find_all(
                "a",
                {
                    "class": "hover:text-label-1 dark:hover:text-dark-label-1 cursor-pointer"
                },
            )

            for link in links:
                if('github' in link['href']):
                    return {
                        "data": link['href'],
                        "message": f"Found github link for user '{self.username}'"
                    }
            
            message = f"No github link found for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }
        except:
            message = f"Failed to scrape github link for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }

    def get_linkedin_link(self):
        if(self.username == ""):
            message = f"username is not given"
            return message

        soup = self.user_profile
        try:
            links = soup.find_all(
                "a",
                {
                    "class": "hover:text-label-1 dark:hover:text-dark-label-1 cursor-pointer"
                },
            )

            for link in links:
                if('linkedin' in link['href']):
                    return {
                        "data": link['href'],
                        "message": f"Found linkedin link for user '{self.username}'"
                    }
            
            message = f"No linkedin link found for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }
        except:
            message = f"Failed to scrape linkedin link for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }

    def get_community_stats(self):
        if(self.username == ""):
            message = f"username is not given"
            return message

        soup = self.user_profile
        try:
            stats = soup.find_all(
                "div", 
                {
                    "class": "flex items-center space-x-2 text-[14px]"
                },
            )

            stats = {
                'views': stats[0].find_all("div")[-1].text,
                'solution': stats[1].find_all("div")[-1].text,
                'discuss': stats[2].find_all("div")[-1].text,
                'reputation': stats[3].find_all("div")[-1].text
            }
            return {
                "data": stats,
                "message": f"Found stats for user '{self.username}'"
            }
        except:
            message = f"Failed to scrape community stats for user '{self.username}'"
            return {
                "data": None,
                "message": message
            }

    def get_problems(self, difficulty="", tags=[], search_key=""):
        url = "https://leetcode.com/problemset/all/?"

        if difficulty != "":
            url += "difficulty=" + difficulty.upper()

        if len(tags) > 0:
            url += "&topicSlugs=" + tags[0]

            for i in range(1, len(tags)):
                url += "%2C" + tags[i]

        if search_key != "":
            url += "&search=" + search_key

        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'space-x-1')))
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        try:
            problems = soup.find_all(
                "a", 
                {
                    "class": "h-5 hover:text-blue-s dark:hover:text-dark-blue-s"
                },
            )
            problems_premium = soup.find_all(
                "a", 
                {
                    "class": "h-5 hover:text-blue-s dark:hover:text-dark-blue-s opacity-60"
                },
            )
            problems.extend(problems_premium)

            problems_list = []

            for problem in problems:
                problem_title = problem.text
                problem_url = "https://leetcode.com" + problem['href']
                problems_list.append({
                    'title': problem_title,
                    'link': problem_url
                })
            
            return {
                "data": problems_list,
                "message": f"Found problems list"
            }
        except:
            message = f"Failed to scrape problems for given filters"
            return {
                "data": None,
                "message": message
            }

    def get_contests(self):
        url = "https://leetcode.com/contest/"
        data = requests.get(url)
        data.raise_for_status()
        soup = BeautifulSoup(data.text, "html.parser")

        try:
            contests = soup.find(
                "div", 
                {
                    "class": "swiper-wrapper"
                },
            ).find_all(
                "div",
                {
                    "class": "h-[54px]"
                }
            )

            contest_list = []
            for contest in contests:
                contest_list.append({
                    'title': contest.div.text,
                    'date': contest.text.replace(contest.div.text, "")
                })

            return {
                "data": contest_list,
                "message": f"Found contest list"
            }
        except:
            message = f"Failed to scrape contest details"
            return {
                "data": None,
                "message": message
            }

    def get_daily_challenge(self):
        try:
            problemset_url = "https://leetcode.com/problemset/all/"
            self.driver.get(problemset_url)
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'flex-0')))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            daily = soup.find(
                "a", 
                {
                    "class": "h-5 hover:text-blue-s dark:hover:text-dark-blue-s"
                },
            )
            daily_link = "https://leetcode.com" + daily['href']

            self.driver.get(daily_link)
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_1l1MA')))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            daily_challenge = {}
            daily_challenge['title'] = daily.text

            difficulty = soup.find("div", class_ = "rounded-[21px]").text
            daily_challenge['difficulty'] = difficulty

            p_tags = soup.find("div", class_ = "_1l1MA").find_all("p")
            pre_tags = soup.find("div", class_ = "_1l1MA").find_all("pre")

            i = 0
            description = ""
            while ("Example" not in p_tags[i].text):
                description += p_tags[i].text
                i += 1
            daily_challenge['description'] = description

            examples = []
            j = 0

            while ("Example" in p_tags[i].text):
                examples.append(pre_tags[j].text)
                i += 1
                j += 1
            daily_challenge['examples'] = examples

            constraints = soup.find(
                "div", 
                {
                    "class": "_1l1MA"
                },
            ).find("ul")
            daily_challenge['constraints'] = constraints.text

            return {
                "data": daily_challenge,
                "message": f"Found daily challenge problem"
            }
        except:
            message = f"Failed to scrape daily challenge"
            return {
                "data": None,
                "message": message
            }

# TEST
leetcodeScraper = LeetCodeScraper()
print("problems list: ", leetcodeScraper.get_problems(difficulty="medium", tags=["dynamic-programming"], search_key="palindrome"))
print("contests: ", leetcodeScraper.get_contests())
print("daily challenge: ", leetcodeScraper.get_daily_challenge())

leetcodeScraper = LeetCodeScraper(username="test")
print("rank: ", leetcodeScraper.scrape_rank())
print("rating: ", leetcodeScraper.scrape_rating())
print("total problems: ", leetcodeScraper.get_problems_solved())
print("difficulty wise problems: " ,leetcodeScraper.get_solved_by_difficulty())
print("github link: ", leetcodeScraper.get_github_link())
print("linkedin link: ", leetcodeScraper.get_linkedin_link())
print("community stats: ", leetcodeScraper.get_community_stats())