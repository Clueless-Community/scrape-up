import requests
from bs4 import BeautifulSoup
from time import sleep
from stringdecorator import stringDecorator


class JobScraper:
    """
    Usage:
    1. Create an instance of the JobScraper class.
        ```python
        scraper = JobScraper()
        ```

    2. Apply filters using the filterJob() method.
        ```python
        scraper.filterJob(title="software engineer", country="Egypt", city="Cairo", minYearsOfExperience=2, maxYearsOfExperience=5)
        ```
        Customize the filters based on your requirements.

    3. Fetch job listings using the fetchJobs() method.
        ```python
        jobs = scraper.fetchJobs()
        ```
        The fetched jobs will be stored in the 'jobs' variable.

    4. Save the fetched jobs to a CSV file using the FileSaver class.
        ```python
        saver = FileSaver()
        saver.saveToFile(jobs, 'jobListings.csv')
        ```
        Specify the desired file path for the CSV file.
    """

    def __init__(self):
        """
        Initializes the JobScraper instance with the base URL.
        """
        self.url = "https://wuzzuf.net/search/jobs/?"

    def filterJob(
        self,
        title=None,
        country=None,
        city=None,
        minYearsOfExperience=None,
        maxYearsOfExperience=None,
    ):
        """
        Filters job listings based on specified criteria.

        Args:
            title (str): The job title to filter by.
            country (str): The country to filter by.
            city (str): The city to filter by.
            minYearsOfExperience (int): The minimum years of experience to filter by.
            maxYearsOfExperience (int): The maximum years of experience to filter by.
        """

        if title is not None:
            title.replace(" ", "+")
            self.url += f"q={title}"
        if country is not None:
            self.url += f"&filters[country][0]={country.strip().capitalize()}"
        if city is not None:
            self.url += f"&filters[city][0]={city.strip().capitalize()}"
        if minYearsOfExperience is not None:
            self.url += f"&filters[years_of_experience_min][0]={minYearsOfExperience}"
        if maxYearsOfExperience is not None:
            self.url += f"&filters[years_of_experience_max][0]={maxYearsOfExperience}"

    def __fetchPageJobs(self, pageNum):
        """
        Fetches job listings from a specific page.

        Args:
            pageNum (int): The page number to fetch job listings from.

        Returns:
            list: A list of job listings from the specified page.

        Raises:
            ConnectionError: If there is an error fetching the job listings.
        """

        response = requests.get(self.url + f"&start={pageNum}")
        jobSubList = []
        if response.status_code == 200:
            parsedHtml = BeautifulSoup(response.content, "lxml")
            jobsData = parsedHtml.find_all("div", {"class": "css-1gatmva e1v1l3u10"})

            for jobData in jobsData:
                job = {
                    "name": self.__getJobName(jobData),
                    "url": self.__getJobUrl(jobData),
                    "company": self.__getJobCompany(jobData),
                    "location": self.__getJobLocation(jobData),
                    "publishedTime": self.__getPublishedTime(jobData),
                    "properties": self.__getJobProperties(jobData),
                }
                jobSubList.append(job)
        else:
            raise ConnectionError(f"Error code: {response.status_code}")
        return jobSubList

    def fetchJobs(self, maxPageNumber=1000):
        """
        Fetches job listings from multiple pages.

        Returns:
            list: A list of job listings from all pages.
        """

        jobList = []
        for pageNum in range(maxPageNumber):
            jobSubList = self.__fetchPageJobs(pageNum)
            if jobSubList:
                jobList.extend(jobSubList)
            else:
                break
            sleep(1)
        return jobList

    @stringDecorator
    def __getJobName(self, jobData):
        return jobData.find("h2", {"class": "css-m604qf"}).find("a")

    def __getJobUrl(self, jobData):
        return jobData.find("h2", {"class": "css-m604qf"}).find("a")["href"]

    @stringDecorator
    def __getJobCompany(self, jobData):
        return jobData.find("div", {"class": "css-d7j1kk"}).find("a")

    @stringDecorator
    def __getJobLocation(self, jobData):
        return jobData.find("span", {"class": "css-5wys0k"})

    @stringDecorator
    def __getPublishedTime(self, jobData):
        return jobData.find("div", {"class": "css-4c4ojb"}) or jobData.find(
            "div", {"class": "css-do6t5g"}
        )

    def __getJobProperties(self, jobData):
        jobPropertiesString = " ,".join(
            [prop.text for prop in jobData.find_all("span", {"class": "eoyjyou0"})]
        )
        return jobPropertiesString if jobPropertiesString else "NA"


def main():
    scraper = JobScraper()
    scraper.filterJob(title="software engineer")
    jobs = scraper.fetchJobs(maxPageNumber=1000)

    print(jobs)


if __name__ == "__main__":
    main()
