# How to use this package? 👀

- Install the package from `pip`

```PowerShell
pip install scrape-up
```

- Scrape the required information, for example, one wants to extract the number of followers of a user.

```python
# Import the required module
from scrape_up import github

# Instantiate an object with the username provided.
user = github.Users(username="nikhil25803")

# Call the followers function - it will return the number of followers
user.followers()
```

---

# The platforms and methods we cover 💫

- GitHub
- Instagram
- Internshala
- GitHub
- Internshala
- TimesJobs
- Swiggy
- Library Genesis

## GitHub

```python
from scrape_up import github
```

### Scrape User details

First, create an object of class `Users`

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

### Scrape Repository details

First, create an object of class `Repository`

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

### Scrape an issue details

First, create an object of class `Issue`

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

First, create an object of class `PullRequest`

```python
repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
```

| Methods            | Details                                                                    |
| ------------------ | -------------------------------------------------------------------------- |
| `.commits()`       | Returns the number of commits made in a pull request.                      |
| `.title()`         | Returns the title of a pull request.                                       |
| `.labels()`        | Returns all the labels of a pull request, empty list in case of no labels. |
| `.files_changed()` | Returns the number of files changed in a pull request.                     |
| `.reviewers()`     | Return the list of reviewers assigned in a pull request.                   |

### Scrape the details of an organization

First, create an object of class `Organization`

```python
repository = github.Organization(organization_name="Clueless-Community")
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

## Gitlab

```python
from scrape_up import gitlab
```

### Scrape up users details

First, create an object of the `User` class:

```python
user = gitlab.Users(username="example_user")
```

| Methods                            | Details                                                      |
| ---------------------------------- | ------------------------------------------------------------ |
| `.get_name()`                      | Returns the name of the user.                                |
| `.get_bio()`                       | Returns the bio of the user.                                 |
| `.get_avatar_url()`                | Returns the avatar URL of the user.                          |
| `.get_repositories()`              | Returns a list of repositories owned by the user.            |
| `.get_project_details(project_id)` | Returns the details of a specific project owned by the user. |

### Scrape Repository Details

First, create an object of the `Repository` class:

```python
repository = gitlab.Repository(username="example_user", repository_name="example_repository")
```

| Methods              | Details                                    |
| -------------------- | ------------------------------------------ |
| `.get_name()`        | Returns the name of the repository.        |
| `.get_description()` | Returns the description of the repository. |

### Scrape Organization Members

First, create an object of the `Organization` class:

```python
organization = gitlab.Organization(organization_name="example_organization")
```

| Methods          | Details                                                           |
| ---------------- | ----------------------------------------------------------------- |
| `.get_members()` | Returns a list of usernames of the members in the organization.   |
| `get_projects()` | Returns a list of project names associated with the organization. |

### Scrape Issues

To scrape information about an `issue` on GitLab, create an object of the `Issue` class by providing the following parameters:

- username: The GitLab username of the repository owner.
- repository: The name of the repository.
- issue_number: The number of the issue.

Here's an example of creating an object of the `Issue` class:

```python
issue = gitlab.Issue(username="example_user", repository="example_repository", issue_number=123)

```

| Methods              | Details                               |
| -------------------- | ------------------------------------- |
| `.get_title()`       | Returns the title of the issue.       |
| `.get_description()` | Returns the description of the issue. |
| `.get_author()`      | Returns the author of the issue.      |

### Scrape Pull Requests

To scrape pull request details from GitLab, create an object of the `PullRequest` class:

```python
pull_request = gitlab.PullRequest(username="example_user", repository="example_repository", pull_request_number=123)


```

| Methods              | Details                                      |
| -------------------- | -------------------------------------------- |
| `.get_title()`       | Returns the title of the pull request.       |
| `.get_description()` | Returns the description of the pull request. |
| `.get_author()`      | Returns the author of the pull request.      |

## Instagram

```python
from scrape_up import instagram
```

### Scrape User details

First, create an object of the class `User`

```python
user = instagram.User(username="nikhil25803")
```

| Methods           | Details                                    |
| ----------------- | ------------------------------------------ |
| `.user_details()` | Returns the number of followers of a user. |

## Internshala

Create an object for the 'Internshala' class:

```python
search = Internshala(search_type="machine learning")
```

| Methods                    | Details                                                                        |
| -------------------------- | ------------------------------------------------------------------------------ |
| `.internships()`           | Scrapes and returns a list of dictionaries representing internships.           |
| `.jobs()`                  | Scrapes and returns a list of dictionaries representing jobs.                  |
| `.certification_courses()` | Scrapes and returns a list of dictionaries representing certification courses. |

## KooApp

```py
from scrape_up import kooapp
```

### Scrap up the kooapp user's detail

Create an instance of `KooUser` class.

```py
user = kooapp.KooUser('krvishal')
```

| Methods                  | Details                                                      |
| ------------------------ | ------------------------------------------------------------ |
| `.get_name()`            | Returns the name of the user.                                |
| `.get_bio()`             | Returns the bio of the user.                                 |
| `.get_avatar_url()`      | Returns the URL of the first avatar of the user.             |
| `.followers()`           | Returns the number of followers of a user.                   |
| `.following()`           | Returns the number of people the user is following.          |
| `.get_social_profiles()` | Returns all the connected social media profiles of the user. |
| `.get_profession()`      | Returns the title/profession of the user.                    |

## Medium

```python
from scrape_up import medium
```

### Scrape user details

First, create an object of class `User`

```python
user = medium.Users(username="nikhil25803")
```

| Methods           | Details                                  |
| ----------------- | ---------------------------------------- |
| `.get_articles()` | Returns the article titles of the users. |

### Scrape trending articles

| Methods           | Details                                    |
| ----------------- | ------------------------------------------ |
| `.get_trending()` | Returns the trending titles of the medium. |

### Scrape publication details

First, create an object of class `Publication`

```python
publication = medium.Publication(link="https://....")
```

| Methods           | Details                                              |
| ----------------- | ---------------------------------------------------- |
| `.get_articles()` | Returns a list of articles of the given publication. |

---

## Hacker News

```py
from scrape_up import hacker_news
```

Create an instance of `HackerNews` class.

```py
articles = HackerNews()
```

| Methods            | Details                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------- |
| `.articles_list()` | Returns the latest articles along with their score, author, author url, time, comment count and link in JSON format. |

## Twitter

```python
from scrape_up import twitter
```

### Scrape

First, create an object of class `TwitterScraper`

```python
twitter_scraper = TwitterScraper()
```

| Methods                    | Details                                       |
| -------------------------- | --------------------------------------------- |
| `.unametoid(username)`     | Returns the numerical_id on passing username. |
| `.idtouname(numerical_id)` | Returns the username on passing numerical_id. |

---

## Leetcode

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

## Finance

```python
from scrape_up import StockPrice
```

### Scrape stock data

First, create an instance of class `StockPrice` with stock name and index name.

```python
infosys = StockPrice('infosys','nse')
```

| Methods                                   | Details                                                                                 |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| `.get_latest_price()`                     | Returns the latest stock price of the given stock name.                                 |
| `.get_historical_data(from_date,to_date)` | Returns stock price from `from_date` to `to_date` in format (date in format dd-mm-yyyy) |

---

## IMDb

Create an instance of the `IMDB` class.

```python
scraper = IMDB()
```

| Methods                       | Details                                                        |
| ----------------------------- | -------------------------------------------------------------- |
| `.top_rated()`                | Returns the top-rated movies listed on IMDB.                   |
| `.scrape_genre_movies(genre)` | Returns the list of movies related to the genre you mentioned. |
| `.top_rated_shows()`          | Returns the top-rated shows listed on IMDB.                    |

Create an instance of `Movie` class.

```python
movie = Movie(movie_name)
```

| Methods          | Details                                                 |
| ---------------- | ------------------------------------------------------- |
| `.rating()`      | Returns the IMDB rating of the movie                    |
| `.description()` | Returns the description, cast and director of the movie |
| `.more_movies()` | Returns similar movies recommended by IMDB              |

Create an instance of `Actor` class.

```python
actor = Actor(actor_name)
```

| Methods             | Details                                                 |
| ------------------- | ------------------------------------------------------- |
| `.popular_movies()` | Returns the popular movies in which the actor has acted |
| `.all_movies()`     | Returns all movies acted in and upcoming movies         |
| `.awards()`         | Returns the number of awards and nominations            |

---

## Coursera

Create an object of the 'Courses' class:

```python
scraper = Courses(topic="topic")
```

| Methods                                | Details                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| `.get_courses()`                       | Returns the courses with title, teached by, skills, rating, review count, img url and link |
| `.fetch_modules(course='Course Name')` | Returns the modules associated with the Coursera.                                          |

## Wikipedia

```python
from scrape_up import Wikipedia
```

### Scrape Wikipedia Details

<br>

Create an object of the 'WikipediaScrapper' class:

```python
Scraper = WikipediaScraper(url)
```

| Methods     | Details                                 |
| ----------- | --------------------------------------- |
| `.scrape()` | Returns the Scraped Data from Wikipedia |

---

## Amazon

### Scrape details about a product

Create an instance of `Product` class with a `product_name` propertiese.

```python
product = Product(product_name="watch")
```

| Methods                  | Details                      |
| ------------------------ | ---------------------------- |
| `.get_product()`         | Returns product data(links). |
| `.get_product_details()` | Returns product detail.      |
| `.get_product_image()`   | Returns product image.       |
| `.customer_review()`     | Returns product review.      |

## Amazon-Kindle Bookstore

Create an instance of `Book` class.

```python
books = AmazonKindle()
```

| Methods          | Details                                                |
| ---------------- | ------------------------------------------------------ |
| `.bestsellers()` | Returns the list of best-selling books on AmazonKindle |
| `.topbooks()`    | Returns the list of top books on AmazonKindle          |

## Flipkart

### Scrape details of products

Create an instance of `Flipkart` class.

```python
item = Flipkart()
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

---

## Spotify

### Scrape up songs

Create an instance of `Spotify` class.

```python
scraper = Spotify()
```

| Methods                      | Details                                                   |
| ---------------------------- | --------------------------------------------------------- |
| `.scrape_songs_by_keyword()` | Returns the list of songs that are related to the keyword |
| `.scrape_homepage()`         | Returns the list of playlists on the homepage             |
| `.close()`                   | To close the chrome tab that is showing results           |

---

## Ask Ubuntu

### Scrape questions, views, votes, answer counts, and descriptions from Ask Ubuntu website regarding a topic

Create an instance of `AskUbuntu` class.

```python
questions = AskUbuntu("topic")
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

## EazyDiner

Create an instance of `EazyDiner` class.

```python
restaurants = EazyDiner(location="city-name")
```

| Methods                   | Details                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| `.get_restaurants()`      | Returns the restaurants name, location, rating, cuisine and prices in JSON format.               |
| `.get_breakfast()`        | Returns the restaurants name, location, rating, cuisine and prices in JSON format for Breakfast. |
| `.get_lunch()`            | Returns the restaurants name, location, rating, cuisine and prices in JSON format for Lunch.     |
| `.get_dinner()`           | Returns the restaurants name, location, rating, cuisine and prices in JSON format for Dinner.    |
| `.dinner_with_discount()` | Returns list of resturant from the entered location with 50% offer.                              |

---

## Stack Overflow

Create an instance of `StackOverflow` class.

```python
questions = StackOverflow("topic")
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

## Tech Crunch

### Scrape articles with title, descriptions, images, author, date and link

Create an instance of `TechCrunch` class.

```python
articles = TechCrunch()
```

| Methods          | Details                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `.getArticles()` | Returns the articles with title, descriptions, images, author, date and link regarding a category in JSON format       |
| `.search()`      | Returns the searched articles with title, descriptions, images, author, date and link regarding a topic in JSON format |

---

## YouTube

### Scrape Video Details

Create an instance of `Video` class.

```python
video = Video(video_url="video_url")
```

| Methods         | Details                  |
| --------------- | ------------------------ |
| `.getDetails()` | Return the video details |

## Scrape Channel Details

Create an instance of `Channel` class.

```python
channel_data = Channel(channel_username="BeABetterDev")
```

| Methods       | Details                                                                |
| ------------- | ---------------------------------------------------------------------- |
| `.getAbout()` | Returns the channel details mentioned in the about page of the channel |

---

## Google News

### Scrape articles with title, descriptions, news source, date and link regarding a topic

Create an instance of `GoogleNews` class.

```python
articles = GoogleNews()
```

| Methods                        | Details                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| `.getArticles(topic="github")` | Returns the list of articles with title, descriptions, news source, date and link in JSON format |
| `.top_stories()`               | Returns the list of top stories listed regarding the mentioned topic                             |
| `.timed_aticles(time)`         | Returns the list of top stories listed regarding the mentioned topic and within that time frame  |

---

## Hashnode

Create an instance of `Hashnode` class.

```python
blogs = Hashnode()
```

| Methods           | Details                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| `.get_feed()`     | Returns the blogs with title, descriptions, author, read time, like and comment count, date and link |
| `.get_featured()` | Returns the featured blogs with title, descriptions, author, like and comment count, date and link   |
| `.get_recent()`   | Returns the recent blogs with title, descriptions, author, like and comment count, date and link     |

---

## Reddit

Create an instance of `Reddit` class.

```python
posts = Reddit()
```

| Methods      | Details                                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `.getFeed()` | Returns the posts with title, descriptions, subreddit, subreddit avatar, time, vote and comment count, image, category and link |

---

## TimesJobs

```python
from timesjobs_scraper import TimesJobs
```

### Scrape Job Details

First, create an object of the class `Job` and specify the domain to which you want to apply.

```python
Job = TimesJobs('example')
```

| Methods     | Details                                                                                 |
| ----------- | --------------------------------------------------------------------------------------- |
| `.scrape()` | Returns the various details regarding the companies based on the Job-role as JSON data. |

---

## Dev Community

Create an instance of `DevCommunity` class.

```python

dev = DevCommunity('francescoxx')

```

| Methods              | Details                                                               |
| -------------------- | --------------------------------------------------------------------- |
| `.all_articles()`    | Returns latest articles from the home page of DevCommunity.           |
| `.__strTag__()`      | Returns name of the tag specified whose articles we want returned.    |
| `.tag_articles()`    | Returns latest articles which have the specified tag in DevCommunity. |
| `.__strUser__()`     | Returns username of the user.                                         |
| `.user_details()`    | Returns the user details.                                             |
| `.pinned_articles()` | Returns all pinned articles which have been written by the user.      |
| `.user_articles()`   | Returns all articles written by the user.                             |

---

---

# Cricbuzz

## Create an instance of `Cricubzz` class.

```python
	cricbuzz = Cricubzz()
```

## Available Methods

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

# Udemy

First, create an object of class `Courses` for `Udemy` module

```python
topic = Udemy.courses(keyword="data science")
```

| Methods          | Details                          |
| ---------------- | -------------------------------- |
| `.get_courses()` | Returns the list of top courses. |

---

# CovidInfo

Create an instance of the `CovidInfo` class.

```python
response = CovidInfo()
```

Class - `CovidInfo`\n
| Methods | Details |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| `.covid_data()` | Returns the list of all the covid data scraped from the website |
| `.total_cases()` | Returns the count of total covid cases all over the world |
| `.total_deaths()` | Returns the count of deaths covid cases all over the world |
| `.total_recovered()` | Returns the count of recovered covid cases all over the world |
| `.latest_news()` | Return the lastest news of the day |

# FlipkartTees

```python
from flipkart_file import FlipkartTees
```

Create an instance of `FlipkartTees` class.

```python
cloth = FlipkartTees()
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

# MediEncyclopedia

Create an instance of `MediEncyclopedia` class.

```python
ency = MediEncyclopedia()
```

| Methods          | Details                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------- |
| `.scrapebyurl()` | Returns the medical dictation of associated topic url                                        |
| `.query()`       | It takes a user query parameter as an argument and returns all relevant terms related to it. |
| `.byletter()`    | Returns the list of medical relics starting with a particular letter                         |

# NewsCNN

Create an instance of `NewsCNN` class.\n

```python
news = newsCNN()
```

| Methods | Details |
| `.newsbylocation(country="india)` | Returns the list of articles by a specific country. |

# FlipkartTees

Create an instance of `FlipkartClothing` class.

```python
cloth = FlipkartClothing()
```

| Methods                     | Details                                                        |
| --------------------------- | -------------------------------------------------------------- |
| `.tshirts()`                | Returns the list of t-shirts with other relevant info          |
| `.tshirts_by_price_range()` | Returns the list of t-shirts between a particular price range. |
| `.tshirts_by_rating()`      | Returns the list of t-shirts havinga minimum given rating.     |
| `.tshirts_for_male()`       | Returns the list of t-shirts which are for males.              |
| `.tshirts_for_female()`     | Returns the list of t-shirts which are there for females.      |
| `.tshirt_by_size()`         | Returns the list of tshirts havning a particular size.         |
| `.Formal_shirts_for_male`   | Returns the list of formal shirts for mens.                    |

# Flyrobu

Create an instance of `Flyrobu` class.

```python
flyrobu = Flyrobu()
```

| Methods                              | Details                                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `.search(keyword)`                   | Returns the json data of all the details related to search with informing about the total amount of items found |
| `.get_product_details(product_name)` | Returns the json data of the product details based on the given `product_name`                                  |

# Robu

Create a new instance of the `Robu` class.

```python
robu = Robu()
```

| Methods     | Details                                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------- |
| `.search()` | Returns the json data of all the details related to search with informing about the total amount of items found |

# LibGen

First, create an object of class `LibGen`

```python
Book = LibGen()
```

| Methods                | Details                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `.getBooks(book_name)` | Returns the books with name, author, size, format, book link, book cover link, language |

# Rotten Tomatoes

Create an instance of `RottenTomatoes` class.

```python
scraper = RottenTomatoes()
```

| Method                       | Details                                                             |
| ---------------------------- | ------------------------------------------------------------------- |
| `.top_rated()`               | Returns the top-rated movies listed on the Rotten Tomatoes website. |
| `.movie_details(movie_name)` | Fetches and returns detailed information about a specific movie.    |

# Quora

Create an instance of Quora class

```python
quora = Quora()
```

| Methods            | Details                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `.fetch_answers()` | Returns the list of answers pertaining to a particular url gien by the user as parameter. |
| `.getbyquery()`    | Returns the list of answers pertaining to a particular query given by the user.           |
| `.getprofile()`    | Returns the list of the name of a user along with their quora profile link.               |

# ICC Rankings

"""
Create an instance of `ICC` class.
`python
    scraper = ICC()
    `
| Method | Details |
| ---------------------------- | ------------------------------------------------------------------- |
| `.team_rankings(format)` | Returns the list of rankings of teams of desired format |
|`.player_ranking(type,format)`| Returns the list of player ranking of desired type and format |
"""

---

# Swiggy

First, create an object of class `Swiggy`

```python
store1 = Swiggy()
```

| Methods                   | Details                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| `get_restraunt_details()` | Returns the restaurant data with name, cuisine, area, rating, offers, etc |
| `get_restaurants()`       | Returns the restaurant names as per given city                            |

---

# eBay

Create an instance of eBay class

```python
quora = eBay()
```

| Methods             | Details                             |
| ------------------- | ----------------------------------- |
| `.spotlights()`     | Returns spotlight deals on eBay.    |
| `.featured()`       | Returns the featured deals on eBay. |
| `.specific_deals()` | Returns the specific deals on eBay. |

---

# Zomato

First, create an object of class `Zomato`

```python
store1 = Zomato()

```

| Methods                                    | Details                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| `.get_restaurants_details(page_url = " ")` | Returns the restraunt data with name, cuisine, area, rating, offers, etc |

---

# UCI

Create an instance of UCI class

```python
uci = UCI()
```

| Methods       | Details                               |
| ------------- | ------------------------------------- |
| `.datasets()` | Fetches datasets information from UCI |

---

# CodeChef

First, create an object of class `Codechef`

```python
user1 = Codechef(id="username")

```

| Methods         | Details                                                          |
| --------------- | ---------------------------------------------------------------- |
| `get_profile()` | Returns name, username, profile_image_link, rating, details etc. |

# HackerRank

First, create an object of class `HackerRank`

```python
hackerank = HackerRank()
```

| Methods                      | Details                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| `get_profile(id="username")` | Returns name, username, country, user_type, details, badges, verified_skills, social etc. |
| `active_contests()`          | Returns information on active contests like title, status, and link                       |
| `archived_contests()`        | Returns information regarding archived contests                                           |

---

# Yahoo Finance

Create an instance of YahooFinance class

```python
yf = YahooFinance()
```

| Methods       | Details                             |
| ------------- | ----------------------------------- |
| `.headline()` | Fetches headlines from yahooFinance |

---

# BBC News

First create an object of class `User`

```python
user = instagram.Users(username="nikhil25803")
```

| Methods            | Details                                                  |
| ------------------ | -------------------------------------------------------- |
| `.get_headlines()` | Returns the list of object containig the headlines       |
| `get_article()`    | Returns an object with proper details about the articles |

---

# Billionaires

Create an instance of `Billionaires` class.

```python
billionaires = Billionaires()
```

| Methods             | Details                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------- |
| `.realtime()`       | It takes a user query parameter as an argument and returns all relevant terms related to it. |
| `.powerfulwomen()`  | Returns as JSON the list of Forbes most powerful women in the world.                         |
| `.powerfulpeople()` | Returns as JSON a list of Forbes Porweful people.                                            |
| `.bylocation()`     | Returns as JSON the billionaires of a particular nation.                                     |

---

# Hackerearth

First, create an object of class `Hackerearth`

```python
hackerearth = Hackerearth()
```

| Methods          | Details                                                |
| ---------------- | ------------------------------------------------------ |
| `get_upcoming()` | Get the details of upcoming challenges on Hackerearth. |
| `get_ongoing()`  | Get the details of ongoing challenges on Hackerearth.  |

---


# Pixabay

First, we create an object of `Pixabay`:
```
 Class - `Pixabay`\n

 pix = Pixabay()

```

| Methods                     | Details                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| `.get_video()`              | Downloads the videos from pixaby to the local storage.                                               |
| `.get_photo()`              | Downloads the photos from pixaby to local storage.                                                   |

___

# Bugmenot

Create an instance of the class `Bugmenot`

```python
website = 'canva.com'
```

| Methods          | Details                                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_upcoming()` | Scrapes account data from Bugmenot.com for the given website and returns a list of dictionaries with account details. Returns `None` if no accounts are found. |

