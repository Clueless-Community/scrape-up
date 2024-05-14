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
        # calling dunder new because we dont want to call the constructor
        obj = cls.__new__(cls)
        resp = requests.get(f"{cls.ANIME_ID_ENDPOINT}/{id}")
        if resp.status_code != 200:
            raise AnimeNotFound(f"the anime with {id=} was not found")
        obj._page = BeautifulSoup(resp.content, "html.parser")
        obj._setup_containers()
        return obj

    @property
    def title(self):
        return self._page.select_one(".title-name > strong").text

    @property
    def title_english(self):
        return self._page.select_one(".title-english").text

    @property
    def title_jp(self):
        return self._divCh("Japanese:")

    @property
    def score(self):
        return float(self._page.select_one(".score-label").text)

    @property
    def rank(self):
        return _sanitize_int(self._page.select_one(".ranked strong").text)

    @property
    def members(self):
        return _sanitize_int(self._page.select_one(".members strong").text)

    @property
    def popularity(self):
        return _sanitize_int(self._page.select_one(".popularity strong").text)

    @property
    def synopsis(self):
        return self._page.select_one("p[itemprop='description']").text

    @property
    def poster_url(self):
        return self._page.select_one("img[itemprop='image']")["data-src"]

    @property
    def genres(self):
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
        themes_ = []
        for container in self._dark:
            if "Themes" in container.text or "Theme" in container.text:
                parent = container.parent
                links = parent.findChildren("a")

                for sub in links:
                    themes_.append(sub.text)

        return themes_


if __name__ == "__main__":
    a = Anime("demon slayer")
    print(a.url)
    print(a.title_english)
    print(a.title)
    print(a.title_jp)
    print(a.score)
    print(a.members)
    print(a.popularity)
    print(a.rank)
    print(a.episodes)
    print(a.aired)
    print(a.broadcast)
    print(a.premiered)
    print(a.synopsis)
    print(a.genres)
    print(a.themes)
    print(a.poster_url)
    b = Anime.from_id(7088)
    print(b.title_english)
