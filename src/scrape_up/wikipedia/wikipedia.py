from bs4 import BeautifulSoup
import requests

class WikipediaScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title
        title = soup.find(id='firstHeading').text
        print('Title:', title)

        # Extract the introduction paragraph
        intro = soup.find('p').text
        print('Introduction:', intro)

        # Extract all the headings and their content
        sections = soup.find_all('h2')
        print('Headings:')
        for section in sections:
            heading = section.find('span', class_='mw-headline')
            if heading:
                print('-', heading.text)
                content = []
                next_node = section.find_next_sibling(['h2', 'h3', 'h4', 'h5', 'h6'])
                while next_node and next_node.name != 'h2':
                    if next_node.name in ['h3', 'h4', 'h5', 'h6']:
                        content.append('\n' + next_node.text.strip() + '\n')
                    elif next_node.name == 'p':
                        content.append(next_node.text.strip())
                    next_node = next_node.find_next_sibling(['h2', 'h3', 'h4', 'h5', 'h6', 'p'])
                print('Content:', '\n'.join(content))

        # Extract all the links
        links = soup.find_all('a')
        print('Links:')
        for link in links:
            href = link.get('href')
            if href and href.startswith('/wiki/'):
                print('-', link.text, '->', 'https://en.wikipedia.org' + href)

        # Extract references
        references = soup.find_all('cite', class_='citation')
        print('References:')
        for reference in references:
            print('-', reference.text.strip())

# Example usage
url = 'https://en.wikipedia.org/wiki/Web_scraping'
scraper = WikipediaScraper(url)
scraper.scrape()
