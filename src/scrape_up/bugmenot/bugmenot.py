from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Bugmenot:
    """
    Create an instance of the class `Bugmenot`

    ```python
    website = Bugmenot()
    ```

    | Method                 | Description                                                                                |
    | :--------------------- | :----------------------------------------------------------------------------------------- |
    | `generate_credentials()` | Scrapes account data from Bugmenot.com for the given website and returns a list of dictionaries with account details. Returns `None` if no accounts are found.|

    """

    def __init__(self, website: str, *, config: RequestConfig = RequestConfig()):
        self.website = website
        self.url = f"https://bugmenot.com/view/{website}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def generate_credentials(self):
        """
        Create an instance of the class `Bugmenot`\n

        ```python
        website = 'canva.com'
        scraper = Bugmenot(website)
        ```
        ```js
        [
            {
                "Username":"Premium accounts here:",
                "Password":"https://cuty.io/NDFkAmiS3q0",
                "Success Rate":"99% success rate",
                "Age":"6 months old"
            }
            ...
        ]
        ```
        """
        # Send a GET request to the website with headers
        response = get(self.url, self.config)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

        # Find all the article elements with class 'account' that contain the usernames and passwords
        account_articles = soup.find_all("article", class_="account")

        # Check if any accounts were found
        if not account_articles:
            print("No accounts found on the page.")
            return None

        accounts_data = []

        # Loop through the article elements and extract the usernames and passwords
        for article in account_articles:
            username = article.find("kbd").text.strip()
            password = article.find_all("kbd")[1].text.strip()
            success_rate = article.find("li", class_="success_rate").text.strip()
            age = article.find_all("li")[-1].text.strip()

            account_data = {
                "Username": username,
                "Password": password,
                "Success Rate": success_rate,
                "Age": age,
            }

            accounts_data.append(account_data)

        return accounts_data


website = "canva.com"
scraper = Bugmenot(website)
print(scraper.generate_credentials())
