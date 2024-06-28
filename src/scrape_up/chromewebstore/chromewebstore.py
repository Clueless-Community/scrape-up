import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_from_bytes


class ChromeWebStore:
    """
    A class to interact with the Chrome Web Store and retrieve extension details.

    Attributes:
    base_url (str): Base URL for the Chrome Web Store.
    """

    base_url = "https://chromewebstore.google.com/"

    def search(self, keyword: str, filter: dict = None):
        """
        Scrapes a list of extensions from the Chrome Web Store based on a keyword search and optional filters.

        Args:
        keyword (str): The keyword(s) to search for (URL encoded).
        filter (dict, optional): Search filters.
            {
                'itemTypes': 'EXTENSION' or 'THEME',
                'filterBy': 'featured' or 'establishedPublisher' or 'featured,establishedPublisher',
                'minimalRating': Rating out of 5
            }

        Returns:
        tuple: A tuple containing two elements:
            - list: A list of dictionaries containing extension details
                {
                    "title": "Elephantastic Theme",
                    "id": "abcdefg1234567890",
                    "link": "https://chromewebstore.google.com/webstore/detail/elephantastic-theme/abcdefg1234567890",
                    "thumbnail": "https://...",  # URL to the thumbnail image
                    "rating": "4.5",
                    "no_of_rating": "1000",
                    "description": "A delightful theme featuring playful elephant illustrations.",
                    "featured": True,
                    "verified_publisher": False
                }
            - str: A message indicating success or errors ("success" or "No results found for given Criteria").

        Raises:
        requests.exceptions.RequestException: If there's an error fetching search results.
        """
        keyword = quote_from_bytes(keyword.encode("utf-8"))
        url = f"{ChromeWebStore.base_url}search/{keyword}"

        try:
            params = filter or {}
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for non-200 status codes

            soup = BeautifulSoup(response.content, "html.parser")
        except requests.exceptions.RequestException as e:
            return [], f"Error fetching search results : {e}"
        finally:
            # to check for no results
            error = soup.find("h1", class_="SCmIo")
            if error:
                return [], "No results found for given criteria"

        extension_elements = soup.find_all("div", class_="Cb7Kte")

        extensions = []
        for element in extension_elements:
            extension = {}

            try:
                # title
                title_element = element.find("div", class_="IcZnBc")
                if title_element:
                    extension["title"] = title_element.text.strip()

                # extension id
                extension["id"] = element["data-item-id"]

                # description
                desc_element = element.find("p", class_="g3IrHd")
                if desc_element:
                    extension["description"] = desc_element.text.strip()

                # thumbnail
                thumb_nail = element.find("img", class_="fzxcm")
                if thumb_nail:
                    extension["thumbnail"] = thumb_nail["src"]

                # hyperlink
                link_element = element.find("a", class_="q6LNgd")
                if link_element:
                    extension["link"] = (
                        ChromeWebStore.base_url + link_element["href"][2:]
                    )

                # average rating
                rating_element = element.find("span", class_="Vq0ZA")
                if rating_element:
                    extension["rating"] = rating_element.text.strip()

                # number of user ratings
                no_of_rating = element.find("span", class_="Y30PE")
                if no_of_rating:
                    extension["no_of_rating"] = no_of_rating.text.strip()

                # is the extension or theme featured in chrome store
                featured_tag = element.find("span", class_="OmOMFc")
                extension["featured"] = True if featured_tag else False

                # is the publisher established
                verified_publisher = element.find(
                    "svg", class_="BFBOHf z088xd RVihJ NMm5M"
                )
                extension["verified_publisher"] = True if verified_publisher else False

            except AttributeError as e:
                print(f"Error parsing search element {e}")
                continue

            extensions.append(extension)

        if extensions:
            return extensions, "success"
        else:
            return extensions, "No results found for given criteria"

    def get_details(self, id: str, overview: bool = False):
        """
        Fetches details about a specific extension from the Chrome Web Store.

        Args:
            id (str): The ID of the extension to fetch details for. Example: "gjdmanggfaalgnpinolamlefhcjimmam".
            overview (bool, optional): Whether to include the extension's overview description. Defaults to False.

        Returns:
            tuple[dict, str]: A tuple containing a dictionary with the fetched details and a status message
                The dictionary will be empty if there's an error, and the message will indicate the error type.
                EXAMPLE FOR DICT
                {
                 title: Minesweeper Original
                thumbnail: https:/....
                rating: 4.8
                tags: ['Extension', 'Workflow & Planning']
                no_of_users: 2,000,000
                Updated: July 21, 2023
                Offered by: Davi Hendrix
                Size: 133KiB
                Languages: Bahasa Indonesia, Bahasa Melayu, Deutsch, English, English (UK), English (United States), Filipino, Français, Kiswahili, Nederlands, Norsk, Tiếng Việt, Türkçe, català, dansk, eesti, español, español (Latinoamérica), hrvatski, italiano, latviešu, lietuvių, magyar, polski, português (Brasil), português (Portugal), română, slovenský, slovenščina, suomi, svenska, čeština, Ελληνικά, Српски, български, русский, українська, עברית, فارسی‎, मराठी, हिन्दी, বাংলা, ગુજરાતી, தமிழ், తెలుగు, ಕನ್ನಡ, മലയാളം, ไทย, አማርኛ, ‫العربية, 中文 (简体), 中, suomi文 (繁體), 日本語, 한국어
                文 (繁體), 日本語, 한국어
                Developer: Email davihendrixm3602@gmail.com
                Non-trader: True
                }

        Raises:
            requests.exceptions.RequestException: If there's an error fetching the details from the web.

        Notes:
            - This method fetches details from the Chrome Web Store using the provided extension ID.
            - If overview is set to True, the returned dictionary will include the extension's overview description.
            - The fetched details include information like name, version, size, languages, and other metadata.

        Example:
            >>> chrome_extension_id = "gjdmanggfaalgnpinolamlefhcjimmam"
            >>> details, status = get_details(chrome_extension_id, overview=True)
            >>> print(details)
            {'Name': 'Example Extension', 'Version': '1.0', 'Size': '2.1 MB', 'Languages': ['English'], ...}
            >>> print(status)
            'success'
        """
        id = quote_from_bytes(id.encode("utf-8"))
        url = f"{ChromeWebStore.base_url}detail/{id}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
        except requests.exceptions.RequestException as e:
            return {}, f"Error fetching search results : {e}"

        # to check for invalid id
        error = soup.find("h1", class_="eFHPDf")
        if error:
            return {}, "No results found"

        extension = {}

        try:

            # title
            title = soup.find("h1", class_="Pa2dE")
            extension["title"] = title.text.strip()

            # thumbnail
            thumbnail = soup.find("img", class_="rBxtY")
            extension["thumbnail"] = thumbnail["src"]

            # user rating out of 5
            rate = soup.find("span", class_="Vq0ZA")
            extension["rating"] = rate.text.strip()

            # is the extension or theme featured in chrome store
            featured_tag = soup.find("span", class_="OmOMFc")
            extension["featured"] = True if featured_tag else False

            # is the publisher established
            verified_publisher = soup.find("svg", class_="cJI8ee")
            extension["verified_publisher"] = True if verified_publisher else False

            div_element = soup.find("div", class_="F9iKBc")
            if div_element:
                # tags
                tag_elements = div_element.find_all("a", class_="gqpEIe")
                extension["tags"] = [tag.text for tag in tag_elements]

                # number of users
                user_text = div_element.get_text(strip=True, separator=" ")
                extension["no_of_users"] = user_text.split()[-2]

            # Description / overview of extension
            if overview:
                overview_ele = soup.find("div", class_="JJ3H1e")
                extension["overview"] = overview_ele.text.strip()

            # extracting details from <ul>
            detail_ele = soup.find("ul", class_="v7vKf")
            if detail_ele:
                for li in detail_ele.find_all("li"):
                    if li.has_attr("class") and "ZbWJPd" in li["class"]:
                        first_div = li.find("div", class_="nws2nb")
                        second_div = li.find("div", class_=False)

                        if first_div and second_div:
                            key = first_div.text.strip()
                            value = second_div.text.strip()
                            extension[key] = value
            else:
                return extension, f"error scraping details about extension-{id}"

            # cleaning the output dict
            if extension["Languages"]:
                i = extension["Languages"].find(" languages")
                extension["Languages"] = extension["Languages"][i + 10 :].split(", ")

            if "Non-trader" in extension:
                extension["Non-trader"] = True
            else:
                extension["Non-trader"] = False

        except AttributeError as e:
            print(f"Error parsing search element {e}")

        return extension, "success"
