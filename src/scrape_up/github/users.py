import requests
from bs4 import BeautifulSoup


class Users:

    def __init__(self, username: str):
        self.username = username

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://github.com/{username}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self):
        """
        Fetch the number of followers of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            followers = page.find(class_="text-bold color-fg-default")
            return followers.text
        except:
            message = f"{self.username} not found !"
            return message

    def get_avatar(self):
        """
        Fetch the avatar URL of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            avatar = page.find(
                class_="avatar avatar-user width-full border color-bg-default")
            return avatar["src"]
        except:
            message = f"Avatart not found for username {self.username}"
            return message

    def get_bio(self):
        """
        Fetch the bio of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            bio = page.find(class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
            return bio.text
        except:
            message = f"Bio not found for username {self.username}"
            return message
        
    def get_repo(self):
        """
        Fetch the titles of all pinned repositories of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            pinned_repos = page.find_all(class_="mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6")
            titles = [repo.find('span', class_='repo').text for repo in pinned_repos]
            return titles
        except:
            message=f"pinned repositories not found for username {self.username}" 
            return message
    def repo_count(self):
        """
        Fetch the number of repositories of Github user.
        """
        page = self.__scrape_page()
        try:
            count_repo = page.find_all(class_="Counter")
            count_repo_list=[]
            for word in count_repo:
                find_all_example=word.get_text()
                count_repo_list.append(find_all_example)
            return(count_repo_list[0])
        except:        
            message = f"No. of Repos not found for username {self.username}"
            return message

    def star_count(self):
        """
        Fetch the number of stars of Github user.
        """
        page = self.__scrape_page()
        try:           
            count_star = page.find_all(class_="Counter")
            count_star_list=[]
            for words in count_star:
                find_all_example=words.get_text()
                count_star_list.append(find_all_example)
            return(count_star_list[3])
        except:        
            message = f"Starred repo not found for username {self.username}"
            return message
        
    def get_yearly_contributions(self):
        
        """         
        Fetch the contributions made in 365 days frame
        """        
        page=self.__scrape_page()
        try:
            contributions = page.find('h2',class_="f4 text-normal mb-2")
            return ''.join(contributions.text.split())
        except:
            message = f"Yearly contributions not found for username {self.username}"
            return message
    
    def __get_repo_page(self):
        """
        Scrape the repositories page of a GitHub user.
        """
        username = self.username
        repo_data = requests.get(f"https://github.com/{username}?tab=repositories")
        repo_data = BeautifulSoup(repo_data.text, "html.parser")
        return repo_data

    def get_repositories(self):
        """
        Fetch the number of repositories of a GitHub user.
        """
        page = self.__get_repo_page()
        try:
            repo_body = page.find('div', id = 'user-repositories-list')
            repositories = []
            if repo_body != None:
                for repo in repo_body.find_all('div', class_='col-10 col-lg-9 d-inline-block'):
                    repositories.append('https://github.com' + repo.a['href'])
            return repositories
        except:
            message = f"Repositories not found for username {self.username}"
            return message


    def get_organizations(self):

        """
        Fetch the names of organization, a user is part of
        """
        page = self.__scrape_page()
        try:
            orgs = [org.login for org in page.get_orgs()]
            return orgs
        except:
            message = f"No organizations found for the username {self.username}"
            return message

    def following(self):
        """
        Fetch the number of following of Github user.
        """
        page = self.__scrape_page()

        try:           
            following = page.find_all(class_="text-bold color-fg-default")
            following_num_list=[]
            for num in following:
                find_all_following=num.get_text()
                following_num_list.append(find_all_following)
            print(following_num_list[1])
        except:        
            message = f"Following not found for username: {self.username}"
            return message
            

