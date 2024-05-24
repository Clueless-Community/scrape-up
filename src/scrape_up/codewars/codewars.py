from bs4 import BeautifulSoup
import json
from scrape_up.config.request_config import RequestConfig, get


class Codewars:
    """
    Create an instance of the class `GeeksforGeeks`
    ```py
    cwars = Codewars(user="agastya463")
    cwars.get_profile()
    ```

    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_profile()`  | Returns the user data in json format.                                              |


    Response:
    ```js
    {
      "Name": "Agastya Kumar Yadav",
      "Clan": "Unknown",
      "Member Since": "May 2024",
      "Last Seen": "May 2024",
      "Profiles": "",
      "Following": "0",
      "Followers": "0",
      "Allies": "0",
      "Rank": "8 kyu",
      "Honor": "3",
      "Total Completed Kata": "1",
      "Total Languages Trained": "1",
      "Highest Trained": "C++ (8 kyu)",
      "Most Recent": "C++",
      "Comments": "0 (0 replies)",
      "Collections": "0",
      "Kumite": "0",
      "Translations": "0 (0 approved)"
    }
    ```
    """

    def __init__(self, user: str, *, config: RequestConfig = RequestConfig()):
        self.user = user
        headers = {"User-Agent": "scrapeup"}
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_profile(self):
        try:
            url = f"https://www.codewars.com/users/{self.user}"
            response = get(url, self.config)
            soup = BeautifulSoup(response.text, "html.parser")
            d = soup.find_all("div", class_="stat")
            data = {}
            for i in d:
                k = i.text.split(":")
                data[k[0]] = k[1]
            return json.dumps(data)
        except Exception:
            return None
