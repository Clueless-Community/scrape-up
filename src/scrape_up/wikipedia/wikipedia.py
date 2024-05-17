from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


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

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def scrape(self, query: str):
        try:
            URL = f"https://en.wikipedia.org/wiki/{query}"
            response = get(URL, self.config)
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
