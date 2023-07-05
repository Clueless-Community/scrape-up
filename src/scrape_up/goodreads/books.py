from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from time import sleep
import json





class BookScraper:
    """
    
    """
    search_url = "https://www.goodreads.com/search?utf8=%E2%9C%93&query={}"
    autocomplete_url = "https://www.goodreads.com/book/auto_complete?format=json&q={}"
    book_url = "https://www.goodreads.com/book/show/{}"
    # headers = {
    #     "Connection": "keep-alive",
    #     "Cache-Control": "max-age=0",
    #     "DNT": "1",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    #     "Sec-Fetch-User": "?1",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Sec-Fetch-Site": "none",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    # }
    # to handle html requests
    fetcher = requests.Session()
    # fetcher.headers.update(headers)

    # adding all options for chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-logging")

    def __init__(self,book_title="",author="",book_id=None):
        # searching for book based on given parameters
        if book_id:
            self.book_id = book_id
            self.book_url = self.book_url.format(str(book_id))
            if self.is_valid_id():
                self.book_title = self.get_title()
        else:
            if book_title == "" or author == "":
                raise Exception("Please provide book_id or book_title and author argument.")
            try:
                book_found = False
                books_data = self.fetcher.get(
                    self.autocomplete_url.format(book_title)
                    ).json()
                for i in books_data:
                    if i["author"]["name"].lower() == author.lower().strip():
                        if (
                            i["bookTitleBare"].lower() == book_title.lower().strip()
                            ):
                            self.book_id = i["bookId"]
                            self.book_url = self.book_url.format(i["bookId"])
                            self.book_title = i["bookTitleBare"]
                            self.author = i["author"]["name"]
                            book_found = True
                if not book_found:
                    raise Exception("Book not found. Please check your book_name and author")
                self.book_soup = self.get_soup()
                
            except requests.exceptions.ConnectionError:
                raise Exception("Connection error, Please try again.")
    
    def get_soup(self):
        """
        Using selenium to get page source after executing javascript
        """
        driver = webdriver.Chrome(
                service=Service(r".\Drivers\.wdm\drivers\chromedriver\win32\114.0.5735.90\chromedriver.exe"),
                options=self.chrome_options
            )
        driver.get(
            self.book_url
        )

        element = driver.find_element("xpath","/html/body/div[1]/div[2]/main/div[1]/div[2]/div[1]/div[2]/div[6]/div/div/button/span[1]")
        driver.execute_script("arguments[0].click();", element)

        book_html = driver.page_source
        driver.quit()
        return BeautifulSoup(book_html,"html.parser")

    def is_valid_id(self):
        self.book_soup = self.get_soup()
        error_div = self.book_soup.find("div",class_="ErrorPage__title")
        if error_div:
            return False
        else:
            return True

    def get_title(self):
            self.book_title = self.book_soup.find("h1",class_="Text__title1").text
            return self.book_title

    def get_author(self):
        self.author = self.book_soup.find("span",class_="ContributorLink__name").text
        return self.author

    def get_description(self):
        self.description = self.book_soup.find("span",class_="Formatted").text
        return self.description
    
    def get_genres(self):
        self.genres =list( map(lambda x:x.text,
            self.book_soup
            .find("div",class_="BookPageMetadataSection__genres")
            .find_all("span",class_="Button__labelItem")
            ))[:-1]
        return self.genres

    




    
if __name__=="__main__":
    hp = BookScraper(book_title="harry potter and the prisoner of azkaban ",author="J.K. Rowling")
    print(hp.get_title())