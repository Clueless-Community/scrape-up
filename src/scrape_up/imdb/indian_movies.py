from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class IndianMovies:
    """
    Create an instance of `IndianMovies` class.
    ```python
    indianmovies = IndianMovies()
    ```
    | Methods                | Details                                       |
    | -----------------------|-----------------------------------------------|
    | `.top_indian_movies()` | Returns the current list of top Indian movies |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=fea_eds_center-1_india_tr_india250_cta"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def top_movies(self):
        """
        Create an instance of `IndianMovies` class.
        ```python
        indianmovies = IndianMovies()
        movies = indianmovies.top_movies()
        ```

        Return\n
        ```js
        [
            'Ramayana: The Legend of Prince Rama',
            'Rocketry: The Nambi Effect',
            'Nayakan',
            'Gol Maal',
            'Anbe Sivam',
            ...
        ]
        ```
        """
        try:
            x = self.page_soup.find_all("span", {"data-testid": "rank-list-item-title"})

            lis = []
            for i in range(len(x)):
                lis.append(x[i].get_text()[len(str(i)) :])

            return lis

        except:
            return None
