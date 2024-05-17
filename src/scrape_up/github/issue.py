from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Issue:
    """
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
    """

    def __init__(
        self,
        username: str,
        repository_name: str,
        issue_number: int,
        *,
        config: RequestConfig = RequestConfig(),
    ):
        self.username = username
        self.repository = repository_name
        self.issue_number = issue_number
        self.config = config

    def __scrape_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/issues/{self.issue_number}"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def assignees(self):
        """
        Class - `Issues`
        Example:
        ```
        repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
        assignees = repository.assignees()
        ```
        Returns: Assignees | None
        ```
        """
        data = self.__scrape_page()
        try:
            assignees_body = data.find("span", class_="css-truncate js-issue-assignees")
            assignees = []
            for assignee in assignees_body.find_all(
                "a", class_="assignee Link--primary css-truncate-target width-fit"
            ):
                assignees.append(assignee.text.replace("\n", "").strip())
            return assignees
        except:
            None

    def labels(self):
        """
        Class - `Issues`
        Example:
        ```
        repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
        labels = repository.labels()
        ```
        Returns: Labels | None
        """
        data = self.__scrape_page()
        try:
            labelsDiv = data.find(class_="js-issue-labels d-flex flex-wrap")
            allLabelsHtml = labelsDiv.find_all(
                class_="css-truncate css-truncate-target width-fit"
            )
            allLabels = []
            for label in allLabelsHtml:
                allLabels.append(label.text)
            return allLabels
        except:
            return None

    def opened_by(self):
        """
        Class - `Issues`
        Example:
        ```
        repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
        opened_by = repository.opened_by()
        ```
        Returns: Author Name | None
        """
        data = self.__scrape_page()
        try:
            author_name = data.find("a", class_="author text-bold Link--secondary").text
            return author_name
        except:
            return None

    def title(self):
        """
        Class - `Issues`
        Example:
        ```
        repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
        title = repository.title()
        ```
        Returns: Title | None
        """
        data = self.__scrape_page()
        try:
            title_body = data.find("bdi", class_="js-issue-title markdown-title")
            title = title_body.text.strip()
            return title
        except:
            return None

    def opened_at(self):
        """
        Class - `Issues`
        Example:
        ```
        repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
        opened_at = repository.opened_at()
        ```
        Returns: Opened at | None
        """
        try:
            data = self.__scrape_page()
            return data.find("relative-time").text
        except:
            return None

    def is_milestone(self):
        """
        Class - `Issues`
        Example:
        ```
        repository = github.Issue(username="nikhil25803", repository_name="scrape-up", issue_number=59)
        is_milestone = repository.is_milestone()
        ```js
        Returns: Milestones | None
        """
        data = self.__scrape_page()
        try:
            milestone = data.find(
                "a", class_="Link--secondary mt-1 d-block text-bold css-truncate"
            ).text.strip()
            return milestone
        except:
            return None
