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
        try:
            languages=[]
            data=self.__scrape_page()
            lang_raw=data.find_all("a",class_="no-wrap color-fg-muted d-inline-block Link--muted mt-2")
            for lang in lang_raw:
                
                languages.append(lang.get_text().strip())
            return languages
        except:
            return "An exception occured, cannot get the languages"
        
