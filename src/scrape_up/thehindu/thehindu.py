from bs4 import BeautifulSoup as bs

from scrape_up.config.request_config import RequestConfig, get


class TheHindu:
    """
    Create an object of the 'TheHindu' class\n
    ```python
    scraper = TheHindu()
    ```
    | Methods               | Details                                                                   |
    | --------------------- | ------------------------------------------------------------------------- |
    | `.get_news(page_url)` |  gets heading, subheading, time, and news content                         |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_news(self, page_url):
        """
        Create an object of the 'TheHindu' class\n
        ```python
        scraper = TheHindu()
        scraper.get_news(page_url="https://www.thehindu.com/news/cities/Delhi/sc-appoints-former-delhi-hc-judge-justice-jayant-nath-as-interim-chairperson-of-power-regulator-derc/article67157713.ece")
        ```
        Response
        ```js
        {
            "title":"SC appoints former Delhi HC judge Justice Jayant Nath as interim chairperson of power regulator DERC",
            "subtitle":"The office of the DERC chairperson has been vacant for over six months",
            "last_updated":"August 04, 2023 02:59 pm | Updated 03:11 pm IST - New Delhi",
            "news":"The Supreme Court on Friday appointed former Delhi High Court judge, ..."
        }
        ```
        """
        try:
            page_url = "https://www.thehindu.com/news/cities/Delhi/sc-appoints-former-delhi-hc-judge-justice-jayant-nath-as-interim-chairperson-of-power-regulator-derc/article67157713.ece"
            response = get(page_url, self.config).text
            soup = bs(response, "lxml")
            main_content_box = soup.find("div", {"class": "articlebodycontent"})
            news_text = main_content_box.find_all("p")
            news = ""
            for p in news_text:
                if "class" not in str(p):
                    news += p.text
            heading = soup.find("h1", {"class": "title"}).text.strip()
            sub_heading = soup.find("h3", {"class": "sub-title"}).text.strip()
            last_updated = soup.find("p", {"class": "publish-time"}).text.strip()
            news_data = {
                "title": heading,
                "subtitle": sub_heading,
                "last_updated": last_updated,
                "news": news,
            }
            return news_data
        except:
            return None
