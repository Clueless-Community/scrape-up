import requests
from bs4 import BeautifulSoup
from github.repository import Repository

class Users:
    def __init__(self, username: str):
        self.username = username

    def __str__(self):
        return f" The username is: {self.username}"

    def __scrape_page(self):
        username = self.username
        data = requests.get(f"https://github.com/{username}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def followers(self) -> str:
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        followers = user.followers()
        ```
        Return\n
        ```python
        return
        {
            "data": followers.text,
            "message":f"Followers found for user {self.username}"
        }
        ```
        """
        page = self.__scrape_page()
        try:
            followers = page.find(class_="text-bold color-fg-default")
            return {
                "data": followers.text,
                "message": f"Followers found for user {self.username}",
            }
        except:
            message = f"{self.username} not found !"
            return {"data": None, "message": message}

    def following(self):
        """ 
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        following = user.following()
        ```
        Return\n
        ```python
        return
        {
            following = page.find_all(class_="text-bold color-fg-default")
            # print(page.find_all("span"))
            return following[1].text
        }
        ```
        """
        page = self.__scrape_page()
        try:
            following = page.find_all(class_="text-bold color-fg-default")
            # print(page.find_all("span"))
            return following[1].text
        except:
            message = f"{self.username} not found !"
            return message

    def get_avatar(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_avatar = user.get_avatar()
        ```
        Return\n
        ```python
        return
        {
            return avatar["src"]
        }
        ```
        """
        page = self.__scrape_page()
        try:
            avatar = page.find(
                class_="avatar avatar-user width-full border color-bg-default"
            )
            return avatar["src"]
        except:
            message = f"Avatar not found for username {self.username}"
            return message

    def get_bio(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_bio = user.get_bio()
        ```
        Return\n
        ```python
        return
        {
            return bio.text
        }
        ```
        """
        page = self.__scrape_page()
        try:
            bio = page.find(
                class_="p-note user-profile-bio mb-3 js-user-profile-bio f4"
            )
            return bio.text
        except:
            message = f"Bio not found for username {self.username}"
            return message

    def get_repo(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_repo = user.get_repo()
        ```
        Return\n
        ```python
        return
        {
            return titles
        }
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
            message = f"pinned repositories not found for username {self.username}"
            return message

    def repo_count(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        repo_count = user.repo_count()
        ```
        Return\n
        ```python
        return
        {
           return count_repo_list[0]
        }
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
            message = f"No. of Repos not found for username {self.username}"
            return message

    def star_count(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        star_count = user.star_count()
        ```
        Return\n
        ```python
        return
        {
            return count_star_list[3]
        }
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
            message = f"Starred repo not found for username {self.username}"
            return message

    def get_yearly_contributions(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_yearly_contributions = user.get_yearly_contributions()
        ```
        Return\n
        ```python
        return
        {
           return " ".join(contributions.text.split())
        }
        ```
        """
        page = self.__scrape_page()
        try:
            contributions = page.find("h2", class_="f4 text-normal mb-2")
            return " ".join(contributions.text.split())
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
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_repositories = user.get_repositories()
        ```
        Return\n
        ```python
        return
        {
            return repositories
        }
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
            message = f"Repositories not found for username {self.username}"
            return message

    def get_organizations(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_organizations = user.get_organizations()
        ```
        Return\n
        ```python
        return
        {
            return orgs
        }
        ```
        """
        page = self.__scrape_page()
        try:
            orgs = [org.login for org in page.get_orgs()]
            return orgs
        except:
            message = f"No organizations found for the username {self.username}"
            return message

    def get_achievements(self):
        """
        Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_achievements = user.get_achievements()
        ```
        Return\n
        ```python
        return
        {
            return achievement
        }
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
            return "Achievements cannot be fetched"

    def __get_starred_page(self):
        """
        Scrape the starred page of a GitHub user.
        """
        username = self.username
        starred_data = requests.get(f"https://github.com/{username}?tab=stars")
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
        Return\n
        ```python
        return
        {
             return starred_repos
        }
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
            message = f"Starred repositories not found for username {self.username}"
            return message

    def __scrape_followers_page(self):
        """
        Scrape the followers page of a GitHub user.
        """
        username = self.username
        followers_data = requests.get(f"https://github.com/{username}?tab=followers")
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
        Return\n
        ```python
        return
        {
            return followers
        }
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
            message = f"Followers not found for username {self.username}"
            return message

    def __scrape_following_page(self):
        """

        Scrape the following page of a GitHub user.
        """
        username = self.username
        following_data = requests.get(f"https://github.com/{username}?tab=following")
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
        Return\n
        ```python
        return
        {
            return following
        }
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
            message = f"Following users not found for username {self.username}"
            return message

    def company(self):
        page = self.__scrape_following_page()
        try:
            cmp = page.find(class_="Link--primary")
            print(cmp.text)
            # print(page.find_all("a"))
        except:
            message = f"Following users not found for username {self.username}"
            message = f"Following users not found for username {self.username}"
            return message

    def get_status(self):
        """Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_status = user.get_status()
        ```
        Return\n
        ```python
        return
        {
            return t.text.strip().replace("\n", "")
        }
        
        """
        try:
            data = self.__scrape_page()
            t = data.find(
                "div", class_="user-status-container position-relative hide-sm hide-md"
            )
            return t.text.strip().replace("\n", "")
        except:
            message = f"Status not found for username {self.username}"
            return message

    def get_contribution_streak(self):
        """
         Class - `Users`\n
        Example -\n
        ```python
        user = github.User(username="nikhil25803")
        get_contribution_streak = user.get_contribution_streak()
        ```
        Return\n
        ```python
        return
        {
             return int(result)
        }
        
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
            return "contribution streak cannot be obtained"

    def __get_page_details(self, link):
        """
        scrape the data in the page
        """
        data = requests.get(link)
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
        Return\n
        ```python
        return
        {
            return pages_links
        }
        ```
        """
        data = self.__get_page_details(curr_repo_link)
        pages_body = data.find("div", class_="paginate-container")
        if pages_body.find("a", class_="next_page") != None:
            pages_links.append(
                "https://github.com" + pages_body.find("a", class_="next_page")["href"]
            )
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
        Return\n
        ```python
        return
        {
            return repositories
        }
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
            return "No repositories found"


# TEST
# user = Users(username="nikhil25803")
# breakpoint()
# user.followers()
