from bs4 import BeautifulSoup
from urllib.request import urlopen

from scrape_up.config.request_config import RequestConfig, get


class Dictionary:
    """
    Create an instance of the `Dictionary` class.
    ```python
    scraper = Dictionary()
    ```
    | Methods        | Details                                      |
    | -------------- | -------------------------------------------- |
    | `.get_word_of_the_day()` | Returns word of the day from Dictionary.com. |
    | `.word_of_the_day_definition()` | Returns the definition of the word of the day. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()) -> None:
        self.config = config

    def __get_word_of_the_day_url(self):
        try:
            response = get("https://www.dictionary.com/", self.config)
            soup = BeautifulSoup(response.text, "html.parser")

            for anchor in soup("button"):
                url = anchor.get("data-linkurl", "/")

                if "word-of-the-day" in url:
                    return url

        except:
            return None

    def __word_of_the_day_definition(self):
        try:
            response = get(self.__get_word_of_the_day_url(), self.config)
            soup = BeautifulSoup(response.text, "html.parser")

            for para in soup("p"):
                if para.string and para.string[0] not in "EG":
                    return para.string
        except:
            return None

    def get_word_of_the_day(self):
        """
        Returns a string containing the word of the day.

        ```python
        scraper = Dictionary()
        print(scraper.get_word_of_the_day())
        ```

        Sample output:
        >> unfalsifiable
        """
        response = {}
        try:
            response["word"] = (
                self.__get_word_of_the_day_url().split("/")[-2].split("-")[0]
            )
            response["meaning"] = self.__word_of_the_day_definition()
            return response
        except:
            return None
