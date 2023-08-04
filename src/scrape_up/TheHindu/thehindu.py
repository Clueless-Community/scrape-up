import requests
from bs4 import BeautifulSoup as bs


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

    def __init__(self):
        pass

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
            "news":"The Supreme Court on Friday appointed former Delhi High Court judge, Justice Jayant Nath, as the interim chairperson of the Delhi Electricity Regulatory Commission (DERC).The order was passed by a bench headed by Chief Justice D. Y. Chandrachud, which was told by senior advocate Abhishek Singhvi, appearing for the Delhi Government, that the apex court could pick anyone for the post.“We request Justice Jayant Nath, a former judge of the high court, to discharge the duties of the office of the chairperson, DERC,” said the bench, also comprising Justices J. B. Pardiwala and Manoj Misra.While hearing the matter on July 20, the apex court had said it would appoint a DERC chairperson for a brief period on an ad-hoc basis pending a decision on the Delhi government’s plea contesting the Lieutenant Governor’s power to make such an appointment.It had expressed anguish that nobody cares about the “headless” institution.Amid the deadlock between the Arvind Kejriwal-led Aam Aadmi Party (AAP) government and Delhi Lieutenant Governor (LG) V. K. Saxena over the appointment of DERC chairperson, the top court had said it will do some homework and appoint someone on a “pro tem basis” to the post."
        }
        ```
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            page_url = "https://www.thehindu.com/news/cities/Delhi/sc-appoints-former-delhi-hc-judge-justice-jayant-nath-as-interim-chairperson-of-power-regulator-derc/article67157713.ece"
            response = requests.get(page_url, headers = headers).text
            soup = bs(response, "lxml")
            main_content_box = soup.find("div", {"class": "articlebodycontent"})
            news_text = main_content_box.find_all("p")
            news = ""
            for p in news_text:
                if "class" not in str(p):
                    news+=p.text
            heading = soup.find("h1", {"class": "title"}).text.strip()
            sub_heading = soup.find("h3", {"class": "sub-title"}).text.strip()
            last_updated = soup.find("p", {"class": "publish-time"}).text.strip()
            news_data = {
                "title" : heading,
                "subtitle" : sub_heading,
                "last_updated" : last_updated,
                "news" : news 
            }
            return news_data
        except:
            return None
