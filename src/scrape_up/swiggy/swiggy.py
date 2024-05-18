from bs4 import BeautifulSoup as bs

from scrape_up.config.request_config import RequestConfig, get


class Swiggy:
    """
    First, create an object of class `Swiggy`.\n
    ```python
    store1 = Swiggy()
    ```
    | Methods                   | Details                                                                   |
    | ------------------------- | ------------------------------------------------------------------------- |
    | `get_restraunt_details()` | Returns the restaurant data with name, cuisine, area, rating, offers, etc |
    | `get_restaurants()`       | Returns the restaurant names as per given city                            |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_restraunt_details(self, restraunt_url: str):
        """
        Create an object of the 'Swiggy' class\n
        ```python
        scraper = Swiggy()
        scraper.(restraunt_url="https://www.swiggy.com/restaurants/pizza-hut-western-extension-area-karol-bagh-delhi-435678")
        ```
        Response
        ```js
        {
            "name":"Pizza Hut",
            "cuisine":"Pizzas",
            "area":"Karol Bagh",
            "rating":"3.7",
            "rating_count":"1K+ ratings",
            "cost_per_person":"₹350 for two",
            "offers":[
                {
                    "15% OFF UPTO ₹300":"USE CITIFOODIE | ABOVE ₹1200"
                }
                ...
            ]
        }
        ```
        """
        try:
            response = get(restraunt_url, self.config).text
            soup = bs(response, "lxml")
            restaurant_data = []
            name = soup.find(
                "p", {"class": "RestaurantNameAddress_name__2IaTv"}
            ).text.strip()
            cuisine = soup.find(
                "p", {"class": "RestaurantNameAddress_cuisines__mBHr2"}
            ).text.strip()
            area = soup.find(
                "p", {"class": "RestaurantNameAddress_area__2P9ib"}
            ).text.strip()
            rating = soup.find(
                "span", {"class": "RestaurantRatings_avgRating__1TOWY"}
            ).text.strip()
            rating_count = soup.find(
                "span", {"class": "RestaurantRatings_totalRatings__3d6Zc"}
            ).text.strip()
            cost_per = soup.find_all("li", {"class": "RestaurantTimeCost_item__2HCUz"})[
                -1
            ].text.strip()
            offers = []
            offer_box = soup.find_all(
                "div", {"class": "RestaurantOffer_infoWrapper__2trmg"}
            )
            for offer in offer_box:
                offer_ = {}
                offer_header = offer.find(
                    "p", {"class": "RestaurantOffer_header__3FBtQ"}
                ).text.strip()
                offer_content_1 = offer.find("span").text.strip()
                offer_content_2 = offer.find(
                    "span", {"class": "RestaurantOffer_description__1SRJf"}
                ).text.strip()
                offer_content = offer_content_1 + " | " + offer_content_2
                offer_[offer_header] = offer_content
                offers.append(offer_)
            restaurant_data = {
                "name": name,
                "cuisine": cuisine,
                "area": area,
                "rating": rating,
                "rating_count": rating_count,
                "cost_per_person": cost_per,
                "offers": offers,
            }
            return restaurant_data
        except:
            return None

    def get_restaurants(self, city: str):
        """
        Get a list of restaurants in the given city.

        Parameters:
        - city (str): The name of the city.

        Returns:
        ```js
        [
            {
                "Name":"Domino's Pizza",
                "Rating":"4.2",
                "Cusine":"Pizzas, Italian, Pastas, Desserts",
                "Location":"Punjabi Bagh",
                "Link":"https://www.swiggy.com/restaurants/dominos-pizza-sm-arya-secondary-school-punjabi-bagh-delhi-24152"
            }
            ...
        ]
        ```
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            url = "https://www.swiggy.com/city/" + city.lower()
            html_text = get(url, self.config).text
            soup = bs(html_text, "lxml")

            container = soup.find("div", {"class": "sc-iBdmCd hPntbc"})
            restaurants = []
            for items in container.find_all(
                "a",
                {"class": "RestaurantList__RestaurantAnchor-sc-1d3nl43-3 jrDRCS"},
                href=True,
            ):
                name = items.find("div", {"class": "sc-dmyDGi bJRtXU"})
                rating = items.find("span", {"class": "sc-dmyDGi flXrCy"})
                cusine = items.find("div", {"class": "sc-dmyDGi jHWzLy"})
                location = cusine.next_sibling
                data = {
                    "Name": name.text,
                    "Rating": rating.text,
                    "Cusine": cusine.text,
                    "Location": location.text,
                    "Link": items["href"],
                }
                restaurants.append(data)
            return restaurants
        except:
            return None
