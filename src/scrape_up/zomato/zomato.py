from bs4 import BeautifulSoup as bs
from scrape_up.config.request_config import RequestConfig, get


class Zomato:
    """
    Create an object of the 'Zomato' class\n
    ```python
    scraper = Zomato()
    ```
    | Methods                    | Details                                                                   |
    | -------------------------- | ------------------------------------------------------------------------- |
    | `.get_restaurants_details()` | Returns the restraunt data with name, cuisine, area, rating, offers, etc  |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def get_restaurants_details(self, page_url: str):
        """
        Create an object of the 'Zomato' class\n
        ```python
        scraper = Zomato()
        scraper.get_restaurants_details(page_url="https://www.zomato.com/ncr/music-mountains-hillside-cafe-greater-kailash-gk-1-new-delhi/order")
        ```
        Response
        ```js
        {
            'name': 'Music & Mountains - Hillside Cafe',
            'cuisine':
                [
                    'Italian',
                    'Continental',
                    'Fast Food',
                    'Salad',
                    'Desserts',
                    'Beverages',
                    'Shake'
                ],
            'area': 'M Block Market, Greater Kailash 1 (GK1), New Delhi',
            'dining_rating': '4.6',
            'dining_review_count': '6,165',
            'delivery_rating': '4.5',
            'delivery_review_count': '1,097',
            'offers':
                [
                    {'50% OFF up to ₹100': 'use code HUNGRY'},
                    {'Flat ₹125 OFF': 'use code GET125'},
                    {'Flat ₹125 OFF': 'use code CANARAPARTY'},
                    {'₹25 - ₹250 cashback': 'use code PAYTMWEE...'}
                ]
        }
        ```
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            # self.config = config
            if self.config.headers == {}:
                self.config.set_headers(headers)
            response = get(page_url, self.config).text
            soup = bs(response, "lxml")
            restaurant_data = []
            name = soup.find(
                "h1", {"class": "sc-7kepeu-0 sc-iSDuPN fwzNdh"}
            ).text.strip()
            cuisine_box = soup.find("div", {"class": "sc-fgfRvd gBMRZZ"})
            cuisines_all = cuisine_box.find_all("span")
            cuisines = []
            for cuisine in cuisines_all:
                cuisine_add = cuisine.text.strip().replace(",", "")
                if cuisine_add != "," and cuisine_add != "":
                    cuisines.append(cuisine_add)
            area = soup.find("a", {"class": "sc-clNaTc vNCcy"}).text.strip()
            rating_boxes = soup.find("section", {"class": "sc-dxZgTM QvFZM"})
            ratings = rating_boxes.find_all("div", {"class": "sc-1q7bklc-1 cILgox"})
            dining_rating = ratings[0].text.strip()
            delivery_rating = ratings[1].text.strip()
            review_count_boxes = rating_boxes.find_all(
                "div", {"class": "sc-1q7bklc-8 kEgyiI"}
            )
            dining_review_count = review_count_boxes[0].text.strip()
            delivery_review_count = review_count_boxes[1].text.strip()
            offers = []
            offer_boxes = soup.find_all("div", {"class": "sc-1a03l6b-2 gerWzu"})
            for offer in offer_boxes:
                offer_ = {}
                offer_text = offer.find_all("div")
                offer_[offer_text[0].text.strip()] = offer_text[1].text.strip()
                offers.append(offer_)
            restaurant_data = {
                "name": name,
                "cuisine": cuisines,
                "area": area,
                "dining_rating": dining_rating,
                "dining_review_count": dining_review_count,
                "delivery_rating": delivery_rating,
                "delivery_review_count": delivery_review_count,
                "offers": offers,
            }
            return restaurant_data
        except:
            return None
