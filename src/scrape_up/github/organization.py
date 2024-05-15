from typing import Dict, List, Union
import requests
from bs4 import BeautifulSoup, Tag


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

    def __init__(self, organization_name: str):
        self.organization = organization_name
        self._timeout = 10

    def __scrape_page(self):
        data = requests.get(
            f"https://github.com/{self.organization}", timeout=self._timeout
        )
        if data.status_code != 200:
            return None
        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def top_languages(self):
        """
        Class - `Organisation`

        Example:
        ```python
        repository = github.Organization(organization_name="Clueless-Community")
        top_languages = repository.top_languages()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None
        lang_raw = page.find_all(
            "a", class_="no-wrap color-fg-muted d-inline-block Link--muted mt-2"
        )
        languages = [lang.get_text().strip() for lang in lang_raw]
        return languages

    def top_topics(self):
        """
        Class - `Organisation`

        Example:
        ```python
        repository = github.Organization(organization_name="Clueless-Community")
        top_topics = repository.top_topics()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        all_topics = page.find_all(class_="topic-tag topic-tag-link")
        topics = [topic.text.strip() for topic in all_topics]
        return topics

    def followers(self):
        """
        Class - `Organisation`

        Example:
        ```python
        repository = github.Organization(organization_name="Clueless-Community")
        followers = repository.followers()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        followers_body = page.findChild(
            "span", class_="Link--secondary no-underline no-wrap"
        )
        return followers_body.text.strip() if followers_body else None

    def avatar(self):
        """
        Class - `Organisation`

        Example:
        ```python
        repository = github.Organization(organization_name="Clueless-Community")
        avatar = repository.avatar()
        ```
        """
        page = self.__scrape_page()
        if page is None:
            return None

        avatar = page.find("a", attrs={"itemprop": "url"})
        return avatar.text.strip() if avatar else None

    def __scrape_repositories_page(self):
        """
        scrapes the head page of repositories of an organization
        """
        organization = self.organization
        data = requests.get(
            f"https://github.com/orgs/{organization}/repositories",
            timeout=self._timeout,
        )
        if data.status_code != 200:
            return None

        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_repositories(self, page: str):
        """
        scrapes the repositories page of an organization
        """
        data = requests.get(page, timeout=self._timeout)
        if data.status_code != 200:
            return None

        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def repositories(self):
        """
        Class - `Organisation`

        Example:
        ```python
        repository = github.Organization(organization_name="Clueless-Community")
        repositories = repository.repositories()
        ```
        """
        organization = self.organization
        page = self.__scrape_repositories_page()
        if page is None:
            return None

        pages_body = page.find("div", class_="paginate-container")
        if not isinstance(pages_body, Tag):
            return None

        current_page = pages_body.find("em", class_="current")
        total_pages = 1
        if (
            isinstance(current_page, Tag)
            and "data-total-pages" in current_page.attrs
            and str(current_page["data-total-pages"]).isdigit()
        ):
            total_pages = int(current_page["data-total-pages"])

        pages: List[str] = []
        base = f"https://github.com/orgs/{organization}/repositories"
        if total_pages == 1:
            pages.append(base)
        else:
            for i in range(total_pages):
                pages.append(f"{base}?page={i+1}")

        repositories: List[str] = []
        for page in pages:
            page_data = self.__scrape_repositories(page)
            if page_data is None:
                continue

            repositories_body = page_data.find("div", id="org-repositories")
            if not isinstance(repositories_body, Tag):
                continue

            repos = repositories_body.find_all(
                "a", attrs={"itemprop": "name codeRepository"}
            )
            repositories.extend([repo.text.strip() for repo in repos])

        return repositories

    def __scrape_people_page(self):
        """
        scrapes the head page of people of an organization

        """
        data = requests.get(
            f"https://github.com/orgs/{self.organization}/people", timeout=self._timeout
        )
        if data.status_code != 200:
            return None

        soup = BeautifulSoup(data.text, "html.parser")
        return soup

    def __scrape_people(self, page: str):
        """
        scrapes the people page of an organization
        """
        data = requests.get(page, timeout=self._timeout)
        if data.status_code != 200:
            return None

        soup = BeautifulSoup(data.text, "html.parser")
        return soup

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
        page = self.__scrape_people_page()
        if page is None:
            return None

        pages_body = page.find("div", class_="paginate-container")
        if not isinstance(pages_body, Tag):
            return None

        current_page = pages_body.find("em", class_="current")
        total_pages = 1
        if (
            isinstance(current_page, Tag)
            and "data-total-pages" in current_page.attrs
            and str(current_page["data-total-pages"]).isdigit()
        ):
            total_pages = int(current_page["data-total-pages"])

        pages: List[str] = []
        base = f"https://github.com/orgs/{organization}/people"
        if total_pages == 1:
            pages.append(base)
        else:
            for i in range(1, total_pages + 1):
                pages.append(f"{base}?page={i}")

        peoples: List[str] = []
        for page in pages:
            page_data = self.__scrape_people(page)
            if page_data is None:
                continue

            people_body = page_data.find("div", id="org-members-table")
            if not isinstance(people_body, Tag):
                continue

            people = people_body.find_all("li")
            for person in people:
                person_username = person.find("a", class_="d-inline-block")
                peoples.append(person_username["href"][1:])

        return peoples

    def peoples(self):
        """
        Class - `Organisation`

        Example:
        ```python
        repository = github.Organization(organization_name="Clueless-Community")
        peoples = repository.peoples()
        ```
        """
        data = self.__scrape_people_page()
        if data is None:
            return None

        body = data.find("div", class_="paginate-container")
        if body is None:
            return None

        current_page = body.find("em", class_="current")
        page_count = 1
        if (
            isinstance(current_page, Tag)
            and "data-total-pages" in current_page.attrs
            and str(current_page["data-total-pages"]).isdigit()
        ):
            page_count = int(current_page["data-total-pages"])

        pages: List[str] = []
        base = f"https://github.com/orgs/{self.organization}/people"
        if page_count == 1:
            pages.append(base)
        else:
            for i in range(page_count):
                pages.append(f"{base}?page={i+1}")

        people_count = 0
        for page in pages:
            page_data = self.__scrape_people(page)
            if page_data is None:
                continue

            people_body = page_data.find("div", id="org-members-table")
            if not isinstance(people_body, Tag):
                continue

            people_count += len(people_body.find_all("li"))
        return people_count

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
        if page is None:
            return None

        lc = page.find("span", itemprop="location")
        return lc.text.strip() if lc else None

    def repository_stats(self, repo_url: str):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        repository_stats = repository.repository_stats()
        ```
        """
        data = self.__scrape_repositories(repo_url)
        if data is None:
            return None

        # forks
        forksCount = data.find("span", id="repo-network-counter")
        # stars
        starCount = data.find("span", id="repo-stars-counter-star")
        # issues
        issuesCount = data.find("span", id="issues-repo-tab-count")
        # pull requests
        pullRequests = data.find("span", id="pull-requests-repo-tab-count")

        # Final data
        data = {
            "forks": forksCount.text.strip() if forksCount else None,
            "stars": starCount.text.strip() if starCount else None,
            "issues": issuesCount.text.strip() if issuesCount else None,
            "pullRequests": pullRequests.text.strip() if pullRequests else None,
        }
        return data

    def repository_details(self):
        """
        Class - `Organisation`
        Example:
        ```
        repository = github.Organization(organization_name="Clueless-Community")
        repository_details = repository.repository_details()
        ```
        """
        page = self.__scrape_repositories_page()
        if page is None:
            return None

        pages_body = page.find("div", class_="paginate-container")
        if not isinstance(pages_body, Tag):
            return None

        current_page = pages_body.find("em", class_="current")
        total_pages = 1
        if (
            isinstance(current_page, Tag)
            and "data-total-pages" in current_page.attrs
            and str(current_page["data-total-pages"]).isdigit()
        ):
            total_pages = int(current_page["data-total-pages"])

        pages: List[str] = []
        base = f"https://github.com/orgs/{self.organization}/repositories"
        if total_pages == 1:
            pages.append(base)
        else:
            for i in range(1, total_pages + 1):
                pages.append(f"{base}?page={i}")

        repositories = []
        for page in pages:
            page_data = self.__scrape_repositories(page)
            if page_data is None:
                continue

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
                    str(repo_description_body.text).strip()
                    if repo_description_body
                    else "No description"
                )
                repo_language_body = repo.find(
                    "span", attrs={"itemprop": "programmingLanguage"}
                )
                repo_language = (
                    str(repo_language_body.text).strip()
                    if repo_language_body
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
                response = requests.get(url)

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
        page = self.__scrape_page()
        if page is None:
            return None

        website_link = page.find("a", rel="nofollow", itemprop="url", href=True)
        gmail = page.find("a", itemprop="email", href=True)

        links: Dict[str, Union[str, None]] = {}
        links["website"] = (
            website_link.get("href", None) if isinstance(website_link, Tag) else None
        )
        links["gmail"] = gmail.get("href", None) if isinstance(gmail, Tag) else None

        other_link = page.find_all("a", rel="nofollow", href=True)
        for o in other_link:
            name = (
                str(o["href"])
                .split("//")[1]
                .split("/")[0]
                .replace("www.", "")
                .split(".")[0]
            )
            if (
                name != self.organization or name.find(self.organization) == -1
            ) and name not in links:
                links[name] = o["href"]
        return links
