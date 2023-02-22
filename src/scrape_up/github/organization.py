import requests
from bs4 import BeautifulSoup



class Organization:
    def __init__(self,organization_name: str):
        self.organization  = organization_name

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.organization}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

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
