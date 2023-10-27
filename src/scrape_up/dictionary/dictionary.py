from bs4 import BeautifulSoup
from urllib.request import urlopen

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

    def get_word_of_the_day_url(self):
        try:
            with urlopen("https://www.dictionary.com/") as response:
                soup = BeautifulSoup(response, 'html.parser')

                for anchor in soup('button'):
                    url = anchor.get('data-linkurl', '/')

                    if "word-of-the-day" in url:
                        return url

        finally:       
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
        try:
            return self.get_word_of_the_day_url().split("/")[-2].split("-")[0]
        except:
            return None
    
    def word_of_the_day_definition(self):
        """
        Returns a string containing the definition of the word of the day.

        ```python
        scraper = Dictionary()
        print(scraper.word_of_the_day_definition())
        ```

        Sample output:
        >> not able to be proven false, and therefore not scientific.
        """
        try:
            with urlopen(self.get_word_of_the_day_url()) as response:
                soup = BeautifulSoup(response, 'html.parser')

                for para in soup('p'):
                    if para.string and para.string[0] not in "EG":
                        return para.string

        finally:
            return None           






