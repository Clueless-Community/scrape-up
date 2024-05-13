import requests
from bs4 import BeautifulSoup


class FlexJobs:
    """
    A class to scrape job listings from FlexJobs website based on search query and location.

    Attributes:
        search_query (str): The search query to filter job listings.
        location_query (str): The location query to filter job listings (optional, defaults to '').
        min_jobs (int): The maximum number of job listings to retrieve (optional, defaults to 100).

    # Instantiate FlexJobs class with search query
    flexjobs = FlexJobs("python developer")

    # Optionally, specify location query and maximum number of job listings
    # flexjobs = FlexJobs("python developer", "New York", min_jobs=50)

    # flexjobs = FlexJobs("python developer", min_jobs=150)

    # Retrieve job listings
    jobs = flexjobs.get_jobs()

    # Print job details
    for job in jobs:
        print(job)

    """

    def __init__(self, search_query: str, location_query: str = '', min_jobs: int = 100):
        """
        Initializes the FlexJobs class with search query, location query, and maximum number of job listings.

        Args:
            search_query (str): The search query to filter job listings.
            location_query (str): The location query to filter job listings (optional, defaults to '').
            min_jobs (int): The maximum number of job listings to retrieve (optional, defaults to 100).
        """
        self.search_query = search_query
        self.location_query = location_query
        self.min_jobs = min_jobs

    def get_jobs(self):
        """
        Retrieves job listings from FlexJobs website based on search and location queries.

        Returns:
            list: A list of dictionaries containing job details.
        """
        # Formatting search and location queries for URL
        search = self.search_query.strip().replace(' ', '%20')
        location = self.location_query.strip().replace(' ', '%2C%20')

        # Constructing base URL
        base_url: str = f'https://www.flexjobs.com/search?searchkeyword={search}'
        if location != '':
            base_url = f'{base_url}&joblocations={location}'

        job_listings = []
        page = 1
        # Loop until maximum job listings are retrieved or no more listings available
        while len(job_listings) < self.min_jobs:
            url = f"{base_url}&page={page}"
            response = requests.get(url)
            if response.status_code == 200:
                # Parsing HTML content
                soup = BeautifulSoup(response.content, 'html.parser')
                job_cards = soup.find_all('div', class_='sc-jv5lm6-0')
                if not job_cards:
                    break
                # Extracting job information from each listing
                for job_card in job_cards:
                    job_listings.append(self.scrape_job_info(job_card))
                    if len(job_listings) >= self.min_jobs:
                        break
                page += 1
            else:
                print(f"Failed to fetch URL: {url}")
                break
        return job_listings

    def scrape_job_info(self, job_listing):
        """
        Extracts job details from a job listing HTML element.

        Args:
            job_listing (BeautifulSoup.element.Tag): HTML element containing job listing information.

        Returns:
            dict: A dictionary containing job details.
        """
        # Extracting job details from HTML elements
        job_title_element = job_listing.find('a', id=lambda x: x and x.startswith('job-name-'))
        job_title = job_title_element.text.strip() if job_title_element else None

        link: str = 'https://www.flexjobs.com/' + job_title_element['href'] if job_title_element else None

        location_element = job_listing.find('span', id=lambda x: x and x.startswith('allowedlocation-'))
        location = location_element.text.strip() if location_element else None

        job_age_element = job_listing.find('div', id=lambda x: x and x.startswith('job-age-'))
        job_age = job_age_element.text.strip() if job_age_element else None

        remote_option = job_listing.find('li', id=lambda x: x and x.startswith('remoteoption-'))
        remote = remote_option.text.strip() if remote_option else None

        job_schedule = job_listing.find('li', id=lambda x: x and x.startswith('jobschedule-'))
        schedule = job_schedule.text.strip() if job_schedule else None

        job_type = job_listing.find('li', id=lambda x: x and x.startswith('jobTypes-'))
        job_type_text = job_type.text.strip() if job_type else None

        salary_range = job_listing.find('li', id=lambda x: x and x.startswith('salartRange-'))
        salary = salary_range.text.strip() if salary_range else None

        description = job_listing.find('p', class_='sc-jv5lm6-4')
        job_description = description.text.strip() if description else None

        job = {
            "title": job_title,
            "location": location,
            "link": link,
            "posted_day": job_age,
            "remote": remote,
            "schedule": schedule,
            "job_type": job_type_text,
            "salary": salary,
            "description": job_description
        }

        return job
