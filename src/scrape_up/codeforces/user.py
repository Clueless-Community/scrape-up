from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Users:
    """
    Create an object of class `LeetCodeScraper`

    ```python
    from scrape_up import codeforces
    ```

    Methods
    ```md
    | Methods                    | Details                                       |
    | -------------------------- | --------------------------------------------- |
    | `.get_user_data(username)` | Fetches user data from CodeForces. |
    ```
    """

    user_url = "https://codeforces.com/profile/{}"

    def __init__(self, username: str, *, config: RequestConfig = RequestConfig()):
        self.username = username
        headers = {"User-Agent": "scrapeup"}
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def _extract_text_or_empty(self, element):
        """
        Extract text from an element or return an empty string if the element is None.
        """
        return element.text.strip() if element else ""

    def get_user_data(self):
        """
        Fetches user data from CodeForces.\n
        Example

        ```python
        codeforces_user = codeforces.Users(username="tourist")
        codeforces_user.get_user_data()
        ```
        Response
        ```js
        {
            "rank":"Legendary Grandmaster",
            "handle":"tourist",
            "firstname":"Gennady",
            "lastname":"Korotkevich",
            "city":" Gomel",
            "country":"Belarus",
            "organization":" ITMO University",
            "rating":"3775",
            "contribution":"+127",
            "friendsofcount":"59,071",
            "lastvisit":"14400",
            "registered":"441806400.0",
            "titlephoto":"https://userpic.codeforces.org/422/title/50a270ed4a722867.jpg",
            "avatar":"https://userpic.codeforces.org/422/title/50a270ed4a722867.jpg"
        }
        ```
        """
        try:
            url = self.user_url.format(self.username)
            response = get(url, self.config)
            response.raise_for_status()  # Raise an exception for HTTP errors

            soup = BeautifulSoup(response.text, "html.parser")

            # Extracting user information
            user_info = {}

            # Find the main-info div
            main_info = soup.find("div", class_="main-info")

            # Extract user's rank
            user_info["rank"] = self._extract_text_or_empty(
                main_info.find("div", class_="user-rank")
            )

            # Extract user's name and handle
            user_name = main_info.find("h1")
            user_info["handle"] = user_name.find("a").text.strip()

            # Find the div with user information
            user_info_string = self._extract_text_or_empty(
                main_info.find("div", style="margin-top: 0.5em;")
            )
            info_list = user_info_string.split(",")

            user_info["firstName"], user_info["lastName"] = info_list[0].split()
            user_info["city"] = info_list[1]

            location_info = info_list[2].split("From")
            user_info["country"] = location_info[0].strip()
            user_info["organization"] = location_info[1]

            # Extract user's rating and max rating
            user_rating = soup.find("div", class_="info").find_all("li")
            for item in user_rating:
                if "Contest rating:" in item.text:
                    rating_span = item.find("span", class_="user-legendary")
                    user_info["rating"] = (
                        self._extract_text_or_empty(rating_span) if rating_span else ""
                    )
                elif "max. legendary grandmaster" in item.text:
                    max_rating_span = item.find("span", class_="user-legendary")
                    user_info["maxRating"] = (
                        self._extract_text_or_empty(max_rating_span)
                        if max_rating_span
                        else ""
                    )

            # Find the <div> element with class "info"
            info_div = soup.find("div", class_="info")

            # Initialize an empty string to store the contest rating and other such info text
            extracted_text = ""

            # Check if the <div> element exists
            if info_div:
                # Find the <ul> element within the <div>
                ul_element = info_div.find("ul")

                # Check if the <ul> element exists
                if ul_element:
                    # Find all <li> elements within the <ul>
                    li_elements = ul_element.find_all("li")

                    # Loop through each <li> element and extract its text
                    for li in li_elements:
                        text = li.get_text(strip=True)
                        extracted_text += text + " "

            temp = extracted_text.split(":")

            user_info["contribution"] = temp[2].split()[0]
            user_info["friendsOfCount"] = temp[3].split()[0]
            user_info["lastVisit"] = int(temp[4].split()[0]) * 3600
            user_info["registered"] = int(temp[5].split()[0]) * 365.25 * 24 * 60 * 60

            # Extract title photo and avatar
            title_photo_div = soup.find("div", class_="title-photo")
            user_info["titlePhoto"] = (
                title_photo_div.find("img")["src"] if title_photo_div else ""
            )
            user_info["avatar"] = (
                title_photo_div.find("img")["src"] if title_photo_div else ""
            )

            # Extracting keys
            keys = [f"{i}".lower() for i in user_info.keys()]

            # Extracting values

            values = [f"{i}" for i in user_info.values()]

            response = dict(zip(keys, values))

            return response

        except:
            return None
