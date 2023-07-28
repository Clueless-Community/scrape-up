from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class Actor:
    """
    Create an instance of `Actor` class with the name of the actor.
    ```python
    actor = Actor(actor_name)
    ```
    | Methods            | Details                                                 |
    | -------------------| --------------------------------------------------------|
    | `.popular_movies()`| Returns the popular movies in which the actor has acted |
    | `.all_movies()`    | Returns all movies acted in and upcoming movies         |
    | `.awards()`        | Returns the number of awards and nominations            |
    """

    def __init__(self, actor_name):
        self.actor_name = actor_name
        self.__find_url()
        self.__scrape_page()

    def __find_url(self):
        try:
            actor_name = "%20".join(self.actor_name.split())
            base_url = "https://www.imdb.com/find/?q="
            url = base_url + actor_name + "&ref_=nv_sr_sm"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")

            movie_url = page_soup.find("a", {"ipc-metadata-list-summary-item__t"})
            self.url = "https://www.imdb.com" + str(movie_url["href"])

        except:
            return None

    def __scrape_page(self):
        try:
            req = Request(self.url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")
            title = self.page_soup.find("title")
            self.title = title.get_text()

        except:
            return None

    def popular_movies(self):
        """
        Create an instance of Actor class
        ```python
        actor = Actor(actor_name="Tom Holland")
        actor.popular_movies()
        ```
        Return\n
        ```js
        {

            "title": "Tom Holland - IMDb",
            "rating": ["Spider-Man: Homecoming", "Spider-Man: Far from Home", "Captain America: Civil War", "Lo Imposible"]
        }
        ```
        """
        obj_keys = ["title", "popular_movies"]
        try:
            name = self.page_soup.find_all(
                "a", {"class": "ipc-primary-image-list-card__title"}
            )
            lis = []
            for n in name:
                lis.append(n.get_text())
            obj_values = [self.title, lis]
            return dict(zip(obj_keys, obj_values))
        except:
            return None

    def all_movies(self):
        """
        Create an instance of Actor class
        ```python
        actor = Actor(actor_name="Tom Holland")
        actor.popular_movies()
        ```
        Return\n
        ```js
        {
            "title": "Tom Holland - IMDb",
            "all_movies": ["The Crowded Room", "Untitled Spider-Man Sequel", "Untitled Fred Astaire Biopic", "The Crowded Room", "Last Call", "Uncharted", "The Daily Bugle", "Spider-Man: No Way Home", "Fortnite: Chapter 3", "Hyundai Ioniq 5: Spiderman Only Way Home", "Venom: Let There Be Carnage", "Web Slingers: A Spider-Man Adventure", "Cherry", "Chaos Walking", "The Devil All the Time", "Onward: Magic Gems", "Onward", "Dolittle", "The Crowded Room", "The Crowded Room", "Uncharted", "Tweet"]

        }
        ```
        """
        obj_keys = ["title", "all_movies"]

        try:
            all_movies = self.page_soup.find_all(
                "a", {"class": "ipc-metadata-list-summary-item__t"}
            )
            lis = []
            for a in all_movies:
                lis.append(a.get_text())
            obj_values = [self.title, lis]
            return dict(zip(obj_keys, obj_values))
        except:
            return None

    def awards(self):
        """
        Create an instance of Actor class
        ```python
        actor = Actor(actor_name="Tom Holland")
        actor.popular_movies()
        ```
        Return\n
        ```js
        {
            "title": "Tom Holland - IMDb",
            "awards": ["Won 1 BAFTA Award", "25 wins & 35 nominations total"]
        }

        ```
        """
        obj_keys = ["title", "awards"]

        lis = []
        try:
            awards = self.page_soup.find_all(
                "a",
                {
                    "class": "ipc-metadata-list-item__label ipc-metadata-list-item__label--link"
                },
            )
            lis.append(awards[1].get_text())
        except:
            pass

        try:
            awards2 = self.page_soup.find(
                "span", {"class": "ipc-metadata-list-item__list-content-item"}
            )
            lis.append(awards2.get_text())
        except:
            return None

        obj_values = [self.title, lis]
        return dict(zip(obj_keys, obj_values))
