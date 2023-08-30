import requests
from bs4 import BeautifulSoup
USER_AGENT = "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"

class BBCNews:
    """
    First create an object of class `BBCNews`\n
    ```python
    scraper = BBCNews()
    ```
    | Methods            | Details                                                  |
    | ------------------ | -------------------------------------------------------- |
    | `.get_headlines()` | Returns the list of object containig the headlines       |
    | `get_article()`    | Returns an object with proper details about the articles |
    """

    def __init__(self):
        self.base_url = "https://www.bbc.co.uk"
        self.headlines_url = self.base_url + "/news"

    def get_headlines(self):
        """
        Fetches the latest headlines from BBC News website.\n
        Returns:
        A list of dictionaries, each containing the index and headline text.
        Example: [{'index': 1, 'headline': 'Headline 1'}, {'index': 2, 'headline': 'Headline 2'}, ...]
        """
        try:
            response = requests.get(self.headlines_url)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        except requests.RequestException as e:
            print(f"Error fetching headlines: {e}")
            return []

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

    def get_article(self, url):
        """
        Create an instance of the class - `BBCNews`\n
        ```python
        scraper = BBCNews()
        article = scraper.get_article()
        print(article)
        ```
        """
        try:
            headers = {
                "User-Agent": USER_AGENT
            }
            response = requests.get(url, headers=headers).text
            soup = BeautifulSoup(response, "lxml")

            main_heading = soup.find("h1", {"id": "main-heading"}).text.strip()
            time = soup.find("time").text.strip()
            text_content = soup.find_all("div", {"data-component": "text-block"})
            Text = ""
            for text in text_content:
                Text += text.text.strip() + " "
            data = {"main_heading": main_heading, "time": time, "text": Text}
            return data
        except:
            return None
