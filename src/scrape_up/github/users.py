import requests
from bs4 import BeautifulSoup
import respository


class Users:
    def __init__(self, username: str):
        self.username = username

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
                "message":f"Followers found for user {self.username}"
            }
        except:
            message = f"Followers not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def following(self):
        """ "
        Fetch the number of following of a GitHub users.
        """
        page = self.__scrape_page()
        try:
            following = page.find_all(class_="text-bold color-fg-default")
            return {
                "data": following[1].text,
                "message":f"Following found for user {self.username}"
            }
        except:
            message = f"Following users are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_avatar(self):
        """
        Fetch the avatar URL of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            avatar = page.find(
                class_="avatar avatar-user width-full border color-bg-default"
            )
            return {
                "data": avatar["src"],
                "message":f"Avatar found for user {self.username}"
            }
        except:
            message = f"Avatar not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_bio(self):
        """
        Fetch the bio of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            bio = page.find(
                class_="p-note user-profile-bio mb-3 js-user-profile-bio f4"
            )
            return {
                "data": bio.text,
                "message":f"Bio found for user {self.username}"
            }
        except:
            message = f"Bio not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_repo(self):
        """
        Fetch the titles of all pinned repositories of a GitHub user.
        """
        page = self.__scrape_page()
        try:
            pinned_repos = page.find_all(
                class_="mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6"
            )
            titles = [repo.find("span", class_="repo").text for repo in pinned_repos]
            return {
                "data": titles,
                "message":f"Repo found for user {self.username}"
            }
        except:
            message = f"Repos are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def repo_count(self):
        """
        Fetch the number of repositories of Github user.
        """
        page = self.__scrape_page()
        try:
            count_repo = page.find_all(class_="Counter")
            count_repo_list = []
            for word in count_repo:
                find_all_example = word.get_text()
                count_repo_list.append(find_all_example)
            return {
                "data": count_repo_list[0],
                "message":f"Repo found for user {self.username}"
            }
        except:
            message = f"Repos are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def star_count(self):
        """
        Fetch the number of stars of Github user.
        """
        page = self.__scrape_page()
        try:
            count_star = page.find_all(class_="Counter")
            count_star_list = []
            for words in count_star:
                find_all_example = words.get_text()
                count_star_list.append(find_all_example)
            return {
                "data": count_star_list[3],
                "message":f"Star found for user {self.username}"
            }
        except:
            message = f"Stars are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_yearly_contributions(self):
        """
        Fetch the contributions made in 365 days frame
        """
        page = self.__scrape_page()
        try:
            contributions = page.find("h2", class_="f4 text-normal mb-2")
            return {
                "data": "".join(contributions.text.split()),
                "message":f"Yearly contributions found for user {self.username}"
            }
        except:
            message = f"Yearly contributions not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

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
            repo_body = page.find("div", id="user-repositories-list")
            repositories = []
            if repo_body != None:
                for repo in repo_body.find_all(
                    "div", class_="col-10 col-lg-9 d-inline-block"
                ):
                    repositories.append("https://github.com" + repo.a["href"])
            return {
                "data": repositories,
                "message":f"Repositories found for user {self.username}"
            }
        except:
            message = f"Repositories are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_organizations(self):
        """
        Fetch the names of organization, a user is part of
        """
        page = self.__scrape_page()
        try:
            orgs = [org.login for org in page.get_orgs()]
            return {
                "data": orgs,
                "message":f"Organizations found for user {self.username}"
            }
        except:
            message = f"Organizations are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_achievements(self):
        """
        Fetch the names of achievements, a user is has achieved
        """
        try:
            achievement = []
            data = self.__scrape_page()
            data = data.find_all("img", class_="achievement-badge-sidebar", alt=True)
            itr = 0
            while itr < len(data) / 2:
                achievement.append(data[itr]["alt"].split(":")[1].strip(" "))
                itr = itr + 1

            return {
                "data": achievement,
                "message":f"Achievements found for user {self.username}"
            }
        except:
            message = f"Achievements are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

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
        Fetches the starred repositories of a GitHub user.
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
            return {
                "data": starred_repos,
                "message":f"Starred repositories found for user {self.username}"
            }
        except:
            message = f"Starred repositories are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

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
        Fetch the list of followers a user have.
        """
        page = self.__scrape_followers_page()
        try:
            followers_body = page.find("turbo-frame", id="user-profile-frame")
            followers = []
            for user in followers_body.find_all("span", class_="Link--secondary"):
                followers.append(user.text.strip())

            return {
                "data": followers,
                "message":f"Followers found for user {self.username}"
            }
        except:
            message = f"Followers are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

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
        Fetches the following users of a GitHub user.
        """
        page = self.__scrape_following_page()
        try:
            following_body = page.find("turbo-frame", id="user-profile-frame")
            following = []
            for user in following_body.find_all("span", class_="Link--secondary"):
                following.append(user.text.strip())

            return {
                "data": following,
                "message":f"Following users found for user {self.username}"
            }
        except:
            message = f"Following users are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def company(self):
        page = self.__scrape_following_page()
        try:
            cmp = page.find(class_="Link--primary")
            return {
                "data": cmp.text,
                "message":f"Company found for user {self.username}"
            }
        except:
            message = f"Company is not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_status(self):
        """
        Fetch the number of contribution made in recent month.
        """
        try:
            data = self.__scrape_page()
            t = data.find(
                "div", class_="user-status-container position-relative hide-sm hide-md"
            )
            return {
                "data": t.text.strip().replace("\n", ""),
                "message":f"Status found for user {self.username}"
            }
        except:
            message = f"Status is not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_contribution_streak(self):
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
            return {
                "data": int(result),
                "message":f"Contribution streak found for user {self.username}"
            }
        except:
            message = f"Contribution streak is not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def __get_page_details(self, link):
        """
        scrape the data in the page
        """
        data = requests.get(link)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def get_pages(self, curr_repo_link, pages_links):
        """
        get the links of all the pages of the repositories
        """
        data = self.__get_page_details(curr_repo_link)
        try:
            pages_body = data.find("div", class_="paginate-container")
            if pages_body.find("a", class_="next_page") != None:
                pages_links.append(
                    "https://github.com" + pages_body.find("a", class_="next_page")["href"]
                )
                self.get_pages(pages_links[-1], pages_links)

            return {
                "data": pages_links,
                "message":f"Pages found for user {self.username}"
            }
        except:
            message = f"Pages for repos are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }

    def get_repository_details(self):
        """
        Fetches the details of the repositories of a GitHub user.
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
                    repository = respository.Repository(username, repository_name)
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

            return {
                "data": repositories,
                "message":f"Repositories found for user {self.username}"
            }
        except:
            message = f"Repositories are not found for user {self.username}"
            return {
                "data":None,
                "message":message
            }
