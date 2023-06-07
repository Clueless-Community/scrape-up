from scrape_up.twitter.numidconverter import TwitterScraper

twitter_scraper = TwitterScraper()

numid = "44196397"
username = twitter_scraper.idtouname(numid)
print(username)

username = "elonmusk"
user_id = twitter_scraper.unametoid(username)
print(user_id)
