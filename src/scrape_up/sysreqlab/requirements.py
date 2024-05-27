from bs4 import BeautifulSoup as bs
import requests


class Requirements:
    """
    Create an instance of `Requirements` class.
    ```python
    requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
    ```
    ```
    | Methods                     | Details                                                                                   |
    | --------------------------- | ----------------------------------------------------------------------------------------- |
    | `.minimum_graphics()`       | Returns the minimum graphics required for the game.                                       |
    | `.minimum_cpu()`            | Returns the minimum CPU required for the game.                                            |
    | `.minimum_ram()`            | Returns the minimum RAM required for the game.                                            |
    | `.minimum_os()`             | Returns the minimum OS required for the game.                                             |
    | `.minimum_storage()`        | Returns the minimum storage required for the game.                                        |
    | `.minimum_vram()`           | Returns the minimum VRAM required for the game.                                           |
    | `.recommended_graphics()`   | Returns the recommended graphics required for the game.                                   |
    | `.recommended_cpu()`        | Returns the recommended CPU required for the game.                                        |
    | `.recommended_ram()`        | Returns the recommended RAM required for the game.                                        |
    | `.recommended_os()`         | Returns the recommended OS required for the game.                                         |
    | `.recommended_storage()`    | Returns the recommended storage required for the game.                                    |
    | `.recommended_vram()`       | Returns the recommended VRAM required for the game.                                       |
    | `.minimum_requirements()`   | Returns the minimum requirements for the game.                                            |
    | `.recommended_requirements()`| Returns the recommended requirements for the game.                                        |
    ```
    """

    def __init__(self, search_term: str, search_alphabet: str):
        self.search_term = search_term
        self.search_alphabet = search_alphabet
        self.details = None

    def __scrape_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def __parse_page(self):
        url = f"https://www.systemrequirementslab.com/all-games-list/?filter={self.search_alphabet}"
        html = self.__scrape_data(url)
        soup = bs(html, "html.parser")
        return soup

    def __find_game(self):
        soup = self.__parse_page()
        div_elements = soup.find("div", class_="pt-3")
        li_elements = div_elements.find_all("li")

        for li in li_elements:
            a_tag = li.find("a", title=True)
            if self.search_term.lower() in a_tag["title"].lower():
                return a_tag["href"]
        return None

    def __fetch_details(self):
        if self.details is None:
            game_url = self.__find_game()
            if game_url:
                url = f"https://www.systemrequirementslab.com{game_url}"
                html = self.__scrape_data(url)
                soup = bs(html, "html.parser")
                self.details = soup.find_all("div", class_="col col-8")
            else:
                raise Exception("Game not found")
        return self.details

    def __extract_requirement(self, category, index=0):
        try:
            details = self.__fetch_details()
            for li in details[index].find_all("li"):
                if category in li.find("strong").text:
                    return li.text.split(":")[1].strip()
        except Exception as e:
            raise Exception(
                f"An error occurred while fetching the {category.lower()}:\n{str(e)}"
            )

    def minimum_graphics(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_graphics = requirements.minimum_graphics()
        ```
        """
        return self.__extract_requirement("VIDEO CARD", 0)

    def minimum_cpu(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_cpu = requirements.minimum_cpu()
        ```
        """
        return self.__extract_requirement("CPU", 0)

    def minimum_ram(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_ram = requirements.minimum_ram()
        ```
        """
        return self.__extract_requirement("RAM", 0)

    def minimum_os(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_os = requirements.minimum_os()
        ```
        """
        return self.__extract_requirement("OS", 0)

    def minimum_storage(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_storage = requirements.minimum_storage()
        ```
        """
        return self.__extract_requirement("FREE DISK SPACE", 0)

    def minimum_vram(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_vram = requirements.minimum_vram()
        ```
        """
        return self.__extract_requirement("DEDICATED VIDEO RAM", 0)

    def recommended_graphics(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_graphics = requirements.recommended_graphics()
        ```
        """
        return self.__extract_requirement("VIDEO CARD", 1)

    def recommended_cpu(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_cpu = requirements.recommended_cpu()
        ```
        """
        return self.__extract_requirement("CPU", 1)

    def recommended_ram(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_ram = requirements.recommended_ram()
        ```
        """
        return self.__extract_requirement("RAM", 1)

    def recommended_os(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_os = requirements.recommended_os()
        ```
        """
        return self.__extract_requirement("OS", 1)

    def recommended_storage(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_storage = requirements.recommended_storage()
        ```
        """
        return self.__extract_requirement("FREE DISK SPACE", 1)

    def recommended_vram(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_vram = requirements.recommended_vram()
        ```
        """
        return self.__extract_requirement("DEDICATED VIDEO RAM", 1)

    def minimum_requirements(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            minimum_requirements = requirements.minimum_requirements()
        ```
        """
        return {
            "Graphics": self.minimum_graphics(),
            "CPU": self.minimum_cpu(),
            "RAM": self.minimum_ram(),
            "OS": self.minimum_os(),
            "Storage": self.minimum_storage(),
            "VRAM": self.minimum_vram(),
        }

    def recommended_requirements(self):
        """
        Class - `Requirements`
        Example:
        ```python
            requirements = Requirements(search_term="Cyberpunk", search_alphabet="c")
            recommended_requirements = requirements.recommended_requirements()
        ```
        """
        return {
            "Graphics": self.recommended_graphics(),
            "CPU": self.recommended_cpu(),
            "RAM": self.recommended_ram(),
            "OS": self.recommended_os(),
            "Storage": self.recommended_storage(),
            "VRAM": self.recommended_vram(),
        }
