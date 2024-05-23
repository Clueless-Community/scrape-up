import requests
from bs4 import BeautifulSoup


class Yellowpages:
    """
    Create an instance of `yellowpages` class

    ```python
    # This will return the list of restaurtants in New York and their information
    data = yellowpages("restaurtant", "New York")
    ```
    | Method            | Details                                                           |
    | ----------------- | ----------------------------------------------------------------- |
    | `business_info()` | Returns the list of dictionaries containing business information. |

    """

    def __init__(self, business, place):
        self.business = business
        self.place = place
        self.info = []
        try:
            url = f"https://www.yellowpages.com/search?search_terms={self.business}&geo_location_terms={self.place}"
            response = requests.get(url, headers={"User-Agent": "XY"})
            self.soup = BeautifulSoup(response.content, "lxml")

        except:
            return None

    def business_info(self):
        businesses = self.soup.find_all("div", class_="srp-listing clickable-area mdm")
        for item in businesses:
            name = item.find("a", class_="business-name").text
            address = item.find("div", class_="street-address").text
            try:
                rating = item.find("div", class_="ratings").text
            except:
                rating = " "
            try:
                website = item.find("a", class_="track-visit-website")["href"]
            except:
                website = " "
            try:
                phone_no = item.find("div", class_="phones phone primary").text
            except:
                phone_no = " "
            try:
                menu = (
                    "https://www.yellowpages.com"
                    + item.find("a", class_="menu")["href"]
                )
            except:
                menu = " "
            try:
                description = item.find("p", class_="body").text
            except:
                description = " "
            try:
                amenities = item.find("div", class_="amenities-info").text
            except:
                amenities = " "
            try:
                opentime = item.find("div", class_="open-status").text
            except:
                opentime = " "
            businessinfo = {
                "name": name,
                "address": address,
                "rating": rating,
                "website": website,
                "phone_no": phone_no,
                "menu": menu,
                "description": description,
                "amenities": amenities,
                "opentime": opentime,
            }
            self.info.append(businessinfo)
        return self.info
