import requests
from bs4 import BeautifulSoup


class PullRequest:
    def __init__(self, username: str, repository_name: str, pull_request_number: int):
        self.username = username
        self.repository = repository_name
        self.pr_number = pull_request_number

    def __scrape_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def labels(self):
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
            return {
                "data": labels_found,
                "message": f"Found labels for {self.repository}",
            }
        except:
            message = f"No labels found for {self.repository}"
            return {
                "data": labels_found,
                "message": message,
            }

    def commits(self):
        """
        Fetch the number of commits made in a pull request
        """
        data = self.__scrape_page()
        try:
            commits_count = data.find("span", id="commits_tab_counter").text.strip()
            return {
                "data": commits_count,
                "message": f"Found {commits_count} commits for {self.pr_number}",
            }
        except:
            message = f"No commits found for {self.pr_number}"
            return {
                "data": None,
                "message": message,
            }

    def title(self):
        """
        Fetch the title of a pull request
        """
        data = self.__scrape_page()
        try:
            title_body = data.find("bdi", class_="js-issue-title markdown-title")
            title = title_body.text.strip()
            return {
                "data": title,
                "message": f"Found title for {self.pr_number}",
            }
        except:
            message = f"No title found for {self.pr_number}"
            return {
                "data": None,
                "message": message,
            }

    def __files_changed_body(self):
        """
        scrape the data of files changed in a pull request
        """
        link = f"https://github.com/{self.username}/{self.repository}/pull/{self.pr_number}/files"
        data = requests.get(link)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def files_changed(self):
        """
        Fetch the number of files changed in a pull request
        """
        data = self.__files_changed_body()
        try:
            files_changed_body = data.find("span", id="files_tab_counter")
            files_changed = files_changed_body.text.strip()
            return {
                "data": files_changed,
                "message": f"Found {files_changed} files changed for {self.pr_number}",
            }
        except:
            message = f"No files changed found for {self.pr_number}"
            return {
                "data": None,
                "message": message,
            }

    def reviewers(self):
        """
        Get the list of reviewers assigned in a PR
        """
        data = self.__scrape_page()
        try:
            reviewerList = []
            reviewers = data.find_all(
                "span", class_="css-truncate-target width-fit v-align-middle"
            )
            if len(reviewers) == 0:
                message = f"No reviewers found for {self.pr_number}"
                return {
                    "data": reviewerList,
                    "message": message,
                }
            else:
                for reviewer in reviewers:
                    reviewerList.append(reviewer.text)
                return {
                    "data": reviewerList,
                    "message": f"Found {len(reviewerList)} reviewers for {self.pr_number}",
                }
        except:
            message = f"No reviewers found for {self.pr_number}"
            return {
                "data": None,
                "message": message,
            }
