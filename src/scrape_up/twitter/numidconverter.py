from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import json

def unametoid(username):
    url = 'https://twitter.com/{}'.format(username)
    print(url)
    # service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    user_id = soup.find('script', {'data-testid': 'UserProfileSchema-test'})
    # print(user_id)
    data = json.loads(user_id.string)
    # print(data['author']['identifier'])
    return data['author']['identifier']

def idtouname(numid):
    url2='https://twitter.com/i/user/{}'.format(numid)
    # service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    user_id = soup.find('script', {'data-testid': 'UserProfileSchema-test'})
    # print(user_id.string)
    data = json.loads(user_id.string)
    # print(data['author']['additionalName'])
    return data['author']['additionalName']

print(unametoid("elonmusk"))
print(idtouname("44196397"))