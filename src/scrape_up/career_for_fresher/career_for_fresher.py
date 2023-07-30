import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd 

url = "https://careerforfreshers.com/"
r = requests.get(url)


con = r.content
soup = BeautifulSoup(con, 'html.parser')

job  = soup.find_all('h2')
job.pop()
name = []
for j in job:
    name.append(j.text)


link = soup.select(selector = "h2 a")
linklist = []
for l in link:
  linklist.append(l.get('href'))

 
jobs_dict= {"Job titles":name,
            "Link":linklist}
jobs_df=pd.DataFrame(jobs_dict)
print(jobs_df)


jobs_df.to_csv('jobs.csv', index=False, encoding='utf-8')
