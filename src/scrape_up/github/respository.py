import requests
from bs4 import BeautifulSoup
import requests_html


<<<<<<< HEAD


=======
>>>>>>> 9d7599db2898e58413d0191ce4580d48138c853b
class Repository:
    def __init__(self, username: str, repository_name: str):
        self.username = username
        self.repository = repository_name

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_tags_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/tags"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_releases_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/releases"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_issues_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/issues"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_pull_requests_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/pulls"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def languagesUsed(self):
        """
        Fetch list of languages used in repository
        """
        data = self.__scrape_page()

        try:
            languages = data.find_all( class_="color-fg-default text-bold mr-1")
            allLanguages = []
            for item in languages:
                allLanguages.append(item.text)
            allTopics = list(map(lambda s: s.strip(), allTopics))
            return allLanguages  # return list of languages
        except:
            message = "No languages found"
            return message

    def about(self):
        """
        Fetch details in about section of repository
        """
        data = self.__scrape_page()

        try:
            tag = data.find(class_="f4 mb-3")
            about = tag.get_text()
            return about  # return string about
        except:
            message = "No details found in the about section"
            return message

    def fork_count(self):
        """
        Returns the number of forks of the repository
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
            message = f"Repository Stats are not found for username {self.username}"
            return message

    def topics(self):
        """
        Fetch topics of repository
        """
        data = self.__scrape_page()

        try:
            topics = data.find_all(class_="topic-tag topic-tag-link")
            allTopics = []
            print(allTopics)
            for item in topics:
                allTopics.append(item.text)
            return allTopics  # return list of topics
        except:
            message = "No topics found"
            return message

    def star_count(self):
        """
        Fetch star count of a repository
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
            message = "Oops! No Stars found"
            return message

    def pull_requests(self):
        """
        Get the number of pull requests opened in a repository.
        """
        data = self.__scrape_page()
        try:
            pull_requests = (
                data.find_all(class_="UnderlineNav-item mr-0 mr-md-1 mr-lg-3")[2]
                .find_all("span")[1]
                .text.strip()
            )
            return pull_requests
        except:
            message = "Failed to fetch pull requests"
            return message

    def tags(self):
        """
        Fetch last ten tags of repository
        """
        data = self.__scrape_tags_page()

        tags = data.find_all(class_="Link--primary")
        allTags = []
        for item in tags:
            allTags.append(item.text)
        if len(allTags):
            return allTags  # return list of tags
        else:
            message = "No tag found"
            return message

    def releases(self):
        """
        Fetch last ten releases of repository
        """
        data = self.__scrape_tags_page()

        releases = data.find_all(class_="Link--primary")
        allReleases = []
        for item in releases:
            allReleases.append(item.text)
        if len(allReleases):
            return allReleases  # return list of releases
        else:
            message = "No releases found"
            return message

    def issues_count(self):
        """
        Fetch total issues in a repository
        """
        data = self.__scrape_page()
        try:
            issues = data.find("span", {"id": "issues-repo-tab-count"}).text.strip()
            return issues
        except:
            message = "Failed to fetch no. of issues"
            return message

    def readme(self):
        """
        Fetch readme.md of a user
        """
        session = requests_html.HTMLSession()
        r = session.get(
            f"https://github.com/{self.username}/{self.username}/blob/main/README.md"
        )
        markdown_content = r.text

        try:
            with open("out.md", "w", encoding="utf-8") as f:
                f.write(markdown_content)
        except:
            err = f"No readme found for {self.username}"
            return err

    def get_pull_requests_ids(self):
        """
        Fetch all opened pull requests id's of a repository
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
            message = "No pull requests found"
            return message

    def commits(self):
        """
        Fetch the number of commits in a repository
        """
        data = self.__scrape_page()
        try:
            commits = (
                data.find("a", href=f"/{self.username}/{self.repository}/commits")
                .find("span")
                .text.strip()
            )
            return commits
        except:
            message = "No commits found"

    def get_issues(self):
        """
        Fetch the list of issues in a respository
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
            message = "Failed to fetch list of issues"
            return message

    def get_contributors(self):
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
<<<<<<< HEAD
            message="Oops! No contributors found"
            return message 


=======
            message = "Oops! No contributors found"
            return message
>>>>>>> 9d7599db2898e58413d0191ce4580d48138c853b
