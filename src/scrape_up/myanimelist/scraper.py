import re
import requests
from bs4 import BeautifulSoup


class AnimeNotFound(Exception):
    """
    Raised when anime is not found, which happens when the ID is invalid or
    the number of results from search page are zero.
    """


def _sanitize_int(s: str) -> int:
    """
    Removes commas from strings.
    """
    return int(re.sub(r"[,#\"\']", "", s))


class Anime:
    """
    Retrives information about an anime from MyAnimeList (myanimelist.net).

    ```python
    from scrape_up.myanimelist import Anime
    a = Anime("demon slayer")
    # or construct the class by ID
    b = Anime.from_id(38000)
    ```
    | Methods                       | Details                                                        |
    | ----------------------------- | -------------------------------------------------------------- |
    | `.url`                | Returns the MyAnimelist URL of the anime.                   |
    | `.title`                | Returns the title of the anime.                   |
    | `.title_english`                | Returns the English title of the anime.                   |
    | `.title_jp`                | Returns the Japanese title of the anime.                   |
    | `.synopsis`                | Returns the synopsis/brief introduction of the anime.                   |
    | `.score`                | Returns the score of the anime.                   |
    | `.members`                | Returns the number of members of the anime.                   |
    | `.popularity`                | Returns the popularity index of the anime.                   |
    | `.rank`                | Returns the rank of the anime.                   |
    | `.episodes`                | Returns the number of episodes of the anime.                   |
    | `.aired` | Returns the duration the anime was being aired in string format, like `Apr 6, 2019 to Sep 28, 2019`. |
    | `.broadcast`          | Returns the day and time when new episode of the anime used to be broadcasted, like `Saturdays at 23:30 (JST)`.                    |
    | `.premiered`          | Returns the cour and year anime used to be premiered in, like `Spring 2019`.                    |
    | `.genres`          | Returns the list of genres of the anime.                    |
    | `.themes`          | Returns the list of themes of the anime.                    |
    | `.poster_url`          | Returns the the URL to the poster image of the anime.                    |
    """

    SEARCH_ENDPOINT = "https://myanimelist.net/anime.php"
    ANIME_ID_ENDPOINT = "https://myanimelist.net/anime"

    def __init__(self, name: str):
        # use the search endpoint with the following query parameters
        try:
            search_resp = requests.get(
                self.SEARCH_ENDPOINT, {"q": name, "cat": "anime"}
            )
            if search_resp.status_code != 200:
                raise AnimeNotFound(f"the anime {name} was not found")

            search_page = BeautifulSoup(search_resp.content, "html.parser")

            first_result = search_page.select_one(
                "#content > div.js-categories-seasonal.js-block-list.list > table tr:nth-child(2)"
            )
            anime_href = first_result.select_one("a.hoverinfo_trigger").attrs["href"]
            self.url = anime_href

            anime_resp = requests.get(anime_href)
            if anime_resp.status_code != 200:
                raise AnimeNotFound(f"the anime {name} was not found")
            self._page = BeautifulSoup(anime_resp.content, "html.parser")

            self._setup_containers()

        except requests.HTTPError:
            raise

    def _setup_containers(self):
        """A helper method which setups spaceit-pads and dark containers."""
        self._dark = self._page.findAll("span", {"class": "dark_text"})
        self.__spaceit_divs = self._page.findAll("div", {"class": "spaceit_pad"})
        self.episodes = self._divCh("Episodes:")
        self.premiered = self._divCh("Premiered:")
        self.aired = self._divCh("Aired:")
        self.broadcast = self._divCh("Broadcast:")

    def _divCh(self, txt: str):
        for container in self.__spaceit_divs:
            if txt in container.text:
                div_text = container.text.split(txt)[1].split()
                return " ".join(div_text)

    @classmethod
    def from_id(cls, id: int):
        """
        Constructs the Anime class using the anime ID.
        ```python
        anime = myanimelist.Anime.from_id(38000)
        ```
        """
        obj = cls.__new__(cls)
        resp = requests.get(f"{cls.ANIME_ID_ENDPOINT}/{id}")
        if resp.status_code != 200:
            raise AnimeNotFound(f"the anime with {id=} was not found")
        obj._page = BeautifulSoup(resp.content, "html.parser")
        obj._setup_containers()
        return obj

    @property
    def title(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        title = anime.title
        ```
        """
        return self._page.select_one(".title-name > strong").text

    @property
    def title_english(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        titlee = anime.title_english
        ```
        """
        return self._page.select_one(".title-english").text

    @property
    def title_jp(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        titlej = anime.title_jp
        ```
        """
        return self._divCh("Japanese:")

    @property
    def score(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        score = anime.score
        ```
        """
        return float(self._page.select_one(".score-label").text)

    @property
    def rank(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        rank = anime.rank
        ```
        """
        return _sanitize_int(self._page.select_one(".ranked strong").text)

    @property
    def members(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        members = anime.members
        ```
        """
        return _sanitize_int(self._page.select_one(".members strong").text)

    @property
    def popularity(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        pop = anime.popularity
        ```
        """
        return _sanitize_int(self._page.select_one(".popularity strong").text)

    @property
    def synopsis(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        synopsis = animesynopsis.
        ```
        """
        return self._page.select_one("p[itemprop='description']").text

    @property
    def poster_url(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        poster_url = anime.poster_url
        ```
        """
        return self._page.select_one("img[itemprop='image']")["data-src"]

    @property
    def genres(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        genres = anime.genres
        ```
        """
        genres = []
        for container in self._dark:
            if "Genres" in container.text or "Genre" in container.text:
                parent = container.parent
                links = parent.findChildren("a")

                for sub in links:
                    genres.append(sub.text)

        return genres

    @property
    def themes(self):
        """
        Class - `Anime`
        ```python
        anime = myanimelist.Anime("demon slayer")
        themes= anime.themes
        ```
        """
        themes_ = []
        for container in self._dark:
            if "Themes" in container.text or "Theme" in container.text:
                parent = container.parent
                links = parent.findChildren("a")

                for sub in links:
                    themes_.append(sub.text)

        return themes_
