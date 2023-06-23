import requests 
from bs4 import BeautifulSoup

#scrape python docs
class Python:
    def __init__(self, version: str):
        self.version = version
    
    def get_version(self):
        return self.version
    
    def get_url(self):
        return f'https://docs.python.org/{self.version}/'
    
    def tutorial(self):
        url = self.get_url() + 'tutorial/index.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        details=soup.find_all('p')
        passage=[]
        for paragraph in (details):
            text=(paragraph.text.strip())
            passage.append(text)
        return passage
    
    def library_reference(self):
        url=self.get_url() + 'library/index.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        details=soup.find_all('p')
         
        passage=[]
        for paragraph in (details):
            text=(paragraph.text.strip())
            passage.append(text)
        return passage
    
    def language_reference(self):
        url=self.get_url() + 'reference/index.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        details=soup.find_all('p')
         
        passage=[]
        for paragraph in (details):
            text=(paragraph.text.strip())
            passage.append(text)
        return passage
    
    def whats_new(self):
        url=self.get_url() + 'whatsnew/index.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        details=soup.find_all('p')
         
        passage=[]
        for paragraph in (details):
            text=(paragraph.text.strip())
            passage.append(text)
        return passage
    def get_all(self):
        return {
            "version": self.get_version(),
            "url": self.get_url(),
            "tutorial": self.tutorial(),
            "library_reference": self.library_reference(),
            "language_reference": self.language_reference(),
            "whats_new": self.whats_new(),
        }