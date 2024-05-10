from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class DayInHistory:
    """
    Create an instance of `DayInHistory` class.

    ```python
    dayinhistory = DayInHistory()

    ```
    | Methods              | Details                                          |
    | ---------------------|--------------------------------------------------|
    | `.important_events()`| Returns the timezones of cites around the world  |
    | `.holidays()`        | Returns the holidays on the specific day         |
    | `.births()`          | Returns the important birthdays on that day      |
    | `.deaths()`          | Returns the important deaths on that day         |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.timeanddate.com/on-this-day/"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def important_events(self):
        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.important_events()
        ```

        Return\n
        ```js
        [
            {
                'year': '2008',
                'event': 'War Between Russia and Georgia Breaks Out. The conflict began over South
                        Ossetia and Abkhazia, two breakaway regions of Georgia. When the two provinces
                        broke away from  Georgia in the early 1990s and most of the international
                        community did not recognize their independence. Russia on the other hand,
                        backed them and placed peacekeeping forces in the two regions. In 2008,
                        tensions escalated between the two countries after Russia moved a large number
                        of troops in the area. The war ended with Russian victory and with Georgia
                        losing parts of South Ossetia and Abkhazia to Russia.'
            },
            ...
        ]
        ```
        """

        try:
            x = self.page_soup.find("ul", {"class": "list--big"})
            x = x.get_text().split("\n")
            x = x[1:-1]
            history = []

            for i in range(0, len(x), 3):
                dic = {}
                dic["year"] = x[i][:4]
                dic["event"] = x[i][4:].strip() + ". " + x[i + 1].strip()
                history.append(dic)
            return history

        except:
            return None

    def holidays(self):
        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.holidays()
        ```

        Return\n
        ```js
        [
            {
                'country': 'Ireland',
                'holidays': ['August Bank Holiday']
            },
            ...
        ]
        ```
        """

        try:
            x = self.page_soup.find("div", {"class": "sidebar-holidays"})
            x = x.get_text().split("\n")[5:-1]
            x = [[z.strip() for z in y.split("-")] for y in x]

            holidays = {}
            for y in x:
                if y[1] not in holidays:
                    holidays[y[1]] = [y[0]]
                else:
                    holidays[y[1]].append(y[0])

            list_of_hols = []
            for h in holidays:
                dic = {}
                dic["country"] = h
                dic["holidays"] = holidays[h]
                list_of_hols.append(dic)

            return list_of_hols

        except:
            return None

    def births(self):
        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.births()
        ```

        Return\n
        ```js
        [
            {
                'year': '1987',
                'births': 'Sidney Crosby, Canadian ice hockey player'
            },
            ...
        ]
        ```
        """

        try:
            x = self.page_soup.find("div", {"class": "otd-life__block"})

            births_dic = {}

            for y in x.find_all("li"):
                z = y.get_text().strip("\n").split("\n")

                if len(z) == 2:
                    births_dic[z[0][:4]] = z[0][4:].strip() + ", " + z[1]
                else:
                    births_dic[z[0][:4]] = z[0][4:]

            births_list = []
            for b in births_dic:
                dic = {}
                dic["year"] = b
                dic["births"] = births_dic[b]
                births_list.append(dic)

            return births_list

        except:
            return None

    def deaths(self):
        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.deaths()
        ```

        Return\n
        ```js

        [
            {
                'year': '2011',
                'deaths': 'Mark Hatfield, American politician'
            },
            ....
        ]

        ```
        """

        try:
            x = self.page_soup.find_all("div", {"class": "otd-life__block"})
            x = x[1]

            deaths_dic = {}
            for y in x.find_all("li"):
                z = y.get_text().strip("\n").split("\n")
                if len(z) == 2:
                    deaths_dic[z[0][:4]] = z[0][4:].strip() + ", " + z[1]
                else:
                    deaths_dic[z[0][:4]] = z[0][4:]

            deaths_list = []
            for b in deaths_dic:
                dic = {}
                dic["year"] = b
                dic["deaths"] = deaths_dic[b]
                deaths_list.append(dic)

            return deaths_list

        except:
            return None
