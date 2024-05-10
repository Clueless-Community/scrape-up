from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class Celeb:
    """
    Create an instance of `Celeb` class.
    ```python
    celeb = Celeb()
    ```
    | Methods            | Details                                            |
    | -------------------|----------------------------------------------------|
    | `.top_celebs()`    | Returns the name, roles, famous movie of the celeb |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.imdb.com/chart/starmeter/?ref_=chtbo_ql_8"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def top_celebs(self):
        """
        Create an instance of `Celeb` class.\n
        ```python
        celeb = Celeb()
        celeb.top_celebs()
        ```
        Return\n
        ```js
        [
            {
                'Name': 'Paul Reubens',
                'Roles': ['Actor', 'Writer', 'Director'],
                'Famous Movie': "Pee-wee's Playhouse"
            },
            ...
        ]
        ```
        """
        try:
            x = self.page_soup.find_all("div", {"class": "sc-89c756a0-4 euZqVD"})
            celeb_list = []
            for y in x:
                dic = {}
                dic["Name"] = y.find("h3", {"class": "ipc-title__text"}).get_text()

                lis = []
                for z in y.find_all(
                    "li", {"class": "ipc-inline-list__item sc-89c756a0-6 jpNWoI"}
                ):
                    lis.append(z.get_text())

                dic["Roles"] = lis

                dic["Famous Movie"] = y.find(
                    "span", {"class": "sc-1c8554ae-1 cKAFFg"}
                ).get_text()

                celeb_list.append(dic)

            return celeb_list

        except:
            return None
