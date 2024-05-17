from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class RottenTomatoes:
    """
    Create an instance of `RottenTomatoes` class.
    ```python
    scraper = RottenTomatoes()
    ```
    | Method                       | Details                                                             |
    | ---------------------------- | ------------------------------------------------------------------- |
    | `.top_rated()`               | Returns the top-rated movies listed on the Rotten Tomatoes website. |
    | `.movie_details(movie_name)` | Fetches and returns detailed information about a specific movie.    |
    | `.best_shows()`              | Returns the best TV shows listed on the Rotten Tomatoes website.    |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.url = "https://www.rottentomatoes.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def top_rated(self):
        """
        Create an instance of `RottenTomatoes` class.
        ```python
        scraper = RottenTomatoes()
        scraper.top_rated()
        ```
        ```js
        [
            {
                "name":"The Cow Who Sang a Song Into the Future",
                "streaming_date":"Streaming Jul 18, 2023"
            }
            ...
        ]
        ```
        """
        try:
            url = self.url + "top/bestofrt/"
            response = get(url, self.config)
            soup = BeautifulSoup(response.content, "html.parser")

            movie_titles = []
            title_elements = soup.find_all(
                "span",
                class_="p--small",
                attrs={"data-qa": "discovery-media-list-item-title"},
            )
            for title_element in title_elements:
                movie_titles.append(title_element.text.strip())

            # Extract streaming dates
            streaming_dates = []
            streaming_elements = soup.find_all(
                "span",
                class_="smaller",
                attrs={"data-qa": "discovery-media-list-item-start-date"},
            )
            for streaming_element in streaming_elements:
                streaming_dates.append(streaming_element.text.strip())

            response_list = []
            if len(movie_titles) == len(streaming_dates):
                for i in range(len(movie_titles)):
                    response_list.append(
                        dict(
                            zip(
                                ["name", "streaming_date"],
                                [movie_titles[i], streaming_dates[i]],
                            )
                        )
                    )

            return response_list
        except:
            return None

    def movie_details(self, movie_name):
        """
        Create an instance of `RottenTomatoes` class.
        ```python
        scraper = RottenTomatoes()
        scraper.movie_details(movie_name="iron man")
        ```
        Returns\n
        ```js
        {
            "rating":"PG-13(SuggestiveReferences|BriefLanguage)",
            "genre":"Comedy",
            "director":"English",
            "producers":[
                "David Heyman",
                "Margot Robbie",
                "Tom Ackerley",
                "Robbie Brenner"
            ],
            "writers":[
                "Greta Gerwig",
                "Noah Baumbach"
            ],
            "release_date":"Jul 21, 2023\n\\xa0wide",
            "runtime":"1h 54m",
            "distributor":"WarnerBros.Pictures",
            "production_co":"NB/GGPictures,HeydayFilms,LuckyChapEntertainment,Mattel"
        }
        ```
        """
        try:
            movie_name = movie_name.replace(" ", "_")
            url = f"{self.url}m/{movie_name}"
            response = get(url, self.config)
            soup = BeautifulSoup(response.content, "html.parser")
            movie_details = {}
            # Extract the movie details from the <ul> element with id="info"
            ul_element = soup.find("ul", id="info")
            producers = []
            writers = []
            movie_details = ul_element.find_all(
                "span",
                class_="info-item-value",
                attrs={"data-qa": "movie-info-item-value"},
            )
            rating = movie_details[0].text.strip().replace("\n", "").replace(" ", "")
            genre = movie_details[1].text.strip().replace("\n", "").replace(" ", "")
            director = movie_details[2].text.strip()
            producers_name = movie_details[4].find_all("a")
            writers_name = movie_details[5].find_all("a")
            release_date = movie_details[6].text.strip()
            runtime = movie_details[7].text.strip()
            distributor = (
                movie_details[8].text.strip().replace("\n", "").replace(" ", "")
            )
            production_co = (
                movie_details[9].text.strip().replace("\n", "").replace(" ", "")
            )

            for writer in writers_name:
                writer = writer.text.strip()
                writers.append(writer)
            for producer in producers_name:
                producer = producer.text.strip()
                producers.append(producer)

            movie_details = {
                "rating": rating,
                "genre": genre,
                "director": director,
                "producers": producers,
                "writers": writers,
                "release_date": release_date,
                "runtime": runtime,
                "distributor": distributor,
                "production_co": production_co,
            }

            return movie_details
        except:
            return "Movie not found"

    def best_shows(self):
        """
        Returns the best TV shows listed on the Rotten Tomatoes website.
        ```python
        scraper = RottenTomatoes()
        scraper.movie_details(movie_name="iron man")
        ```
        Returns:
        ```js
        [
            {
                "Title":"Secret Invasion",
                "Link":"https://www.rottentomatoes.com//tv/secret_invasion",
                "Latest Episode":"Latest Episode: Jul 26"
            },
            ...
        ]
        ```
        """
        try:
            url = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular"
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")

            movies = []
            container = soup.find("div", {"class": "discovery-tiles__wrap"})
            for items in container.find_all("div", {"class": "js-tile-link"}):
                link = (
                    "https://www.rottentomatoes.com/"
                    + items.find("a", href=True)["href"]
                )
                title = items.find("span", {"class": "p--small"}).text.strip()
                latest = items.find("span", {"class": "smaller"})
                if latest:
                    latest = latest.text.strip()
                else:
                    latest = None
                data = {"Title": title, "Link": link, "Latest Episode": latest}
                movies.append(data)
            return movies
        except:
            return None
