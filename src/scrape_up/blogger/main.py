import requests
from bs4 import BeautifulSoup

class Blogger:
    """
    Create an instance of `Blogger` class.
    """
    def __init__(self):
        pass

    def get_articles(self, topic: str):
        """
        Retrieve articles from Google Blogger for a given topic.
        """
        url = f"https://www.blogger.com/search?q={topic}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('div', class_='search-result')
            result = []
            for article in articles:
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                author = article.find('div', class_='byline').text.strip()
                result.append({'title': title, 'link': link})
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
