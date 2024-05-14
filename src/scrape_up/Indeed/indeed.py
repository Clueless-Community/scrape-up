import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

class Indeed:
    """
    Create an instance of `Indeed` class.
     ```python
     indeed = Indeed()
     ```
    | Methods                | Details                                                                                          |
    | ---------------------- | ------------------------------------------------------------------------------------------------ |
    | `.get_url()`           | Returns the URL of the job having a specific position and location.                              |
    | `.get_record()`        | Returns the company details like job title, company name, location, job post date, and salary.   |
    """

    def __init__(self):
        self.position=position
        self.location=location
      
    def get_url (self, position,location):
        template = 'https://www.indeed.com/jobs?q={}&l={}'
        url = template.format(position,location)
        return url

    #getting the record
    def get_record(self, card):
        atag1= card.h2.a.span
        job_title= atag1.get('title')
        atag2= card.h2.a
        job_url= 'https://indeed.com'+atag2.get('href')
      
        company= card.find('span','companyName').text.strip()
        location= card.find('div','companyLocation').text.strip()
        summary= card.find('div','job-snippet').text.strip()
        posted_date= card.find('span','date').text.strip()
        today= datetime.today().strftime('%Y-%m-%d')

        try: 
            salary =  card.find('div','metadata estimated-salary-container').text.strip()
        except AttributeError:
            salary = ''
        
        record = (job_title, job_url, location, company, posted_date, today, summary, salary)
        return record

    #writing the main function
    def main(self, position, location):
        records = []
        url = get_url(position, location)

        while True:
            response=requests.get(url)
            soup = BeautifulSoup(response.text,'html.parser')
            cards=soup.find_all('div','job_seen_beacon')
            for card in cards:
                record=get_record(card)
                records.append(record)
            try:
                url='https://indeed.com'+soup.find('a',{'aria-label':'Next'}).get('href')
            except AttributeError:
                break
    
        with open(f'{position}-{location}.csv','w',newline='',encoding= 'utf-8') as f:
            writer= csv.writer(f)
            writer.writerow(['Job_Title', 'Job_Url', 'Location', 'Company', 'Post_Date', 'Extraction_Date', 'Summary', 'Salary'])
            writer.writerows(records) 

main('business manager', 'Geneva')      #creating a demo csv file to access the records
