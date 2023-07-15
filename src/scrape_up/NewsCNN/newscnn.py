import bs4
from bs4 import BeautifulSoup
import requests


class NewsCNN:
    """
    Create an instance of `NewsCNN` class.\n
    ```python
    news = newsCNN()
    ```
    | Methods               | Details                                                            |
    | `.newsbylocation(country="india)`   | Returns the list of articles by a specific country.               |
    """

    def __init__(self):
        pass

    def news_by_location(self, country:str):
        """
        Returns the relevant news articles corresponding to that particular geo-continent or country\n
        Class - `NewsCNN`
        Parameters: \n
        - country: Name of the country\n
        ```python
        news = newsCNN()
        news.news_by_location()
        ```
        """
        
        try:
            sol = []
            obj_keys = ['news','link']
            location = country.lower()
            URL = f"https://edition.cnn.com/world/{location}"
            page = requests.get(URL)
            parse = BeautifulSoup(page.content, "html.parser")
            heads = parse.find_all("span", attrs={"data-editable": "headline"})
            links1 = parse.find_all(
                "a",
                attrs={
                    "class": "container__link container_lead-plus-headlines-with-images__link"
                },
            )
            links2 = parse.find_all(
                "a", attrs={"class": "container__link container_vertical-strip__link"}
            )
            links3 = parse.find_all(
                "a",
                attrs={"class": "container__link container_lead-plus-headlines__link"},
            )

            base = "https://edition.cnn.com/"
            allurls = []
            allheads = []

            for i in heads:
                tmp = i.text
                allheads.append(tmp)

            for i in links1 + links2 + links3:
                t = base + i["href"]
                allurls.append(t)
            allurls = list(set(allurls))

            for i in range(len(allurls)):
                obj_values = [allheads[i], allurls[i]]
                new_obj = dict(zip(obj_keys, obj_values))
                sol.append(new_obj)

            return sol
        except:
            return None


news = NewsCNN()
print(news.news_by_location(country="usa"))
