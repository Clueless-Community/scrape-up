import requests
from bs4 import BeautifulSoup


# Function to scrape BBC News headlines
def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = []

    # Find all headline elements
    headline_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')

    # Extract the headlines
    for headline_element in headline_elements:
        headline = headline_element.text.strip()
        headlines.append(headline)

    return headlines


# Main function
if __name__ == "__main__":
    # Scrape headlines
    news_headlines = scrape_bbc_news()

    # Print headlines and avoid repeated ones with indexing
    seen_headlines = set()
    for i, headline in enumerate(news_headlines, start=1):
        if headline not in seen_headlines:
            print(f"{i}. {headline}")
            seen_headlines.add(headline)

