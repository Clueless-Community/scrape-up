from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class Movie:
    """
    Create an instance of `Movie` class.
    ```python
    movie = Movie(movie_name)
    ```
    | Methods          | Details                                                 |
    | ---------------- | ------------------------------------------------------- |
    | `.rating()`      | Returns the IMDB rating of the movie                    |
    | `.description()` | Returns the description, cast and director of the movie |
    | `.more_movies()` | Returns similar movies recommended by IMDB              |
    | `.box_office()`  | Returns budget, gross worldwide collections of the movie|

    """

    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.__find_url()
        self.__scrape_page()

    def __find_url(self):
        try:
            movie_search = "+".join(self.movie_name.split())

            base_url = "https://www.imdb.com/find/?q="
            url = base_url + movie_search + "&s=all"

            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")

            movie_url = page_soup.find("a", {"ipc-metadata-list-summary-item__t"})
            self.url = "https://www.imdb.com" + str(movie_url["href"])
        except:
            return "No movie found"

    def __scrape_page(self):
        try:
            req = Request(self.url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")
            title = self.page_soup.find("title")
            self.title = title.get_text()
        except:
            return None

    def rating(self):
        """
        Create an instance of Movie class
        ```python
        movie = Movie(movie_name)
        movie.rating()
        ```
        Return\n
        ```js
        {
            "title":"Avengers: Endgame (2019) - IMDb",
            "rating":"8.4"
        }
        ```
        """
        obj_keys = ["title", "rating"]
        try:
            info = self.page_soup.find("span", {"class": "sc-bde20123-1 iZlgcd"})
            obj_values = [self.title, info.get_text()]
            return dict(zip(obj_keys, obj_values))
        except:
            return None

    def description(self):
        """
        Create an instance of Movie class
        ```python
        movie = Movie(movie_name)
        movie.rating()
        ```
        Return\n
        ```js
        {
            "title":"Avengers: Endgame (2019) - IMDb",
            "description":"Avengers: Endgame: Directed by Anthony Russo, Joe Russo. With Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth....."
        }
        ```
        """
        obj_keys = ["title", "description"]
        try:
            des = self.page_soup.find("meta", {"name": "description"})
            obj_values = [self.title, des["content"]]
            return dict(zip(obj_keys, obj_values))
        except:
            return None

    def such_movies(self):
        """
        Create an instance of Movie class
        ```python
        movie = Movie(movie_name)
        movie.such_movies()
        ```
        Return\n
        ```js
        {
            "title": "Avengers: Endgame (2019) - IMDb",
            "more_like_this": ["Avengers: Infinity War", "Spider-Man: No Way Home", "The Avengers", "Avengers: Age of Ultron", "Joker", "Thor: Ragnarok", "Captain America: Civil War", "The Dark Knight Rises", "Doctor Strange", "The Dark Knight", "Spider-Man: Far from Home", "Guardians of the Galaxy"]
        }
        ```
        """

        obj_keys = ["title", "more_like_this"]
        try:
            more = self.page_soup.find_all("span", {"data-testid": "title"})
            lst = [m.get_text() for m in more]
            obj_values = [self.title, lst]
            return dict(zip(obj_keys, obj_values))
        except:
            return None

    def box_office(self):
        """
        Create an instance of Movie class
        ```python
        movie = Movie(movie_name="Avengers")
        movie.box_office()
        ```
        Return\n
        ```js
        {
            "title": "Avengers: Endgame (2019) - IMDb",
            "box_office": {"Budget": "$356,000,000 (estimated)", "Gross worldwide": "$2,799,439,100"}
        }
        ```
        """

        obj_keys = ["title", "box_office"]
        try:
            x = self.page_soup.find(
                "ul",
                {
                    "class": "ipc-metadata-list ipc-metadata-list--dividers-none ipc-metadata-list--compact sc-6d4f3f8c-0 VdkJY ipc-metadata-list--base"
                },
            )
            results = {}

            for y in x:
                text = y.get_text()
                if "Budget" in text:
                    results["Budget"] = text[6:]
                elif "Gross worldwide" in text:
                    results["Gross worldwide"] = text[15:]
            obj_values = [self.title, results]
            return dict(zip(obj_keys, obj_values))
        except:
            return None
