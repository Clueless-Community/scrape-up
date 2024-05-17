from bs4 import BeautifulSoup
from scrape_up.config.request_config import RequestConfig, get
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

    def __init__(self, username: str, *, config: RequestConfig = RequestConfig()):
        self.username = username
        self.config = config

    def __str__(self):
        return f" The username is: {self.username}"

    def __scrape_page(self):
        username = self.username
        data = get(f"https://github.com/{username}", self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self) -> str:
        """
        Class - `Users`
        ```python
        user = github.User(username="nikhil25803")
        followers = user.followers()
        ```
        """
        page = self.__scrape_page()
        try:
            followers = page.find(class_="text-bold color-fg-default")
            return followers.text
        except:
            return None

    def following(self):
        """
        Class - `Users`\n
        ```python
        user = github.User(username="nikhil25803")
        following = user.following()
        ```
        """
        page = self.__scrape_page()
        try:
            following = page.find_all(class_="text-bold color-fg-default")

            return following[1].text
        except:
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
        try:
            avatar = page.find(
                class_="avatar avatar-user width-full border color-bg-default"
            )
            return avatar["src"]
        except:
            return None

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
        try:
            bio = page.find(
                class_="p-note user-profile-bio mb-3 js-user-profile-bio f4"
            )
            return bio.text
        except:
            return None

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
        try:
            pinned_repos = page.find_all(
                class_="mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6"
            )
            titles = [repo.find("span", class_="repo").text for repo in pinned_repos]
            return titles
        except:
            return None

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
        try:
            count_repo = page.find_all(class_="Counter")
            count_repo_list = []
            for word in count_repo:
                find_all_example = word.get_text()
                count_repo_list.append(find_all_example)
            return count_repo_list[0]
        except:
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
        try:
            count_star = page.find_all(class_="Counter")
            count_star_list = []
            for words in count_star:
                find_all_example = words.get_text()
                count_star_list.append(find_all_example)
            return count_star_list[3]
        except:
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
        try:
            contributions = page.find("h2", class_="f4 text-normal mb-2")
            return " ".join(contributions.text.split())
        except:
            return None

    def __get_repo_page(self):
        """
        Scrape the repositories page of a GitHub user.
        """
        username = self.username
        repo_data = get(f"https://github.com/{username}?tab=repositories", self.config)
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
        try:
            repo_body = page.find("div", id="user-repositories-list")
            repositories = []
            if repo_body != None:
                for repo in repo_body.find_all(
                    "div", class_="col-10 col-lg-9 d-inline-block"
                ):
                    repositories.append("https://github.com" + repo.a["href"])
            return repositories
        except:
            return None

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
        try:
            orgs = [org.login for org in page.get_orgs()]
            return orgs
        except:
            return None

    def get_achievements(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_achievements = user.get_achievements()
        ```
        """
        try:
            achievement = []
            data = self.__scrape_page()
            data = data.find_all("img", class_="achievement-badge-sidebar", alt=True)
            itr = 0
            while itr < len(data) / 2:
                achievement.append(data[itr]["alt"].split(":")[1].strip(" "))
                itr = itr + 1

            return achievement
        except:
            return None

    def __get_starred_page(self):
        """
        Scrape the starred page of a GitHub user.
        """
        username = self.username
        starred_data = get(f"https://github.com/{username}?tab=stars", self.config)
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
        try:
            starred_body = page.find("turbo-frame", id="user-starred-repos")
            starred_repos = []
            if starred_body != None:
                for repo in starred_body.find_all(
                    "div",
                    class_="col-12 d-block width-full py-4 border-bottom color-border-muted",
                ):
                    starred_repos.append("https://github.com" + repo.a["href"])
            return starred_repos
        except:
            return None

    def __scrape_followers_page(self):
        """
        Scrape the followers page of a GitHub user.
        """
        username = self.username
        url = f"https://github.com/{username}?tab=followers"
        followers_data = get(url, self.config)
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
        try:
            followers_body = page.find("turbo-frame", id="user-profile-frame")
            followers = []
            for user in followers_body.find_all("span", class_="Link--secondary"):
                followers.append(user.text.strip())

            return followers
        except:
            return None

    def __scrape_following_page(self):
        """

        Scrape the following page of a GitHub user.
        """
        username = self.username
        url = f"https://github.com/{username}?tab=following"
        following_data = get(url, self.config)
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
        try:
            following_body = page.find("turbo-frame", id="user-profile-frame")
            following = []
            for user in following_body.find_all("span", class_="Link--secondary"):
                following.append(user.text.strip())

            return following
        except:
            return None

    def company(self):
        page = self.__scrape_following_page()
        try:
            cmp = page.find(class_="Link--primary")
            return cmp.text
        except:
            return None

    def get_status(self):
        """Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_status = user.get_status()
        ```
        """
        try:
            data = self.__scrape_page()
            t = data.find(
                "div", class_="user-status-container position-relative hide-sm hide-md"
            )
            return t.text.strip().replace("\n", "")
        except:
            return None

    def get_contribution_streak(self):
        """
         Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_contribution_streak = user.get_contribution_streak()
        ```
        """
        try:
            data = self.__scrape_page()
            t = data.find_all("rect", class_="ContributionCalendar-day")
            array = []
            for a in t:
                contri = a.get_text()
                if contri:
                    if contri[0] == "N":
                        array.append(0)
                    else:
                        array.append(1)

            count = 0
            result = 0

            for i in range(0, len(array)):
                if array[i] == 0:
                    count = 0.0
                else:
                    count += 1
                    result = max(result, count)
            return int(result)
        except:
            return None

    def __get_page_details(self, link: str):
        """
        scrape the data in the page
        """
        data = get(link, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def get_pages(self, curr_repo_link, pages_links):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_pages = user.get_pages()
        ```
        """
        try:
            data = self.__get_page_details(curr_repo_link)
            pages_body = data.find("div", class_="paginate-container")
            if pages_body.find("a", class_="next_page") != None:
                pages_links.append(
                    "https://github.com"
                    + pages_body.find("a", class_="next_page")["href"]
                )
                self.get_pages(pages_links[-1], pages_links)

            return pages_links
        except:
            return None

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
        try:
            # get all the pages of the repositories
            pages_links = self.get_pages(repository_link, [repository_link])
            repositories = []
            for page in pages_links:
                page_data = self.__get_page_details(page)
                # get the repositories in the page
                repositories_body = page_data.find("div", id="user-repositories-list")
                for repo in repositories_body.find_all("li"):
                    repo_name = repo.find(
                        "a", attrs={"itemprop": "name codeRepository"}
                    ).text.strip()
                    repo_url = f"https://github.com/{repo.find('a', attrs = {'itemprop': 'name codeRepository'})['href']}"
                    repo_description_body = repo.find(
                        "p", attrs={"itemprop": "description"}
                    )
                    repo_description = (
                        repo_description_body.text.strip()
                        if repo_description_body != None
                        else "No description"
                    )
                    repo_language_body = repo.find(
                        "span", attrs={"itemprop": "programmingLanguage"}
                    )
                    repo_language = (
                        repo_language_body.text.strip()
                        if repo_language_body != None
                        else "No language"
                    )
                    # create a repository object
                    repository_name = repo_url.split("/")[-1]
                    repository = Repository(username, repository_name)
                    repo_forks, repo_stars, repo_issues, repo_pull_requests = (
                        repository.fork_count(),
                        repository.star_count(),
                        repository.issues_count(),
                        repository.pull_requests(),
                    )
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
        except:
            return None

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

        repo_elements = page.select("#user-repositories-list ul li")
        repositories = []

        try:
            for repo_element in repo_elements:
                link = repo_element.find("a")["href"]
                repositories.append(f"https://github.com{link}")

                name = repo_element.find("a").text.split("/")[-1]
                repositories.append(name.replace("\n", ""))

                description = (
                    repo_element.find("p").get_text(strip=True)
                    if repo_element.find("p")
                    else None
                )
                # description= description.replace('\n','')
                repositories.append(description)

                url1 = f"https://github.com{link}"
                response1 = get(url1, self.config)
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
                pullresponse = get(
                    pullurl, self.config
                )  # getting the content of pull requests page
                issueresponse = get(
                    issuesurl, self.config
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
                num_of_pull_requests = (
                    pullrequests.text.strip() if pullrequests else "N/A"
                )
                repositories.append(num_of_pull_requests.replace("\n", ""))

                issues = i_soup.select_one("span#issues-repo-tab-count")
                num_of_issues = issues.text.strip() if issues else "N/A"
                repositories.append(num_of_issues.replace("\n", ""))

            return repositories
        except:
            return None

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

        repo_elements = page.select("#user-repositories-list ul li")
        merged_pull_requests = []

        try:
            forked_repos = []
            for repo_element in repo_elements:
                forked_repo = repo_element.select_one("h3+span a")

                if forked_repo:
                    forked_repo = "https://github.com" + forked_repo.get("href")
                    forked_repos.append(forked_repo)

            for repo in forked_repos:
                closed_pr_url = (
                    repo + f"/pulls?q=is:pr+author:{self.username}+is:merged"
                )

                response = self.__get_page_details(closed_pr_url)
                pr_links = response.select('a[data-hovercard-type="pull_request"]')
                links = ["https://github.com" + link["href"] for link in pr_links]

                merged_pull_requests.extend(links)
        except:
            return None

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

        repo_elements = page.select("#user-repositories-list ul li")
        open_issues = []

        try:
            forked_repos = []
            for repo_element in repo_elements:
                forked_repo = repo_element.select_one("h3+span a")

                if forked_repo:
                    forked_repo = "https://github.com" + forked_repo.get("href")
                    forked_repos.append(forked_repo)

            for repo in forked_repos:
                open_issues_url = repo + f"/issues/created_by/{self.username}"

                response = self.__get_page_details(open_issues_url)
                issues_list = response.select(
                    'div[aria-label="Issues"] div[data-pjax="#repo-content-pjax-container"]'
                )
                issue_links = [
                    "https://github.com" + issue.select_one("a").get("href")
                    for issue in issues_list
                ]

                open_issues.extend(issue_links)
        except:
            return None

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
        try:
            ul_element = page.find("ul", class_="filter-list small")
            li_element = ul_element.find_all("li")

            years_active = len(li_element)

            return years_active
        except:
            return None
