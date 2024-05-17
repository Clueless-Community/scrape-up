from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


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

    def __init__(
        self,
        username: str,
        repository_name: str,
        pull_request_number: int,
        *,
        config: RequestConfig = RequestConfig(),
    ):
        self.username = username
        self.repository = repository_name
        self.pr_number = pull_request_number
        self.config = config

    def __scrape_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}"
        data = get(url, self.config)
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
        labels_found = []
        data = self.__scrape_page()
        label_raw = data.find_all(
            "a", class_="IssueLabel hx_IssueLabel width-fit mb-1 mr-1"
        )
        try:
            for d in label_raw:
                labels_found.append(d.get_text().strip())
            labels_found + 1
            # return labels_found
            return labels_found
        except:
            return None

    def commits(self):
        """
        Class - `PullRequest`
        Example:
        ```python
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        commits = repository.commits()
        ```
        """
        data = self.__scrape_page()
        try:
            commits_count = data.find("span", id="commits_tab_counter").text.strip()
            return commits_count
        except:
            return None

    def title(self):
        """
        Class - `PullRequest`
        Example:
        ```python
        repository = github.PullRequest(username="nikhil25803", repository_name="scrape-up", pull_request_number=30)
        title = repository.title()
        ```
        """
        data = self.__scrape_page()
        try:
            title_body = data.find("bdi", class_="js-issue-title markdown-title")
            title = title_body.text.strip()
            return title
        except:
            return None

    def __files_changed_body(self):
        """
        scrape the data of files changed in a pull request
        """
        link = f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}/files"
        data = get(link, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

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
        try:
            files_changed_body = data.find("span", id="files_tab_counter")
            files_changed = files_changed_body.text.strip()
            return files_changed
        except:
            return None

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
        try:
            reviewerList = []
            reviewers = data.find_all(
                "span", class_="css-truncate-target width-fit v-align-middle"
            )
            if len(reviewers) == 0:
                message = f"No reviewers found for {self.pr_number}"
                return reviewerList
            else:
                for reviewer in reviewers:
                    reviewerList.append(reviewer.text)
                return reviewerList
        except:
            return None
