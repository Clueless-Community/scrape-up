import requests
from bs4 import BeautifulSoup


class BBCNews:
    """
    First create an object of class `BBCNews`\n
    ```python
    scraper = BBCNews()
    ```
    | Methods        | Details                                             |
    | -------------- | --------------------------------------------------- |
    | `.get_headlines()` | Returns a list of objects containing the headlines          |
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
