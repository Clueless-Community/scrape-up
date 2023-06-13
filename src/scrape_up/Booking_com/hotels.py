import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})

class HotelInfo:
    def __init__(self,location,startdate,enddate):
        self.location = location
        self.start_date, self.start_month, self.start_year = startdate.split('-')
        self.end_date, self.end_month, self.end_year = enddate.split('-')

    def scrape_page(self):
        page_no = 0
        URL = f"https://www.booking.com/searchresults.html?aid=304142&label=gen173rf-1FCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGiAg1wcm9qZWN0cHJvLmlvqAIDuAKwwPadBsACAdICJDU0NThkNDAzLTM1OTMtNDRmOC1iZWQ0LTdhOTNjOTJmOWJlONgCBeACAQ&sid=2214b1422694e7b065e28995af4e22d9&sb=1&sb_lp=1&src=theme_landing_index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fhotel%2Findex.html%3Faid%3D304142%26label%3Dgen173rf-1FCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGiAg1wcm9qZWN0cHJvLmlvqAIDuAKwwPadBsACAdICJDU0NThkNDAzLTM1OTMtNDRmOC1iZWQ0LTdhOTNjOTJmOWJlONgCBeACAQ%26sid%3D2214b1422694e7b065e28995af4e22d9%26&ss={self.location}&is_ski_area=0&checkin_year={self.start_year}&checkin_month={self.start_month}&checkin_monthday={self.start_date}&checkout_year={self.end_year}&checkout_month={self.end_month}&checkout_monthday={self.end_date}&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&offset={page_no}"
        new_webpage = requests.get(URL, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        links = new_soup.find_all("a", attrs={"class": "e13098a59f"})
        return links

    def get_Hotel_Name(self, soup):
        try:
            title = soup.find("h2", attrs={"class": 'd2fee87262 pp-header__title'})
            title_value = title.text
            title_string = title_value.strip()
        except AttributeError:
            title_string = ""
        return title_string

    def get_all_hotel_names(self):
        links = self.scrape_page()
        hotel_names = []
        for link in links:
            new_webpage = requests.get(link.get('href'), headers=HEADERS)
            new_soup = BeautifulSoup(new_webpage.content, "html.parser")
            hotel_name = self.get_Hotel_Name(new_soup)
            hotel_names.append(hotel_name)
        return hotel_names

