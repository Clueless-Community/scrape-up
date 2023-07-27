import requests
import numpy as np
from pandas import DataFrame
from pathlib import Path

class Billionaires:
  """
        Create an instance of `Billionaires` class.

    ```python
    billionaires = Billionaires()
    ```

    | Methods               | Details                                                                                      |
    | --------------------- | -------------------------------------------------------------------------------------------- |
    | `.storeascsv()`       | Stores as local CSV files of all categories in user's local storage.                         |
    | `.realtime()`         | It takes a user query parameter as an argument and returns all relevant terms related to it. |
    | `.americanrealtime()` | Returns the JSON list of American realtime billionaires.                                     |
    | `.worldrichest()`     | Returns the JSON list of the world's richest people.                                         |
    | `.hedgefund()`        | Returns the JSON list of world's biggest hedge fund capitalists.                             |
    | `.powerfulwomen()`    | Returns as JSON the list of Forbes most powerful women in the world.                         |
    | `.powerfulpeople()`   | Returns as JSON a list of Forbes Porweful people.                                            |
    | `.bylocation()`       | Returns as JSON the billionaires of a particular nation.                                     |


  """

  def __init__(self):
    self.lists = [
      
      { 'type': 'person', 'year': 2022, 'uri': 'billionaires' },                # World richest
      { 'type': 'person', 'year': 2022, 'uri': 'forbes-400' },                  # American richest 400
      { 'type': 'person', 'year': 2022, 'uri': 'hong-kong-billionaires' },      # Hong Kong richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'australia-billionaires' },      # Australia richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'china-billionaires' },          # China richest 400
      { 'type': 'person', 'year': 2022, 'uri': 'taiwan-billionaires' },         # Taiwan richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'india-billionaires' },          # India richest 100
      { 'type': 'person', 'year': 2022, 'uri': 'japan-billionaires' },          # Japan richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'africa-billionaires' },         # Africa richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'korea-billionaires' },          # Korea richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'malaysia-billionaires' },       # Malaysia richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'philippines-billionaires' },    # Philippines richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'singapore-billionaires' },      # Singapore richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'indonesia-billionaires' },      # Indonesia richest 50
      { 'type': 'person', 'year': 2022, 'uri': 'thailand-billionaires' },       # Thailand richest 50
      { 'type': 'person', 'year': 2017, 'uri': 'self-made-women' },             # American richest self-made women
      { 'type': 'person', 'year': 2017, 'uri': 'richest-in-tech' },             # tech richest
      { 'type': 'person', 'year': 2019, 'uri': 'hedge-fund-managers' },         # hedge fund highest-earning
      { 'type': 'person', 'year': 2018, 'uri': 'powerful-people' },             # world powerful
      { 'type': 'person', 'year': 2022, 'uri': 'power-women' },                 # world powerful women
      { 'type': 'person', 'year': 0, 'uri': 'rtb' },                            # real-time world billionaires
      { 'type': 'person', 'year': 0, 'uri': 'rtrl' },                           # real-time American richest 400
    ]
    print(self)


  def storeascsv(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.storeascsv()
            """
    try:

      url = 'http://www.forbes.com/ajax/list/data'
      SOURCES_DIR = Path('./sources')
      for forbes_list in self.lists:
        response = requests.get(url, params=forbes_list)
        if not SOURCES_DIR.exists():
          SOURCES_DIR.mkdir(exist_ok=True, parents=True)
        DataFrame(response.json()).to_csv('sources/forbes-{}.csv'.format(forbes_list['uri']))
    except:
      return None    

  def realtime(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.realtime()
            """
    try:
      url = 'http://www.forbes.com/ajax/list/data'
      response = requests.get(url, params=self.lists[20])
      k = response.json()
      return k
    except:
      return None  

  def americanrealtime(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.americanrealtime()
            """
    try:
      url = 'http://www.forbes.com/ajax/list/data'
      response = requests.get(url, params=self.lists[21])
      k = response.json()
      return k
    except:
      return None  

  def worldrichest(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.worldrichest()
            """
    try:
      url = 'http://www.forbes.com/ajax/list/data'
      response = requests.get(url, params=self.lists[4])
      k = response.json()
      return k
    except:
      return None     

  def hedgefund(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.hedgefund()
            """
    try:
      url = 'http://www.forbes.com/ajax/list/data'
      response = requests.get(url, params=self.lists[17])
      k = response.json()
      return k
    except:
      return None  

  def powerfulwomen(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.powerfulwomen()
            """
    try: 
      url = 'http://www.forbes.com/ajax/list/data'
      response = requests.get(url, params=self.lists[19])
      k = response.json()
      return k
    except:
      return None  

  def powerfulpeople(self):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.powerfulpeople()
            """
    try:
      url = 'http://www.forbes.com/ajax/list/data'
      response = requests.get(url, params=self.lists[18])
      k = response.json()
      return k
    except:
      return None


  def bylocation(self, loc):
    """
            Class - `Billionaires`\n
            Example -\n
            ```python
            item = Billionaires()
            item.bylocation(location)
            """
    k = None
    url = 'http://www.forbes.com/ajax/list/data'
    for i in self.lists:
      if loc in i['uri']:
        k = i
        break
    if i is not None:
      response = requests.get(url, params=k)
      k = response.json()
      return k
    else:
      return None      







