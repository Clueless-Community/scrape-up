'''
Web Scraper Module for website https://bugmenot.com

Author: github.com/hashfx

This module provides a class: Bugmenot, that allows you to scrape account data from https://bugmenot.com for a given website
'''

# import required libraries
import requests
from bs4 import BeautifulSoup
import json

class Bugmenot:
    """
    Methods:
    --------

    | Method                 | Description                                                                                |
    | :--------------------- | :----------------------------------------------------------------------------------------- |
    | `__init__(self, website: str)` | Initializes the Bugmenot object with the specified website to scrape.                        |
    | `bugmenot(self) -> Union[List[Dict[str, str]], None]`     | Scrapes account data from Bugmenot.com for the given website and returns a list of dictionaries with account details. Returns `None` if no accounts are found.|



    Example:
    
    ```python
    from bugmenot import Bugmenot
    import json
 
    website = 'canva.com'
    scraper = Bugmenot(website)  # object
    accounts_json = scraper.Bugmenot()

    if accounts_json:
        # Convert the list of dictionaries to JSON format
        json_output = json.dumps(accounts_json, indent=4)
        print(json_output)
    ```

    """

    def __init__(self, website):
        self.website = website
        self.url = f'https://bugmenot.com/view/{website}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def Bugmenot(self):
        # Send a GET request to the website with headers
        response = requests.get(self.url, headers=self.headers)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

        # Find all the article elements with class 'account' that contain the usernames and passwords
        account_articles = soup.find_all('article', class_='account')

        # Check if any accounts were found
        if not account_articles:
            print("No accounts found on the page.")
            return None

        accounts_data = []

        # Loop through the article elements and extract the usernames and passwords
        for article in account_articles:
            username = article.find('kbd').text.strip()
            password = article.find_all('kbd')[1].text.strip()
            success_rate = article.find('li', class_='success_rate').text.strip()
            age = article.find_all('li')[-1].text.strip()

            account_data = {
                'Username': username,
                'Password': password,
                'Success Rate': success_rate,
                'Age': age
            }

            accounts_data.append(account_data)

        return accounts_data

