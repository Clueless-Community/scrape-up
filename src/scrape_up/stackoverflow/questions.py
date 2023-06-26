from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup


class StackOverflowScraper:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920,1080")

    def scrape_stack_overflow(self, keyword):
        url = f"https://stackoverflow.com/search?q={keyword}&tab=votes"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        driver.get(url)

        sleep(2)  # Give the page time to load (you can adjust the delay as needed)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        questions = soup.select(".s-post-summary")
        
        # print(questions)
        for question in questions:
            que_content = question.select_one(".s-post-summary--content")
            que_stats = question.select_one(".s-post-summary--stats")


            title = que_content.select_one(".s-post-summary--content-title").find("a").attrs.get("href")
            description = que_content.select_one(".s-post-summary--content-title").find("a").getText()

            stats_content = que_stats.select(".s-post-summary--stats-item")
            votes =  stats_content[0].findChild(attrs={"class":"s-post-summary--stats-item-number"}).getText()
            # answers =  stats_content[1].findChild(attrs={"class":"s-post-summary--stats-item-number"}).getText()
            try:
                answers =  stats_content[1].findChild(attrs={"class":"s-post-summary--stats-item-number"}).getText()
            except (AttributeError, IndexError):
                answers = "N/A"

            print(f"Title: {title}")
            print(f"Votes: {votes}")
            print(f"No of Answers: {answers}")
            print(f"Question Description: {description}")
            print("----")

        driver.quit()


# Create an instance of the StackOverflowScraper class
scraper = StackOverflowScraper()

# Take a keyword as input from the user
keyword = input("Enter a keyword to search for questions on Stack Overflow: ")

# Call the scrape_stack_overflow method to start scraping Stack Overflow
scraper.scrape_stack_overflow(keyword)
