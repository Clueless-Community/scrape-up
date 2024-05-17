from bs4 import BeautifulSoup
import requests

from scrape_up.config.request_config import RequestConfig, get


class Internshala:
    """
    Create an object for the 'Internships' class :\n
    ```python
    scraper = Internshala()
    ```
    | Methods                  | Details                                                                 |
    | ------------------------ | ----------------------------------------------------------------------- |
    | `.internships()`         | Scrapes and returns a list of dictionaries representing internships.    |
    | `.jobs()`                | Scrapes and returns a list of dictionaries representing jobs.           |
    | `.certification_courses()`| Scrapes and returns a list of dictionaries representing certification courses.|
    """

    def __init__(self, search_type: str, *, config: RequestConfig = RequestConfig()):
        self.base_url = "https://internshala.com/"
        self.search_type = search_type
        self.config = config

    def __scrape_page(self, url: str):
        try:
            html_text = get(url, self.config)
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
                return None

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

                return internships["data"]
        except:
            return None

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
                return None
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

                return jobs
        except:
            return None

    def certification_courses(self):
        """
        Fetches the certification courses data.
        Example:
        ```python
        search = Internshala(search_type="web development")
        search.certification_courses()
        ```
        Returns:
        ```js
        [
            {
                "title":"Web Development",
                "duration":"8 weeks",
                "rating":"4.1",
                "learners":"91,313",
                "link":"https://trainings.internshala.com/web-development-course/?utm_source=is_web_IS-home-midsection_web1"
            }
            ...
        ]
        ```
        """
        try:
            url = self.base_url
            html = self.__scrape_page(url)
            page = self.__parse_page(html)
            certification_courses = []

            certification_section = page.find(
                "div", class_="certification-trainings-section"
            )
            if certification_section:
                certification_cards = certification_section.find_all(
                    "div", class_="card"
                )
                for card in certification_cards:
                    title_element = card.find("h6")
                    duration_element = card.find("span", class_="duration")
                    rating_element = card.find("span", class_="rating")
                    learners_element = card.find("span", class_="learners")
                    link_element = card.find("a")

                    title = title_element.text.strip() if title_element else None
                    duration = (
                        duration_element.text.strip() if duration_element else None
                    )
                    rating = rating_element.text.strip() if rating_element else None
                    learners = (
                        learners_element.text.strip() if learners_element else None
                    )
                    link = link_element["href"] if link_element else None

                    if all((title, duration, rating, learners, link)):
                        certification_data = {
                            "title": title,
                            "duration": duration,
                            "rating": rating,
                            "learners": learners,
                            "link": link,
                        }
                        certification_courses.append(certification_data)

                return certification_courses
            else:
                return None
        except:
            return None
