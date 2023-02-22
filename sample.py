from bs4 import BeautifulSoup
import requests
page = requests.get('https://github.com/PalaVenkiReddy?tab=followers')
page = BeautifulSoup(page.text, 'html.parser')
followers_body = page.find('turbo-frame', id = 'user-profile-frame')
followers = []
for user in followers_body.find_all('a', class_='d-inline-block'):
    followers.append((user['href'])[1:])

followers = set(followers)
print(followers)