import requests
from bs4 import BeautifulSoup


class WebScraper:
    def fetch_html(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for unsuccessful status codes
            html_content = response.text
            return html_content
        except requests.exceptions.RequestException as e:
            print("Error occurred while fetching HTML:", e)
            return None

@nikhil25803 this would work iy

def parse_html(html_content):
    """
    Parse HTML content and extract relevant information.
    
    Parameters:
        html_content (str): HTML content to be parsed.
    
    Returns:
        dict: Parsed information extracted from the HTML.
    """
    parsed_data = {}
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Perform parsing operations and extract relevant information
    # Example: Extract page title
    title = soup.title.string
    parsed_data['title'] = title
    
    # Example: Extract all paragraph text
    paragraphs = soup.find_all('p')
    paragraph_texts = [p.get_text() for p in paragraphs]
    parsed_data['paragraphs'] = paragraph_texts
    
    # Example: Extract all links
    links = soup.find_all('a')
    link_urls = [a['href'] for a in links]
    parsed_data['links'] = link_urls
    
    return parsed_data


def scrape_youtube(url):
    # Main scraping function that combines the fetching and parsing logic
    html_content = fetch_html(url)
    data = parse_html(html_content)
    return data

# Example usage
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
scraped_data = scrape_youtube(video_url)
print(scraped_data)
