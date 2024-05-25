from bs4 import BeautifulSoup as bs
import requests


class Requirements:
    def __init__(self, search_term: str, search_alphabet: str):
        self.search_term = search_term
        self.search_alphabet = search_alphabet

    def __scrape_data(self, url):
        try:
            html = requests.get(url)
            return html.text

        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching the page: {str(e)}")

    def __parse_page(self):
        url = f"https://www.systemrequirementslab.com/all-games-list/?filter={self.search_alphabet}"
        html = self.__scrape_data(url)
        soup = bs(html, "html.parser")
        return soup

    def __find_game(self):
        try:
            soup = self.__parse_page()

            div_elements = soup.find("div", class_="pt-3")
            li_elements = div_elements.find_all("li")

            for li in li_elements:
                a_tag = li.find("a", title=True)
                if self.search_term.lower() in a_tag["title"].lower():
                    return a_tag["href"]

            return None

        except Exception as e:
            raise Exception(f"An error occurred while finding the game:\n{str(e)}")

    def details(self):
        try:
            url = f"https://www.systemrequirementslab.com{self.__find_game()}"
            html = self.__scrape_data(url)
            soup = bs(html, "html.parser")
            requirements = soup.find_all("div", class_="col col-8")
            if not requirements:
                raise Exception("Game not found")
            return requirements

        except Exception as e:
            raise Exception(f"An error occurred while fetching the game requirements:\n{str(e)}")


    def minimum_graphics(self):
        try:
            details = self.details()
            for li in details[0].find_all("li"):
                if "VIDEO CARD" in li.find("strong").text:
                    return li.text[12:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum graphics:\n{str(e)}")

    def minimum_cpu(self):
        try:
            details = self.details()
            for li in details[0].find_all("li"):
                if "CPU" in li.find("strong").text:
                    return li.text[5:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum CPU:\n{str(e)}")

    def minimum_ram(self):
        try:
            details = self.details()
            for li in details[0].find_all("li"):
                if "RAM" in li.find("strong").text:
                    return li.text[5:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum RAM:\n{str(e)}")

    def minimum_os(self):
        try:
            details = self.details()
            for li in details[0].find_all("li"):
                if "OS" in li.find("strong").text:
                    return li.text[4:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum OS:\n{str(e)}")

    def minimum_storage(self):
        try:
            details = self.details()
            for li in details[0].find_all("li"):
                if "FREE DISK SPACE" in li.find("strong").text:
                    return li.text[15:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum storage:\n{str(e)}")

    def minimum_vram(self):
        try:
            details = self.details()
            for li in details[0].find_all("li"):
                if "DEDICATED VIDEO RAM" in li.find("strong").text:
                    return li.text[19:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum VRAM:\n{str(e)}")

    def recommended_graphics(self):
        try:
            details = self.details()
            for li in details[1].find_all("li"):
                if "VIDEO CARD" in li.find("strong").text:
                    return li.text[12:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended graphics:\n{str(e)}")

    def recommended_cpu(self):
        try:
            details = self.details()
            for li in details[1].find_all("li"):
                if "CPU" in li.find("strong").text:
                    return li.text[5:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended CPU:\n{str(e)}")

    def recommended_ram(self):
        try:
            details = self.details()
            for li in details[1].find_all("li"):
                if "RAM" in li.find("strong").text:
                    return li.text[5:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended RAM:\n{str(e)}")

    def recommended_os(self):
        try:
            details = self.details()
            for li in details[1].find_all("li"):
                if "OS" in li.find("strong").text:
                    return li.text[4:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended OS:\n{str(e)}")

    def recommended_storage(self):
        try:
            details = self.details()
            for li in details[1].find_all("li"):
                if "FREE DISK SPACE" in li.find("strong").text:
                    return li.text[15:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended storage:\n{str(e)}")

    def recommended_vram(self):
        try:
            details = self.details()
            for li in details[1].find_all("li"):
                if "DEDICATED VIDEO RAM" in li.find("strong").text:
                    return li.text[19:]

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended VRAM:\n{str(e)}")

    def minimum_requirements(self):
        try:
            return {
                "Graphics": self.minimum_graphics(),
                "CPU": self.minimum_cpu(),
                "RAM": self.minimum_ram(),
                "OS": self.minimum_os(),
                "Storage": self.minimum_storage(),
                "VRAM": self.minimum_vram()
            }

        except Exception as e:
            raise Exception(f"An error occurred while fetching the minimum requirements:\n{str(e)}")

    def recommended_requirements(self):
        try:
            return {
                "Graphics": self.recommended_graphics(),
                "CPU": self.recommended_cpu(),
                "RAM": self.recommended_ram(),
                "OS": self.recommended_os(),
                "Storage": self.recommended_storage(),
                "VRAM": self.recommended_vram()
            }

        except Exception as e:
            raise Exception(f"An error occurred while fetching the recommended requirements:\n{str(e)}")