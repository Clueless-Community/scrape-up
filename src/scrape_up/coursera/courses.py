from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Coursera:
    def __init__(self, keyword, page_count):
        self.keyword = keyword
        self.page_count = page_count

    def __scrape_page(self):
        chromedriver_path = ""
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.coursera.org/search?query=" + self.keyword)
        return wait, driver

    def titles(self):
        """
        Class - `Courses`
        Example:
        ```
        topic = Courses("Machine Learning", 11)
        courses = topic.titles()
        ```
        Returns:
        {
            "data": titles,
            "message": f"Course Titles for {self.keyword}"
        }
        """
        wait, driver = self.__scrape_page()
        titles = []
        try:
            for i in range(self.page_count):
                courses = wait.until(
                    EC.visibility_of_all_elements_located(
                        (By.CSS_SELECTOR, "main ul>li")
                    )
                )
                titles.extend(
                    [
                        driver.execute_script(
                            'return arguments[0].querySelector("h3")?.innerText', course
                        )
                        for course in courses
                    ]
                )
                next_btn = driver.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Next Page"]'
                )
                if "disabled" in next_btn.get_attribute("class"):
                    break
                else:
                    next_btn.click()
            return {"data": titles, "message": f"Course Titles for {self.keyword}"}
        except:
            return {"data": None, "message": f"No courses found for {self.keyword}"}
