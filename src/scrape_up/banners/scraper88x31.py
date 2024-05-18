import bs4

from scrape_up.config.request_config import RequestConfig, get


class Scraper88x31:
    """
    Create an instance of the `Scraper88x31` class.
    ```python
    scraper = Scraper88x31()
    ```
    | Methods            | Details                                                  |
    | ------------------ | -------------------------------------------------------- |
    | `get_all()`        | Returns the list of all available 88x31 banners          |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.urls_to_scrape = [
            "https://cyber.dabamos.de/88x31/index.html",
            "https://cyber.dabamos.de/88x31/index2.html",
            "https://cyber.dabamos.de/88x31/index3.html",
            "https://cyber.dabamos.de/88x31/index4.html",
            "https://cyber.dabamos.de/88x31/index5.html",
        ]
        self.config = config

    def get_all(self):
        """
        Class: Scraper88x31
        Returns the list of all available 88x31 banners
        Example:
        ```python
        banners = Scraper88x31()
        result = banners.get_all()
        ```

        Returns:
        ```json
        ["https://cyber.dabamos.de/88x31/000010.gif", "https://cyber.dabamos.de/88x31/007button.gif", "..."]
        ```
        """
        img_alt = []
        for url in self.urls_to_scrape:
            try:
                response = get(url, self.config)
                response.raise_for_status()
                source = response.content
                soup = bs4.BeautifulSoup(source, "lxml")
                for img_tag in soup.find_all("img"):
                    img_alt.append(
                        "https://cyber.dabamos.de/88x31/" + img_tag.get("alt") + ".gif"
                    )
                return img_alt
            except:
                return None
