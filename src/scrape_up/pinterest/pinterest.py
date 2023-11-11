from bs4 import BeautifulSoup as bs 
import requests

class Pinterest():

    """
        Create an instance of `Flipkart` class.
        ```python
        pin = Pinterest()
        ```
        | Methods                | Details                                                            |
        | ---------------------- | ------------------------------------------------------------------ |
        | `.get_today()`         | Returns the list of todays topics                                  |
        | `.get_photo(your url)` | Returns the link to the image (so you dont need an account)        |
    """
    def __init__(self):
        pass

    def get_today(self):
        """
            Class - `Pinterest`
            Example - 
                pinterest = Pinterest()
                pinterest.get_today()
        """
        try:
            page = requests.get("https://www.pinterest.com/today/")
            soup = bs(page.content, "html.parser")
            unique_items = set()

            for item in soup.findAll("div", class_="zI7"):
                link = item.find("a", class_="Wk9")
                title = item.find("h1", class_="lH1")
                subtitle = item.find("div", class_="tBJ")
                image = item.find("img", class_="hCL")

                link = link.get("href") if link and "href" in link.attrs else None
                title = title.get_text() if title else None
                subtitle = subtitle.get_text() if subtitle else None
                image = image.get("src") if image and "src" in image.attrs else None
                item_tuple = (link, title, subtitle, image)
                if all([link, title, subtitle, image]):
                    if item_tuple not in unique_items:
                        unique_items.add(item_tuple)
            return [{'link': link, 'title': title, 'subtitle': subtitle, 'image': image} for (link, title, subtitle, image) in unique_items]
        except:
            return None
    
    def get_photo(self, url):
        """
            Class - `Pinterest`
            Example - 
                pinterestphoto = Pinterest()
                pinterestphoto.get_photo(your pinterest url)
        """
        try:
            page = requests.get(url)
            soup = bs(page.content, "html.parser")
            image = soup.find("img", class_="hCL")
            return {"alt": image.get("alt"), "image": image.get("src")}
        except:
            return None
        