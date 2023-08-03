from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class Timezones:
    """
    Create an instance of `Timezones` class.\n
    ```python
    timezones = Timezones()
    ```
    | Methods            | Details                                          |
    | -------------------|--------------------------------------------------|
    | `.city_timezones()`| Returns the timezones of cites around the world  |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.timeanddate.com/worldclock/full.html"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def city_timezones(self):
        """
        Create an instance of `Timezones` class
        ```python
        timezones = Timezones()
        timezones.city_timezones()
        ```

        Return\n
        ```js
        {
            "Abidjan": "16.31",
            "Gitega": "18.31",
            "Oral": "21.31",
            "Abu Dhabi": "20.31",
            "Grise Fiord *": "12.31",
            "Oslo *": "18.31",
            "Abuja": "17.31"
        }
        ```
        """
        try:
            x = self.page_soup.find_all("td")
            p = False

            timezones_dict = {}
            for y in x[:-1]:
                if p == False:
                    key = y.get_text()
                else:
                    timezones_dict[key] = (y.get_text())[5:]
                p = not (p)

            return timezones_dict

        except:
            return None
