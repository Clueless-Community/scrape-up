import json
import requests
from bs4 import BeautifulSoup

ac = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"

target_url = "https://www.walmart.com/ip/AT-T-iPhone-14-128GB-Midnight/1756765288"

headers = {"Referer": "https://www.google.com", "Connection": "Keep-Alive", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate, br",
           "Accept": ac, "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"}

resp = requests.get(target_url)
# print(resp.text)
# if("Robot or human" in resp.text):
#     print(True)
# else:
#     print(False)

soup = BeautifulSoup(resp.text, 'html.parser')
l = []
obj = {}

try:
    obj["price"] = soup.find(
        "span", {"itemprop": "price"}).text.replace("Now ", "")
except:
    obj["price"] = None

try:
    obj["name"] = soup.find("h1", {"itemprop": "name"}).text
except:
    obj["name"] = None

try:
    obj["rating"] = soup.find(
        "span", {"class": "rating-number"}).text.replace("(", "").replace(")", "")
except:
    obj["rating"] = None


nextTag = soup.find("script", {"id": "__NEXT_DATA__"})
jsonData = json.loads(nextTag.text)

Detail = jsonData['props']['pageProps']['initialData']['data']['product']['shortDescription']

try:
    obj["detail"] = Detail
except:
    obj["detail"] = None

l.append(obj)
print(l)
