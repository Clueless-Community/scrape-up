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

# Call the followers function
print(user.followers())

# Output - '59'
```

---

# The platforms and methods we cover 💫

- GitHub
- Instagram
- Internshala
- GitHub
- Internshala

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

**Example:**

```python
bio = user.get_bio() #user var taken from above example
print(bio)
```

---

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

**Example:**

```python
fork_count = repository.fork_count() #repository var taken from above example
print(fork_count)
```

---

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

**Example:**

```python
assigned = repository.assignees() #user var taken from above example
print(assigned)
```

---

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

**Example:**

```python
files_changed = repository.files_changed() #user var taken from above example
print(files_changed)
```

---

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

**Example:**

```python
top = repository.top_topics() #user var taken from above example
print(top)
```

---

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

**Example:**

```python
name_result = user.get_name()
print("Name:", name_result["data"])
print("Status:", name_result["message"])
```

---

### Scrape Repository Details

First, create an object of the `Repository` class:

```python
repository = gitlab.Repository(username="example_user", repository_name="example_repository")
```

| Methods              | Details                                    |
| -------------------- | ------------------------------------------ |
| `.get_name()`        | Returns the name of the repository.        |
| `.get_description()` | Returns the description of the repository. |

**Example:**

```python
name_result = repository.get_name()
print("Repository Name:", name_result["data"])
```

---

### Scrape Organization Members

First, create an object of the `Organization` class:

```python
organization = gitlab.Organization(organization_name="example_organization")
```

| Methods          | Details                                                           |
| ---------------- | ----------------------------------------------------------------- |
| `.get_members()` | Returns a list of usernames of the members in the organization.   |
| `get_projects()` | Returns a list of project names associated with the organization. |

**Example:**

```python
members = organization.get_members()
print("Organization Members:", members)

projects = organization.get_projects()
print("Organization Projects:", projects)

```

---

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

**Example:**

```python
title = issue.get_title()
print("Issue Title:", title["data"])

description = issue.get_description()
print("Issue Description:", description["data"])

author = issue.get_author()
print("Issue Author:", author["data"])

```

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

**Example:**

```python
title = pull_request.get_title()
print("Pull Request Title:", title)

description = pull_request.get_description()
print("Pull Request Description:", description)

author = pull_request.get_author()
print("Pull Request Author:", author)

```

---

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

**Example:**

```python
print(user.user_details()) #user var taken from above
```

---

## Internshala

```python
from scrape_up.internshala.internships import Internships
```

### Scrape Internship details

Create an object for the 'Internships' class:

```python
scraper = Internships()
```

| Methods          | Details                                                              |
| ---------------- | -------------------------------------------------------------------- |
| `.internships()` | Scrapes and returns a list of dictionaries representing internships. |

**Example:**

```python
scraper = Internships()
internships = scraper.scrape_internships()
for internship in internships:
    print(internship)

```

---

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

**Example:**

```py
name = user.get_name() # user variable is taken from above example
print(name)
```

---

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

**Example**

```python
articles = user.get_articles() #user var taken from above
for article in articles:
    print(article) #For better visibility/readability
```

### Scrape trending articles

| Methods           | Details                                    |
| ----------------- | ------------------------------------------ |
| `.get_trending()` | Returns the trending titles of the medium. |

**Example**

```python
Trending.get_trending() #Prints the trending titles
```

### Scrape publication details

First, create an object of class `Publication`

```python
publication = medium.Publication(link="https://....")
```

| Methods           | Details                                              |
| ----------------- | ---------------------------------------------------- |
| `.get_articles()` | Returns a list of articles of the given publication. |

**Example**

```python
articles = publication.get_articles() #publication var taken from above
for article in articles:
    print(article) #For better visibility/readability
```

---

## Hacker News

```py
from scrape_up import hacker_news
```

### Scrap up Hacker News's latest articles

Create an instance of `Article` class.

```py
articles = hacker_news.Article()
```

| Methods            | Details                                                            |
| ------------------ | ------------------------------------------------------------------ |
| `.articles_list()` | Returns the latest articles along with their links in JSON format. |

**Example:**

```py
article = Article()
print(article.articles_list())
```

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

### Scrape

First, create an object of class `LeetCodeScraper`

```python
leetcode_scraper = LeetCodeScraper()
```

| Methods                    | Details                                          |
| -------------------------- | ------------------------------------------------ |
| `.scrape_rank(username)`   | Used to scrape the rank of a user on LeetCode.   |
| `.scrape_rating(username)` | Used to scrape the rating of a user on LeetCode. |

---

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

**Example**

```python
# all data returned in dictionary format
latest_info = infosys.get_latest_price() # infosys var taken from above
historical_data = infosys.get_historical_data('02-05-2023', '31-05-2023')
```

---

## IMDb

### Scrap up IMDb Top 250 details

Create an instance of the `Movie` class.

```python
top_250 = IMDB()
```

| Methods        | Details                                      |
| -------------- | -------------------------------------------- |
| `.top_rated()` | Returns the top-rated movies listed on IMDB. |

---

## Coursera

```python
from scrape_up import Coursera
```

### Scrape Courses Details

<br>

Create an object of the 'Courses' class:

```python
scraper = Courses("courses","page_count")
```

| Methods     | Details                       |
| ----------- | ----------------------------- |
| `.titles()` | Returns the titles of courses |

**Example**

```python
# All data returned in dictionary format
javaCourses = Courses("java", 4)  # Keyword,Pages
print(javaCourses.titles())
 #For better visibility/readability
```

---

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

**Example**

```python
# Returning the data
scraped_data = scraper.scrape()
print(scraped_data)
```

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

### Scrape details of a book

Create an instance of `Book` class.

```python
books = AmazonKindle()
```

| Methods          | Details                                                |
| ---------------- | ------------------------------------------------------ |
| `.bestsellers()` | Returns the list of best seeling books on AmazonKindle |

## Flipkart

### Scrape details of products

Create an instance of `Flipkart` class.

```python
item = Flipkart()
```

| Methods               | Details                                          |
| --------------------- | ------------------------------------------------ |
| `.TVs()`              | Returns the list of TV sets on flipkart          |
| `.BestsellersBooks()` | Returns the list of Bestseller items on flipkart |

---

## Ask Ubuntu

### Scrape questions, views, votes, answer counts, and descriptions from Ask Ubuntu website regarding a topic

Create an instance of `Questions` class.

```python
questions = Questions("topic")
```

| Methods     | Details                                                                             |
| ----------- | ----------------------------------------------------------------------------------- |
| `.scrape()` | Returns the questions, views, votes, answer counts, and descriptions in JSON format |

**Example**

```python
que = Questions("github")
scrape = que.scrape()
json = json.loads(scrape)
questions = json["questions"]
for q in questions:
    print("\nQuestion: ", q["question"])
    print("Views: ", q["views"])
    print("Votes: ", q["vote_count"])
    print("Answers: ", q["answer_count"])
    print("Description: ", q["description\n"])

```

---
