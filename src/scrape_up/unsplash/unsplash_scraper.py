from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Unsplash:
    """
    Create an instance of `Unsplash` class with search query as argument.

    ```python
    from scrape_up import unsplash
    ```

    | Methods                                   | Details                                    |
    | ----------------------------------------- | ------------------------------------------ |
    | `.get_image_quality()`                    | Return list of available image quality     |
    | `.get_image_links(quality="2000w")`       | Return image links of quality 2000w        |
    | `.get_non_premium_links(quality="2000w")` | Returns non-premium links of quality 2000w |

    """

    BASE_URL = "https://unsplash.com/s/photos/"

    def __init__(self, search_query: str, *, config: RequestConfig = RequestConfig()):
        self.search_query = search_query
        self.non_premium_images = {}
        self.all_images = self.__get_images()
        self.config = config

    def __get_url(self):
        return self.BASE_URL + "-".join(self.search_query.split(" "))

    def __get_images(self):
        url = self.__get_url()
        response = get(url, self.config).text

        soup = BeautifulSoup(response, "html.parser")
        img_data = []
        try:
            img_tags = soup.select("figure div.zmDAx a div.MorZF img")
            img_data = [img.get("srcset") for img in img_tags]
        except:
            pass

        image_links = {}
        for data in img_data:
            data = data.split(",")
            # print(data)
            for d in data:
                d = d.split(" ")
                if len(d) > 2:
                    d = d[1:]

                link, quality = d
                if not image_links.get(quality):
                    image_links[quality] = []
                image_links[quality].append(link)

                if "plus.unsplash" not in link:
                    if not self.non_premium_images.get(quality):
                        self.non_premium_images[quality] = []
                    self.non_premium_images[quality].append(link)

        return image_links

    def get_image_quality(self):
        """
        Class - `Unsplash`
        Example:
        ```
        unsplash = unsplash.Unsplash(search_query="Tech wallpaper")
        quality = unsplash.get_image_quality()
        ```
        Returns: List of quality | None
        """
        try:
            response = list(self.all_images.keys())
            return response
        except:
            return None

    def get_image_links(self, quality):
        """
        Class - `Unsplash`
        Example:
        ```
        unsplash = unsplash.Unsplash(search_query="Tech wallpaper")
        links = unsplash.get_image_links(quality="2000w")
        ```
        Returns: List of image links of quality 2000w | None
        """
        try:
            if not self.all_images.get(quality):
                return None
            response = self.all_images[quality]
            return response
        except:
            return None

    def get_non_premium_links(self, quality):
        """
        Class - `Unsplash`
        Example:
        ```
        unsplash = unsplash.Unsplash(search_query="Tech wallpaper")
        links = unsplash.get_non_premium_links(quality="2000w")
        ```
        Returns: List of non-premium image links of quality 2000w | None
        """
        try:
            if not self.non_premium_images.get(quality):
                return None

            response = self.non_premium_images[quality]
            return response
        except:
            return None
