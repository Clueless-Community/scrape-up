import requests
from bs4 import BeautifulSoup


class BBCNews:
    """
    First create an object of class `User`\n
    ```python
    user = instagram.Users(username="nikhil25803")
    ```
    | Methods        | Details                                             |
    | -------------- | --------------------------------------------------- |
    | `.get_headlines()` | Returns the list of object containig the headlines          |
    """

    def __init__(self):
        self.base_url = "https://www.bbc.co.uk"
        self.headlines_url = self.base_url + "/news"

    def get_headlines(self):
        """
        Create an instance of the class - `BBCNews`\n
        ```python
        scraper = BBCNews()
        headlines = scraper.get_headlines()
        print(headlines)
        ```
        """
        response = requests.get(self.headlines_url)
        soup = BeautifulSoup(response.content, "html.parser")
        headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

        news_set = set()
        news_list = []
        index = 1

        for headline in headlines:
            news_text = headline.get_text(strip=True)
            if news_text not in news_set:
                news_set.add(news_text)
                news_list.append({"index": index, "headline": news_text})
                index += 1

        return news_list
