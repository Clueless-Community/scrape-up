import requests
from bs4 import BeautifulSoup

class TimesJobs:
    def __init__(self):
        pass
        
    
    def scrape(self):
        '''
        This is a Webscraped module used to
        find jobs on a platform named TimesJobs.
        It gives the information of 

        Company: The name of the company\n
        Location: The location at which the company is located\n
        Experience: The experience of the applicants required for the post\n
        Days: The number of days before which this job was posted on this webiste\n
        Application Links: The link which directly takes you to the Web-page where you can fill-in the details\n
        
        '''
        Job_role = input('Enter your desired role: ')
        try:
            spl = Job_role.split()
            Job_role = '%20'.join(spl)
        except:
            pass
        try:
            url=f'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords={Job_role}&txtLocation=India&cboWorkExp1=-1'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            companies = soup.find_all('h4')
            experiences = soup.find_all('div', class_='srp-exp')
            locations = soup.find_all('div', class_='srp-loc')
            days_ago = soup.find_all('span', class_='posting-time')
            application_links = soup.find_all('h3')


            for i in range(len(companies)):
                company = companies[i].text
                location = locations[i].text
                experience = experiences[i].text
                days = days_ago[i].text
                href_value = application_links[i].a['href']
                
                
                print(f'Company: {company}\nLocation: {location}\nExperience: {experience}\nPosted: {days} ago')
                print(f'Apply here: {href_value}\n')

        
        except Exception as e:
            print('Not possible to webscrape')
            return None
        
if __name__ == "__main__":
    jobs = TimesJobs()
    jobs.scrape()

