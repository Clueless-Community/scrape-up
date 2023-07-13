import pandas as pd
import requests
from bs4 import BeautifulSoup

"""
        Class - `Covid Info`\n

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.scrape()`                 | Returns the scraped data from the target website of all the countries in the form of a list          |
    | `.findCountry()`            | Returns the data related to the specific country passed as a parameter into the function             |
    | `.sortbycases()`            | Returns the list of datas of all the country, sorted according to the number of cases                |
    | `.sortbydeaths()`           | Returns the list of datas of all the country, sorted according to the number of deaths               |
    | `.totalcases()`             | Returns the total number of covid cases as of yet in the form of a string of numbers                 |
    | `.totaldeaths()`            | Returns the total number of covid deaths as of yet in the form of a string of numbers                |
"""

class CovidInfo:
  """This class is used to get live covid-related data such as realtime worldwide cases, deaths, cases and related info by country, info of all the countries, and so on."""  

  def __init__(self):
        print(self)

  def scrape(self):
    """Get the scraped data of all the countries"""


    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = [['Country','Number of Cases', 'Deaths']]
    data_iterator = iter(soup.find_all('td'))
    while True:
      try:
        country = next(data_iterator).text
        confirmed = str(next(data_iterator).text.replace(',','').replace(' ',''))
        deaths = str(next(data_iterator).text.replace(',','').replace(' ',''))
        continent = next(data_iterator).text

        data.append([
            country,
            int(confirmed),
            int(deaths),
            continent
        ])

      except StopIteration:
        break
    if data.length == 1:
      return None
    else:
      return data  


  def findCountry(self, name):
    """Get the covid-data of any particular country.\n
    Parameters info: \n
    - "name": it is the full name of the country whose data is to be returned"""


    try:

      ata = self.scrape()
      fc = [['Country','Number of Cases', 'Deaths']]
      for i in data:
        if i[0].lower() == name.lower():
          fc.append([i[0],i[1],i[2]])

          return fc
      return 'Data not aviliable for value entered'
    except:
      return None

  def sortbycases(self, rev):
    """Get the covid detail list of all the country sorted by total cases in that country"""
    try:
      data = self.scrape()
      data.remove(['Country','Number of Cases', 'Deaths'])
      data = sorted(data, key= lambda r:r[1],reverse=rev)
      return data
    except:
      return None  

  def sortbydeaths(self, rev):
    """Get the covid detail list of all the country sorted by total deaths in that country"""
    try:
      data = self.scrape()
      data.remove(['Country','Number of Cases', 'Deaths'])
      data = sorted(data, key= lambda r:r[2],reverse=rev)
      return data
    except:
      return None  

  def totalcases(self):
    """Get the total number of COVID cases in the world"""
    try:
      url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
      page = requests.get(url)
      soup = BeautifulSoup(page.text, 'html.parser')
      req = soup.find_all('span',{"class": "bold_number"})

      z = req[0].find_all('a')
      fin = ''
      for i in z:
        fin = fin + i.contents[0]
      sol = fin.split(' ')
      return sol[0]
    except:
      return None  

  def totaldeaths(self):
    """Get the total number of COVID-deaths in the world"""
    try:
      url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
      page = requests.get(url)
      soup = BeautifulSoup(page.text, 'html.parser')
      req = soup.find_all('a',{"href": "/coronavirus/coronavirus-death-toll/"})
      k = req[0].find('strong').contents[0].split(' ')
      return k[0]
    except:
      return None  
