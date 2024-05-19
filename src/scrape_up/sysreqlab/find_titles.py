from bs4 import BeautifulSoup
import requests

class SysReqLab:
    def __init__(self, search_term: str, search_alphabet: str[1]):
        self.search_term = search_term
        self.search_alphabet = search_alphabet

    def __find_the_game(self):
        try:
            url = f"https://www.systemrequirementslab.com/all-games-list/?filter={self.search_alphabet}"
            html = requests.get(url)
            html.raise_for_status()
            return html.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")`
        

