from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class TimesJobs:
    def __init__(self, role: str, *, config: RequestConfig = RequestConfig()):
        self.role = role
        self.config = config

    def list_jobs(self):
        """
        Class - `TimesJobs`\n
        Example -\n
        ```python

        jobs = TimesJobs(role="developer")
        jobs.list_jobs()
        ```
        Return\n
        ```python
        return
        {
            "Company": "Name of the comapny",
            "Location": "Location at which the company is located",
            "Experience": "Experience of the applicants required for that post",
            "Posted": "Number of days before which this job was posted on this webiste",
            "Apply here": "Link which directly takes you to the Web-page where you can apply for the job"
        }
        """
        try:
            spl = self.role.split()
            self.role = "%20".join(spl)
        except:
            return None
        try:
            url = f"https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords={self.role}&txtLocation=India&cboWorkExp1=-1"
            response = get(url, self.config)
            soup = BeautifulSoup(response.text, "html.parser")
            companies = soup.find_all("h4")
            experiences = soup.find_all("div", class_="srp-exp")
            locations = soup.find_all("div", class_="srp-loc")
            days_ago = soup.find_all("span", class_="posting-time")
            application_links = soup.find_all("h3")

            job_data = []

            for i in range(len(companies)):
                company = companies[i].text
                location = locations[i].text
                experience = experiences[i].text
                days = days_ago[i].text
                href_value = application_links[i].a["href"]

                job_info = {
                    "Company": company,
                    "Location": location,
                    "Experience": experience,
                    "Posted": days,
                    "Apply here": href_value,
                }
                job_data.append(job_info)

            return job_data

        except Exception as e:
            print("Not possible to webscrape")
            return None
