from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class User:
    def __init__(self, username: str):
        self.username = username

    def user_details(self):
        """
        user = User(username=" ")
        print(user.user_details())
        """
        try:
            driver.get(f"https://www.instagram.com/{self.username}/")
            wait = WebDriverWait(driver, 180)
            account_details = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//span[@class="_ac2a"]')
                )
            )
            return {
                "Number of Posts:": account_details[0].text,
                "Number of Followers:": account_details[1].text,
                "Number of Following:": account_details[2].text,
            }

        except Exception as e:
            message = f"{self.username} not found!"
            return {"data": None, "message": message}
        finally:
            driver.quit()
