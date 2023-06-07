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
    # Parse the HTML content using BeautifulSoup and extract the desired data
    # Use the BeautifulSoup library

def scrape_youtube(url):
    # Main scraping function that combines the fetching and parsing logic
    html_content = fetch_html(url)
    data = parse_html(html_content)
    return data

# Example usage
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
scraped_data = scrape_youtube(video_url)
print(scraped_data)
