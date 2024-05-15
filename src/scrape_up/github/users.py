from typing import List, Union
import requests
from bs4 import BeautifulSoup, Tag
from scrape_up.github.repository import Repository


class Users:
    """
    Create an instance of the class `Users`
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
    """

    def __init__(self, username: str):
        self.username = username
        self._timeout: int = 10

    def __str__(self):
        return f" The username is: {self.username}"

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://github.com/{username}", timeout=self._timeout)
        if data.status_code != 200:
            return None
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self) -> Union[str, None]:
        """
        Class - `Users`
        ```python
        user = github.User(username="nikhil25803")
        followers = user.followers()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        followers = page.find(class_="text-bold color-fg-default")
        return followers.text if followers is not None else None

    def following(self):
        """
        Class - `Users`\n
        ```python
        user = github.User(username="nikhil25803")
        following = user.following()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        try:
            following = page.find_all(class_="text-bold color-fg-default")
            return following[1].text
        except IndexError:
            return None

    def get_avatar(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_avatar = user.get_avatar()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        avatar = page.find(
            class_="avatar avatar-user width-full border color-bg-default"
        )
        return avatar["src"] if isinstance(avatar, Tag) else None

    def get_bio(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_bio = user.get_bio()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        bio = page.find(class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
        return bio.text if bio is not None else None

    def get_repo(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_repo = user.get_repo()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        pinned_repos = page.find_all(
            class_="mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6"
        )
        titles = [repo.find("span", class_="repo").text for repo in pinned_repos]
        return titles if pinned_repos else None

    def repo_count(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        repo_count = user.repo_count()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        try:
            count_repo = page.find_all(class_="Counter")
            return count_repo[0].get_text()
        except IndexError:
            return None

    def star_count(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        star_count = user.star_count()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        try:
            count_star = page.find_all(class_="Counter")
            return count_star[3].get_text()
        except IndexError:
            return None

    def get_yearly_contributions(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_yearly_contributions = user.get_yearly_contributions()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        contributions = page.find("h2", class_="f4 text-normal mb-2")
        if contributions is None:
            return None
        return " ".join(contributions.text.split())

    def __get_repo_page(self):
        """
        Scrape the repositories page of a GitHub user.
        """
        username = self.username
        repo_data = requests.get(
            f"https://github.com/{username}?tab=repositories",
            timeout=self._timeout,
        )
        if repo_data.status_code != 200:
            return None
        repo_data = BeautifulSoup(repo_data.text, "html.parser")
        return repo_data

    def get_repositories(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_repositories = user.get_repositories()
        ```
        """
        page = self.__get_repo_page()
        if page is None:
            return None
        repo_body = page.find("div", id="user-repositories-list")
        if not isinstance(repo_body, Tag):
            return None
        repos = repo_body.find_all("div", class_="col-10 col-lg-9 d-inline-block")
        repositories = list(map(lambda x: "https://github.com" + x.a["href"], repos))
        return repositories

    def get_organizations(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_organizations = user.get_organizations()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        orgs_res = page.find_all("a", class_="avatar-group-item", href=True)
        orgs = [org.get("href") for org in orgs_res]
        return orgs

    def get_achievements(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_achievements = user.get_achievements()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        achievement = []
        data = page.find_all("img", class_="achievement-badge-sidebar", alt=True)
        itr = 0
        while itr < len(data) / 2:
            achievement.append(str(data[itr]["alt"]).split(":", 2)[1].strip(" "))
            itr = itr + 1
        return achievement

    def __get_starred_page(self):
        """
        Scrape the starred page of a GitHub user.
        """
        username = self.username
        starred_data = requests.get(
            f"https://github.com/{username}?tab=stars",
            timeout=self._timeout,
        )
        if starred_data.status_code != 200:
            return None
        starred_data = BeautifulSoup(starred_data.text, "html.parser")
        return starred_data

    def get_starred_repos(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_starred_repos = user.get_starred_repos()
        ```
        """
        page = self.__get_starred_page()
        if page is None:
            return None

        starred_body = page.find("turbo-frame", id="user-starred-repos")
        if not isinstance(starred_body, Tag):
            return []
        repos = starred_body.find_all(
            "div",
            class_="col-12 d-block width-full py-4 border-bottom color-border-muted",
        )
        return list(map(lambda x: "https://github.com" + x.a["href"], repos))

    def __scrape_followers_page(self):
        """
        Scrape the followers page of a GitHub user.
        """
        username = self.username
        followers_data = requests.get(
            f"https://github.com/{username}?tab=followers",
            timeout=self._timeout,
        )
        if followers_data.status_code != 200:
            return None
        followers_data = BeautifulSoup(followers_data.text, "html.parser")
        return followers_data

    def get_followers(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_followers = user.get_followers()
        ```
        """
        page = self.__scrape_followers_page()
        if page is None:
            return None
        followers_body = page.find("turbo-frame", id="user-profile-frame")
        if not isinstance(followers_body, Tag):
            return []
        followers_data = followers_body.find_all("span", class_="Link--secondary")
        followers = list(map(lambda x: x.text.strip(), followers_data))
        return followers

    def __scrape_following_page(self):
        """

        Scrape the following page of a GitHub user.
        """
        username = self.username
        following_data = requests.get(
            f"https://github.com/{username}?tab=following",
            timeout=self._timeout,
        )
        if following_data.status_code != 200:
            return None
        following_data = BeautifulSoup(following_data.text, "html.parser")
        return following_data

    def get_following_users(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_following_users = user.get_following_users()
        ```
        """
        page = self.__scrape_following_page()
        if page is None:
            return None
        following_body = page.find("turbo-frame", id="user-profile-frame")
        if not isinstance(following_body, Tag):
            return []
        following_data = following_body.find_all("span", class_="Link--secondary")
        following = list(map(lambda x: x.text.strip(), following_data))
        return following

    def company(self):
        page = self.__scrape_following_page()
        if page is None:
            return None
        cmp = page.find(class_="Link--primary")
        return cmp.text if cmp is not None else None

    def get_status(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_status = user.get_status()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        t = page.find(
            "div", class_="user-status-container position-relative hide-sm hide-md"
        )
        if t is None:
            return None
        return t.text.strip().replace("\n", "")

    def get_contribution_streak(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_contribution_streak = user.get_contribution_streak()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        t = page.find_all("rect", class_="ContributionCalendar-day")
        array: List[int] = []
        for a in t:
            contri = a.get_text()
            if contri:
                if contri[0] == "N":
                    array.append(0)
                else:
                    array.append(1)
        count = 0
        result = 0
        for i in array:
            if i == 0:
                count = 0
            else:
                count += 1
                result = max(result, count)
        return result

    def __get_page_details(self, link: str):
        """
        scrape the data in the page
        """
        data = requests.get(link, timeout=self._timeout)
        if data.status_code != 200:
            return None
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def get_pages(self, curr_repo_link: str, pages_links: List[str]):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_pages = user.get_pages()
        ```
        """
        page = self.__get_page_details(curr_repo_link)
        if page is None:
            return pages_links
        pages_body = page.find("div", class_="paginate-container")
        if not isinstance(pages_body, Tag):
            return pages_links
        next_page = pages_body.find("a", class_="next_page")
        if not isinstance(next_page, Tag):
            return pages_links
        pages_links.append(f"https://github.com{next_page.get('href')}")
        self.get_pages(pages_links[-1], pages_links)
        return pages_links

    def get_repository_details(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_repository_details = user.get_repository_details()
        ```
        """
        username = self.username
        repository_link = f"https://github.com/{username}?tab=repositories"
        pages_links = self.get_pages(repository_link, [repository_link])
        # get all the pages of the repositories
        repositories = []
        for page in pages_links:
            page_data = self.__get_page_details(page)
            if page_data is None:
                continue
            # get the repositories in the page
            repositories_body = page_data.find("div", id="user-repositories-list")
            if not isinstance(repositories_body, Tag):
                continue
            for repo in repositories_body.find_all("li"):
                repo_name = repo.find(
                    "a", attrs={"itemprop": "name codeRepository"}
                ).text.strip()
                repo_url = f"https://github.com/{repo.find('a', attrs = {'itemprop': 'name codeRepository'})['href']}"
                repo_description_body = repo.find(
                    "p", attrs={"itemprop": "description"}
                )
                repo_description = (
                    "No description"
                    if repo_description_body is None
                    else repo_description_body.text.strip()
                )
                repo_language_body = repo.find(
                    "span", attrs={"itemprop": "programmingLanguage"}
                )
                repo_language = (
                    "No language"
                    if repo_language_body is None
                    else repo_language_body.text.strip()
                )
                # create a repository object
                repository_name = repo_url.split("/")[-1]
                repository = Repository(username, repository_name)
                repo_forks = repository.fork_count()
                repo_stars = repository.star_count()
                repo_issues = repository.issues_count()
                repo_pull_requests = repository.pull_requests()
                repositories.append(
                    {
                        "name": repo_name,
                        "url": repo_url,
                        "description": repo_description,
                        "language": repo_language,
                        "forks": repo_forks,
                        "stars": repo_stars,
                        "issues": repo_issues,
                        "pull_requests": repo_pull_requests,
                    }
                )
        return repositories

    def get_all_repo_details(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_all_repo_details = user.get_all_repo_details()
        ```
        """
        page = self.__get_repo_page()
        if page is None:
            return None
        repo_elements = page.select("#user-repositories-list ul li")
        repositories: List[str] = []
        for repo_element in repo_elements:
            a_tag = repo_element.find("a")
            if not isinstance(a_tag, Tag):
                continue
            link = a_tag.get("href", None)
            if not isinstance(link, str):
                continue

            repositories.append(f"https://github.com{link}")
            name = a_tag.text.split("/")[-1]
            repositories.append(name.replace("\n", ""))
            p_tag = repo_element.find("p")
            description = p_tag.get_text(strip=True) if p_tag else None
            if description is not None:
                description = description.replace("\n", "")
                repositories.append(description)

            url1 = "https://github.com" + link
            response1 = requests.get(url1, timeout=self._timeout)
            soup = BeautifulSoup(response1.content, "html.parser")
            li_elements = soup.find_all("li", class_="d-inline")
            for li in li_elements:
                language = li.text.strip()
                repositories.append(language.replace("\n", ""))
                stars = soup.find("span", class_="text-bold")
                num_of_stars = stars.text if stars else "N/A"
                repositories.append(num_of_stars.replace("\n", ""))

            pullurl = url1 + "/pulls"
            issuesurl = url1 + "/issues"
            pullresponse = requests.get(
                pullurl, timeout=self._timeout
            )  # getting the content of pull requests page
            issueresponse = requests.get(
                issuesurl, timeout=self._timeout
            )  # getting the content of issues page
            p_soup = BeautifulSoup(
                pullresponse.content, "html.parser"
            )  # creating beautifulsoup object for pull requests page
            i_soup = BeautifulSoup(
                issueresponse.content, "html.parser"
            )  # creating beautifulsoup object for issues page
            # to find number of pull requests
            pullrequests = p_soup.find(
                "div", class_="table-list-header-toggle states flex-auto pl-0"
            )
            num_of_pull_requests = pullrequests.text.strip() if pullrequests else "N/A"
            repositories.append(num_of_pull_requests.replace("\n", ""))
            issues = i_soup.select_one("span#issues-repo-tab-count")
            num_of_issues = issues.text.strip() if issues else "N/A"
            repositories.append(num_of_issues.replace("\n", ""))

        return repositories

    def get_merged_pull_requests(self):
        """
        Returns the list of all the merged PRs\n
        Warning -This methods take longer time to run.\n
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_merged_pull_requests = user.get_merged_pull_requests()
        ```
        """

        page = self.__get_repo_page()
        if page is None:
            return None

        repo_elements = page.select("#user-repositories-list ul li")

        forked_repos: List[str] = []
        for repo_element in repo_elements:
            forked_repo = repo_element.select_one("h3+span a")
            if forked_repo is not None:
                forked_repo = f"https://github.com{forked_repo.get('href')}"
                forked_repos.append(forked_repo)

        merged_pull_requests: List[str] = []
        for repo in forked_repos:
            closed_pr_url = repo + f"/pulls?q=is:pr+author:{self.username}+is:merged"
            response = self.__get_page_details(closed_pr_url)
            if response is None:
                continue
            pr_links = response.select('a[data-hovercard-type="pull_request"]')
            links = [f"https://github.com{link['href']}" for link in pr_links]
            merged_pull_requests.extend(links)

        return merged_pull_requests

    def get_open_issues(self):
        """
        Return the list of open issues.\n
        Warning -This methods take longer time to run.\n
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_open_issues = user.get_open_issues()
        ```
        """

        page = self.__get_repo_page()
        if page is None:
            return None

        repo_elements = page.select("#user-repositories-list ul li")
        open_issues: List[str] = []

        forked_repos: List[str] = []
        for repo_element in repo_elements:
            forked_repo = repo_element.select_one("h3+span a")
            if forked_repo is not None:
                forked_repo = f"https://github.com{forked_repo.get('href')}"
                forked_repos.append(forked_repo)

        for repo in forked_repos:
            open_issues_url = repo + f"/issues/created_by/{self.username}"
            response = self.__get_page_details(open_issues_url)
            if response is None:
                continue
            issues_list = response.select(
                'div[aria-label="Issues"] div[data-pjax="#repo-content-pjax-container"]'
            )
            issue_links = list(
                map(
                    lambda x: str(x.get("href")),
                    filter(lambda x: x.select_one("a"), issues_list),
                )
            )
            open_issues.extend(issue_links)

        return open_issues

    def get_years_active(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        years_active = user.get_years_active()
        ```
        Return `int` - Number of year(s) you have been active on GitHub.
        """
        page = self.__scrape_page()
        if page is None:
            return None

        ul_element = page.find("ul", class_="filter-list small")
        if not isinstance(ul_element, Tag):
            return None
        li_element = ul_element.find_all("li")
        years_active = len(li_element)
        return years_active
