import bs4
from bs4 import BeautifulSoup
import requests

"""
         Create an instance of `NewsCNN` class.

     ```python
     news = newsCNN()
     ```

     | Methods               | Details                                                            |
     | --------------------- | ------------------------------------------------------------------ |
     | `.get()`              | Returns an article's headline, content, time, and author(s).       |
     | `.toparticles()`      | Returns the list of top trending articles with their urls          |
     | `.newsAsia()`         | Returns a list of articles pertaining to the Asia in CNN           |
     | `.newsAustralia()`    | Returns a list of articles pertaining to the Australia in CNN      | 
     | `.newsUS()`           | Returns a list of articles pertaining to the USA in CNN            |
     | `.newsAmericas()`     | Returns a list of articles pertaining to the Americas in CNN       |
     | `.newsUK()`           | Returns a list of articles pertaining to the UK in CNN             |
     | `.newsAfrica()`       | Returns a list of articles pertaining to the Africas in CNN        |
     | `.newsMiddleEast()`   | Returns a list of articles pertaining to the Middle East in CNN    |
     | `.newsChina()`        | Returns a list of articles pertaining to the China in CNN          |
     | `.newsEurope()`       | Returns a list of articles pertaining to the Europe in CNN         |
     | `.newsIndia()`        | Returns a list of articles pertaining to the India in CNN          |
     | `.newsbylocation()`   | Returns the list of articles by a specific location.               |

     """

class NewsCNN:
  """This class is used for getting articles and their revelant information from the CNN website."""

  def __init__(self):
    print(self)


  def get(self, url):
    """Returns a CNN-lite article along with it's author details, timestamp, and it's link"""
    try:

      page = requests.get(url)
      parse = BeautifulSoup(page.content,'html.parser')
      headline = parse.find('h2',attrs={'class':'headline'}).text.replace('\n','').strip()
      paras = parse.find_all('p',attrs={'class':'paragraph--lite'})
      author = parse.find('p',attrs={'class':'byline--lite'}).text.replace('By ','').replace('\n','').strip()
      time = parse.find('p',attrs={'class':'timestamp--lite'}).text.replace('Updated: ','').replace('\n','').strip()
      p = ''
      for para in paras:
        p = p + para.text.replace('\n','')

      return [headline,author,time,p]
    except:
      return None  



  def toparticles(self):

    """Returns the CNN's top stories of current day along with their necessary elements"""
    try:
      returnee = []
      articlelinks = []
      articletitle = []

      URL = 'https://lite.cnn.com'
      page = requests.get(URL)
      parsedHTML = BeautifulSoup(page.content, 'html.parser')
      urls = parsedHTML.find_all('li',attrs={'class':'card--lite'})
      for u in urls:
        k = u.find('a')['href']
        l = u.find('a').text.replace('\n','').strip()
        k = URL + k
        returnee.append([l,k])
      inst = returnee

      for i in range(len(returnee)):
        k = NewsCNN().get(returnee[i][1])
        returnee[i].append(k[1])
        returnee[i].append(k[2])
        returnee[i].append(k[3])


      return returnee
    except:
      return None  

  def newsAsia(self):
    """Returns the latest news articles pertaining to the Asia in CNN"""

    try:

      url = 'https://edition.cnn.com/world/asia'

      return NewsCNN().newsbylocation(url)
    except:
      return None  

  def newsAustralia(self):
    """Returns the latest news articles pertaining to the Australia in CNN"""

    try:

      url = 'https://edition.cnn.com/world/australia'

      return NewsCNN().newsbylocation(url)  
    except:
      return None  


  def newsAmericas(self):
    """Returns the latest news articles pertaining to the Americas in CNN"""

    try:

      url = 'https://edition.cnn.com/world/americas'

      return NewsCNN().newsbylocation(url)   
    except:
      return None
  
  def newsUS(self):
    """Returns the latest news articles pertaining to the US in CNN"""

    try:

      url = 'https://edition.cnn.com/world/us'

      return NewsCNN().newsbylocation(url)
    except:
      return  

  
  def newsMiddleEast(self):
    """Returns the latest news articles pertaining to the Middle-East in CNN"""

    try:
      url = 'https://edition.cnn.com/world/middle-east'

      return NewsCNN().newsbylocation(url)
    except:
      return None  

  
  def newsIndia(self):
    """Returns the latest news articles pertaining to the Indian Union in CNN"""

    try:

      url = 'https://edition.cnn.com/world/india'

      return NewsCNN().newsbylocation(url)  
    except:
      return None  

  
  def newsEurope(self):
    """Returns the latest news articles pertaining to the Europe in CNN"""

    try:

      url = 'https://edition.cnn.com/world/europe'

      return NewsCNN().newsbylocation(url)  
    except:
      return None    

  def newsAfrica(self):
    """Returns the latest news articles pertaining to the Africas in CNN"""

    try:

      url = 'https://edition.cnn.com/world/africa'

      return NewsCNN().newsbylocation(url) 
    except:
      return None   

  def newsChina(self):
    """Returns the latest news articles pertaining to the China in CNN"""
    try:

      url = 'https://edition.cnn.com/world/china'

      return NewsCNN().newsbylocation(url)  
    except:
      return None  


  def newsUK(self):
    """Returns the latest news articles pertaining to the UK in CNN"""
    try:

      url = 'https://edition.cnn.com/world/united-kingdom'

      return NewsCNN().newsbylocation(url)      
    except:
      return None      


    


  def newsbylocation(self, url = 'https://edition.cnn.com/world'):
    """Returns the relevant news articles corresponding to that particular geo-continent or country\n
    Parameters: \n
     - url: URL of the location page in CNN"""
    try:

      sol = [] 

      page = requests.get(url)
      parse = BeautifulSoup(page.content,'html.parser')
      heads = parse.find_all('span',attrs={'data-editable':'headline'})
      links1 = parse.find_all('a',attrs={'class':'container__link container_lead-plus-headlines-with-images__link'})
      links2 = parse.find_all('a',attrs={'class':'container__link container_vertical-strip__link'})
      links3 = parse.find_all('a',attrs={'class':'container__link container_lead-plus-headlines__link'})
    
      base = 'https://edition.cnn.com/'
      allurls = []
      allheads = []

      for i in heads:
        tmp = i.text
        allheads.append(tmp)


      for i in (links1 + links2 + links3):
        t = base + i['href']
        allurls.append(t)
      allurls = list(set(allurls))  
    
      for i in range(len(allurls)):
        sol.append([allheads[i],allurls[i]])

      return sol
    except:
      return None  
         

    

