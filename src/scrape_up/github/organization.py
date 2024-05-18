from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Organization:
    """
    Create an instance of class `Organization`
    ```python
    organization = github.Organization(organization_name="Clueless-Community")
    ```
    | Methods                     | Details                                                         |
    | --------------------------- | --------------------------------------------------------------- |
    | `.top_topics()`             | Returns a list of the most used topics in an organization.      |
    | `.followers()`              | Returns the number of followers of an organization.             |
    | `.top_languages()`          | Returns the top languages used in an organization.              |
    | `.followers()`              | Returns the number of followers of an organization.             |
    | `.avatar()`                 | Returns the avatar URL of an organization.                      |
    | `.repositories()`           | Returns the list of repositories of an organization.            |
    | `.people()`                 | Returns the list of people in an organization.                  |
    | `.peoples() `               | Returns the number of people in an organization.                |
    | `.get_location() `          | Returns the location of an organization.                        |
    | `.repository_details()`     | Returns the list of repositories with their details.            |
    | `.pinned_repository()`      | Returns the list of pinned repositories with their details.     |
    | `.get_organization_links()` | Returns a dictionary of important website links of a community. |
    """

    def __init__(
        self, organization_name: str, *, config: RequestConfig = RequestConfig()
    ):
        self.organization = organization_name
        self.config = config

    def __scrape_page(self):
        data = get(f"https://github.com/{self.organization}", self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def top_languages(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        top_languages = repository.top_languages()
        ```
        """
        try:
            languages = []
            data = self.__scrape_page()
            lang_raw = data.find_all(
                "a", class_="no-wrap color-fg-muted d-inline-block Link--muted mt-2"
            )
            for lang in lang_raw:
                languages.append(lang.get_text().strip())
            return languages
        except:
            return None

    def top_topics(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        top_topics = repository.top_topics()
        ```
        """
        page = self.__scrape_page()
        try:
            all_topics = page.find_all(class_="topic-tag topic-tag-link")
            topics = []
            for topic in all_topics:
                topics.append(topic.text.strip())
            return topics
        except:
            return None

    def followers(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        followers = repository.followers()
        ```
        """
        page = self.__scrape_page()
        try:
            followers_body = page.find(
                "a", class_="Link--secondary no-underline no-wrap"
            )
            followers = followers_body.span.text.strip()
            return followers
        except:
            return None

    def avatar(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        avatar = repository.avatar()
        ```
        """
        page = self.__scrape_page()
        try:
            avatar = page.find("a", attrs={"itemprop": "url"})
            avatar_url = avatar.text.strip()
            return avatar_url
        except:
            return None

    def __scrape_repositories_page(self):
        """
        scrapes the head page of repositories of an organization
        """
        organization = self.organization
        data = get(f"https://github.com/orgs/{organization}/repositories", self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_repositories(self, page: str):
        """
        scrapes the repositories page of an organization
        """
        data = get(page, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def repositories(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        repositories = repository.repositories()
        ```
        """
        organization = self.organization
        data = self.__scrape_repositories_page()
        try:
            pages_body = data.find("div", class_="paginate-container")
            current_page = pages_body.find("em", class_="current")
            total_pages = 1
            if current_page != None:
                total_pages = (int)(current_page["data-total-pages"])

            pages = []
            if total_pages == 1:
                pages.append(f"https://github.com/orgs/{organization}/repositories")
            else:
                for i in range(1, total_pages + 1):
                    pages.append(
                        f"https://github.com/orgs/{organization}/repositories?page={i}"
                    )

            repositories = []
            for page in pages:
                page_data = self.__scrape_repositories(page)
                repositories_body = page_data.find("div", id="org-repositories")
                for repo in repositories_body.find_all(
                    "a", attrs={"itemprop": "name codeRepository"}
                ):
                    repositories.append(repo.text.strip())

            return repositories
        except:
            return None

    def __scrape_people_page(self):
        """
        scrapes the head page of people of an organization

        """
        organization = self.organization
        data = get(f"https://github.com/orgs/{organization}/people", self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_people(self, page: str):
        """
        scrapes the people page of an organization
        """
        data = get(page, self.config)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def people(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        people = repository.people()
        ```
        Returns:
        {
           "data": people,
           "message": f"Found {len(people)} people for {organization}",
        }
        """
        organization = self.organization
        data = self.__scrape_people_page()
        try:
            pages_body = data.find("div", class_="paginate-container")
            current_page = pages_body.find("em", class_="current")
            total_pages = 1
            if current_page != None:
                total_pages = (int)(current_page["data-total-pages"])

            pages = []
            if total_pages == 1:
                pages.append(f"https://github.com/orgs/{organization}/people")
            else:
                for i in range(1, total_pages + 1):
                    pages.append(
                        f"https://github.com/orgs/{organization}/people?page={i}"
                    )

            peoples = []
            for page in pages:
                page_data = self.__scrape_people(page)
                people_body = page_data.find("div", id="org-members-table")
                for person in people_body.find_all("li"):
                    person_username = person.find("a", class_="d-inline-block")
                    peoples.append(person_username["href"][1:])

            return peoples
        except:
            return None

    def peoples(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        peoples = repository.peoples()
        ```
        """
        data = self.__scrape_people_page()
        try:
            body = data.find("div", class_="paginate-container")
            current_page = body.find("em", class_="current")
            page_count = 1
            if current_page != None:
                page_count = int((current_page["data-total-pages"]))

            pages = []

            if page_count == 1:
                pages.append(f"https://github.com/orgs/{self.organization}/people")
            else:
                for i in range(1, page_count + 1):
                    pages.append(
                        f"https://github.com/orgs/{self.organization}/people?page={i}"
                    )

            people_count = 0
            for page in pages:
                page_data = self.__scrape_people(page)
                people_body = page_data.find("div", id="org-members-table")
                people_count = len(people_body.find_all("li"))

            return people_count
        except:
            return None

    def get_location(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        get_location = repository.get_location()
        ```
        """
        page = self.__scrape_page()
        try:
            lc = page.find("span", itemprop="location")
            return lc.text.strip()
        except:
            return None

    def repository_stats(self, repo_url):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        repository_stats = repository.repository_stats()
        ```
        """
        data = self.__scrape_repositories(repo_url)
        try:
            # forks
            forksCount = data.find("span", id="repo-network-counter").text.strip()
            # stars
            starCount = data.find("span", id="repo-stars-counter-star").text.strip()
            # issues
            issuesCount = data.find("span", id="issues-repo-tab-count").text.strip()
            # pull requests
            pullRequests = data.find(
                "span", id="pull-requests-repo-tab-count"
            ).text.strip()
            data = {
                "forks": forksCount,
                "stars": starCount,
                "issues": issuesCount,
                "pullRequests": pullRequests,
            }
            return data
        except:
            return None

    def repository_details(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        repository_details = repository.repository_details()
        ```
        """
        organization = self.organization
        data = self.__scrape_repositories_page()
        try:
            pages_body = data.find("div", class_="paginate-container")
            current_page = pages_body.find("em", class_="current")
            total_pages = 1
            if current_page != None:
                total_pages = (int)(current_page["data-total-pages"])

            pages = []
            if total_pages == 1:
                pages.append(f"https://github.com/orgs/{organization}/repositories")
            else:
                for i in range(1, total_pages + 1):
                    pages.append(
                        f"https://github.com/orgs/{organization}/repositories?page={i}"
                    )

            repositories = []
            for page in pages:
                page_data = self.__scrape_repositories(page)
                repositories_body = page_data.find("div", id="org-repositories")
                for repo in repositories_body.find_all("li"):
                    repo_name = repo.find(
                        "a", attrs={"itemprop": "name codeRepository"}
                    ).text.strip()
                    repo_url = f"https://github.com{repo.find('a', attrs = {'itemprop': 'name codeRepository'})['href']}"
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
                    (
                        repo_forks,
                        repo_stars,
                        repo_issues,
                        repo_pull_requests,
                    ) = self.repository_stats(repo_url)
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

    def pinned_repository(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        pinned_repository = repository.pinned_repository()
        ```
        """
        organization = self.organization

        data = self.__scrape_page()

        try:
            pinned_repos = data.find(
                "ol",
                class_="d-flex flex-wrap list-style-none gutter-condensed mb-2 js-pinned-items-reorder-list",
            )

            repo_info_list = []

            for repo in pinned_repos.find_all("li"):
                name = repo.find("span", class_="repo").text.strip()

                desc = repo.find(
                    "p", class_="pinned-item-desc color-fg-muted text-small mt-2 mb-0"
                ).text.strip()

                top_tech = repo.find(
                    "span", itemprop="programmingLanguage"
                ).text.strip()

                url = "https://github.com" + repo.find("a", href=True)["href"]
                response = get(url, self.config)

                url_parts = url.split("/")

                organization = url_parts[3]

                repository = url_parts[4]

                soup = BeautifulSoup(response.content, "html.parser")

                star_count_elem = soup.find(
                    "a", href=f"/{organization}/{repository}/stargazers"
                ).find("span")
                star_count = int(star_count_elem.text.strip())

                stats_body = soup.find(
                    "ul", class_="pagehead-actions flex-shrink-0 d-none d-md-inline"
                )
                forks = stats_body.find("span", id="repo-network-counter")
                fork_count = forks.text.strip()

                repo_info = {
                    "name": name,
                    "link": url,
                    "detail": desc,
                    "top_lang": top_tech,
                    "stars": star_count,
                    "forks": fork_count,
                }
                repo_info_list.append(repo_info)
            return repo_info_list
        except:
            return None

    def get_organization_links(self):
        """ "
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        get_organization_links = repository.get_organization_links()
        ```
        """
        try:
            links = {}
            data = self.__scrape_page()
            website_link = data.find("a", rel="nofollow", itemprop="url", href=True)[
                "href"
            ]
            links["website"] = website_link
            gmail = data.find("a", itemprop="email", href=True)["href"]
            links["gmail"] = gmail
            other_link = data.find_all("a", rel="nofollow", href=True)
            for o in other_link:
                name = (
                    o["href"]
                    .split("//")[1]
                    .split("/")[0]
                    .replace("www.", "")
                    .split(".")[0]
                )
                if name != self.organization or name.find(self.organization) == -1:
                    if not name in links:
                        links[name] = o["href"]
            return links
        except:
            return None
