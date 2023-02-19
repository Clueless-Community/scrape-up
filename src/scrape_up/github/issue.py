import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

class Issue:

    def __init__(self, username: str, repository_name:str, issue_number:int):
        self.username = username
        self.repository = repository_name
        self.issue_number = issue_number

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}/issues/{self.issue_number}")
        data = BeautifulSoup(data.text,"html.parser")
        return data
    
    def assignees(self):
        """
        Fetch list of assignees
        """
        data = self.__scrape_page()
        try:
            assignees_body = data.find('span', class_='css-truncate js-issue-assignees')
            assignees = []
            for assignee in assignees_body.find_all('a', class_='assignee Link--primary css-truncate-target width-fit'):
                assignees.append(assignee.text.replace('\n','').strip())
            return assignees
        except:
            message = "No assignees found"
            return message

    def labels(self):
        """
        Fetch labels of issues
        """
        data = self.__scrape_page()
        try:
            labelsDiv = data.find(class_ = "js-issue-labels d-flex flex-wrap")
            allLabelsHtml = labelsDiv.find_all(class_="css-truncate css-truncate-target width-fit")
            allLabels = []
            for label in allLabelsHtml:
                allLabels.append(label.text)
            return allLabels
        except:
            message = "No label found"
            return message


    def opened_by(self):
        """
        Fetch the name of the user, who opened the issue
        """
        data = self.__scrape_page()
        author_name = data.find('a', class_='author text-bold Link--secondary').text
        return author_name

    
    def title(self):
        """
        Fetch title of the issue
        """
        data = self.__scrape_page()
        try:
            title_body = data.find('bdi', class_="js-issue-title markdown-title")
            title = title_body.text.strip()
            return title
        except:
            message = "No title found"
            return message
        
    def opened_at(self,time_zone='UTC'):
        """
        Returns a string containing the time range when the issue was opened in local time
        """
        data = self.__scrape_page()
        opened_time = data.find('relative-time')['datetime']
        opened_time_utc = datetime.fromisoformat(opened_time[:-1]).replace(tzinfo=pytz.utc)
        opened_time_local = opened_time_utc.astimezone(pytz.timezone(time_zone))
        return self.__time_range(opened_time_local,time_zone)

    def __time_range(self, date_time,time_zone):
        """
        Returns a string containing the time range between the given date/time and now
        """
        now = datetime.now(pytz.timezone(time_zone))
        delta = now - date_time

        days = delta.days
        seconds = delta.seconds

        if days > 7:
            return f"{days // 7} weeks ago"
        elif days > 0:
            return f"{days} days ago"
        elif seconds >= 3600:
            return f"{seconds // 3600} hours ago"
        elif seconds >= 60:
            return f"{seconds // 60} minutes ago"
        else:
            return "just now"