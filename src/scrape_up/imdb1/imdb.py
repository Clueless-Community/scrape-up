from bs4 import BeautifulSoup
import requests
import openpyxl


class IMDB:
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
