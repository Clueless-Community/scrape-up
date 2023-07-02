import requests
from bs4 import BeautifulSoup
import json


class TimesJobs:
    def __init__(self, Job_role:str):
        self.Job_role=Job_role
        
    
    def scrape(self):
        """
        Class - `TimesJobs`\n
        Example -\n
        ```python

        jobs = TimesJobs()
        jobs.scrape('Python')
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
        if isinstance(self.Job_role, int):
            print('Enter a valid Job role')
            return None
            
        try:
            spl = self.Job_role.split()
            self.Job_role = '%20'.join(spl)
        except:
            pass
        try:
            url=f'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords={self.Job_role}&txtLocation=India&cboWorkExp1=-1'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            companies = soup.find_all('h4')
            experiences = soup.find_all('div', class_='srp-exp')
            locations = soup.find_all('div', class_='srp-loc')
            days_ago = soup.find_all('span', class_='posting-time')
            application_links = soup.find_all('h3')

            job_data = []

            for i in range(len(companies)):
                company = companies[i].text
                location = locations[i].text
                experience = experiences[i].text
                days = days_ago[i].text
                href_value = application_links[i].a['href']
                
                job_info = {
                    'Company': company,
                    'Location': location,
                    'Experience': experience,
                    'Posted': days,
                    'Apply here': href_value
                }
                job_data.append(job_info)

            if len(job_data)==0:
                return 'No result found'
            return json.dumps(job_data)

        
        except Exception as e:
            print('Not possible to webscrape')
            return None
        
if __name__ == "__main__":
    jobs = TimesJobs(1)
    job_data=jobs.scrape()
    if job_data:
        print(job_data)
