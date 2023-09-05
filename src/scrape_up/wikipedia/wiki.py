from bs4 import BeautifulSoup
import requests
import re


class Wiki:
    """
    Create an object of the 'Wiki' class:

    ```python
    Scraper = Wiki(query)
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
        Uses regex and BeautifulSoup to get the definition of the query from Wikipedia 
        Returns the definition of the query from Wikipedia, as string
        """

        try:
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
                    
        except Exception as e:
            print(f".define() failed : {e}")
            return None

if __name__ == "__main__":
    # test
    import os
    import time
    
    test_queries = ["dog", "graph theory", "stanford", "computer science", 
                    "machine learning", "artificial intelligence", "data science",
                     "data structure", "programming language", "computer", "computer network", 
                     "computer security", "computer graphics", "computer vision", 
                     "computer architecture", "computer engineering", "computer hardware",
                       "computer software", "computer programming", "computer data storage", 
                       "computer memory", "computer performance", "computer science", "computer scientist",
                         "computer programming", "computer programmer", "computer keyboard", "computer mouse",
                           "computer monitor", "computer terminal", "computer network", "computer security", 
                           "computer graphics", "computer vision", "computer architecture", "computer engineering", 
                           "computer hardware", "computer software", "computer programming", "computer data storage",
                             "computer memory", "computer performance", "computer science", "computer scientist", 
                             "computer programming", "computer programmer", "computer keyboard", "computer mouse", "computer monitor", "computer terminal"]

    for query in test_queries:
        if os.name == "posix":
            os.system("clear")
        if os.name == "nt":
            os.system("cls")

        wiki = Wiki(query)
        print(f"{query} : {wiki.define()}")
        time.sleep(3)
        # The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the wolf
        # In mathematics, graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects
        # Stanford University (officially Leland Stanford Junior University) is a private research university in Stanford, California
        # . . . 
