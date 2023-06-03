import requests
from bs4 import BeautifulSoup as bs

headers= {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    } # mimics a browser's request

class Trending:

    def get_trending():
        try:
            r = requests.get("https://medium.com/", headers=headers)
            soup = bs(r.text, 'html.parser')
            elements = soup.select('h2[class^="by j"]')
            for x in elements:
                print(x.text)
        except:
            print("Something went wrong! Try again")

Trending.get_trending()
