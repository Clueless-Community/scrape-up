from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


class Publication:
    def __init__(self, link):
        self.link = link

    def get_articles(self):
        """
        Class - `Publication`
        Example
        ```python
        publication = medium.Publication("https://towardsdatascience.com")
        articles = publication.get_articles()
        for article in articles:
            print(article) #For better readability/clarity
        ```
        Returns the articles of the publication which are arranged in the form of a list
        """
        try:
            articles = []
            link = self.link
            driver.get(link)
            scroll_pause = 0.5
            # Get scroll height
            last_height = driver.execute_script(
                "return document.documentElement.scrollHeight"
            )
            run_time, max_run_time = 0, 1
            while True:
                iteration_start = time.time()
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, 1000*document.documentElement.scrollHeight);"
                )

                # Wait to load page
                time.sleep(scroll_pause)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script(
                    "return document.documentElement.scrollHeight"
                )
                scrolled = new_height != last_height
                timed_out = run_time >= max_run_time
                if scrolled:
                    run_time = 0
                    last_height = new_height
                elif not scrolled and not timed_out:
                    run_time += time.time() - iteration_start
                elif not scrolled and timed_out:
                    break
            elements = driver.find_elements(By.XPATH, "//h2 | //h3")
            for x in elements:
                articles.append(x.text)
            return articles
        except:
            return "page/publication not found."


# publication = Publication("https://pub.towardsai.net")
# articles = publication.get_articles_list()
# for article in articles:
#     print(article)
