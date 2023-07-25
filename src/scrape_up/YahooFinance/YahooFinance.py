from bs4 import BeautifulSoup
import requests

class YahooFinance():
    def __init__(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"}
        url = "https://finance.yahoo.com/?fr=sycsrp_catchall"
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, "lxml")

        self.container = soup.find("div",{"id":"Main"})


    def headline(self):
        """
        Get Yahoo Finance headlines.

        This method scrapes the headlines and links from the main page of Yahoo Finance.

        Example:
        ```python
        yf = YahooFinance()
        headlines_data = yf.headline()
        print(headlines_data)
        ```

        Returns:
        A dictionary containing the list of headlines and their corresponding links.
        Each dictionary in the list contains the following keys:
        - "Headline": The headline title.
        - "Link": The link to the corresponding news article.
        """
        try:
            news = []
            headlines = self.container.find("div",{"id":"mrt-node-Col1-0-ThreeAmigos"}).find("div",{"class":"W(100%) Maw(900px) Pos(r) Cf Wow(bw) Mb(30px) Mb(20px)--md1100"})
            title = headlines.find("h2").text
            link = headlines.find("a",{"class":"js-content-viewer wafer-caas Td(n)"},href=True)['href']
            data = {
                "Headline":title,
                "Link":link
            }
            news.append(data)
            for item in headlines.find_all("li"):
                title = item.find("h3").text
                link = item.find("a",{"class":"js-content-viewer wafer-caas Fw(b) Td(n)"},href=True)['href']
                data = {
                    "Headline": title,
                    "Link": link
                }
                news.append(data)

            major_news_1 = self.container.find("div",{"class":"W(100%) Maw(900px) Pos(r) Cf Wow(bw) article-cluster-boundary Mb(30px) Mb(20px)--md1100"})
            for item in major_news_1.find_all("li"):
                title = item.find("h3").text
                link = item.find("a",{"class":"js-content-viewer wafer-caas Td(n)"},href=True)['href']
                data = {
                    "Headline": title,
                    "Link": link
                }
                news.append(data)

            major_news_2 = major_news_1.next_sibling
            for item in major_news_2.find_all("li"):
                title = item.find("h3").text
                link = item.find("a",{"class":"js-content-viewer wafer-caas Fw(b) Td(n)"},href=True)['href']
                data = {
                    "Headline": title,
                    "Link": link
                }
                news.append(data)
            return {"data":news,"message":"Headlines are now scraped"}
        except Exception as e:
            return {"data": None, "message": f"An error occurred: {str(e)}"}




