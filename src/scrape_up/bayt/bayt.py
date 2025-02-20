import sys
import requests
from bs4 import BeautifulSoup


class Jobs:
    """
    Create an instance of the class `Jobs`
    ```python
    scraper = Jobs()
    jobs_data = scraper.fetch_jobs(query, page)
    ```
    | Methods                       | Details                                                                    |
    | ----------------------------- | -------------------------------------------------------------------------- |
    | `.fetch_jobs(query, page)`    | Fetch job listings data from Bayt.com based on the given query and page.   |
    """

    def __init__(self):
        self.base_url = "https://www.bayt.com"

    def fetch_jobs(self, query, page=1):
        """
        Fetch job listings data from Bayt.com based on the given query and page.

        Parameters:
        - `query`: The job search query.
        - `page` : The page number of the search results (default: 1).

        Example:
        ```python
        scraper = Jobs()
        jobs_data = scraper.fetch_jobs("software developer", page=1)
        ```
        """
        try:
            url = f"{self.base_url}/en/international/jobs/{query}-jobs/?page={page}"
            response = requests.get(url)

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            job_listings = soup.find_all("li", attrs={"data-js-job": ""})

            jobs = []
            for job in job_listings:
                job_info = self.__extract_job_info(job)
                if job_info:
                    jobs.append(job_info)
            sys.stdout.reconfigure(encoding="utf-8")
            return jobs
        except Exception:
            return None

    def __extract_job_info(self, job):
        """
        Extract job information from a single job listing.
        """
        try: 
            job_general_information = job.find("h2")
            if not job_general_information:
                return None

            job_title = self.__extract_job_title(job_general_information)
            job_url = self.__extract_job_url(job_general_information)
            company_name = self.__extract_company_name(job)
            job_location = self.__extract_job_location(job)

            return {
                "title": job_title,
                "company": company_name,
                "location": job_location,
                "url": job_url,
            }
        except Exception as e:
            print('Error extracting job info:', e)
            return None

    def __extract_job_title(self, job_general_information):
        return job_general_information.get_text(strip=True) if job_general_information else None

    def __extract_job_url(self, job_general_information):
        job_url_tag = job_general_information.find("a") if job_general_information else None
        return self.base_url + job_url_tag["href"] if job_url_tag else None

    def __extract_company_name(self, job):
        company_tag = job.find("div", class_="t-nowrap p10l")
        company_name = company_tag.find("span").get_text(strip=True) if company_tag and company_tag.find("span") else None
        return company_name

    def __extract_job_location(self, job):
        location_tag = job.find("div", class_="t-mute t-small")
        job_location = location_tag.get_text(strip=True) if location_tag else None
        return job_location
