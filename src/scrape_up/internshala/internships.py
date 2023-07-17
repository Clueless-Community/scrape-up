import requests
from bs4 import BeautifulSoup


class Internshala:
    """
    Create an object for the 'Internships' class :\n
    ```python
    scraper = Internships()
    ```
    | Methods          | Details                                                              |
    | ---------------- | -------------------------------------------------------------------- |
    | `.internships()` | Scrapes and returns a list of dictionaries representing internships. |
    | `.jobs()`        | Scrapes and returns a list of dictionaries representing jobs.        |
    """

    def __init__(self, search_type):
        self.base_url = "https://internshala.com/"
        self.search_type = search_type

    def __scrape_page(self, url):
        try:
            html_text = requests.get(url)
            html_text.raise_for_status()
            return html_text.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def __parse_page(self, html):
        try:
            soup = BeautifulSoup(html, "lxml")
            return soup
        except Exception as e:
            raise Exception(f"An error occurred while parsing the page: {str(e)}")

    def internships(self):
        """
        Fetches the jobs data.\n
        Class - `Jobs`
        Example:
        ```
        search = Internshala(search_type="machine learning")
        search.jobs()
        ```
        Returns:
        ```js
        [
            {
            "title":"Machine Learning Instructor",
            "company":"Future Skills",
            "location":"Hyderabad",
            "CTC":"₹  3 - 5 LPA",
            "experience(in years)":"0-5"
            }
        ]
        ```
        """
        try:
            self.search_type = self.search_type.replace(" ", "%20")
            url = self.base_url + "internships/" + "keywords-" + self.search_type
            html = self.__scrape_page(url)
            page = self.__parse_page(html)
            internships = []

            internships_container = page.find_all("div", class_="individual_internship")

            if not internships_container:
                return {"message": "No internships found"}

            else:
                for internship in internships_container:
                    title = internship.find(
                        "h3", class_="heading_4_5 profile"
                    ).text.strip()
                    company = internship.find(
                        "h4", class_="heading_6 company_name"
                    ).text.strip()
                    location = internship.find("a", class_="location_link").text.strip()
                    other_details = internship.find_all(class_="item_body")
                    duration = (
                        other_details[1].text.strip()
                        if len(other_details) > 2
                        else "N/A"
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

    def jobs(self):
        """
        Fetches the jobs data.\n
        Class - `Jobs`
        Example:
        ```
        search = Internshala(search_type="machine learning")
        search.internships()
        ```
        Returns:
        ```js
        [
            {
                "title":"Data Science",
                "company":"Vedasis Analytics",
                "location":"Work From Home",
                "duration":"3 Months",
                "stipend":"₹ 5,000 /month"
            }
        ]
        ```
        """
        try:
            self.search_type = self.search_type.replace(" ", "%20")
            url = self.base_url + "jobs/" + "keywords-" + self.search_type
            html = self.__scrape_page(url)
            page = self.__parse_page(html)
            jobs = []

            jobs_container = page.find("div", {"id": "internship_list_container_1"})

            if not jobs_container.text:
                return {"message": "No jobs found"}
            else:
                for item in jobs_container.find_all(
                    "div",
                    {
                        "class": "container-fluid individual_internship visibilityTrackerItem"
                    },
                ):
                    title = item.find(
                        "h3", {"class": "heading_4_5 profile"}
                    ).text.strip()
                    company = item.find(
                        "h4", {"class": "heading_6 company_name"}
                    ).text.strip()
                    location = item.find("p", {"id": "location_names"}).text.strip()
                    ctc = item.find("div", {"class": "item_body salary"}).text.strip()
                    experience = (
                        item.find("div", {"class": "item_body desktop-text"})
                        .text.strip()
                        .split()[0]
                    )

                    job_data = {
                        "title": title,
                        "company": company,
                        "location": location,
                        "CTC": ctc,
                        "experience(in years)": experience,
                    }

                    jobs.append(job_data)

                return {
                    "data": jobs,
                    "message": "Jobs are now fetched",
                }
        except Exception as e:
            raise Exception(f"An error occurred while scraping jobs: {str(e)}")


internship = Internshala(search_type="machine learning")
print(internship.internships())
