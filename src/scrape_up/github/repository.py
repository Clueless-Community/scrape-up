from bs4 import BeautifulSoup
import requests_html
import os

from scrape_up.config.request_config import RequestConfig, get


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

    def __init__(
        self,
        username: str,
        repository_name: str,
        *,
        config: RequestConfig = RequestConfig(),
    ):
        self.username = username
        self.repository = repository_name
        self.config = config

    def __str__(self):
        return f"{self.repository} belongs to {self.username}"

    def __scrape_page(self):
        url = f"https://github.com/{self.username}/{self.repository}"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_tags_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/tags"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_issues_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/issues"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_pull_requests_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/pulls"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_deployments_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/deployments/activity_log"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_watchers_page(self):
        url = f"https://github.com/{self.username}/{self.repository}/watchers"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_insights_page(self, period):
        url = f"https://github.com/{self.username}/{self.repository}/pulse/{period}"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def languagesUsed(self):
        """
        Class - `Repository`
        Example:
        ```pyhon
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        languagesUsed = repository.languagesUsed()
        ```
        """
        data = self.__scrape_page()

        try:
            languages = data.find_all(class_="color-fg-default text-bold mr-1")
            allLanguages = []
            for item in languages:
                item = str(item)
                item = item[46:]
                item = item[:-7]
                allLanguages.append(item)
            # return allLanguages  # return list of languages
            return allLanguages
        except:
            return None

    def about(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        about = repository.about()
        ```
        """
        data = self.__scrape_page()

        try:
            tag = data.find(class_="f4 mb-3")
            about = tag.get_text()
            return about
        except:
            return None

    def fork_count(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        fork_count = repository.fork_count()
        ```
        """
        data = self.__scrape_page()
        try:
            stats_body = data.find(
                "ul", class_="pagehead-actions flex-shrink-0 d-none d-md-inline"
            )
            forks = stats_body.find("span", id="repo-network-counter")
            fork_count = forks.text.strip()
            return fork_count
        except:
            return None

    def topics(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        topics = repository.topics()
        ```
        """
        data = self.__scrape_page()

        try:
            topics = data.find_all(class_="topic-tag topic-tag-link")
            allTopics = []
            for item in topics:
                allTopics.append(item.text)
            return allTopics
        except:
            return None

    def star_count(self):
        """
        Class - `Repository`
        Example:
        ```pyhton
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        star_count = repository.star_count()
        ```
        """
        try:
            data = self.__scrape_page()
            starCount = (
                data.find("a", href=f"/{self.username}/{self.repository}/stargazers")
                .find("span")
                .text.strip()
            )
            return starCount
        except:
            return None

    def pull_requests(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        pull_requests = repository.pull_requests()
        ```
        """
        data = self.__scrape_page()
        try:
            pull_requests = data.find(
                "span", {"id": "pull-requests-repo-tab-count", "class": "Counter"}
            ).text

            return int(pull_requests.replace(",", ""))
        except:
            return None

    def tags(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        tags = repository.tags()
        ```
        """
        data = self.__scrape_tags_page()
        try:
            tags = data.find_all(class_="Link--primary")
            allTags = []
            for item in tags:
                allTags.append(item.text)
            return allTags
        except:
            return None

    def releases(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        releases = repository.releases()
        ```
        """
        data = self.__scrape_tags_page()
        try:
            releases = data.find_all(class_="Link--primary")
            allReleases = []
            for item in releases:
                allReleases.append(item.text)
            return allReleases
        except:
            return None

    def issues_count(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        issues_count = repository.issues_count()
        ```
        """
        data = self.__scrape_page()
        try:
            issues = data.find("span", {"id": "issues-repo-tab-count"}).text.strip()
            return issues
        except:
            return None

    def readme(self):
        """
        Class - `Repository`\n
        *This downloads the README.md in the root directory*\n
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        readme = repository.readme()
        ```
        """
        session = requests_html.HTMLSession()
        r = session.get(
            f"https://github.com/{self.username}/{self.repository}/blob/main/README.md"
        )
        markdown_content = r.text

        try:
            with open("out.md", "w", encoding="utf-8") as f:
                f.write(markdown_content)
        except:
            return None

    def get_pull_requests_ids(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_pull_requests_ids = repository.get_pull_requests_ids()
        ```
        """
        data = self.__scrape_pull_requests_page()
        try:
            pr_body = data.find(
                "div", class_="js-navigation-container js-active-navigation-container"
            )
            pull_requests_ids = []
            for each_pr in pr_body.find_all(
                "a",
                class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title",
            ):
                pr_id = each_pr["href"].split("/")[-1]
                pull_requests_ids.append(pr_id)

            return pull_requests_ids
        except:
            return None

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
        try:
            commits = str(data.find_all(class_="d-none d-sm-inline"))
            s = commits.split("<strong>")
            s = s[1].split("</strong>")
            commits = int(s[0].replace(",", ""))
            return commits
        except:
            return None

    def get_issues(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_issues = repository.get_issues()
        ```
        """
        data = self.__scrape_issues_page()
        try:
            issues = data.find_all(
                class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"
            )
            allIssues = []

            for item in issues:
                allIssues.append(item.text)
            return allIssues
        except:
            return None

    def get_contributors(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_contributors = repository.get_contributors()
        ```
        """
        data = self.__scrape_page()

        try:
            contributors = data.find_all(
                "a", href=f"/{self.username}/{self.repository}/graphs/contributors"
            )
            contributor = []
            for it in contributors:
                contributor.append(it.get_text())
            return contributor[0].strip()
        except:
            return None

    def last_update_at(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        last_update_at = repository.last_update_at()
        ```
        """
        data = self.__scrape_page()
        try:
            update = data.find_all("relative-time", class_="no-wrap")
            return update[0].get_text()
        except:
            return None

    def get_readme(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_readme = repository.get_readme()
        ```
        """
        url = f"https://raw.githubusercontent.com/{self.username}/{self.repository}/master/README.md"
        data = get(url, self.config)
        if data.status_code == 404:
            data = get(url, self.config)
            if data.status_code == 404:
                message = f"No special repository found with username {self.username}"
                return {
                    "data": None,
                    "message": message,
                }
        else:
            path = f"./{self.username}"
            try:
                os.mkdir(path)
            except OSError as error:
                return None
            data = data.text
            readmeFile = os.open(path + "/README.md", os.O_RDWR | os.O_CREAT)
            os.write(readmeFile, data.encode("utf-8"))
            message = "README.md found & saved"
            return message

    def get_environment(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_environment = repository.get_environment()
        ```
        """
        try:
            data = self.__scrape_deployments_page()
            link = data.find_all("a", class_="select-menu-item")
            return link[0].get("href")
        except:
            return None

    def get_branch(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_branch = repository.get_branch()
        ```
        """
        url = f"https://github.com/{self.username}/{self.repository}/branches"
        data = get(url, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        try:
            branch = data.find_all(
                class_="branch-name css-truncate-target v-align-baseline width-fit mr-2 Details-content--shown"
            )
            allBranches = []
            for branchNames in branch:
                allBranches.append(branchNames.text.strip())
            return allBranches
        except:
            return None

    def watch_count(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        watch_count = repository.watch_count()
        ```
        """
        data = self.__scrape_watchers_page()
        try:
            watches = len(data.find("ol", {"class": "gutter"}).find_all("li"))
            return {
                "data": watches,
                "message": f"Total watches in {self.repository} repository",
            }
        except:
            message = f"No watches found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def all_watchers(self):
        """
        Class - `Repository`
        Example:
        ```python
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        all_watchers = repository.all_watchers()
        ```
        """
        data = self.__scrape_watchers_page()
        try:
            all = data.find("ol", {"class": "gutter"}).find_all(
                "a", {"data-hovercard-type": "user"}
            )[1::2]
            watchers = []
            for watcher in all:
                watchers.append(watcher.text.strip())
            return watchers

        except:
            return None

    def get_insights(self, period):
        self.period = period
        """
        Class - `Repository`.\n
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
        data = self.__scrape_insights_page(self.period)
        try:
            overview = {"overview": []}
            recent_merged_prs_list = []
            recent_open_prs_list = []
            recent_closed_issues_list = []
            recent_open_issues_list = []
            one = data.find_all("div", class_="mt-2")
            try:
                active_pr_count = one[0].find("span").getText()
            except:
                active_pr_count = ""
            try:
                active_issue_count = one[1].find("span").getText()
            except:
                active_issue_count = ""
            two = data.find_all("span", class_="d-block h4 color-fg-default")
            try:
                merged_pr_count = two[0].getText().strip()
            except:
                merged_pr_count = ""
            try:
                open_pr_count = two[1].getText().strip()
            except:
                open_pr_count = ""
            try:
                closed_issue_count = two[2].getText().strip()
            except:
                closed_issue_count = ""
            try:
                new_issue_count = two[3].getText().strip()
            except:
                new_issue_count = ""
            try:
                base = data.find_all("ul", class_="list-style-none my-4")
                recent_merged_prs = base[0].find_all("li", class_="clearfix")
                for pr in recent_merged_prs:
                    try:
                        pr_title = pr.find("a").getText()
                        pr_no = pr.find("p").find("span").getText()
                        pr_date = pr.find("relative-time").getText()
                        pr_link = pr.find("a")["href"]
                        recent_merged_prs_list.append(
                            {
                                "pr_title": pr_title,
                                "pr_no": pr_no,
                                "pr_date": pr_date,
                                "pr_link": "https://github.com" + pr_link,
                            }
                        )
                    except:
                        recent_merged_prs_list = []
                recent_open_prs = base[1].find_all("li", class_="clearfix")
                for pr in recent_open_prs:
                    try:
                        pr_title = pr.find("a").getText()
                        pr_no = pr.find("p").find("span").getText()
                        pr_date = pr.find("relative-time").getText()
                        pr_link = pr.find("a")["href"]
                        recent_open_prs_list.append(
                            {
                                "pr_title": pr_title,
                                "pr_no": pr_no,
                                "pr_date": pr_date,
                                "pr_link": "https://github.com" + pr_link,
                            }
                        )
                    except:
                        recent_open_prs_list = []
                recent_closed_issues = base[2].find_all("li", class_="clearfix")
                for issue in recent_closed_issues:
                    try:
                        issue_title = issue.find("a").getText()
                        issue_no = issue.find("p").find("span").getText()
                        issue_date = issue.find("relative-time").getText()
                        issue_link = issue.find("a")["href"]
                        recent_closed_issues_list.append(
                            {
                                "issue_title": issue_title,
                                "issue_no": issue_no,
                                "issue_date": issue_date,
                                "issue_link": "https://github.com" + issue_link,
                            }
                        )
                    except:
                        recent_closed_issues_list = []
                recent_open_issues = base[3].find_all("li", class_="clearfix")
                for issue in recent_open_issues:
                    try:
                        issue_title = issue.find("a").getText()
                        issue_no = issue.find("p").find("span").getText()
                        issue_date = issue.find("relative-time").getText()
                        issue_link = issue.find("a")["href"]
                        recent_open_issues_list.append(
                            {
                                "issue_title": issue_title,
                                "issue_no": issue_no,
                                "issue_date": issue_date,
                                "issue_link": "https://github.com" + issue_link,
                            }
                        )
                    except:
                        recent_open_issues_list = []
            except:
                pass
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
        except:
            return None
