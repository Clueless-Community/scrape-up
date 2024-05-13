import requests
from bs4 import BeautifulSoup
from time import sleep
from stringdecorator import string_decorator 

class JobScraper:
    """
    Usage:
    1. Create an instance of the JobScraper class:
        ```python
        scraper = JobScraper()
        ```

    2. Apply filters using the filter_job() method:
        ```python
        scraper.filter_job(title="software engineer", country="Egypt", city="Cairo", min_years_of_experience=2, max_years_of_experience=5)
        ```

    3. Fetch job listings using the fetch_jobs() method:
        ```python
        jobs = scraper.fetch_jobs()
        ```

    4. Output or process the fetched jobs as needed.
    """

    def __init__(self):
        self.url = "https://wuzzuf.net/search/jobs/?"

    def filter_job(self, title=None, country=None, city=None, min_years_of_experience=None, max_years_of_experience=None):
        if title:
            title = title.replace(" ", "+")
            self.url += f"q={title}"
        if country:
            self.url += f"&filters[country][0]={country.strip().capitalize()}"
        if city:
            self.url += f"&filters[city][0]={city.strip().capitalize()}"
        if min_years_of_experience:
            self.url += f"&filters[years_of_experience_min][0]={min_years_of_experience}"
        if max_years_of_experience:
            self.url += f"&filters[years_of_experience_max][0]={max_years_of_experience}"
    def _fetch_page_jobs(self, page_num):
            response = requests.get(self.url + f"&start={page_num}")
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
                raise ConnectionError(f"Error code: {response.status_code}")


    def fetch_jobs(self, max_page_number=1000):
        job_list = []
        try:
            for page_num in range(max_page_number):
                job_sub_list = self._fetch_page_jobs(page_num)
                if job_sub_list:
                    job_list.extend(job_sub_list)
                else:
                    break
                sleep(1)
        except requests.RequestException as e:
            return None
        return job_list

    @string_decorator
    def __get_job_name(self, job_data):
        return job_data.find("h2", {"class": "css-m604qf"}).find("a")

    def __get_job_url(self, job_data):
        return job_data.find("h2", {"class": "css-m604qf"}).find("a")["href"]

    @string_decorator
    def __get_job_company(self, job_data):
        return job_data.find("div", {"class": "css-d7j1kk"}).find("a")

    @string_decorator
    def __get_job_location(self, job_data):
        return job_data.find("span", {"class": "css-5wys0k"})

    @string_decorator
    def __get_published_time(self, job_data):
        return job_data.find("div", {"class": "css-4c4ojb"}) or job_data.find("div", {"class": "css-do6t5g"})

    def __get_job_properties(self, job_data):
        job_properties_string = " ,".join(
            [prop.text for prop in job_data.find_all("span", {"class": "eoyjyou0"})]
        )
        return job_properties_string if job_properties_string else "NA"

def main():
    scraper = JobScraper()
    scraper.filter_job(title="software engineer")
    jobs = scraper.fetch_jobs(max_page_number=1)
    print(jobs)

if __name__ == "__main__":
    main()