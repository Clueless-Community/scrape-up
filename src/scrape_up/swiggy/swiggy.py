import requests
from bs4 import BeautifulSoup as bs

class Swiggy:
    """
    Create an object of the 'Swiggy' class\n
    ```python
    scraper = Swiggy()
    ```
    | Methods         | Details                                                                   |
    | --------------- | ------------------------------------------------------------------------- |
    | `.getDetails()` | Returns the restraunt data with name, cuisine, area, rating, offers, etc  |
    """

    def __init__(self, page_url):
        self.page_url = page_url

    def getDetails(self):
        try:
            headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
                }
            response = requests.get(self.page_url, headers = headers).text
            soup = bs(response, "lxml")
            restaurant_data = []
            name = soup.find("p", {"class": "RestaurantNameAddress_name__2IaTv"}).text.strip()
            cuisine = soup.find("p", {"class": "RestaurantNameAddress_cuisines__mBHr2"}).text.strip()
            area = soup.find("p", {"class": "RestaurantNameAddress_area__2P9ib"}).text.strip()
            rating = soup.find("span", {"class": "RestaurantRatings_avgRating__1TOWY"}).text.strip()
            rating_count = soup.find("span", {"class": "RestaurantRatings_totalRatings__3d6Zc"}).text.strip()
            cost_per = soup.find_all("li", {"class": "RestaurantTimeCost_item__2HCUz"})[-1].text.strip()
            offers = []
            offer_box = soup.find_all("div", {"class": "RestaurantOffer_infoWrapper__2trmg"})
            for offer in offer_box:
                offer_ = {}
                offer_header = offer.find("p", {"class": "RestaurantOffer_header__3FBtQ"}).text.strip()
                offer_content_box = offer.find("div", {"class": "RestaurantOffer_offerCodeWrapper__2Cr4F"})
                offer_content_1 = offer.find("span").text.strip()
                offer_content_2 = offer.find("span", {"class": "RestaurantOffer_description__1SRJf"}).text.strip()
                offer_content = offer_content_1 + " | " + offer_content_2
                offer_[offer_header] = offer_content
                offers.append(offer_)
            restaurant_data = {
                "name" : name,
                "cuisine" : cuisine,
                "area" : area,
                "rating" : rating,
                "rating_count" : rating_count,
                "cost_per_person" : cost_per,
                "offers" : offers
            }
            return restaurant_data
        except:
            return None

if __name__ == "__main__":
    store1 = Swiggy("https://www.swiggy.com/restaurants/pizza-hut-western-extension-area-karol-bagh-delhi-435678")
    print(store1.getDetails())