from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class FunHolidays:
    """
    Create an instance of `FunHolidays` class.
    ```python
    funholidays = FunHolidays()
    ```
    | Methods   | Details                                                    |
    | ----------|------------------------------------------------------------|
    | `.dates()`| Returns a list of fun holidays on each date of each month  |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.timeanddate.com/holidays/fun/"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def dates(self):
        """
        Create an instance of `FunHolidays` class.
        ```python
        funholidays = FunHolidays()
        funholidays.dates()
        ```

        Return\n
        ```js
        {
            "January": {
                            "1": ["Polar Bear Plunge Day"],
                            "2": ["Buffet Day", "Run It up the Flagpole and See If Anyone Salutes It Day",
                                "Science Fiction Day"],
                            "3": ["Fruitcake Toss Day", "Festival of Sleep Day"],
                            "4": ["Trivia Day"],
                            "5": ["Bird Day"],
                            "6": ["Bean Day"],
                            "7": ["Old Rock Day"],
                            "8": ["Earths Rotation Day"],
                            "9": ["Static Electricity Day", "Word Nerd Day", "Clean Off Your Desk Day"]
                            ...
                        }
            ...
        }
        ```
        """
        try:
            x = self.page_soup.find("table", {"class": "zebra fw tb-hover"})
            L = []
            lis = {}

            months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]

            for y in x.find_all("tr")[2:]:
                z = y.get_text()
                if len(z) > 10:
                    date = "".join(w for w in z if w.isnumeric())
                    event = "".join(
                        w for w in z if (w.isupper() or w.islower() or w.isspace())
                    ).strip()
                    if date in lis:
                        lis[date] = lis[date] + [event]
                    else:
                        lis[date] = [event]
                else:
                    L.append(lis)
                    lis = {}

            return dict(zip(months, L[1:]))

        except:
            return None


funholidays = FunHolidays()
print(funholidays.dates())
