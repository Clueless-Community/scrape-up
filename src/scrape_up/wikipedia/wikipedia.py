from bs4 import BeautifulSoup
import requests


class WikipediaScraper:
    """
    Create an object of the 'WikipediaScrapper' class:

    ```python
    Scraper = WikipediaScraper()
    ```

    | Methods           | Details                                                 |
    | ----------------- | ------------------------------------------------------- |
    | `.scrape(url)`    | Returns the Scraped Data from Wikipedia                 |
    | `.get_featured()` | Returns the featured article for the day from Wikipedia |
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

        try:
            # get first p
            definition = self.soup.find("p").text

            return definition

        except Exception as e:
            print(f"Error: {e}")
            return None

    # def scrape(self, query):
    #     try:
    #         URL = f"https://en.wikipedia.org/wiki/{query}"
    #         response = requests.get(URL)
    #         soup = BeautifulSoup(response.text, "html.parser")

    #         # Extract the title
    #         title = soup.find(id="firstHeading").text

    #         # Extract all the headings and their content
    #         sections = soup.find_all("h2")
    #         data = {}
    #         for section in sections:
    #             heading = section.find("span", class_="mw-headline")
    #             if heading:
    #                 content = []
    #                 next_node = section.find_next_sibling(
    #                     ["h2", "h3", "h4", "h5", "h6"]
    #                 )
    #                 while next_node and next_node.name != "h2":
    #                     if next_node.name in ["h3", "h4", "h5", "h6"]:
    #                         content.append({"heading": next_node.text.strip()})
    #                     elif next_node.name == "p":
    #                         content.append({"text": next_node.text.strip()})
    #                     next_node = next_node.find_next_sibling(
    #                         ["h2", "h3", "h4", "h5", "h6", "p"]
    #                     )
    #                 data[heading.text] = content

    #         # Return the data as JSON
    #         result = {"title": title, "sections": data}
    #         return result
    #     except:
    #         return None

    # def get_featured(self):
    #     """
    #     Get the featured data from the main page of Wikipedia.

    #     Returns:
    #     A string containing the featured data from the main page of Wikipedia.
    #     """
    #     try:
    #         url = "https://en.wikipedia.org/wiki/Main_Page"
    #         html_text = requests.get(url).text
    #         soup = BeautifulSoup(html_text, "lxml")

    #         container = soup.find("div", {"id": "mp-left"})
    #         data = container.find("p").text
    #         return data
    #     except:
    #         return None

if __name__ == "__main__":
    dog_wiki = WikipediaScraper("dog")

    print(dog_wiki.define())
