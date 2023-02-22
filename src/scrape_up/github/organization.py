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
