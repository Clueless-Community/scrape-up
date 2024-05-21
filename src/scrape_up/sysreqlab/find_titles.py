from bs4 import BeautifulSoup
import requests

class FindTitles:
    def __init__(self, search_term: str, search_alphabet: str):
        self.search_term = search_term
        self.search_alphabet = search_alphabet

    def __scrape_data(self):
        try:
            url = f"https://www.systemrequirementslab.com/all-games-list/?filter={self.search_alphabet}"
            html = requests.get(url)
            html.raise_for_status()
            return html.text

        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def __parse_page(self):
        html = self.__scrape_data()
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def find_titles(self):
        try:
            soup = self.__parse_page()

            div_elements = soup.find("div", class_="pt-3")
            li_elements = div_elements.find_all("li")
            all_titles = [title.text.strip() for title in li_elements]

            titles = [title for title in all_titles if self.search_term.lower() in title.lower()]

            return titles

        except Exception as e:
            raise Exception(f"An error occurred while fetching the titles: {str(e)}")


