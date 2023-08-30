import requests
from bs4 import BeautifulSoup as bs
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
headers = {
    "User-Agent": USER_AGENT
}  # mimics a browser's request


class Trending:
    def get_trending():
        """
        Class - `Trending`
        Example
        ```python
        trending = Trending.get_trending()
        for trend in trending:
            print(trend) #For better readability/clarity
        ```
        Returns a list of trending titles

        """
        try:
            titles = []
            r = requests.get("https://medium.com/", headers=headers)
            soup = bs(r.text, "html.parser")
            elements = soup.select('h2[class^="by j"]')
            for x in elements:
                titles.append(x.text)
            return titles

        except:
            return {"data": None, "message": "Something went wrong! Try again!"}
