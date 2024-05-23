from bs4 import BeautifulSoup as Soup
from scrape_up.config.request_config import RequestConfig, get


class Letterboxd:
    """
    Class - `Letterboxd`

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.films_watched()`          | Returns the numbers of films watched by the user.                                                    |
    | `.recent_activity(n)`       | Returns a list of length `n` of the latest activity by the user.                                     |
    | `.recent_reviews(n)`        | Returns a list of dictionaries of length `n` with the latest reviews by the user.                    |
    | `.get_watchlist(n)`         | Returns a list of length `n` including movies and series watchlisted by the user.                    |
    | `.get_followers_count()`    | Returns the number of followers of the user.                                                         |
    | `.get_following_count()`    | Returns the number of following of the user.                                                         |

    Note: `n` is an integer value which is optional and can be used to limit the number of results returned by the methods.
    """

    def __init__(self, username, *, config: RequestConfig = RequestConfig()):
        self.config = config
        self.username = username
        self.url = f"https://letterboxd.com/{self.username}/"

    def films_watched(self) -> int:
        """
        Class - `Letterboxd`

        Example:
        ```
        letterboxd_user = Letterboxd(username="arpy8")
        letterboxd_user.films_watched()
        ```

        Returns the numbers of films watched by the user.:
        ```python
        251
        ```
        """
        try:
            req = get(self.url, self.config)

            page_soup = Soup(req.content, "html.parser")
            data = (
                page_soup.find("a", attrs={"href": f"/{self.username}/films/"})
                .find("span")
                .text.replace(",", "")
            )

            return {"data": int(data)}

        except Exception:
            return None

    def recent_activity(self, n=None) -> list:
        """
        Class - `Letterboxd`

        Example:
        ```
        letterboxd_user = Letterboxd(username="arpy8")
        letterboxd_user.recent_activity(n=5)
        ```

        Returns a list of the latest activity by the user of length `n`.:
        ```python
        ['Challengers', 'Dune: Part Two', 'The Hunger Games: The Ballad of Songbirds & Snakes', 'BLUE EYE SAMURAI', 'Jaane Jaan']
        ```
        """
        try:
            req = get(f"{self.url}/films/", self.config)

            page_soup = Soup(req.content, "html.parser")
            data = [
                film.img["alt"]
                for film in page_soup.find(
                    "ul", attrs={"class": "poster-list"}
                ).findAll("li")
            ]

            return {"data": data[:n]}

        except Exception:
            return None

    def recent_reviews(self, n=None) -> list:
        """
        Class - `Letterboxd`

        Example:
        ```
        letterboxd_user = Letterboxd(username="arpy8")
        letterboxd_user.recent_reviews(n=1)
        ```

        Returns a list of dictionaries containing the latest reviews by the user of length `n`.:
        ```python
        [{'title': 'Dune: Part Two 2024', 'rating': '★★★★', 'date': '11 Mar 2024', 'review': 'feyd-rautha and his uncle had a more passionate kiss than the main characters'}]
        ```
        """
        try:
            keys = ["title", "rating", "date", "review"]
            response = get(f"{self.url}/films/reviews/by/added/", self.config)
            soup = Soup(response.content, "html.parser")
            reviews_list = [
                dict(
                    zip(
                        keys,
                        [
                            text.replace("Watched", "").strip()
                            for text in review_item.text.strip().split("  ")
                            if text not in ["", "\n"]
                        ],
                    )
                )
                for review_item in soup.find_all(
                    "li", attrs={"class": ["film-detail", "viewing-poster-container"]}
                )
            ]

            return {"data": reviews_list[:n]}

        except Exception:
            return None

    def get_watchlist(self, n=None) -> list:
        """
        Class - `Letterboxd`

        Example:
        ```
        letterboxd_user = Letterboxd(username="arpy8")
        letterboxd_user.get_watchlist(n=5)
        ```

        Returns a list of watchlisted movies by the user of length `n`.:
        ```python
        ['Good Time', 'Beginners', 'Y Tu Mamá También', 'Dogville', 'The House That Jack Built']
        ```
        """
        try:
            req = get(f"{self.url}/watchlist/", self.config)
            page_soup = Soup(req.content, "html.parser")
            data = [
                [j.get("alt") for j in i.find_all("img")]
                for i in page_soup.find_all("ul", attrs={"class": "poster-list"})
            ][0]

            return {"data": data[:n]}

        except Exception:
            return None

    def get_followers_count(self) -> int:
        """
        Class - `Letterboxd`

        Example:
        ```
        letterboxd_user = Letterboxd(username="arpy8")
        letterboxd_user.get_followers_count()
        ```

        Returns the number of followers of the user.:
        ```python
        25
        ```
        """
        try:
            req = get(self.url, self.config)

            page_soup = Soup(req.content, "html.parser")
            data = (
                page_soup.find_all("a", attrs={"href": f"/{self.username}/followers/"})[
                    0
                ]
                .find("span")
                .text
            )

            return {"data": int(data)}

        except Exception:
            return None

    def get_following_count(self) -> int:
        """
        Class - `Letterboxd`

        Example:
        ```
        letterboxd_user = Letterboxd(username="shubhranshi")
        letterboxd_user.get_following_count()
        ```

        Returns the a number of following of the user.:
        ```python
        60
        ```
        """
        try:
            req = get(self.url, self.config)

            page_soup = Soup(req.content, "html.parser")
            data = (
                page_soup.find_all("a", attrs={"href": f"/{self.username}/following/"})[
                    0
                ]
                .find("span")
                .text
            )

            return {"data": int(data)}

        except Exception:
            return None
