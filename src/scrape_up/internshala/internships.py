import requests
from bs4 import BeautifulSoup


class Internships:
    """
    Class to scrape internships from Internshala website.
    """

    def __init__(self):
        """
        Initializes the Internships class.
        """
        self.base_url = "https://internshala.com/internships/"

    def scrape_page(self, url):
        """
        Fetches the HTML content of the specified URL.

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The HTML content of the URL.

        Raises:
            Exception: If an error occurs while fetching the page.
        """
        try:
            html_text = requests.get(url)
            html_text.raise_for_status()
            return html_text.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def parse_page(self, html):
        """
        Parses the HTML content using BeautifulSoup.

        Args:
            html (str): The HTML content to parse.

        Returns:
            BeautifulSoup: The parsed BeautifulSoup object.

        Raises:
            Exception: If an error occurs while parsing the page.
        """
        try:
            soup = BeautifulSoup(html, "lxml")
            return soup
        except Exception as e:
            raise Exception(f"An error occurred while parsing the page: {str(e)}")

    def internships(self):
        """
        Fetches the internships data.

        Returns:
            dict: A dictionary containing the fetched internships data.

        Raises:
            Exception: If an error occurs while scraping internships.
        """
        try:
            search_type = input(
                "Enter the type of internships you want to search for: "
            )
            url = self.base_url + search_type
            html = self.scrape_page(url)
            page = self.parse_page(html)
            internships = []

            internships_container = page.find_all("div", class_="individual_internship")

            for internship in internships_container:
                title = internship.find("h3", class_="heading_4_5 profile").text.strip()
                company = internship.find(
                    "h4", class_="heading_6 company_name"
                ).text.strip()
                location = internship.find("a", class_="location_link").text.strip()
                other_details = internship.find_all(class_="item_body")
                duration = (
                    other_details[1].text.strip() if len(other_details) > 2 else "N/A"
                )
                stipend_element = internship.find("span", class_="stipend")
                stipend = stipend_element.text.strip() if stipend_element else "N/A"

                internship_data = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "duration": duration,
                    "stipend": stipend,
                }

                internships.append(internship_data)

            return {
                "data": internships,
                "message": "Internships are now fetched",
            }
        except Exception as e:
            raise Exception(f"An error occurred while scraping internships: {str(e)}")
