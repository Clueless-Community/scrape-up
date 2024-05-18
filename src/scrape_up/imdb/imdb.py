from bs4 import BeautifulSoup
import requests

from scrape_up.config.request_config import RequestConfig, get


class IMDB:
    """
    Create an instance of the `Movie` class.
    ```python
    scraper = IMDB()
    ```
    | Methods        | Details                                      |
    | -------------- | -------------------------------------------- |
    | `.top_rated()` | Returns the top-rated movies listed on IMDB. |
    | `.scrape_genre_movies(genre)` | Returns the list of movies related to the genre you mentioned. |
    | `.top_rated_shows()` | Returns the top-rated shows listed on IMDB. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config

    def top_rated(self):
        """
        Class: `IMDB`\n
        Retrieves the top-rated movies listed on IMDB.
        Example:
        ```python
        top_movies = IMDB()
        result = top_movies.top_rated()
        ```
        Returns:
        ```js
        [
            {
                "title":"1. The Shawshank Redemption",
                "year":"1994",
                "duration":"2h 22m",
                "rating":"9.3"
            }
            ...
        ]
        ```
        """
        try:
            url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")
            movies_container = soup.find(
                "ul",
                {
                    "class": "ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"
                },
            )
            movies = []

            for items in movies_container.find_all("li"):
                title = items.find("h3").text
                years = items.find(
                    "span", {"class": "sc-c7e5f54-8 hgjcbi cli-title-metadata-item"}
                )
                duration = years.next_sibling.text
                rating = items.find(
                    "span",
                    {
                        "class": "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"
                    },
                ).text

                data = {
                    "title": title,
                    "year": years.text,
                    "duration": duration,
                    "rating": rating,
                }

                movies.append(data)

            return movies
        except requests.exceptions.RequestException as e:
            return None

    def scrape_genre_movies(self, genre):
        """
        Class - `IMDB`\n
        Example -\n
        ```python
        scraper = IMDB()
        genre = "Adventure"
        genre_data = scraper.scrape_genre_movies(genre)

        json_data = json.dumps(genre_data, indent=4)
        print(json_data)
        ```
        Return\n
        ```python
        return
        {
            "data": movie_data,
        }
        ```
        """
        try:
            url = "https://www.imdb.com/search/title/?genres={}&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=N97GEQS6R7J9EV7V770D&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16"
            formatted_url = url.format(genre)
            print(formatted_url)

            resp = get(formatted_url, self.config)
            content = BeautifulSoup(resp.content, "lxml")
            genres = [
                "Adventure",
                "Animation",
                "Biography",
                "Comedy",
                "Crime",
                "Drama",
                "Family",
                "Fantasy",
                "Film-Noir",
                "History",
                "Horror",
                "Music",
                "Musical",
                "Mystery",
                "Romance",
                "Sci-Fi",
                "Sport",
                "Thriller",
                "War",
                "Western",
            ]

            movie_list = []

            for movie in content.select(".lister-item-content"):
                try:
                    title_info = movie.select(".lister-item-header")[0]
                    movie_name = title_info.a.text
                    year = title_info.find(
                        "span", class_="lister-item-year"
                    ).text.strip("()")
                    certificate = movie.select(".certificate")[0].text.strip()
                    time = movie.select(".runtime")[0].text.strip()
                    genre = movie.select(".genre")[0].text.strip()
                    rating = movie.select(".ratings-imdb-rating")[0].strong.text.strip()
                    simple_desc = movie.select(".text-muted")[2].text.strip()
                    votes = (
                        movie.select(".sort-num_votes-visible")[0]
                        .text.strip()
                        .split("|")[0]
                        .replace("Votes:", "")
                        .strip()
                    )

                    data = {
                        "title": movie_name,
                        "year": year,
                        "certificate": certificate,
                        "time": time,
                        "genre": genre,
                        "rating": rating,
                        "simple_desc": simple_desc,
                        "votes": votes,
                    }
                    movie_list.append(data)
                except IndexError:
                    continue

            return movie_list

        except requests.exceptions.RequestException as e:
            return None

    def top_rated_shows(self):
        """
        Class: `IMDB`\n
        Retrieves the top-rated TV shows listed on IMDb.
        Example:
        ```python
        top_shows = IMDB()
        result = top_shows.top_rated_shows()
        ```
        Returns:
        ```js
        [
            {
                "title":"1. Breaking Bad",
                "year":"2008-2013",
                "episode":"62",
                "rating":"9.5"
            }
        ]
        ```
        """
        try:
            url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")
            shows_container = soup.find(
                "ul",
                {
                    "class": "ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"
                },
            )
            shows = []

            for items in shows_container.find_all("li"):
                title = items.find("h3").text
                years = items.find(
                    "span", {"class": "sc-c7e5f54-8 hgjcbi cli-title-metadata-item"}
                )
                eps = years.next_sibling.text.split()[0]
                rating = items.find(
                    "span",
                    {
                        "class": "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"
                    },
                ).text

                data = {
                    "title": title,
                    "year": years.text,
                    "episode": eps,
                    "rating": rating,
                }

                shows.append(data)

            return shows
        except requests.exceptions.RequestException as e:
            return None
