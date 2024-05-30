import unicodedata
from bs4 import BeautifulSoup as Soup
from scrape_up.config.request_config import RequestConfig, get


class Lastfm:
    """
    Class - `Lastfm`

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.user_stats()`             | Returns the numbers of scrobbles, artists and loved tracks.                                          |
    | `.recent_tracks()`          | Returns a dictionary containing the latest tracks scrobbled by the user.                             |
    | `.top_tracks()`             | Returns a dictionary containing the top tracks of the user.                                          |
    | `.top_albums()`             | Returns a dictionary containing the top albums of the user.                                          |
    | `.top_artists()`            | Returns a dictionary containing the top artists of the user.                                         |
    | `.get_following()`          | Returns the total number of users followed by the user.                                              |
    | `.get_followers()`          | Returns the total number of followers of the user.                                                   |

    Note: usernames are case sensitive.
    """

    def __init__(self, username, *, config: RequestConfig = RequestConfig()):
        self.config = config
        self.username = username
        self.url = f"https://www.last.fm/user/{self.username}"

    def user_stats(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="arpy8")
        lastfm_user.user_stats()
        ```

        Returns the total number of scrobbles, artists and loved tracks:
        ```python
        {'data': {'scrobbles': 4207, 'artists': 289, 'loved_tracks': 9}, 'status': 'success'}
        ```
        """
        try:
            req = get(self.url, self.config)
            page_soup = Soup(req.content, "html.parser")

            scrobbles = page_soup.find_all(
                "a", attrs={"href": f"/user/{self.username}/library"}
            )[1].text.replace(",", "")
            artists = page_soup.find_all(
                "a", attrs={"href": f"/user/{self.username}/library/artists"}
            )[0].text.replace(",", "")
            try:
                loved_tracks = page_soup.find_all(
                    "a", attrs={"href": f"/user/{self.username}/loved"}
                )[1].text
            except IndexError:
                loved_tracks = 0

            return {
                "data": {
                    "scrobbles": int(scrobbles),
                    "artists": int(artists),
                    "loved_tracks": loved_tracks,
                },
                "status": "success",
            }

        except Exception as e:
            return e

    def recent_tracks(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="arpy8")
        lastfm_user.recent_tracks()
        ```

        Returns a dictionary containing the latest tracks scrobbled by the user.:
        ```python
        {
        "data": [
            {
            "song": "killstreaks (with Don Toliver & PinkPantheress)",
            "artist": "Baby Keem",
            "time": "Scrobbling now"
            },
            {
            "song": "True romance",
            "artist": "PinkPantheress",
            "time": "4 minutes ago"
        ],
        "status": "success"
        }
        ```
        """
        try:
            req = get(f"{self.url}", self.config)
            page_soup = Soup(req.content, "html.parser")

            song_names = [
                i.text.strip("\n")
                for i in page_soup.find_all("td", attrs={"class": "chartlist-name"})
            ]
            artist_names = [
                i.text.strip("\n")
                for i in page_soup.find_all("td", attrs={"class": "chartlist-artist"})
            ]
            time_stamps = [
                unicodedata.normalize("NFKD", i.get_text(strip=True))
                for i in page_soup.find_all(
                    "td", attrs={"class": "chartlist-timestamp"}
                )
            ]

            min_len = min(len(song_names), len(time_stamps), len(artist_names))
            return {
                "data": [
                    {
                        "song": song_names[i],
                        "artist": artist_names[i],
                        "time": time_stamps[i],
                    }
                    for i in range(min_len)
                ],
                "status": "success",
            }

        except Exception as e:
            return e

    def top_artists(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="lil_horrer")
        lastfm_user.top_artists()
        ```

        Returns a dictionary containing the top artists of the user.:
        ```python
        {
        "data": [
            {
            "artist": "Mach-Hommy",
            "plays": "33 plays"
            },
            {
            "artist": "王若琳",
            "plays": "24 plays"
            },
            {
            "artist": "Ocean media",
            "plays": "23 plays"
            }
        ],
        "status": "success"
        }
        ```
        """
        try:
            req = get(f"{self.url}", self.config)
            page_soup = Soup(req.content, "html.parser")
            data = page_soup.find("section", attrs={"id": "top-artists"}).text.split(
                "All time"
            )[1]
            data = [
                i.strip()
                for i in data.replace("\n", "").strip().split("  ")
                if i not in [""]
            ][:-1]

            return {
                "data": [
                    {"artist": data[i], "plays": data[i + 1]}
                    for i in range(0, len(data), 2)
                ],
                "status": "success",
            }

        except Exception as e:
            return e

    def top_albums(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="arpy8")
        lastfm_user.top_albums()
        ```

        Returns a dictionary containing the top albums of the user.:
        ```python
        {
        "data": [
            {
            "album": "to hell with it",
            "artist": "PinkPantheress",
            "plays": "29 plays"
            },
            {
            "album": "Heaven knows",
            "artist": "PinkPantheress",
            "plays": "13 plays"
            },
        ],
        "status": "success"
        }
        ```
        """
        try:
            req = get(f"{self.url}", self.config)
            page_soup = Soup(req.content, "html.parser").find(
                "section", attrs={"id": "top-albums"}
            )
            data = [
                j.get_text(strip=True)
                for i in page_soup.find_all(
                    "div", attrs={"class": "grid-items-item-details"}
                )
                for j in i.find_all("a")
            ]

            return {
                "data": [
                    {"album": data[i], "artist": data[i + 1], "plays": data[i + 2]}
                    for i in range(0, len(data), 3)
                ],
                "status": "success",
            }

        except Exception as e:
            return e

    def top_tracks(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="lil_horrer")
        lastfm_user.top_tracks()
        ```

        Returns a dictionary containing the top tracks of the user.:
        ```python
            {"data": [{"song": "Pain", "artist": "PinkPantheress", "plays": 10}, {"song": "Attracted to You", "artist": "PinkPantheress", "plays": 5}, {"song": "Boy's a liar Pt. 2", "artist": "PinkPantheress", "plays": 4}, {"song": "I must apologise", "artist": "PinkPantheress", "plays": 4}], "status": "success"}
        ```
        """

        try:
            req = get(f"{self.url}", self.config)
            page_soup = Soup(req.content, "html.parser").find(
                "section", attrs={"id": "top-tracks"}
            )
            song = [
                i.get_text(strip=True)
                for i in page_soup.find_all("td", attrs={"class": "chartlist-name"})
            ]
            artist = [
                i.get_text(strip=True)
                for i in page_soup.find_all("td", attrs={"class": "chartlist-artist"})
            ]
            plays = [
                int(i.get_text(strip=True).split("scrobbles")[0])
                for i in page_soup.find_all(
                    "span", attrs={"class": "chartlist-count-bar-value"}
                )
            ]

            return {
                "data": [
                    {"song": song[i], "artist": artist[i], "plays": plays[i]}
                    for i in range(min(len(song), len(artist), len(plays)))
                ],
                "status": "success",
            }

        except Exception as e:
            return e

    def get_following(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="arpy8")
        lastfm_user.get_following()
        ```

        Returns the total number of users followed by the user.:
        ```python
        {'data': {'following': 1}, 'status': 'success'}
        ```
        """
        try:
            req = get(f"{self.url}/following", self.config)
            page_soup = Soup(req.content, "html.parser")
            following = (
                page_soup.find("h1", attrs={"class": "content-top-header"})
                .get_text(strip=True)
                .split("\n")[-1]
                .strip()
            )
            following = following.replace(")", "").replace("(", "")

            return {"data": {"following": int(following)}, "status": "success"}

        except Exception as e:
            return e

    def get_followers(self) -> dict:
        """
        Class - `Lastfm`

        Example:
        ```
        lastfm_user = Lastfm(username="arpy8")
        lastfm_user.get_followers()
        ```

        Returns the total number of followers of the user.:
        ```python
        {'data': {'followers': 1}, 'status': 'success'}
        ```
        """
        try:
            req = get(f"{self.url}/followers", self.config)
            page_soup = Soup(req.content, "html.parser")
            followers = (
                page_soup.find("h1", attrs={"class": "content-top-header"})
                .get_text(strip=True)
                .split("\n")[-1]
                .strip()
            )
            followers = followers.replace(")", "").replace("(", "")

            return {"data": {"followers": int(followers)}, "status": "success"}

        except Exception as e:
            return e
