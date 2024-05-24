import requests
from bs4 import BeautifulSoup
from time import sleep

from scrape_up.config.request_config import RequestConfig, get


class Jobs:
    """
    Create an instance of the class `Jobs`
    ```python
    scraper = Jobs()
    ```
    | Methods                       | Details                                                                                            |
    | ----------------------------- | -------------------------------------------------------------------------------------------------- |
    | `.filter_job()`               | Apply filters to the job search using parameters like title, country, city, minimum and maximum years of experience. |
    | `.fetch_jobs()`               | Fetch job listings based on the applied filters, with an optional maximum number of pages to scrape. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.url = "https://wuzzuf.net/search/jobs/?"
        self.config = config

    def filter_job(
        self,
        title=None,
        country=None,
        city=None,
        min_years_of_experience=None,
        max_years_of_experience=None,
    ):
        """
        Apply filters to the job search.

        Parameters:
        - `title` (str): Job title to search for.
        - `country` (str): Country to search for jobs in.
        - `city` (str): City to search for jobs in.
        - `min_years_of_experience` (int): Minimum years of experience required.
        - `max_years_of_experience` (int): Maximum years of experience allowed.

        Example:
        ```python
        scraper.filter_job(title="software engineer", country="Egypt", city="Cairo", min_years_of_experience=2, max_years_of_experience=5)
        ```
        """
        if title:
            title = title.replace(" ", "+")
            self.url += f"q={title}"
        if country:
            self.url += f"&filters[country][0]={country.strip().capitalize()}"
        if city:
            self.url += f"&filters[city][0]={city.strip().capitalize()}"
        if min_years_of_experience:
            self.url += (
                f"&filters[years_of_experience_min][0]={min_years_of_experience}"
            )
        if max_years_of_experience:
            self.url += (
                f"&filters[years_of_experience_max][0]={max_years_of_experience}"
            )

    def __fetch_page_jobs(self, page_num):
        response = get(self.url + f"&start={page_num}", self.config)
        if response.status_code == 200:
            parsed_html = BeautifulSoup(response.content, "lxml")
            jobs_data = parsed_html.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
            job_sub_list = []
            for job_data in jobs_data:
                job = {
                    "name": self.__get_job_name(job_data),
                    "url": self.__get_job_url(job_data),
                    "company": self.__get_job_company(job_data),
                    "location": self.__get_job_location(job_data),
                    "published_time": self.__get_published_time(job_data),
                    "properties": self.__get_job_properties(job_data),
                }
                job_sub_list.append(job)
            return job_sub_list
        else:
            raise None

    def fetch_jobs(self, max_page_number=50):
        """
        Fetch job listings based on the applied filters.

        Parameters:
        - `max_page_number` (int): Maximum number of pages to scrape (default is 50).

        Returns:
        - `list`: A list of dictionaries representing the fetched job listings.

        Example:
        ```python
        jobs = scraper.fetch_jobs(max_page_number=5)
        ```
        """
        job_list = []
        try:
            for page_num in range(max_page_number):
                job_sub_list = self.__fetch_page_jobs(page_num)
                if job_sub_list:
                    job_list.extend(job_sub_list)
                else:
                    break
                sleep(1)
        except requests.RequestException as e:
            return None
        return job_list

    def __get_job_name(self, job_data):
        return job_data.find("h2", {"class": "css-m604qf"}).find("a").text.strip()

    def __get_job_url(self, job_data):
        return job_data.find("h2", {"class": "css-m604qf"}).find("a")["href"]

    def __get_job_company(self, job_data):
        return job_data.find("div", {"class": "css-d7j1kk"}).find("a").text.strip()

    def __get_job_location(self, job_data):
        data = job_data.find("span", {"class": "css-5wys0k"})
        return data.text.strip() if data else None

    def __get_published_time(self, job_data):
        return (
            job_data.find("div", {"class": "css-4c4ojb"})
            or job_data.find("div", {"class": "css-do6t5g"})
        ).text.strip()

    def __get_job_properties(self, job_data):
        job_properties_string = " ,".join(
            [prop.text for prop in job_data.find_all("span", {"class": "eoyjyou0"})]
        )
        return job_properties_string if job_properties_string else None
