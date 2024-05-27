```python
from scrape_up import leetcode
```

### Scrape user details

First, create an object of class `LeetCodeScraper`

```python
leetcode_scraper = LeetCodeScraper(username="nikhil25803")
```

**User Specific Methods - Require Username**

| Methods                       | Details                                                               |
| ----------------------------- | --------------------------------------------------------------------- |
| `.scrape_rank()`              | Used to scrape the rank of a user on LeetCode.                        |
| `.scrape_rating()`            | Used to scrape the rating of a user on LeetCode.                      |
| `.get_problems_solved()`      | Used to scrape total problems solved by a user on LeetCode.           |
| `.get_solved_by_difficulty()` | Used to scrape difficulty wise problems solved by a user on LeetCode. |
| `.get_github_link()`          | Used to scrape github link of a user on LeetCode.                     |
| `.get_linkedin_link()`        | Used to scrape linkedin link of a user on LeetCode.                   |
| `.get_community_stats()`      | Used to scrape community stats of a user on LeetCode.                 |

**General Purpose Methods - Does not Require Username**

| Methods                                            | Details                                                                                                                                                                                                      |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `.get_problems(difficulty, tags_list, search_key)` | Used to scrape top problems of LeetCode based on filters. Difficulty is string from ("easy", "medium", "hard"). Tags_list is list of tags. Search_key is string to search. All ther parameters are optional. |
| `.get_contests()`                                  | Used to scrape the upcoming LeetCode Contests details.                                                                                                                                                       |
| `.get_daily_challenge()`                           | Used to scrape LeetCode Daily Challenge details.                                                                                                                                                             |
