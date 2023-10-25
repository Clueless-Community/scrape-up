import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Spotify:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()

    def __scrape_songs_by_keyword(self, keyword):
        """
        Class - `Spotify`\n
        Example -\n
        ```python
        scraper = Spotify()
        songs = scrape_songs_by_keyword("love")
        for song in songs:
            print("Name:", song["name"])
            print("Artist:", song["artist"])

        scraper.close()
        ```
        Return\n
        ```python
        return {all_books with details in json}
        ```
        """
        try:
            self.driver.get("https://open.spotify.com/search/")
            self.driver.implicitly_wait(100)

            search_box = self.driver.find_element(
                By.XPATH, "//input[@data-testid='search-input']"
            )
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)

            songs = []
            for song in self.driver.find_elements(
                By.XPATH,
                "//div[@class='search-results']/section//div[@data-testid='tracklist-row']",
            ):
                songs.append(
                    {
                        "name": song.find_element(
                            By.XPATH,
                            ".//span[@data-testid='tracklist-row__track-name']",
                        ).text,
                        "artist": song.find_element(
                            By.XPATH,
                            ".//span[@data-testid='tracklist-row__artist-name-link']",
                        ).text,
                    }
                )

            return songs

        except Exception as e:
            return None

    def __scrape_homepage(self):
        """
        Class - `Spotify`\n
        Example -\n
        ```python
        scraper = Spotify()
        songs = scrape_homepage()
        for song in songs:
            print("Name:", song["name"])
            print("Artist:", song["artist"])

        scraper.close()
        ```
        Return\n
        ```python
        return {playlists on homepage}
        ```
        """
        try:
            self.driver.get("https://open.spotify.com/")
            self.driver.implicitly_wait(100)

            playlists = []
            for song in self.driver.find_elements(
                By.XPATH, "//div[@data-testid='tracklist-row']"
            ):
                playlists.append(
                    {
                        "name": song.find_element(
                            By.XPATH,
                            ".//span[@data-testid='tracklist-row__track-name']",
                        ).text,
                        "artist": song.find_element(
                            By.XPATH,
                            ".//span[@data-testid='tracklist-row__artist-name-link']",
                        ).text,
                    }
                )

            return playlists

        except Exception as e:
            return None

    def close(self):
        self.driver.quit()
