import requests
from bs4 import BeautifulSoup, Tag


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

    def __init__(self, username: str, repository_name: str, issue_number: int):
        self.username = username
        self.repository = repository_name
        self.issue_number = issue_number
        self._timeout = 10

    def __scrape_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/issues/{self.issue_number}",
            timeout=self._timeout,
        )
        if data.status_code != 200:
            return None
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
        page = self.__scrape_page()
        if page is None:
            return None

        assignees_body = page.find("span", class_="css-truncate js-issue-assignees")
        if not isinstance(assignees_body, Tag):
            return None

        assignees_body_search = assignees_body.find_all(
            "a", class_="assignee Link--primary css-truncate-target width-fit"
        )
        assignees = map(
            lambda x: x.text.replace("\n", "").strip(), assignees_body_search
        )
        return list(assignees)

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
        page = self.__scrape_page()
        if page is None:
            return None

        labelsDiv = page.find(class_="js-issue-labels d-flex flex-wrap")
        if not isinstance(labelsDiv, Tag):
            return None

        allLabelsHtml = labelsDiv.find_all(
            class_="css-truncate css-truncate-target width-fit"
        )
        allLabels = list(map(lambda x: x.text, allLabelsHtml))
        return allLabels

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
        page = self.__scrape_page()
        if page is None:
            return None

        author_name = page.find("a", class_="author text-bold Link--secondary")
        return None if author_name is None else author_name.text

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
        page = self.__scrape_page()
        if page is None:
            return None

        title_body = page.find("bdi", class_="js-issue-title markdown-title")
        return None if title_body is None else title_body.text.strip()

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
        page = self.__scrape_page()
        if page is None:
            return None

        relative_time = page.find("relative-time")
        return None if relative_time is None else relative_time.text

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
        page = self.__scrape_page()
        if page is None:
            return None

        milestone = page.find(
            "a", class_="Link--secondary mt-1 d-block text-bold css-truncate"
        )
        return None if milestone is None else milestone.text.strip()
