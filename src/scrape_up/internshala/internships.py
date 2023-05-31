import requests
from bs4 import BeautifulSoup

class Internships:
    def __init__(self):
        self.base_url = 'https://internshala.com/internships/'
        
    def scrape_page(self, url):
        try:
            html_text = requests.get(url)
            html_text.raise_for_status()
            return html_text.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def parse_page(self, html):
        try:
            soup = BeautifulSoup(html, "lxml")
            return soup
        except Exception as e:
            raise Exception(f"An error occurred while parsing the page: {str(e)}")

    def internships(self):
        """
        Class - `Internships`
        Example:
        ```
        scraper = Internships()
        internships = scraper.internships()
        ```
        Returns:
        List of dictionaries, where each dictionary represents an internship and contains the following keys:
        - 'title': Title of the internship
        - 'company': Company offering the internship
        - 'location': Location of the internship
        - 'duration': Duration of the internship
        - 'stipend': Stipend offered for the internship
        """
        try:
            search_type = input("Enter the type of internships you want to search for: ")
            url = self.base_url + search_type
            html = self.scrape_page(url)
            page = self.parse_page(html)
            internships = []

            internships_container = page.find_all('div', class_='individual_internship')

            for internship in internships_container:
                title = internship.find('div', class_='heading_4_5 profile').text.strip()
                company = internship.find('div', class_='heading_6 company_name').text.strip()
                location = internship.find('a', class_='location_link').text.strip()
                duration = internship.find('span', class_='internship_durations').text.strip()
                stipend = internship.find('span', class_='stipend').text.strip()

                internship_data = {
                    'title': title,
                    'company': company,
                    'location': location,
                    'duration': duration,
                    'stipend': stipend
                }

                internships.append(internship_data)

            return internships
        except Exception as e:
            raise Exception(f"An error occurred while scraping internships: {str(e)}")



 