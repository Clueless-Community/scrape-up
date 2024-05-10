from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class UTC:
    """
    Create an instance of `UTC` class.\n
    ```python
    utc = UTC()
    ```
    | Methods             | Details                                      |
    | --------------------|----------------------------------------------|
    | `.time_now`         | Returns UTC time now                         |
    | `.get_abbreviations`| Returns abbreviations of each time zone      |
    | `.get_location`      | Returns location of each time zone           |
    | `.get_offset`       | Returns offset of each time zone from UTC    |


    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.timeanddate.com/time/zones/"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def __get_timezones(self):
        x = self.x
        for y in x.find_all("a"):
            y.decompose()

        x = [y.get_text() for y in x.find_all("td")]
        x = ["".join(z for z in y if z not in "\t\n") for y in x]
        x = [y for y in x if y != ""]

        self.t_list = []
        for y in range(0, len(x), 3):
            self.t_list.append([x[y], x[y + 1], x[y + 2]])

    def time_now(self):
        """
        Create an instance of `UTC` class
        ```python
        utc = UTC()
        utc.time_now()
        ```

        Return\n
        ```js
        {
            'utc time now': '08.53:39'
        }
        ```
        """

        try:
            x = self.page_soup.find("div", {"class": "ctm-clock"})
            dic = {}
            dic["utc time now"] = x.get_text()[12:20]
            return dic

        except:
            return None

    def get_abbreviations(self):
        """
        Create an instance of `UTC` class
        ```python
        utc = UTC()
        utc.get_abbreviations()
        ```

        Return\n
        ```js
        [
            {
                'timezone': 'Alfa Time Zone',
                'abbreviation': 'A'
            },
            ...
        ]
        ```
        """
        try:
            self.x = self.page_soup.find("tbody")
            for span in self.x.find_all("span", {"class": "smaller abb-other"}):
                span.decompose()

            self.abbr = []
            for x in self.x.find_all("a"):
                self.abbr.append(x.get_text())

            self.__get_timezones()

            lis = []

            for i in range(len(self.abbr)):
                dic = {}
                dic["timezone"] = self.t_list[i][0]
                dic["abbreviation"] = self.abbr[i]
                lis.append(dic)

            return lis

        except:
            return None

    def get_offset(self):
        """
        Create an instance of `UTC` class
        ```python
        utc = UTC()
        utc.get_offset()
        ```

        Return\n
        ```js
        [
            {
                'timezone': 'Alfa Time Zone',
                'offset': 'UTC +1'
            },
            ...
        ]
        ```
        """

        try:
            self.x = self.page_soup.find("tbody")
            for span in self.x.find_all("span", {"class": "smaller abb-other"}):
                span.decompose()

            self.__get_timezones()

            lis = []

            for i in range(len(self.t_list)):
                dic = {}
                dic["timezone"] = self.t_list[i][0]
                dic["offset"] = self.t_list[i][2]
                lis.append(dic)

            return lis

        except:
            return None

    def get_locations(self):
        """
        Create an instance of `UTC` class
        ```python
        utc = UTC()
        utc.get_locations()
        ```

        Return\n
        ```js
        [
            {
                'timezone': 'Alfa Time Zone',
                'location': 'Military'
            },
            ...
        ]

        ```
        """

        try:
            self.x = self.page_soup.find("tbody")
            for span in self.x.find_all("span", {"class": "smaller abb-other"}):
                span.decompose()

            self.__get_timezones()

            lis = []

            for i in range(len(self.t_list)):
                dic = {}
                dic["timezone"] = self.t_list[i][0]
                dic["location"] = self.t_list[i][1]
                lis.append(dic)

            return lis

        except:
            return None
