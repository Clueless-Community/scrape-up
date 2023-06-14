import re
from selenium import webdriver

chrome_driver = ''       # your chrome driver
driver = webdriver.Chrome(chrome_driver)
driver.get('')           # the website from which you want to scrap emails.

page_source = driver.page_source

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

list_of_emails = []

for re_match in re.finditer(EMAIL_REGEX, page_source):
    list_of_emails.append(re_match.group())

for i, email in enumerate(list_of_emails):
    driver.close()
