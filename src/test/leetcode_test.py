from scrape_up.leetcode.leetcode_scraper import LeetCodeScraper

leetcodeScraper = LeetCodeScraper()
print("problems list: ", leetcodeScraper.get_problems(difficulty="medium", tags=["dynamic-programming"], search_key="palindrome"))
print("contests: ", leetcodeScraper.get_contests())
print("daily challenge: ", leetcodeScraper.get_daily_challenge())

leetcodeScraper = LeetCodeScraper(username="test")
print("rank: ", leetcodeScraper.scrape_rank())
print("rating: ", leetcodeScraper.scrape_rating())
print("total problems: ", leetcodeScraper.get_problems_solved())
print("difficulty wise problems: " ,leetcodeScraper.get_solved_by_difficulty())
print("github link: ", leetcodeScraper.get_github_link())
print("linkedin link: ", leetcodeScraper.get_linkedin_link())
print("community stats: ", leetcodeScraper.get_community_stats())