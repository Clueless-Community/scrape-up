from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class FlexJobs:
    """
    ```python
    flex_jobs = FlexJobs(search_query, location_query, min_jobs)
    ```

    Attributes:
    | Attribute         | Optional | Details                                        |
    |-------------------|----------|------------------------------------------------|
    | `search_query`    | No       | The search query for job listings              |
    | `location_query`  | Yes      | The location query for job listings            |
    | `min_jobs`        | Yes      | The minimum number of job listings to retrieve |

    Methods:
    | Method                          | Details                                                                  |
    |---------------------------------|--------------------------------------------------------------------------|
    | `.get_jobs()`                   | Returns a list of job listings based on the search and location queries. |
    | `.scrape_job_info(job_listing)` | Extracts job details from a given job listing HTML element               |
    """

    def __init__(
        self,
        search_query: str,
        location_query: str = "",
        min_jobs: int = 100,
        *,
        config: RequestConfig = RequestConfig(),
    ):
        self.search_query = search_query
        self.location_query = location_query
        self.min_jobs = min_jobs
        self.config = config

    def get_jobs(self):
        """
        Retrieves job listings based on the search and location queries.

        Returns:
        list: A list of dictionaries, each containing details of a job listing.
        ```js
        [
            {
                'title': 'Contract Administrator',
                'location': 'Springboro, OH',
                'link': 'https://www.flexjobs.com//HostedJob.aspx?id=2061188',
                'posted_day': '13 days ago',
                'remote': 'Hybrid Remote Work',
                'schedule': 'Full-Time',
                'job_type': 'Freelance',
                'salary': 'A range of 70,000.00 - 90,000.00 USD Annually',
                'description': 'Coordinate and administer construction contracts, prepare bid documentation, manage purchase orders and subcontracts, manage certificates of insurance and bonds, and liaise with internal teams, clients, and subcontractors.',
            },
            {...},
            {...},
        ]
        ```
        """
        # Formatting search and location queries for URL
        search = self.search_query.strip().replace(" ", "%20")
        location = self.location_query.strip().replace(" ", "%2C%20")

        # Constructing base URL
        base_url: str = f"https://www.flexjobs.com/search?searchkeyword={search}"
        if location != "":
            base_url = f"{base_url}&joblocations={location}"

        job_listings = []
        page = 1
        # Loop until maximum job listings are retrieved or no more listings available
        while len(job_listings) < self.min_jobs:
            url = f"{base_url}&page={page}"
            response = get(url, self.config)
            if response.status_code == 200:
                # Parsing HTML content
                soup = BeautifulSoup(response.content, "html.parser")
                job_cards = soup.find_all("div", class_="sc-jv5lm6-0")
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
        Extracts job details from a given job listing HTML element.

        Args:
        job_listing: BeautifulSoup HTML element representing a job listing.

        Returns:
        dict: A dictionary containing details of the extracted job.
        ```js
        {
            'title': 'Contract Administrator',
            'location': 'Springboro, OH',
            'link': 'https://www.flexjobs.com//HostedJob.aspx?id=2061188',
            'posted_day': '13 days ago',
            'remote': 'Hybrid Remote Work',
            'schedule': 'Full-Time',
            'job_type': 'Freelance',
            'salary': 'A range of 70,000.00 - 90,000.00 USD Annually',
            'description': 'Coordinate and administer construction contracts, prepare bid documentation, manage purchase orders and subcontracts, manage certificates of insurance and bonds, and liaise with internal teams, clients, and subcontractors.',
        }
        ```
        """
        # Extracting job details from HTML elements
        job_title_element = job_listing.find(
            "a", id=lambda x: x and x.startswith("job-name-")
        )
        job_title = job_title_element.text.strip() if job_title_element else None

        link: str = (
            "https://www.flexjobs.com/" + job_title_element["href"]
            if job_title_element
            else None
        )

        location_element = job_listing.find(
            "span", id=lambda x: x and x.startswith("allowedlocation-")
        )
        location = location_element.text.strip() if location_element else None

        job_age_element = job_listing.find(
            "div", id=lambda x: x and x.startswith("job-age-")
        )
        job_age = job_age_element.text.strip() if job_age_element else None

        remote_option = job_listing.find(
            "li", id=lambda x: x and x.startswith("remoteoption-")
        )
        remote = remote_option.text.strip() if remote_option else None

        job_schedule = job_listing.find(
            "li", id=lambda x: x and x.startswith("jobschedule-")
        )
        schedule = job_schedule.text.strip() if job_schedule else None

        job_type = job_listing.find("li", id=lambda x: x and x.startswith("jobTypes-"))
        job_type_text = job_type.text.strip() if job_type else None

        salary_range = job_listing.find(
            "li", id=lambda x: x and x.startswith("salartRange-")
        )
        salary = salary_range.text.strip() if salary_range else None

        description = job_listing.find("p", class_="sc-jv5lm6-4")
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
            "description": job_description,
        }

        return job
