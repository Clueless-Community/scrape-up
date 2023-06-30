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

        Company: The name of the company\n
        Location: The location at which the company is located\n
        Experience: The experience of the applicants required for the post\n
        Days: The number of days before which this job was posted on this webiste\n
        Application Links: The link which directly takes you to the Web-page where you can fill-in the details\n
        
        '''
        Job_role = input('Enter your desired role: ')
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
    jobs = TimesJobs('Python')
    job_data=jobs.scrape()
    if job_data:
        print(job_data)

