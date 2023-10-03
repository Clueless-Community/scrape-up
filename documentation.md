# Documentation

## Package Installation

```PowerShell
pip install scrape-up
```

## Examples

### Scrape the numbers of followers on GitHub

```python
# Import the required module
from scrape_up import github

# Instantiate an object with the username provided.
user = github.Users(username="nikhil25803")

# Call the followers function - it will return the number of followers
per user.followers()
```

---

## The platforms we cover.

- [GitHub](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#github)
- [GitHub Education](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#github-education)
- [Codechef](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#codechef)
- [Hacker News](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#hacker-news)
- [HackerEarth](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#hackerearth)
- [HackerRank](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#hackerrank)
- [Hashnode](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#hashnode)
- [ICC Rankings](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#icc-rankings)
- [Academia](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#academia)
- [BBC News](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#bbc-news)
- [Coin Market Cap](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#coinmarketcap)
- [Covid Info](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#covidinfo)
- [Cricbuzz](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#cricbuzz)
- [Dribbble](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#dribbble)
- [Ebay](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#ebay)
- [Flipkart](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#flipkart)
- [Flyrobu](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md#flyrobu)

### GitHub

```python
from scrape_up import github
```

### Scrape User details

Create an instance of the class `Users`.

```python
user = github.Users(username="nikhil25803")
```

| Methods                       | Details                                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------- |
| `.followers()`                | Returns the number of followers of a user.                                                         |
| `.following()`                | Returns the number of following of a user.                                                         |
| `.get_avatar()`               | Returns the avatar URL of a user.                                                                  |
| `.get_bio()`                  | Returns the bio of a user.                                                                         |
| `.get_repo()`                 | Returns the list of pinned repositories for a user.                                                |
| `.repo_count()`               | Returns the number of Repositories of a user.                                                      |
| `.star_count()`               | Returns the number of stars of a user.                                                             |
| `.get_yearly_contributions()` | Returns the number of contributions made in 365 days frame.                                        |
| `.get_repositories()`         | Returns the list of repositories of a user.                                                        |
| `.get_starred_repos()`        | Return the list of starred repositories of a user.                                                 |
| `.pul_requests()`             | Return the number of pull requests opened in a repository.                                         |
| `.get_followers()`            | Returns the list of followers of a user.                                                           |
| `.get_following_users()`      | Returns the list of users followed by a user.                                                      |
| `.get_achievements()`         | Returns the list of achievements of a user.                                                        |
| `.get_status()`               | Returns the status of a user.                                                                      |
| `.get_contribution_streak()`  | Returns the maximum contribution streak of a user in the past year starting from the current date. |
| `.get_repository_details()`   | Returns the list of repositories with their details.                                               |
| `.get_branch()`               | Returns the list of branches in a repository.                                                      |
| `.get_merged_pull_requests()` | Returns the list of merged pull requests                                                           |
| `.get_open_issues()`          | Returns the list of open issues                                                                    |
| `.get_years_active()`         | Returns the number of years that user have been active on github.                                  |

### Scrape Repository details

Create an instance of the class `Repository`.

```python
repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
```

| Methods                    | Details                                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.fork_count()`            | Returns the number of forks of a repository.                                                                                                                   |
| `.get_contributors()`      | Returns the number of contributors of a repository.                                                                                                            |
| `.topics()`                | Returns the topics of a repository.                                                                                                                            |
| `.pull_requests()`         | Returns the number of pull requests opened in a repository.                                                                                                    |
| `.last_updated_at()`       | Returns the last updated date of a repository.                                                                                                                 |
| `.tags()`                  | Returns the last ten tags of a repository.                                                                                                                     |
| `.releases()`              | Returns the last ten releases of a repository.                                                                                                                 |
| `.issues_count()`          | Returns number of issues in a repository                                                                                                                       |
| `.readme`                  | Saves the readme.md file of the given user to the current working directory. To view the readme.md with a live server, change ".md" to ".html" in "readme.md". |
| `.get_pull_requests_ids()` | Returns all ids of opened pull requests in a repository.                                                                                                       |
| `.get_issues()`            | Returns the list of all open issues in a repository.                                                                                                           |
| `.commits()`               | Returns the number of commits in a repository.                                                                                                                 |
| `.get_readme()`            | Returns & saves README.md file of the special repository (if exists)                                                                                           |
| `.get_environment()`       | Returns the latest deployed link of a repository (if exists).                                                                                                  |
| `.watch_count()`           | Returns the number of watchers of a repository                                                                                                                 |
| `.all_watchers()`          | Returns the username of all watches of a repository                                                                                                            |

### Scrape details of an issue

Create an instance of the class `Issue`

```python
repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
```

| Methods           | Details                                                                            |
| ----------------- | ---------------------------------------------------------------------------------- |
| `.assignees()`    | Returns the assignees of an issue.                                                 |
| `.labels()`       | Returns the labels of an issue.                                                    |
| `.opened_by()`    | Returns the name of the user, who opened the issue.                                |
| `.title()`        | Returns the title of an issue.                                                     |
| `.is_milestone()` | Returns the milestone, if the issue is part of one or 'No milestone', if it's not. |
| `.opened_at()`    | Returns a string containing the time when the issue was opened in ISO format.      |

### Scrape a pull request details

Create an instance of the class `PullRequest`

```python
pull_request = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
```

| Methods            | Details                                                                    |
| ------------------ | -------------------------------------------------------------------------- |
| `.commits()`       | Returns the number of commits made in a pull request.                      |
| `.title()`         | Returns the title of a pull request.                                       |
| `.labels()`        | Returns all the labels of a pull request, empty list in case of no labels. |
| `.files_changed()` | Returns the number of files changed in a pull request.                     |
| `.reviewers()`     | Return the list of reviewers assigned in a pull request.                   |

### Scrape the details of an organization

Create an instance of class `Organization`

```python
organization = github.Organization(organization_name="Clueless-Community")
```

| Methods                     | Details                                                         |
| --------------------------- | --------------------------------------------------------------- |
| `.top_topics()`             | Returns a list of the most used topics in an organization.      |
| `.followers()`              | Returns the number of followers of an organization.             |
| `.top_languages()`          | Returns the top languages used in an organization.              |
| `.followers()`              | Returns the number of followers of an organization.             |
| `.avatar()`                 | Returns the avatar URL of an organization.                      |
| `.repositories()`           | Returns the list of repositories of an organization.            |
| `.people()`                 | Returns the list of people in an organization.                  |
| `.peoples() `               | Returns the number of people in an organization.                |
| `.get_location() `          | Returns the location of an organization.                        |
| `.repository_details()`     | Returns the list of repositories with their details.            |
| `.pinned_repository()`      | Returns the list of pinned repositories with their details.     |
| `.get_organization_links()` | Returns a dictionary of important website links of a community. |

---

### GitHub Education

```python
from scrape_up import github_education
```

### Scrape user details

Create an instance of the `Events` class.

```py
events = github_education.Events()
```

| Methods         | Details                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| `.get_events()` | Returns the latest events along with their title, image_url, description, date, location, language, tags, and link. |

---

### CodeChef

```python
from scrape_up import codechef
```

### Scrape user details

Create an object of class `Codechef`

```python
user1 = codechef.User(id="username")

```

| Methods         | Details                                                          |
| --------------- | ---------------------------------------------------------------- |
| `get_profile()` | Returns name, username, profile_image_link, rating, details etc. |

---

### Hacker News

```py
from scrape_up import hackernews
```

### Scrape article details

Create an instance of the `Articles` class.

```py
articles = hackernews.Articles()
```

| Methods            | Details                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| `.articles_list()` | Returns the latest articles along with their score, author, author URL, time, comment count, and link.     |
| `.new_articles()`  | Returns the latest new articles along with their score, author, author URL, time, comment count, and link. |
| `.past_articles()` | Returns the past articles along with their score, author, author URL, time, comment count, and link.       |
| `.ask_articles()`  | Returns the asked articles along with their score, author, author URL, time, comment count, and link.      |
| `.show_articles()` | Returns the show articles along with their score, author, author URL, time, comment count, and link.       |
| `.jobs()`          | Returns the jobs along with their time and link.                                                           |

---

### HackerEarth

```py
from scrape_up import hackerearth
```

Create an object of class `Challanges`

```python
hackerearth = hackerearth.Challanges()
```

| Methods          | Details                                                |
| ---------------- | ------------------------------------------------------ |
| `get_upcoming()` | Get the details of upcoming challenges on Hackerearth. |
| `get_ongoing()`  | Get the details of ongoing challenges on Hackerearth.  |
| `get_hiring()`   | Get the details of hiring challenges on Hackerearth.   |

---

### HackerRank

```py
from scrape_up import hackerrank
```

### Scrape user details

Create an object of class `User`.

```python
hackerank = hackerrank.User()
```

| Methods                      | Details                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| `get_profile(id="username")` | Returns name, username, country, user_type, details, badges, verified_skills, social etc. |
| `get_skills()`               | Returns a list of verified skills and their links                                         |

### Scrape contest details

Create an object of class `Contest`.

```python
hackerank = hackerrank.Contest()
```

| Methods               | Details                                                             |
| --------------------- | ------------------------------------------------------------------- |
| `active_contests()`   | Returns information on active contests like title, status, and link |
| `archived_contests()` | Returns information regarding archived contests                     |

---

### Hashnode

```py
from scrape_up import hashnode
```

Create an instance of `Hashnode` class.

```python
blogs = hashnode.Hashnode()
```

| Methods           | Details                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| `.get_feed()`     | Returns the blogs with title, descriptions, author, read time, like and comment count, date and link  |
| `.get_featured()` | Returns the featured blogs with title, descriptions, author, like and comment count, date and link    |
| `.get_recent()`   | Returns the recent blogs with title, descriptions, author, like and comment count, date and link      |
| `.search(topic)`  | Returns the blogs with title, descriptions, author, like and comment count, date and link for a topic |

---

### ICC Rankings

```py
from scrape_up import icc
```

Create an instance of `ICC` class.

```python
scraper = icc.ICC()
```

| Method                               | Details                                                             |
| ------------------------------------ | ------------------------------------------------------------------- |
| `.team_rankings(format)`             | Returns the list of rankings of teams of the desired format         |
| `.player_ranking(type,format)`       | Returns the list of player ranking of desired type and format       |
| `.team_rankings_women(format)`       | Returns the list of rankings of teams of the desired format         |
| `.player_ranking_women(type,format)` | Returns the list of women player ranking of desired type and format |

---

### Academia

```py
from scrape_up import academia
```

Create an instance of `Academia` class

```python
academia = academia.Academia()
```

| Method                        | Details                                                               |
| ----------------------------- | --------------------------------------------------------------------- |
| `get_research_topics(letter)` | Fetches and returns research topics starting with the given letter.   |
| `get_research_papers(search)` | Fetches and returns research papers related to the given search term. |

---

### AskUbuntu

```py
from scrape_up import askubuntu
```

Create an instance of `Questions` class.

```python
questions = askubuntu.Questions("topic")
```

| Methods                     | Details                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| `.getNewQuestions()`        | Returns the new questions, views, votes, answer counts, and descriptions in JSON format              |
| `.getActiveQuestions()`     | Returns the active questions, views, votes, answer counts, and descriptions in JSON format           |
| `.getUnansweredQuestions()` | Returns the unanswered questions, views, votes, answer counts, and descriptions in JSON format       |
| `.getBountiedQuestions()`   | Returns the bountied questions, views, votes, answer counts, and descriptions in JSON format         |
| `.getFrequentQuestions()`   | Returns the frequently asked questions, views, votes, answer counts, and descriptions in JSON format |
| `.getHighScoredQuestions()` | Returns the most voted questions, views, votes, answer counts, and descriptions in JSON format       |

---

### BBC News

```py
from scrape_up import bbcnews
```

First create an object of class `BBCNews`

```python
user = bbcnews.BBCNews()
```

| Methods            | Details                                                  |
| ------------------ | -------------------------------------------------------- |
| `.get_headlines()` | Returns the list of object containig the headlines       |
| `get_article()`    | Returns an object with proper details about the articles |

---

### CoinMarketCap

```py
from scrape_up import coinmarketcap
```

Create an instance of `Crypto` class

```python
crypto = coinmarketcap.Crypto()
```

| Method                       | Details                                                  |
| ---------------------------- | -------------------------------------------------------- |
| `get_top_cryptocurrencies()` | Fetches and returns data about the top cryptocurrencies. |

---

### CovidInfo

```py
from scrape_up import covidinfo
```

Create an instance of the `CovidInfo` class.

```python
response = covidinfo.CovidInfo()
```

| Methods              | Details                                                         |
| -------------------- | --------------------------------------------------------------- |
| `.covid_data()`      | Returns the list of all the covid data scraped from the website |
| `.total_cases()`     | Returns the count of total covid cases all over the world       |
| `.total_deaths()`    | Returns the count of deaths covid cases all over the world      |
| `.total_recovered()` | Returns the count of recovered covid cases all over the world   |
| `.latest_news()`     | Return the lastest news of the day                              |

---

### Cricbuzz

```py
from scrape_up import cricbuzz
```

Create an instance of `Cricubzz` class.

```python
	cricbuzz = cricbuzz.Cricubzz()
```

| Methods                      | Details                                                                |
| ---------------------------- | ---------------------------------------------------------------------- |
| `.get_live_matches()`        | Returns a list of live matches from Cricbuzz.                          |
| `.get_recent_matches()`      | Returns a list of recent matches from Cricbuzz.                        |
| `.get_upcoming_matches()`    | Returns a list of upcoming matches from Cricbuzz.                      |
| `.get_series()`              | Returns a dictionary of series in month and year format from Cricbuzz. |
| `.get_series_from_archive()` | Returns a list of series from archive from Cricbuzz.                   |
| `.get_matches_by_day()`      | Returns a dictionary of matches by day from Cricbuzz.                  |
| `.get_series_matches()`      | Returns a list of matches in a series from Cricbuzz.                   |
| `.get_series_stats()`        | Returns a list of stats of players in a series from Cricbuzz.          |
| `.get_teams_list()`          | Returns a list of teams from Cricbuzz.                                 |
| `.get_team_schedule()`       | Returns a list of matches of a team from Cricbuzz.                     |
| `.get_team_players()`        | Returns a list of players of a team from Cricbuzz.                     |
| `.get_team_results()`        | Returns a list of past results of a team from Cricbuzz.                |
| `.get_team_stats()`          | Returns a list of player stats of a team from Cricbuzz.                |

---

### Dribbble

```py
from scrape_up import dribbble
```

Create an instance of `Dribbble` class.

```python
shots = dribbble.Dribbble()
```

| Methods               | Details                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `.get_shots()`        | Returns the latest shots along with their title, designer and designer url like and view count and link.                        |
| `.search(topic)`      | Returns the latest shots along with their title, designer and designer url like and view count and link for the searched topic. |
| `.get_animation()`    | Returns the latest animation along with their title, designer and designer url like and view count and link.                    |
| `.get_branding()`     | Returns the latest branding along with their title, designer and designer url like and view count and link.                     |
| `.get_illustration()` | Returns the latest illustration along with their title, designer and designer url like and view count and link.                 |
| `.get_mobile()`       | Returns the latest mobile shots along with their title, designer and designer url like and view count and link.                 |
| `.get_webdesign()`    | Returns the latest web-design shots along with their title, designer and designer url like and view count and link.             |

---

### EazyDiner

```py
from scrape_up import eazydiner
```

Create an instance of `EazyDiner` class.

```python
restaurants = eazydiner.EazyDiner(location="city-name")
```

| Methods                   | Details                                                                           |
| ------------------------- | --------------------------------------------------------------------------------- |
| `.get_restaurants()`      | Returns the restaurants name, location, rating, cuisine and prices.               |
| `.get_breakfast()`        | Returns the restaurants name, location, rating, cuisine and prices for Breakfast. |
| `.get_lunch()`            | Returns the restaurants name, location, rating, cuisine and prices for Lunch.     |
| `.get_dinner()`           | Returns the restaurants name, location, rating, cuisine and prices for Dinner.    |
| `.dinner_with_discount()` | Returns a list of restaurants from the entered location with a 50% offer.         |
| `.get_top10()`            | Returns a list of the top 10 restaurants from a given city.                       |

---

### ESPN

```py
from scrape_up import espn
```

Create an instance of `ESPN` class

```python
espn = espn.ESPN()
```

| Method              | Details                                                        |
| ------------------- | -------------------------------------------------------------- |
| `get_scoreboard()`  | Fetches and returns the football scoreboards for a given date. |
| `get_tournaments()` | Fetches and returns information about football tournaments.    |
| `get_teams()`       | Fetches and returns information about football teams.          |

---

### eBay

```py
from scrape_up import ebay
```

Create an instance of `EBAY` class

```python
quora = ebay.eBay()
```

| Methods             | Details                             |
| ------------------- | ----------------------------------- |
| `.spotlights()`     | Returns spotlight deals on eBay.    |
| `.featured()`       | Returns the featured deals on eBay. |
| `.specific_deals()` | Returns the specific deals on eBay. |

---

### Flipkart

```py
from scrape_up import flipkart
```

Create an instance of `Flipkart` class.

```python
item = flipkart.Flipkart()
```

| Methods               | Details                                                            |
| --------------------- | ------------------------------------------------------------------ |
| `.TVs()`              | Returns the list of TV sets on flipkart                            |
| `.bestseller_books()` | Returns the list of bestselling books data listed on Flipkart.     |
| `.mobiles()`          | Returns the list of mobile phones under 50K along with their data. |
| `.sport_shoes()`      | Returns the list of trendong sport shoes data.                     |
| `.laptops()`          | Returns the list of laptop from flipkart.                          |
| `.camera()`           | Returns the list of camera from flipkart.                          |
| `.computer()`         | Returns the list of computer from flipkart.                        |
| `.tablets()`          | Returns the list of tablets from flipkart.                         |
| `.cycle()`            | Returns the list of bicycles from flipkart.                        |
| `.printers()`         | Returns the list of printers from flipkart.                        |
| `.monitor()`          | Returns the list of monitors from flipkart.                        |
| `.ac()`               | Returns the list of acs from flipkart.                             |
| `.refrigerator()`     | Returns the list of refrigerators from flipkart.                   |
| `.VRbox()`            | Returns the list of VRbox from flipkart.                           |
| `.Speakers()`         | Returns the list of Speakers from flipkart.                        |

---

#### FlipkartClothing

Create an instance of `FlipkartClothing` class.

```python
cloth = flipkart.FlipkartClothing()
```

| Methods                    | Details                                                        |
| -------------------------- | -------------------------------------------------------------- |
| `.scrape()`                | Returns the list of t-shirts with other relevant info          |
| `.range()`                 | Returns the list of t-shirts between a particular price range. |
| `.minrating()`             | Returns the list of t-shirts havinga minimum given rating.     |
| `.gendermale()`            | Returns the list of t-shirts which are for males.              |
| `.genderfemale()`          | Returns the list of t-shirts which are there for females.      |
| `.size()`                  | Returns the list of tshirts havning a particular size.         |
| `formal_shirts_for_male()` | It returns those t-shirts which are of a particular size       |

---

#### Flipkart laptops

Create an instance of `FlipkartLaptops` class.

```python
item = flipkart.FlipkartLaptops()
```

| Methods      | Details                                  |
| ------------ | ---------------------------------------- |
| `.laptops()` | Returns the list of laptops with details |

---

### Flyrobu

```py
from scrape_up import flyrobu
```

Create an instance of `Flyrobu` class.

```python
flyrobu = flyrobu.Flyrobu()
```

| Methods                              | Details                                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `.search(keyword)`                   | Returns the json data of all the details related to search with informing about the total amount of items found |
| `.get_product_details(product_name)` | Returns the json data of the product details based on the given `product_name`                                  |
