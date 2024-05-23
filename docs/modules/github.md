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
| `.get_starred_repos()`        | Returns the list of starred repositories of a user.                                                |
| `.pul_requests()`             | Returns the number of pull requests opened in a repository.                                        |
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

| Methods                    | Details                                                                                                                                                                                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.fork_count()`            | Returns the number of forks of a repository.                                                                                                                                                                                                              |
| `.get_contributors()`      | Returns the number of contributors of a repository.                                                                                                                                                                                                       |
| `.topics()`                | Returns the topics of a repository.                                                                                                                                                                                                                       |
| `.pull_requests()`         | Returns the number of pull requests opened in a repository.                                                                                                                                                                                               |
| `.last_updated_at()`       | Returns the last updated date of a repository.                                                                                                                                                                                                            |
| `.tags()`                  | Returns the last ten tags of a repository.                                                                                                                                                                                                                |
| `.releases()`              | Returns the last ten releases of a repository.                                                                                                                                                                                                            |
| `.issues_count()`          | Returns number of issues in a repository                                                                                                                                                                                                                  |
| `.readme`                  | Saves the readme.md file of the given user to the current working directory. To view the readme.md with a live server, change ".md" to ".html" in "readme.md".                                                                                            |
| `.get_pull_requests_ids()` | Returns all ids of opened pull requests in a repository.                                                                                                                                                                                                  |
| `.get_issues()`            | Returns the list of all open issues in a repository.                                                                                                                                                                                                      |
| `.commits()`               | Returns the number of commits in a repository.                                                                                                                                                                                                            |
| `.get_readme()`            | Returns & saves README.md file of the special repository (if exists)                                                                                                                                                                                      |
| `.get_environment()`       | Returns the latest deployed link of a repository (if exists).                                                                                                                                                                                             |
| `.watch_count()`           | Returns the number of watchers of a repository                                                                                                                                                                                                            |
| `.all_watchers()`          | Returns the username of all watches of a repository                                                                                                                                                                                                       |
| `.get_insights(period)`    | Returns the active pr count, active issue count, merged pr count, open pr count, closed issue count, new issue count, list of recent merged prs, list of recent open prs, list of recent closed issues, list of recent open issues for a specified period |

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
<p align="right">(<a href="#top">Back to top</a>)</p>
