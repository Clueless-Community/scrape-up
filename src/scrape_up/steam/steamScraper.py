import re
import sys
import io
import requests
from bs4 import BeautifulSoup


class SteamStoreScraper:
    """
    A class to scrape game data from the Steam store.

    How to use?
    ```python
    steam = SteamStoreScraper()
    result = steam.ScrapeGames(n0Games=5, tags=["Discounts", "F2P"])
    ```

    | Args            | Details                                            |
    | --------------- | -------------------------------------------------- |
    | `n0Games (int)` | Number of games to scrape for each tag             |
    | `tags (list)`   | List of tags to filter games by                    |

    Note: Use `help(SteamStoreScraper.ScrapeGames)` for more information on tags.
    """

    def __init__(self):
        self.base_url = "https://store.steampowered.com/search/?"
        self.cols = [
            "Name",
            "Date",
            "Platforms",
            "Original Price",
            "Discount %",
            "Discount Price",
            "Reviews",
            "Review Count",
            "Filter",
        ]

    def _get_total_pages(self, url):
        """
        Retrieves the total number of pages for a given URL.

        Args:
            url (str): The URL to scrape.

        Returns:
            int: Total number of pages.
        """
        response = requests.get(url)
        doc = BeautifulSoup(response.content, "html.parser")
        total_pages = int(
            doc.find("div", {"class": "search_pagination_right"}).find_all("a")[-2].text
        )
        return total_pages

    def _extract_game_info(self, game):
        """
        Extracts game information from the BeautifulSoup game element.

        Args:
            game (BeautifulSoup): The BeautifulSoup element containing game information.

        Returns:
            tuple: Game information tuple.
        """
        name = game.find("span", {"class": "title"}).text
        published_date = game.find(
            "div", {"class": "col search_released responsive_secondrow"}
        ).text.strip()
        published_date = published_date if published_date else "N/A"

        div_element = game.find("div", class_="col search_name ellipsis")
        platform_images = div_element.find_all("span", class_="platform_img")
        platforms = [
            img.get("class")[1] if len(img.get("class")) > 1 else None
            for img in platform_images
        ]

        original_price_elem = game.find("div", {"class": "discount_original_price"})
        original_price = (
            original_price_elem.text.strip() if original_price_elem else "N/A"
        )

        discount_pct_elem = game.find("div", {"class": "discount_pct"})
        discount_pct = discount_pct_elem.text.strip() if discount_pct_elem else "N/A"

        discount_price_elem = game.find("div", {"class": "discount_final_price"})
        discount_price = (
            discount_price_elem.text.strip() if discount_price_elem else "N/A"
        )

        review_summary = game.find("span", {"class": "search_review_summary"})
        reviews_html = review_summary["data-tooltip-html"] if review_summary else "N/A"
        pattern = r"(.+)<br>(\d+%)\s+of\s+the\s+([\d,]+)\s+user reviews.*"
        match = re.match(pattern, reviews_html)
        sentiment = match.group(1) if match else "N/A"
        percentage = match.group(2) if match else "N/A"
        review_count = match.group(3) if match else "N/A"
        review_count = review_count.strip()
        reviews = f"{sentiment.strip()} - {percentage.strip()}"

        return (
            name,
            published_date,
            platforms,
            original_price,
            discount_pct,
            discount_price,
            reviews,
            review_count,
        )

    def _scrape_page(self, url, filter, n0Games):
        """
        Scrapes game data for a given URL and filter.

        Args:
            url (str): The URL to scrape.
            filter (str): The filter for the game data.

        Returns:
            list: List of game data for the filter.
        """
        total_pages = self._get_total_pages(url)
        all_game_info = []

        for page in range(1, total_pages + 1):
            response = requests.get(f"{url}&page={page}")
            doc = BeautifulSoup(response.content, "html.parser")
            games = doc.find_all("div", {"class": "responsive_search_name_combined"})

            for game in games:
                game_info = self._extract_game_info(game)
                all_game_info.append([*game_info, filter])

                if len(all_game_info) >= n0Games:
                    break
            if len(all_game_info) >= n0Games:
                break
        return all_game_info

    def ScrapeGames(self, n0Games=5, tags=["Discounts", "F2P"]):
        """
        Scrapes game data for each tag specified in the 'tags' attribute and returns a dictionary.

        Returns:
            dict: Dictionary containing game data.

        Tags:
            The 'tags' attribute specifies the filters to be applied during scraping.
            These tags correspond to keys in the 'search_filters' dictionary, which maps each tag to its respective filter query parameter.

            Example:
            If 'tags' is ['Discounts', 'F2P'], the scraper will retrieve games that are discounted and free to play.
            The available tags are:
                Top Sellers, Discounts, F2P (Free to Play)
                Software, DLC, Demos, Mods, Games
                Windows, MacOS, Linux, VR, Deck
                MP, PvP, Co-op
        """
        all_data = []
        search_filters = {
            "Top Sellers": "topselling",
            "Discounts": "specials=1",
            "F2P": "?maxprice=free",
            "Software": "category1=994",
            "DLC": "category1=21",
            "Demos": "category1=10",
            "Mods": "category1=997",
            "Games": "category1=998",
            "Windows": "os=win",
            "MacOS": "os=mac",
            "Linux": "os=linux",
            "VR": "vrsupport=402",
            "Deck": "deck_compatibility=2",
            "MP": "category3=1",
            "PvP": "category3=49",
            "Co-op": "category3=9",
        }
        for filter in tags:
            url = f"{self.base_url}{search_filters[filter]}"
            filter_data = self._scrape_page(url, filter, n0Games)
            all_data.extend(filter_data)

        data = {col: [] for col in self.cols}
        for row in all_data:
            for col, value in zip(self.cols, row):
                data[col].append(value)

        return self.__to_readable_format(data)

    def __to_readable_format(self, data):
        """
        Converts the data dictionary to a list for better readability.

        Args:
            data (dict): The data dictionary to convert.

        Returns:
            list: List of dictionaries with game data.
        """
        # Ensure the output is encoded in utf-8 to avoid encoding issues

        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

        print(data)
        readable_data = []
        for i in range(len(data["Name"])):
            game_data = {col: data[col][i] for col in self.cols}
            readable_data.append(game_data)
        return readable_data


steam = SteamStoreScraper()
result = steam.ScrapeGames(n0Games=5, tags=["Discounts", "F2P"])
