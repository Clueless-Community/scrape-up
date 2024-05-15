from bs4 import BeautifulSoup as bs
import requests


class Pinterest:
    """
    Create an instance of `Pinterest` class.
     ```python
     pinterest = Pinterest()
     ```
     | Methods                | Details                                                            |
    | ---------------------- | ------------------------------------------------------------------ |
    | `.get_today()`         | Returns the list of todays topics                                  |
    | `.get_photo(your url)` | Returns the link to the image (so you dont need an account)        |
    | `.search_pins(keyword)`| Search for pins containing a specific keyword on Pinterest         |
    | `.get_pin_details(pin_url)`| Fetch details about a specific pin on Pinterest                 |
    """

    def __init__(self):
        pass

    def get_today(self):
        """
        Class - `Pinterest`
        Example:
        ```python
            pinterest = Pinterest()
            today = pinterest.get_today()
        ```
        Output
        ```js
        [
            {
                "link":"/today/best/how-to-style-a-shawl-this-winter/116286/",
                "title":"How To Style A Shawl This Winter",
                "subtitle":"Perfect Winter Companion",
                "image":"https://i.pinimg.com/736x/10/46/c8/1046c8dc21138326568405a24f871e17.jpg"
            },
        ```
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
            return [
                {"link": link, "title": title, "subtitle": subtitle, "image": image}
                for (link, title, subtitle, image) in unique_items
            ]
        except:
            return None

    def get_photo(self, url):
      
      """
       Class - `Pinterest`
      Example:
     ```python
        pinterestphoto = Pinterest()
        photo = pinterestphoto.get_photo(your pinterest url)
     ```
        Returns: Photo Image URL | None
        """
      try:
        page = requests.get(url)
        soup = bs(page.content, "html.parser")
        image = soup.find("img", class_="hCL")
        print("Image tag:", image)  # Add this line
        if image:
            return {"alt": image.get("alt"), "image": image.get("src")}
        else:
            print("No image found")  # Add this line
            return None
      except Exception as e:
        print("Error:", e)
        return None
    

        
    def search_pins(self, keyword):
        """
        Search for pins containing a specific keyword on Pinterest.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            list: A list of dictionaries containing information about the matching pins.
        """
        try:
            url = f"https://www.pinterest.com/search/pins/?q={keyword}"
            page = requests.get(url)
            soup = bs(page.content, "html.parser")
            pins = []
            for item in soup.find_all("div", class_="GrowthUnauthPinImage"):
                link = item.find("a").get("href")
                image = item.find("img").get("src")
                pins.append({"link": link, "image": image})
            return pins
        except Exception as e:
            print("Error:", e)
            return None

    def get_pin_details(self, pin_url):
        """
        Fetch details about a specific pin on Pinterest.

        Args:
            pin_url (str): The URL of the Pinterest pin.

        Returns:
            dict: A dictionary containing details about the pin, such as title, description, saves, and comments.
        """
        try:
            page = requests.get(pin_url)
            soup = bs(page.content, "html.parser")
            title = soup.find("meta", property="og:title").get("content")
            description = soup.find("meta", property="og:description").get("content")
            saves = soup.find("meta", property="pinterestapp:saves").get("content")
            comments = soup.find("meta", property="pinterestapp:comments").get("content")
            return {"title": title, "description": description, "saves": saves, "comments": comments}
        except Exception as e:
            print("Error:", e)
            return None
