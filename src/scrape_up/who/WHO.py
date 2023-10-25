from bs4 import BeautifulSoup
import requests


class WHO:
    """
    Create an instance of WHO class.\n
    ```python
    who = WHO()
    ```
    | Methods                        | Details                                     |
    | ------------------------------ | ------------------------------------------- |
    | `get_disease_outbreak()` | Get Disease Outbreak News from WHO website. |
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def get_disease_outbreak(self, number):
        """
        Get Disease Outbreak News from WHO website.\n
        Parameters: `number` (int): The number of pages (each page contains 10 items).
        ```python
        who = WHO()
        who.get_disease_outbreak()
        ```
        Returns:
        ```js
        [
            {
                "Title":"Circulating vaccine-derived poliovirus type 2 (cVDPV2) - United Republic of Tanzania",
                "Date":"28 July 2023 ",
                "Link":"https://www.who.int/emergencies/disease-outbreak-news/item/2023-DON480"
            }
            ...
        ]
        ```
        """

        try:
            number = number // 10
            DON = []
            for i in range(1, number + 1):
                url = f"https://www.who.int/emergencies/disease-outbreak-news/{i}"
                html_text = requests.get(url, headers=self.headers).text
                soup = BeautifulSoup(html_text, "lxml")

                container = soup.find("div", {"class": "sf-list-vertical"})

                for items in container.find_all(
                    "a", {"class": "sf-list-vertical__item"}, href=True
                ):
                    title = items.find("span", {"class": "full-title"})
                    date = title.findNext()
                    date = date.text.split("|")[0]
                    link = items["href"]
                    data = {"Title": title.text, "Date": date, "Link": link}
                    DON.append(data)
            return DON
        except:
            return None


who = WHO()
print(who.get_disease_outbreak(number=10))
