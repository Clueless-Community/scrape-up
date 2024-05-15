import requests
from bs4 import BeautifulSoup


class PullRequest:
    """
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
    """

    def __init__(self, username: str, repository_name: str, pull_request_number: int):
        self.username = username
        self.repository = repository_name
        self.pr_number = pull_request_number
        self._timeout = 10

    def __scrape_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}",
            timeout=self._timeout,
        )
        if data.status_code != 200:
            return None
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def labels(self):
        """
        Class - `PullRequest`
        Example:
        ```
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        labels = repository.labels()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        label_raw = page.find_all(
            "a", class_="IssueLabel hx_IssueLabel width-fit mb-1 mr-1"
        )

        labels_found = map(lambda x: x.get_text().strip(), label_raw)
        return list(labels_found)

    def commits(self):
        """
        Class - `PullRequest`
        Example:
        ```python
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        commits = repository.commits()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        commits_count = page.find("span", id="commits_tab_counter")
        return None if commits_count is None else commits_count.text.strip()

    def title(self):
        """
        Class - `PullRequest`
        Example:
        ```python
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        title = repository.title()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        title_body = page.find("bdi", class_="js-issue-title markdown-title")
        return None if title_body is None else title_body.text.strip()

    def __files_changed_body(self):
        """
        scrape the data of files changed in a pull request
        """
        link = f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}/files"
        data = requests.get(link, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def files_changed(self):
        """
        Class - `PullRequest`
        Example:
        ```python
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        files_changed = repository.files_changed()
        ```
        """
        data = self.__files_changed_body()
        if data is None:
            return None

        files_changed_body = data.find("span", id="files_tab_counter")
        return None if files_changed_body is None else files_changed_body.text.strip()

    def reviewers(self):
        """
        Class - `PullRequest`
        Example:
        ```python
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        reviewers = repository.reviewers()
        ```
        """
        data = self.__scrape_page()
        if data is None:
            return None

        reviewers = data.find_all(
            "span", class_="css-truncate-target width-fit v-align-middle"
        )
        reviewerList = list(map(lambda x: x.text, reviewers))
        return reviewerList
