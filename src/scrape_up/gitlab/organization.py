import requests
from bs4 import BeautifulSoup

class Organization:
    def init(self, organization_name):
        self.organization_name = organization_name

    def __scrape_page(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_members(self):
        """
        Fetch a list of usernames of the members in the organization.
        """
        url = f"https://gitlab.com/{self.organization_name}/-/group_members"
        try:
            data = self.__scrape_page(url)
            members = []
            member_elements = data.find_all("li", class_="group-member-row")
            for member_element in member_elements:
                username = member_element.find("a", class_="group-member-username").text.strip()
                members.append(username)
            return {
                "data": members,
                "message": f"Retrieved members for organization {self.organization_name}"
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving members for organization {self.organization_name}: {str(e)}"
            }

    def get_projects(self):
        """
        Fetch a list of project names associated with the organization.
        """
        url = f"https://gitlab.com/groups/{self.organization_name}/-/projects"
        try:
            data = self.__scrape_page(url)
            projects = []
            project_elements = data.find_all("div", class_="gl-project-card")
            for project_element in project_elements:
                name = project_element.find("a", class_="gl-project-card-title").text.strip()
                projects.append(name)
            return {
                "data": projects,
                "message": f"Retrieved projects for organization {self.organization_name}"
            }
        except Exception as e:
            return {
                "data": None,
                "message": f"Error retrieving projects for organization {self.organization_name}: {str(e)}"
            }

    