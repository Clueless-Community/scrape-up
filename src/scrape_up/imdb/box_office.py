from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class BoxOffice:
    """
    Create an instance of `BoxOffice` class.
    ```python
    boxoffice = BoxOffice()
    ```
    | Methods            | Details                                                                       |
    | -------------------|-------------------------------------------------------------------------------|
    | `.top_movies()`    | Returns the top box office movies, weekend and total gross and weeks released |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def top_movies(self):
        """
        Create an instance of `BoxOffice` class

        ```python
        boxoffice = BoxOffice()
        boxoffice.top_movies()
        ```

        Return\n
        ```js
        [
            {
                "Movie Name": "Barbie",
                "Weekend Gross": "$53M",
                "Total Gross": "$459M",
                "Weeks released": "3"
            },
            ...
        ]

        ```
        """
        try:
            x = self.page_soup.find_all("h3", {"class": "ipc-title__text"})
            x = x[1:11]
            movie_names = []

            for y in x:
                movie_names.append(" ".join(y.get_text().split()[1:]))

            x = self.page_soup.find_all("li", {"class": "sc-ee64acb1-1 lkUVhM"})
            x = [y.get_text() for y in x]

            lis = []

            for y in range(0, len(x), 3):
                dic = {}
                dic["Movie Name"] = movie_names[y // 3]
                dic["Weekend Gross"] = x[y].split()[2]
                dic["Total Gross"] = x[y + 1].split()[2]
                dic["Weeks released"] = x[y + 2].split()[2]
                lis.append(dic)

            return lis

        except:
            return None
