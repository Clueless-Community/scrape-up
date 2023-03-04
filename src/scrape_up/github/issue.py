import requests
from bs4 import BeautifulSoup


class Issue:
    def __init__(self, username: str, repository_name: str, issue_number: int):
        self.username = username
        self.repository = repository_name
        self.issue_number = issue_number

    def __scrape_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/issues/{self.issue_number}"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def assignees(self):
        """
        Fetch list of assignees
        """
        data = self.__scrape_page()
        try:
            assignees_body = data.find("span", class_="css-truncate js-issue-assignees")
            assignees = []
            for assignee in assignees_body.find_all(
                "a", class_="assignee Link--primary css-truncate-target width-fit"
            ):
                assignees.append(assignee.text.replace("\n", "").strip())
            return {
                "data": assignees,
                "message": f"Found assignees for {self.repository}",
            }
        except:
            message = f"No assignees found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def labels(self):
        """
        Fetch labels of issues
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
            return {
                "data": allLabels,
                "message": f"Found labels for {self.repository}",
            }
        except:
            message = f"No labels found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def opened_by(self):
        """
        Fetch the name of the user, who opened the issue
        """
        data = self.__scrape_page()
        try:
            author_name = data.find("a", class_="author text-bold Link--secondary").text
            return {
                "data": author_name,
                "message": f"Found author for {self.repository}",
            }
        except:
            message = f"No author found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def title(self):
        """
        Fetch title of the issue
        """
        data = self.__scrape_page()
        try:
            title_body = data.find("bdi", class_="js-issue-title markdown-title")
            title = title_body.text.strip()
            return {
                "data": title,
                "message": f"Found title for {self.repository}",
            }
        except:
            message = f"No title found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def opened_at(self):
        """
        Returns a string containing the time when the issue was opened in ISO format
        """
        try:
            data = self.__scrape_page()
            return {
                "data": data.find("relative-time").text,
                "message": f"Found time for {self.repository}",
            }
        except:
            message = f"No time found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def is_milestone(self):
        """
        Returns the milestone, if the issue is part of one or 'No milestone', if it's not.
        """
        data = self.__scrape_page()
        try:
            milestone = data.find(
                "a", class_="Link--secondary mt-1 d-block text-bold css-truncate"
            ).text.strip()
            return {
                "data": milestone,
                "message": f"Found milestone for {self.repository}",
            }
        except:
            message = f"No milestone found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }
