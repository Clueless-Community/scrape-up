import requests
from bs4 import BeautifulSoup



class Organization:
    def __init__(self,organization_name: str):
        self.organization  = organization_name

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.organization}")
        data = BeautifulSoup(data.text, "html.parser")
        return data
    def top_languages(self):
        """
        Returns a list of the most used languages in an organization
        """
        try:
            languages=[]
            data=self.__scrape_page()
            lang_raw=data.find_all("a",class_="no-wrap color-fg-muted d-inline-block Link--muted mt-2")
            for lang in lang_raw:
                
                languages.append(lang.get_text().strip())
            return languages
        except:
            return "An exception occured, cannot get the languages"
        

    def top_topics(self):
        """
        Returns list of the most used topics in an organization
        """
        page = self.__scrape_page()
        all_topics = page.find_all(class_='topic-tag topic-tag-link')
        topics = []
        for topic in all_topics:
            topics.append(topic.text.strip())
        return topics
    
    def followers(self):
        """
        Returns number of followers of an organization
        """
        page = self.__scrape_page()
        try:
            followers_body = page.find('a', class_='Link--secondary no-underline no-wrap')
            followers = followers_body.span.text.strip()
            return followers
        except:
            return "No followers found for this organization"
    
    def avatar(self):
        """
        Returns url of the avatar of an organization
        """
        page = self.__scrape_page()
        try:
            avatar = page.find('a', attrs = {'itemprop': 'url'})
            url = avatar.text.strip()
            return url
        except:
            return "No avatar found for this organization"
    
    def __scrape_repositories(self):
        """
        scrapes the repositories page of an organization
        """
        organization = self.organization
        data = requests.get(f"https://github.com/orgs/{organization}/repositories")
    
    def repositories(self):
        """
        Returns List of repositories of an organization
        """
        page = self.__scrape_repositories()
        try:
            repositories_body = page.find('div', id = 'org-repositories')
            repositories = []
            for repo in repositories_body.find_all('a', attrs = {'itemprop': 'name codeRepository'}):
                repositories.append(repo.text.strip())

            return repositories
        except:
            return "No repositories found for this organization"
    
    def __scrape_people_page(self):
        """
        scrapes the head page of people of an organization
        """
        organization = self.organization
        data = requests.get(f"https://github.com/orgs/{organization}/people")
        data = BeautifulSoup(data.text, "html.parser")
        return data
    
    def __scrape_people(self, page):
        """
        scrapes the people page of an organization
        """
        organization = self.organization
        data = requests.get(page)
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def people(self):
        """
        Returns List of people in an organization
        """
        organization = self.organization
        data = self.__scrape_people_page()
        try:
            pages_body = data.find('div', class_='paginate-container')
            current_page = pages_body.find('em', class_='current')
            total_pages = 1
            if current_page != None:
                total_pages = (int)(current_page['data-total-pages'])
            
            pages = []
            if total_pages == 1:
                pages.append(f"https://github.com/orgs/{organization}/people")
            else:
                for i in range(1, total_pages + 1):
                    pages.append(f"https://github.com/orgs/{organization}/people?page={i}")
            
            people = []
            for page in pages:
                page_data = self.__scrape_people(page)
                people_body = page_data.find('div', id = 'org-members-table')
                for person in people_body.find_all('li'):
                    person_username = person.find('a', class_='d-inline-block')
                    people.append(person_username['href'][1:])
            
            return people
        except:
            return "No people found for this organization"


    def peoples(self):
        """
        Return number of people in a organizaton
        """
        data = self.__scrape_people_page()
        try:
            body = data.find('div', class_='paginate-container')
            current_page = body.find('em', class_='current')
            page_count = 1
            if current_page != None:
                page_count = int((current_page['data-total-pages']))

            pages = []

            if page_count == 1:
                pages.append(f"https://github.com/orgs/{self.organization}/people")
            else:
                for i in range(1, page_count + 1):
                    pages.append(f"https://github.com/orgs/{self.organization}/people?page={i}")
            
            people_count = 0
            for page in pages:
                page_data = self.__scrape_people(page)
                people_body = page_data.find('div', id = 'org-members-table')
                people_count = len(people_body.find_all('li'))

            return people_count
        except:
            return "No people found for this organization"



