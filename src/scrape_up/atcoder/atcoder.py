import json
import requests
from bs4 import BeautifulSoup 

class Atcoder:
    '''
    atc=Atcoder(user="chokudai")
    stc.get_profile()

    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_profile()`  | Returns the user data in json format.                                              |

    '''
    def __init__(self,user):
        self.user=user
    
    def get_profile(self):
        try:
            url = f"https://atcoder.jp/users/{self.user}"
            headers = {"User-Agent": "scrapeup"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table=soup.find_all('table',class_="dl-table")
            user_details={}

            row=table[0].find_all('tr')
            for r in row :
               
                user_details[r.find('th').text.replace(' ','_')]=r.find('td').text.replace('\n',' ').strip()

            row=table[1].find_all('tr')
            for r in row :
               
                user_details["Algorithm_"+r.find('th').text.replace(' ','_')]=r.find('td').text.replace('\n',' ').strip()

            url=f"https://atcoder.jp/users/{self.user}?contestType=heuristic"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table=soup.find_all('table',class_="dl-table")
            row=table[1].find_all('tr')
            for r in row :
                
                user_details["Heuristic_"+r.find('th').text.replace(' ','_')]=r.find('td').text.replace('\n',' ').strip()
            return json.dumps(user_details)
        except:
            return None