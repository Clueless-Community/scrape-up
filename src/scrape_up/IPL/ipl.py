import requests

# Replace 'YOUR_API_KEY' with your actual NewsAPI.org API key
API_KEY = 'YOUR_API_KEY'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
IPL_QUERY = 'IPL'
NEWS_API_PARAMS = {
    'q': IPL_QUERY,
    'language': 'en',
    'apiKey': API_KEY
}

def fetch_ipl_news():
    try:
        response = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
        response.raise_for_status()
        news_data = response.json()
        return news_data['articles']
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching IPL news: {e}")
        return None

def display_ipl_news(news_articles):
    if news_articles is None:
        return

    print("\nLatest IPL News Headlines:")
    print("=" * 30)
    for idx, article in enumerate(news_articles, start=1):
        title = article['title']
        source = article['source']['name']
        print(f"{idx}. {title} [{source}]")
    print("=" * 30)

if __name__ == "__main__":
    ipl_news = fetch_ipl_news()
    display_ipl_news(ipl_news)
