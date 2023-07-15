from html.parser import HTMLParser
import bs4
from bs4 import BeautifulSoup
import requests

"""
        Create an instance of `MediEncyclopedia` class.

    ```python
    ency = MediEncyclopedia()
    ```

    | Methods               | Details                                                             |
    | --------------------- | ------------------------------------------------------------------- |
    | `.scrapebyurl()`      | Returns the medical dictation of associated topic url               |
    | `.byletter()`         | Returns the list of medical relics starting with a particular letter|
    

    """


class MediEncyclopedia:

  def __init__(self):
    print(self)

  def scrapebyurl(self,url):
    """Returns the medical data including references, review dates, content, topic-head and so on"""

    try:
      content = requests.get(url)
      soup = BeautifulSoup(content.content, 'html.parser')
      headline = soup.find('h1',attrs={'class':'with-also'}).text
      article = soup.find('article')
      for script in article(["script", "style"]):
        script.extract()
      text = article.get_text().replace('Browse the Encyclopedia','').replace('Clinical Trials','')
      text = text.replace('To use the sharing features on this page, please enable JavaScript.','')

      return [headline,text]
    except:
      return None  




  def byletter(self, character):
    """Returns the list of medical encyclopedia terms starting with a particular english character"""
    try:
      character = character.upper()
      chk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      if character not in chk:
        return None
      url = 'https://medlineplus.gov/ency/encyclopedia_{}.htm'.format(character)
      content = requests.get(url)
      base = 'https://medlineplus.gov/ency/'
      soup = BeautifulSoup(content.content, 'html.parser')
      vals = []
      heads = soup.find_all('li')
      allheads = heads[42:len(heads)-16]
      for i in allheads:
        t = base+i.find('a')['href']
        h = i.find('a').text
        vals.append([h,t])

      return vals
    except:
      return None  




