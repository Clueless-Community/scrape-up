from scrape_up.wikipedia.wikipedia import WikipediaScraper

url = 'https://en.wikipedia.org/wiki/Web_scraping'
scraper = WikipediaScraper(url)
scraped_data = scraper.scrape()
print(scraped_data)

