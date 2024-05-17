import json
import requests
from bs4 import BeautifulSoup 

class Atcoder:
    '''
    '''
    def __init__(self,user):
        self.user=user
    
    def get_profile(self):
        try:
            url = "https://atcoder.jp/users/chokudai"
            headers = {"User-Agent": "scrapeup"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table=soup.find_all('table',class_="dl-table")
            user_details={}

            row=table[0].find_all('tr')
            for r in row :
                # print(r)
                user_details[r.find('th').text.replace(' ','_')]=r.find('td').text.replace('\n',' ').strip()

            row=table[1].find_all('tr')
            for r in row :
                # print(r)
                user_details["Algorithm_"+r.find('th').text.replace(' ','_')]=r.find('td').text.replace('\n',' ').strip()

            url="https://atcoder.jp/users/chokudai?contestType=heuristic"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table=soup.find_all('table',class_="dl-table");
            row=table[1].find_all('tr')
            for r in row :
                # print(r)
                user_details["Heuristic_"+r.find('th').text.replace(' ','_')]=r.find('td').text.replace('\n',' ').strip()
            return json.dumps(user_data)
        except:
            return None