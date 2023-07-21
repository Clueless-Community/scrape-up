import urllib
import requests
import pandas as pd
import json
import sys
from datetime import datetime
from bs4 import BeautifulSoup as Soup


class Quora:

  """
    Class - `Quora`\n
    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.fetch_answers()`          | Returns the list of answers pertaining to a particular url gien by the user as parameter.            |
    | `.getbyquery()`             | Returns the list of answers pertaining to a particular query given by the user.                      |
    | `.getprofile()`             | Returns the list of the name of a user along with their quora profile link.                          |

  """


  def __init__(self):
    print(self)


  def fetch_answers(self,my_url):
    """
         Class - `Quora`
         Example:
         ```
         quora = Quora()
         quora.fetch_answers('url goes here')
         ```
         Returns:
         ```js
         {
             "answers": The list of all the answers aviliable for a particular link of question.
         }
         ```
         """
    try:
      req = requests.get(my_url)

      page_soup = Soup(req.content, "html.parser")
      main_box = page_soup.findAll("script", {"type": "application/ld+json"})[0].text

      data = json.loads(main_box)
      answers = []
      try:
        answers += [x["text"] for x in data["mainEntity"]["acceptedAnswer"]]
      except:
        pass
      answers += [x["text"] for x in data["mainEntity"]["suggestedAnswer"]]

      for i in range(len(answers)):

        print(f"\n\n\n\n Answers #{i+1}\n\n")
        print(answers[i])

      return answers
    except:
      return None


  def getbyquery(self,query):
    """
         Class - `Quora`
         Example:
         ```
         quora = Quora()
         quora.getbyquery('query goes here')
         ```
         Returns:
         ```js
         {
             "answers": The list of all the answers aviliable for a particular query of question given. If there is no data aviliable, then empty list is returned.
         }
         ```
         """
    try:

      base = 'https://www.quora.com/'
      query = query.replace(' ','-')
      url = base+query
      k =Quora().fetch_answers(url)
      return k
    except:
      return None

  def getprofile(self,username):
    """
         Class - `Quora`
         Example:
         ```
         quora = Quora()
         quora.getprofile('quora-username goes here')
         ```
         Returns:
         ```js
         {
             "profile": The list of all the details aviliable for a particular quora profile
         }
         ```
         """
    username = username.upper()
    username = username.split()
    for i in range(1,len(username)):
      username[i]='-'+username[i]

    res = ''.join(username)

    #username.replace(' ','-')
    print(res)
    base = 'https://www.quora.com/profile/'
    url = base+res
    req = requests.get(url)
    print('\n\n\n '+url+ '\n\n\n')
    soup = Soup(req.content, "html.parser")

    name = soup.find_all('meta')[3]['content']
    #print(name)
    returnee = [name,url]
    
    return returnee

