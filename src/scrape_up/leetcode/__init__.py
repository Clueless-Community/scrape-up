from leetcode_scraper import LeetCodeScraper

# Create an instance of the LeetCodeScraper
scraper = LeetCodeScraper()

# Scrape the rank of a user
username = "example_user"
rank_data = scraper.scrape_rank(username)
print(rank_data)

# Scrape the rating of a user
rating_data = scraper.scrape_rating(username)
print(rating_data)