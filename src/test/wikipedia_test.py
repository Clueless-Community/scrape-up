from scrape_up.wikipedia.wikipedia import WikipediaScraper

url = 'https://en.wikipedia.org/wiki/Web_scraping'
scraper = WikipediaScraper(url)
scraper.scrape()
