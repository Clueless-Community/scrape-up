import requests
from bs4 import BeautifulSoup

import requests_html
import os





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
            # return allLanguages  # return list of languages
            return {
                "data": allLanguages,
                "message": f"Languages used in {self.repository} repository",
            }
        except:
            message = f"No languages found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def about(self):
        """
        Fetch details in about section of repository
        """
        data = self.__scrape_page()

        try:
            tag = data.find(class_="f4 mb-3")
            about = tag.get_text()
            return {
                "data": about,
                "message": f"About {self.repository} repository",
            }
        except:
            message = f"No details found in the about section of {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            return {
                "data": fork_count,
                "message": f"Number of forks of {self.repository} repository",
            }
        except:
            message = f"No forks found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            return {
                "data": allTopics,
                "message": f"Topics of {self.repository} repository",
            }
        except:
            message = f"No topics found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            return {
                "data": starCount,
                "message": f"Star count of {self.repository} repository",
            }
        except:
            message = f"No stars found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            return {
                "data": pull_requests,
                "message": f"Pull requests of {self.repository} repository",
            }
        except:
            message = f"No pull requests found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def tags(self):
        """
        Fetch last ten tags of repository
        """
        data = self.__scrape_tags_page()
        try:
            tags = data.find_all(class_="Link--primary")
            allTags = []
            for item in tags:
                allTags.append(item.text)
            return {
                "data": allTags,
                "message": f"Tags of {self.repository} repository",
            }
        except:
            message = f"No tags found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def releases(self):
        """
        Fetch last ten releases of repository
        """
        data = self.__scrape_tags_page()
        try:
            releases = data.find_all(class_="Link--primary")
            allReleases = []
            for item in releases:
                allReleases.append(item.text)
            return {
                "data": allReleases,
                "message": f"Releases of {self.repository} repository",
            }
        except:
            message = f"No releases found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def issues_count(self):
        """
        Fetch total issues in a repository
        """
        data = self.__scrape_page()
        try:
            issues = data.find("span", {"id": "issues-repo-tab-count"}).text.strip()
            return {
                "data": issues,
                "message": f"Total issues in {self.repository} repository",
            }
        except:
            message = f"No issues found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            message = f"No readme found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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

            return {
                "data": pull_requests_ids,
                "message": f"Pull requests of {self.repository} repository",
            }
        except:
            message = f"No pull requests found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            return {
                "data": commits,
                "message": f"Commits of {self.repository} repository",
            }
        except:
            message = f"No commits found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

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
            return {
                "data": allIssues,
                "message": f"Issues of {self.repository} repository",
            }
        except:
            message = f"No issues found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def get_contributors(self):
        data = self.__scrape_page()

        try:
            contributors = data.find_all(
                "a", href=f"/{self.username}/{self.repository}/graphs/contributors"
            )
            contributor = []
            for it in contributors:
                contributor.append(it.get_text())
            return {
                "data": contributor[0].strip(),
                "message": f"Contributors of {self.repository} repository",
            }
        except:
            message = f"No contributors found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }


    def last_update_at(self):
        data=self.__scrape_page()
        try:
            update=data.find_all("relative-time", class_="no-wrap")
            return update[0].get_text()
        except:
            message="Oops! No Repo or Organization found"
            return message
    

            

    def get_readme(self):
        """
        Get the special repository of the user and save it locally.
        """
        data = requests.get(
            f"https://raw.githubusercontent.com/{self.username}/{self.username}/master/README.md"
        )
        if data.status_code == 404:
            data = requests.get(
                f"https://raw.githubusercontent.com/{self.username}/{self.username}/main/README.md"
            )
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
                return error
            data = data.text
            readmeFile = os.open(path + "/README.md", os.O_RDWR | os.O_CREAT)
            os.write(readmeFile, data.encode("utf-8"))
            message = "README.md found & saved"
            return message
