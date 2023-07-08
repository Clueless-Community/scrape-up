from bs4 import BeautifulSoup
import requests


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
    """

    def __init__(self):
        pass

    def __scrape_page(self):
        try:
            source = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
            source.raise_for_status()
            soup = BeautifulSoup(source.text, "html.parser")
            movies = soup.find("tbody", class_="lister-list").find_all("tr")
            return movies
        except:
            return None

    def top_rated(self):
        """
        Class - `IMDB`\n
        Example -\n
        ```python
        top_250 = IMDB()
        print(top_250.top_rated())
        ```
        Return\n
        ```python
        return
        {
            "data": movie_data,
            "message": f"Top rated movie listed on IMDB has been fetched",
        }
        ```
        """
        try:
            movies = self.__scrape_page()
            if movies is not None:
                movie_data = []
                for movie in movies:
                    movie_name = movie.find("td", class_="titleColumn").a.text
                    rank = (
                        movie.find("td", class_="titleColumn")
                        .get_text(strip=True)
                        .split(".")[0]
                    )
                    year = movie.find("td", class_="titleColumn").span.text.strip("()")
                    rating = movie.find(
                        "td", class_="ratingColumn imdbRating"
                    ).strong.text

                    movie_data.append([rank, movie_name, year, rating])

                return {
                    "data": movie_data,
                    "message": f"Top rated movie listed on IMDB has been fetched",
                }
            else:
                return {
                    "data": None,
                    "message": f"Unable to fetch top rate movie",
                }

        except requests.exceptions.RequestException as e:
            return {
                "data": None,
                "message": f"Unable to fetch top rate movie",
            }

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

            resp = requests.get(formatted_url, headers={"User-Agent": "Mozilla/5.0"})
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

