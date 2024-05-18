from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class MediEncyclopedia:
    """
    Create an instance of `MediEncyclopedia` class.
    ```python
    ency = MediEncyclopedia()
    ```
    | Methods               | Details                                                                                      |
    | --------------------- | -------------------------------------------------------------------------------------------- |
    | `.scrapebyurl()`      | Returns the medical dictation of associated topic url                                        |
    | `.query()`            | It takes a user query parameter as an argument and returns all relevant terms related to it. |
    | `.byletter()`         | Returns the list of medical relics starting with a particular letter                         |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def scrapebyurl(self, url: str):
        """
        Class - `MediEncyclopedia`
        Example:
        ```
        ency = MediEncyclopedia()
        ency.scrapebyurl('url goes here')
        ```
        Returns:
        ```js
        {
            "headline": The name of the encyclopedia entry
            "text": Link to the entry
        }
        ```
        """

        try:
            content = get(url, self.config)
            soup = BeautifulSoup(content.content, "html.parser")
            headline = soup.find("h1", attrs={"class": "with-also"}).text
            article = soup.find("article")
            for script in article(["script", "style"]):
                script.extract()
            text = (
                article.get_text()
                .replace("Browse the Encyclopedia", "")
                .replace("Clinical Trials", "")
            )
            text = text.replace(
                "To use the sharing features on this page, please enable JavaScript.",
                "",
            )

            return [headline, text]
        except:
            return None

    def query(self, userquery: str):
        """
        Class - `MediEncyclopedia`
        Example:
        ```
        ency = MediEncyclopedia()
        ency.query(userquery='query goes here')
        ```
        Returns:
        ```js
        {
            "headline": The name of the encyclopedia entry
            "text": Link to the entry
        }
        ```
        """
        try:
            fl = userquery[0].upper()
            resq = []
            vals = MediEncyclopedia().byletter(fl)
            ls = userquery.split(" ")
            for i in ls:
                for j in vals:
                    if i in j[0]:
                        resq.append(j)
            resq = list(resq)
            return resq
        except:
            return None

    def byletter(self, character: str):
        """
        Class - `MediEncyclopedia`
        Example:
        ```
        ency = MediEncyclopedia()
        ency.byletter(character='single english character goes here')
        ```
        Returns:
        ```js
        {
            "headline": The name of the encyclopedia entry
            "text": Link to the entry
        }
        ```
        """
        try:
            character = character.upper()
            chk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if character not in chk:
                return None
            url = f"https://medlineplus.gov/ency/encyclopedia_{character}.htm"
            content = get(url, self.config)
            base = "https://medlineplus.gov/ency/"
            soup = BeautifulSoup(content.content, "html.parser")
            vals = []
            heads = soup.find_all("li")
            allheads = heads[42 : len(heads) - 16]
            for i in allheads:
                t = base + i.find("a")["href"]
                h = i.find("a").text
                vals.append([h, t])

            return vals
        except:
            return None
