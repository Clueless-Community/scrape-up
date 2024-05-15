import requests
from bs4 import BeautifulSoup, ResultSet, Tag
import requests_html
import os


class Repository:
    """
    Create an instance of the class `Repository`
    ```python
    repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
    ```

    | Methods                    | Details                                                                                                                                                        |
    | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `.fork_count()`            | Returns the number of forks of a repository.                                                                                                                   |
    | `.get_contributors()`      | Returns the number of contributors of a repository.                                                                                                            |
    | `.topics()`                | Returns the topics of a repository.                                                                                                                            |
    | `.pull_requests()`         | Returns the number of pull requests opened in a repository.                                                                                                    |
    | `.last_update_at()`        | Returns the last updated date of a repository.                                                                                                                 |
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
    | `.get_insights(period)`    | Returns the active pr count, active issue count, merged pr count, open pr count, closed issue count, new issue count, list of recent merged prs,
                                   list of recent open prs, list of recent closed issues, list of recent open issues for a specified period                                                                           |
    """

    def __init__(self, username: str, repository_name: str):
        self.username = username
        self.repository = repository_name
        self._timeout = 10

    def __str__(self):
        return f"{self.repository} belongs to {self.username}"

    def __scrape_page(self):
        url = f"https://github.com/{self.username}/{self.repository}"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_tags_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/tags"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_issues_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/issues"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_pull_requests_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/pulls"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_deployments_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/deployments/activity_log"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_watchers_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/watchers"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_stargazers_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/stargazers"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_insights_page(self, period: str):
        url = f"https://github.com/{self.username}/{self.repository}/pulse/{period}"
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_contributors_page(self):
        url = (
            f"https://github.com/{self.username}/{self.repository}/graphs/contributors"
        )
        data = requests.get(url, timeout=self._timeout)
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def languagesUsed(self):
        """
        Class - `Repository`
        Example:
        ```pyhon
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        languagesUsed = repository.languagesUsed()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        languages = page.find_all(class_="color-fg-default text-bold mr-1")
        allLanguages = [str(item)[46::-7] for item in languages]
        return allLanguages

    def about(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        about = repository.about()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        tag = page.find(class_="f4 mb-3")
        about = tag.getText() if tag is not None else ""
        return about

    def fork_count(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        fork_count = repository.fork_count()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        stats_body = page.find(
            "ul", class_="pagehead-actions flex-shrink-0 d-none d-md-inline"
        )
        if not isinstance(stats_body, Tag):
            return None

        forks = stats_body.find("span", id="repo-network-counter")
        return forks.text.strip() if forks is not None else None

    def topics(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        topics = repository.topics()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        topics = page.find_all(class_="topic-tag topic-tag-link")
        all_topics = [topic.text for topic in topics]
        return all_topics

    def star_count(self):
        """
        Class - `Repository`

        Example:
        ```pyhton
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        star_count = repository.star_count()
        ```
        """
        page = self.__scrape_stargazers_page()
        if page is None:
            return None

        stars_count_tag = page.find("span")
        if stars_count_tag is None:
            return None
        return stars_count_tag.text.strip()

    def pull_requests(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        pull_requests = repository.pull_requests()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        pull_requests = page.find(
            "span", {"id": "pull-requests-repo-tab-count", "class": "Counter"}
        )
        return int(pull_requests.text.replace(",", "")) if pull_requests else None

    def tags(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        tags = repository.tags()
        ```
        """
        page = self.__scrape_tags_page()
        if page is None:
            return None

        tags = page.find_all(class_="Link--primary")
        allTags = [tag.text for tag in tags]
        return allTags

    def releases(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        releases = repository.releases()
        ```
        """
        page = self.__scrape_tags_page()
        if page is None:
            return None

        releases = page.find_all(class_="Link--primary")
        allReleases = [release.text for release in releases]
        return allReleases

    def issues_count(self):
        """
        Class - `Repository`

        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        issues_count = repository.issues_count()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        issues = page.find("span", {"id": "issues-repo-tab-count"})
        return issues.text.strip() if issues else None

    def readme(self):
        """
        Class - `Repository`

        *This downloads the README.md in the root directory*

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        readme = repository.readme()
        ```
        """
        url = f"https://raw.githubusercontent.com/{self.username}/{self.repository}/main/README.md"
        r = requests.get(url, timeout=self._timeout, stream=True)

        with open("out.md", "w", encoding="utf-8") as f:
            f.write(r.text)

    def get_pull_requests_ids(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_pull_requests_ids = repository.get_pull_requests_ids()
        ```
        """
        page = self.__scrape_pull_requests_page()
        if page is None:
            return None

        pr_body = page.find(
            "div", class_="js-navigation-container js-active-navigation-container"
        )
        if not isinstance(pr_body, Tag):
            return None

        pull_requests = pr_body.find_all(
            "a",
            class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title",
        )
        pull_requests_ids = [
            str(pull_request["href"]).rsplit("/", 1)[-1]
            for pull_request in pull_requests
        ]

        return pull_requests_ids

    def commits(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        commits = repository.commits()
        ```
        """
        data = self.__scrape_page()
        if data is None:
            return None

        commits = "\n".join(data.find_all(class_="d-none d-sm-inline"))
        s = commits.split("<strong>", 2)
        s = s[1].split("</strong>", 1)
        commits = int(s[0].replace(",", "").strip())
        return commits

    def get_issues(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_issues = repository.get_issues()
        ```
        """
        page = self.__scrape_issues_page()
        if page is None:
            return None

        issues = page.find_all(
            class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"
        )
        allIssues = [issue.text for issue in issues]
        return allIssues

    def get_contributors(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_contributors = repository.get_contributors()
        ```
        """
        page = self.__scrape_contributors_page()
        if page is None:
            return None

        contributors = page.find_all("a", class_="text-normal")
        contributor_names = [contributor.get_text() for contributor in contributors]
        return contributor_names

    def last_update_at(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        last_update_at = repository.last_update_at()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        update = page.find("relative-time", class_="no-wrap")
        return update.get_text() if update else None

    def get_readme(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_readme = repository.get_readme()
        ```
        """
        data = requests.get(
            f"https://raw.githubusercontent.com/{self.username}/{self.repository}/master/README.md",
            timeout=self._timeout,
            stream=True,
        )
        if data.status_code != 200:
            return "README.md does not exist"

        path = f"./{self.username}"
        os.makedirs(path, exist_ok=True)

        with open(f"{path}/README.md", "w", encoding="utf-8") as fo:
            fo.write(data.text)
        return "README.md found & saved"

    def get_environment(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_environment = repository.get_environment()
        ```
        """

        page = self.__scrape_deployments_page()
        if page is None:
            return None

        link = page.find("a", class_="select-menu-item")
        return link.get("href", None) if isinstance(link, Tag) else None

    def get_branch(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_branch = repository.get_branch()
        ```
        """
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/branches",
            timeout=self._timeout,
        )
        if data.status_code != 200:
            return None

        soup = BeautifulSoup(data.text, "html.parser")
        branches = soup.find_all(
            class_="branch-name css-truncate-target v-align-baseline width-fit mr-2 Details-content--shown"
        )
        allBranches = [branch.text.strip() for branch in branches]
        return allBranches

    def watch_count(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        watch_count = repository.watch_count()
        ```
        """
        page = self.__scrape_watchers_page()
        if page is None:
            return None

        ol_tag = page.find("ol", {"class": "gutter"})
        if not isinstance(ol_tag, Tag):
            return None

        watches = len(ol_tag.find_all("li"))
        return watches

    def all_watchers(self):
        """
        Class - `Repository`

        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        all_watchers = repository.all_watchers()
        ```
        """
        page = self.__scrape_watchers_page()
        if page is None:
            return None

        ol_tag = page.find("ol", {"class": "gutter"})
        if not isinstance(ol_tag, Tag):
            return None

        watchers_tags = ol_tag.find_all("a", {"data-hovercard-type": "user"})[1::2]
        watchers = [watcher.text.strip() for watcher in watchers_tags]
        return watchers

    def get_insights(self, period: str):
        """
        Class - `Repository`.
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        insights = repository.get_insights(period)
        period parameter accepts: "daily", "halfweekly", "weekly", "monthly" or ""
        ```
        Return\n
        ```js
        {
            "active_pr_count": active_pr_count,
            "active_issue_count": active_issue_count,
            "merged_pr_count": merged_pr_count,
            "open_pr_count": open_pr_count,
            "closed_issue_count": closed_issue_count,
            "new_issue_count": new_issue_count,
            "recent_merged_prs": recent_merged_prs_list,
            "recent_open_prs": recent_open_prs_list,
            "recent_closed_issues": recent_closed_issues_list,
            "recent_open_issues": recent_open_issues_list,
        }
        ```
        """
        page = self.__scrape_insights_page(period)
        if page is None:
            return None

        overview = {"overview": []}
        recent_merged_prs_list = []
        recent_open_prs_list = []
        recent_closed_issues_list = []
        recent_open_issues_list = []
        one = page.find_all("div", class_="mt-2")

        try:
            active_pr_count = one[0].find("span").getText()
        except IndexError:
            active_pr_count = ""

        try:
            active_issue_count = one[1].find("span").getText()
        except IndexError:
            active_issue_count = ""

        two = page.find_all("span", class_="d-block h4 color-fg-default")

        try:
            merged_pr_count = two[0].getText().strip()
        except IndexError:
            merged_pr_count = ""

        try:
            open_pr_count = two[1].getText().strip()
        except IndexError:
            open_pr_count = ""

        try:
            closed_issue_count = two[2].getText().strip()
        except IndexError:
            closed_issue_count = ""

        try:
            new_issue_count = two[3].getText().strip()
        except IndexError:
            new_issue_count = ""

        base = page.find_all("ul", class_="list-style-none my-4")
        recent_merged_prs = base[0].find_all("li", class_="clearfix")
        recent_open_prs = base[1].find_all("li", class_="clearfix")
        recent_closed_issues = base[2].find_all("li", class_="clearfix")
        recent_open_issues = base[3].find_all("li", class_="clearfix")

        def add_item(items: ResultSet[Tag], name: str):
            item_list = []
            for item in items:
                a_tag = item.find("a")
                p_tag = item.find("p")
                p_span_tag = p_tag.find("span") if isinstance(p_tag, Tag) else None
                relative_time = item.find("relative-time")

                title = a_tag.getText() if isinstance(a_tag, Tag) else ""
                link = str(a_tag.get("href", "")) if isinstance(a_tag, Tag) else ""
                issue = p_span_tag.getText() if p_span_tag else ""
                date = relative_time.getText() if isinstance(relative_time, Tag) else ""
                item_list.append(
                    {
                        f"{name}_title": title,
                        f"{name}_no": issue,
                        f"{name}_date": date,
                        f"{name}_link": "https://github.com" + link,
                    }
                )
            return item_list

        recent_merged_prs_list = add_item(recent_merged_prs, "pr")
        recent_open_prs_list = add_item(recent_open_prs, "pr")
        recent_closed_issues_list = add_item(recent_closed_issues, "issue")
        recent_open_issues_list = add_item(recent_open_issues, "issue")

        overview["overview"].append(
            {
                "active_pr_count": active_pr_count,
                "active_issue_count": active_issue_count,
                "merged_pr_count": merged_pr_count,
                "open_pr_count": open_pr_count,
                "closed_issue_count": closed_issue_count,
                "new_issue_count": new_issue_count,
                "recent_merged_prs": recent_merged_prs_list,
                "recent_open_prs": recent_open_prs_list,
                "recent_closed_issues": recent_closed_issues_list,
                "recent_open_issues": recent_open_issues_list,
            }
        )
        return overview["overview"]
