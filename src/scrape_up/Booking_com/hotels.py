import asyncio
import aiohttp
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


class HotelInfo:
    def __init__(self, location, startdate, enddate):
        self.location = location
        self.start_date, self.start_month, self.start_year = startdate.split('-')
        self.end_date, self.end_month, self.end_year = enddate.split('-')

    async def scrape_page(self, page_no):
        URL = f"https://www.booking.com/searchresults.html?aid=304142&label=gen173rf-1FCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGiAg1wcm9qZWN0cHJvLmlvqAIDuAKwwPadBsACAdICJDU0NThkNDAzLTM1OTMtNDRmOC1iZWQ0LTdhOTNjOTJmOWJlONgCBeACAQ&sid=2214b1422694e7b065e28995af4e22d9&sb=1&sb_lp=1&src=theme_landing_index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fhotel%2Findex.html%3Faid%3D304142%26label%3Dgen173rf-1FCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGiAg1wcm9qZWN0cHJvLmlvqAIDuAKwwPadBsACAdICJDU0NThkNDAzLTM1OTMtNDRmOC1iZWQ0LTdhOTNjOTJmOWJlONgCBeACAQ%26sid%3D2214b1422694e7b065e28995af4e22d9%26&ss={self.location}&is_ski_area=0&checkin_year={self.start_year}&checkin_month={self.start_month}&checkin_monthday={self.start_date}&checkout_year={self.end_year}&checkout_month={self.end_month}&checkout_monthday={self.end_date}&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&offset={page_no}"
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers=HEADERS) as response:
                content = await response.text()
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all("a", attrs={"class": "e13098a59f"})
        return links

    async def get_hotel_name(self, link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link.get('href'), headers=HEADERS) as response:
                content = await response.text()
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find("h2", attrs={"class": 'd2fee87262 pp-header__title'})
        title_string = title.text.strip() if title else ""
        return title_string

    async def get_all_hotel_names(self):
        links = await self.scrape_page(0)
        tasks = [self.get_hotel_name(link) for link in links]
        hotel_names = await asyncio.gather(*tasks)
        return hotel_names


async def main():
    hotel_info = HotelInfo("Mumbai", "14-06-2023", "15-06-2023")
    hotels = await hotel_info.get_all_hotel_names()
    print(hotels)


asyncio.run(main())
