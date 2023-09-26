from bs4 import BeautifulSoup
import requests
import re


class Wiki:
    """
    Create an object of the 'WikipediaScrapper' class:

    ```python
    Scraper = WikipediaScraper()
    ```

    | Methods            | Details                                                                          |
    | -----------------  | ---------------------------------------------------------------------------------|
    | `.scrape(url)`     | Returns the Scraped Data from Wikipedia                                          |
    | `.get_featured()`  | Returns the featured article for the day from Wikipedia                          |
    | `.__scrape(query)` | private method to scrape the data from wikipedia, Returns a BeautifulSoup object |
    | `.define()`        | Returns the definition of the query from Wikipedia as string                     |

    """

    def __init__(self, query: str = ""):
        self.query = query

    def __scrape(self) -> BeautifulSoup:
        """ 
        private method to scrape the data from wikipedia, returns a BeautifulSoup object
        """

        URL = f"https://en.wikipedia.org/wiki/{self.query}"

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

        soup = self.__scrape()

        try:
            div = soup.find(id="mw-content-text")

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

    def scrape(self, query):
        try:
            URL = f"https://en.wikipedia.org/wiki/{query}"
            response = requests.get(URL)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract the title
            title = soup.find(id="firstHeading").text

            # Extract all the headings and their content
            sections = soup.find_all("h2")
            data = {}
            for section in sections:
                heading = section.find("span", class_="mw-headline")
                if heading:
                    content = []
                    next_node = section.find_next_sibling(
                        ["h2", "h3", "h4", "h5", "h6"]
                    )
                    while next_node and next_node.name != "h2":
                        if next_node.name in ["h3", "h4", "h5", "h6"]:
                            content.append({"heading": next_node.text.strip()})
                        elif next_node.name == "p":
                            content.append({"text": next_node.text.strip()})
                        next_node = next_node.find_next_sibling(
                            ["h2", "h3", "h4", "h5", "h6", "p"]
                        )
                    data[heading.text] = content

            # Return the data as JSON
            result = {"title": title, "sections": data}
            return result
        except:
            return None

    def get_featured(self):
        """
        Get the featured data from the main page of Wikipedia.

        Returns:
        A string containing the featured data from the main page of Wikipedia.
        """

        try:
            url = "https://en.wikipedia.org/wiki/Main_Page"
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, "lxml")

            container = soup.find("div", {"id": "mp-left"})
            data = container.find("p").text
            return data
        except:
            return None


if __name__ == "__main__":
    wiki = Wiki()
    print(f"public scraper returns the page in the proper format :\n\n {wiki.scrape('dog')}") 

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
