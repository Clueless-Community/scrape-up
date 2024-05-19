import requests
from bs4 import BeautifulSoup
from time import sleep
import re


class LichessGames:
    """
    Create an instance of the class `LichessGames`
    ```python
    lichess = LichessGames(username)
    lichess_games = lichess.fetch_games()
    ```
    | Methods                       | Details                                                                    |
    | ----------------------------- | -------------------------------------------------------------------------- |
    | `.fetch_games()`              | Fetch all the games data for the specified username.                       |

    Note : player score and score_change is None :
        - the game is Casual
        - the player is anonymous or stockfish
    """

    def __init__(self, username):
        """
        Initialize the `LichessGames` instance with the specified username.
        """
        self.url = f"https://lichess.org/@/{username}/all"

    def __fetch_page_games(self, page_num):
        requested_data = requests.get(f"{self.url}?page={page_num}")._content
        parsed_data = BeautifulSoup(requested_data, "lxml")
        games_data = parsed_data.find_all("article", {"class": "game-row paginated"})
        if not games_data:
            return None
        game_list = []
        for game_data in games_data:
            game_info = {}
            game_info["white_player"] = self.__get_player_info(game_data, "white")
            game_info["black_player"] = self.__get_player_info(game_data, "black")
            game_info["pgn"] = self.__get_pgn(game_data)
            game_list.append(game_info)
        return game_list

    def fetch_games(self, start_page=1, end_page=4):
        """
        Fetch all the games data for the specified username.

        Parameters:
        - `start_page` (int): Starting page number. Default is 1.
        - `end_page` (int): Ending page number. Default is 4.

        Example:
        ```python
        # Default usage:
        games = scraper.fetch_games()

        # Custom usage:
        games = scraper.fetch_games(start_page=5, end_page=8)
        ```
        """
        all_games_list = []
        try:
            for counter in range(start_page, end_page):
                game_list = self.__fetch_page_games(counter)
                if game_list is None:
                    break
                all_games_list += game_list
        except Exception:
            return None
        return all_games_list

    def __get_player_info(self, game_data, color):
        """
        Extract the player information from the game data for the specified color (white or black).
        """
        player = game_data.find("div", {"class": f"player {color}"})
        if player.find("span", {"class": "anon"}):
            return self.__get_non_player_info("Anonymous")
        if re.search("Stockfish", str(player)):
            bot_name = player.text.replace("\u00a0", " ")
            return self.__get_non_player_info(bot_name)
        return {
            "username": self.__get_username(player),
            "before_game_score": self.__get_score(player),
            "score_change": self.__get_score_change(player),
        }

    def __get_non_player_info(self, username):
        """
        Create player information for non-player entities (anonymous or bots).
        """
        return {
            "username": f"{username}",
            "before_game_score": None,
            "score_change": None,
        }

    def __get_username(self, player):
        return player.find("a", class_="user-link").text

    def __get_score(self, player):
        """
        Extract the player's score before the game from the player data.

        Returns:
        - `str` or `None`: The player's score before the game, or None if not (Anonymous ).
        """
        score = re.search(">([0-9]{3,4})\?? <", str(player))
        if not score:
            return None
        return score.group(1).strip()

    def __get_score_change(self, player):
        """
        Extract the player's score change after the game from the player data.
        """
        score_change = player.find("bad") or player.find("good") or player.find("span")
        if score_change is None:
            return None
        score_change = score_change.text
        score_change = score_change.replace("\u00b1", "")
        score_change = score_change.replace("\u2212", "-")
        return score_change

    def __get_pgn(self, game_data):
        """
        Extract the PGN (Portable Game Notation) from the game data.
        """
        gameUrl = game_data.find("a", {"class": "game-row__overlay"})["href"]
        pgn_request = requests.get(f"https://lichess.org{gameUrl}")._content
        parsed_pgn = BeautifulSoup(pgn_request, "lxml")
        return parsed_pgn.find("div", {"class": "pgn"}).text
