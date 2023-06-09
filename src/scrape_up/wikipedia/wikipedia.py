from bs4 import BeautifulSoup
import requests
import json

class WikipediaScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title
        title = soup.find(id='firstHeading').text

        # Extract all the headings and their content
        sections = soup.find_all('h2')
        data = {}
        for section in sections:
            heading = section.find('span', class_='mw-headline')
            if heading:
                content = []
                next_node = section.find_next_sibling(['h2', 'h3', 'h4', 'h5', 'h6'])
                while next_node and next_node.name != 'h2':
                    if next_node.name in ['h3', 'h4', 'h5', 'h6']:
                        content.append({'heading': next_node.text.strip()})
                    elif next_node.name == 'p':
                        content.append({'text': next_node.text.strip()})
                    next_node = next_node.find_next_sibling(['h2', 'h3', 'h4', 'h5', 'h6', 'p'])
                data[heading.text] = content

        # Return the data as JSON
        result = {
            'title': title,
            'sections': data
        }
        return json.dumps(result, indent=4)
