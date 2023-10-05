import requests
import bs4

"""how2use:
from scrape_up.banner88x31.scraper88x31 import Scraper88x31

scraper = Scraper88x31()

# Call the get_all method on the instance
img_alt_list = scraper.get_all()
"""

class Scraper88x31:
    """
    First create an object of class `Scraper88x31`\n
    ```python
    scraper = Scraper88x31()
    ```
    | Methods            | Details                                                  |
    | ------------------ | -------------------------------------------------------- |
    | `get_all()`        | Returns the list of all available 88x31 banners          |
    """

    def __init__(self):
        self.urls_to_scrape = [
            'https://cyber.dabamos.de/88x31/index.html',
            'https://cyber.dabamos.de/88x31/index2.html',
            'https://cyber.dabamos.de/88x31/index3.html',
            'https://cyber.dabamos.de/88x31/index4.html',
            'https://cyber.dabamos.de/88x31/index5.html'
        ]

    def get_all(self):
        """
        Fetches all 88x31 banners
        Returns:
        Returns the list of all available 88x31 banners
        """
        img_alt = []
        for url in self.urls_to_scrape:
            try:
                response = requests.get(url)
                response.raise_for_status()
                source = response.content
                soup = bs4.BeautifulSoup(source, 'lxml')
                for img_tag in soup.find_all('img'):
                    img_alt.append("https://cyber.dabamos.de/88x31/" + img_tag.get('alt') + ".gif")
        return img_alt
