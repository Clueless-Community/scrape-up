from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class YahooFinance:
    """
    Yahoo Finance\n
    Create an instance of `YahooFinance` class.\n
    ```python
    yf = YahooFinance()
    ```
    | Methods       | Details                             |
    | ------------- | ----------------------------------- |
    | `.headline()` | Fetches headlines from yahooFinance |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        url = "https://finance.yahoo.com/?fr=sycsrp_catchall"
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)
        html_text = get(url, self.config).text
        soup = BeautifulSoup(html_text, "lxml")

        self.container = soup.find("div", {"id": "Main"})

    def headline(self):
        """
        Get Yahoo Finance headlines.\n
        This method scrapes the headlines and links from the main page of Yahoo Finance.\n
        Example:
        ```python
        yf = YahooFinance()
        headlines_data = yf.headline()
        print(headlines_data)
        ```
        Returns:
        ```js
        [
            {
                "Headline":"Consumer confidence rises to a two-year high",
                "Link":"https://finance.yahoo.com/news/consumer-confidence-hits-highest-level-in-two-years-155813210.html"
            }
            ...
        ]
        ```
        """
        try:
            news = []
            headlines = self.container.find(
                "div", {"id": "mrt-node-Col1-0-ThreeAmigos"}
            ).find(
                "div",
                {
                    "class": "W(100%) Maw(900px) Pos(r) Cf Wow(bw) Mb(30px) Mb(20px)--md1100"
                },
            )
            title = headlines.find("h2").text
            link = headlines.find(
                "a", {"class": "js-content-viewer wafer-caas Td(n)"}, href=True
            )["href"]
            data = {"Headline": title, "Link": link}
            news.append(data)
            for item in headlines.find_all("li"):
                title = item.find("h3").text
                link = item.find(
                    "a",
                    {"class": "js-content-viewer wafer-caas Fw(b) Td(n)"},
                    href=True,
                )["href"]
                data = {"Headline": title, "Link": link}
                news.append(data)

            major_news_1 = self.container.find(
                "div",
                {
                    "class": "W(100%) Maw(900px) Pos(r) Cf Wow(bw) article-cluster-boundary Mb(30px) Mb(20px)--md1100"
                },
            )
            for item in major_news_1.find_all("li"):
                title = item.find("h3").text
                link = item.find(
                    "a", {"class": "js-content-viewer wafer-caas Td(n)"}, href=True
                )["href"]
                data = {"Headline": title, "Link": link}
                news.append(data)

            major_news_2 = major_news_1.next_sibling
            for item in major_news_2.find_all("li"):
                title = item.find("h3").text
                link = item.find(
                    "a",
                    {"class": "js-content-viewer wafer-caas Fw(b) Td(n)"},
                    href=True,
                )["href"]
                data = {"Headline": title, "Link": link}
                news.append(data)
            return news
        except Exception as e:
            return None


if __name__ == "__main__":
    yf = YahooFinance()
    print(yf.headline())
