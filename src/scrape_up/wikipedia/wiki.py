from bs4 import BeautifulSoup
import requests
import re


class WikipediaScraper:
    """
    Create an object of the 'WikipediaScrapper' class:

    ```python
    Scraper = WikipediaScraper()
    ```

    | Methods            | Details                                                                          |
    | -----------------  | -------------------------------------------------------                          |
    | `.__scrape(query)` | private method to scrape the data from wikipedia, Returns a BeautifulSoup object |
    | `.define()`        | Returns the definition of the query from Wikipedia as string                     |

    """

    def __init__(self, query):
        self.query = query
        self.soup = self.__scrape(query)

    def __scrape(self, query):
        """ 
        private method to scrape the data from wikipedia, returns a BeautifulSoup object
        """

        URL = f"https://en.wikipedia.org/wiki/{query}"

        try:
            response = requests.get(URL)
            soup = BeautifulSoup(response.text, "html.parser")

            return soup
        except Exception as e:
            print(f"Error: {e}")
            return None

    def define(self):
        """
        Returns the definition of the query from Wikipedia
        """

        div = self.soup.find(id="mw-content-text")

        # get the first p that is not empty
        paragraphs = div.find_all("p")
        for p in paragraphs:
            if p.text and p.text != "\n":
                # remove the reference numbers in square brackets and numbers whitin square brackets
                definition = p.text
                definition = re.sub(r'\[[0-9]*\]', '', definition)
        
                definition = definition.split(".")[0]
                
                return definition

        try:
            # get first p
            definition = self.soup.find("p").text

            return definition

        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    dog_wiki = WikipediaScraper("dog")
    dog_wiki = WikipediaScraper("graph theory")

    print(dog_wiki.define())
