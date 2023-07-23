import bs4
from bs4 import BeautifulSoup
import requests


class FlipkartClothing:
    """
    Create an instance of `FlipkartClothing` class\n
    ```python
    cloth = FlipkartClothing()
    ```
    \n
    | Methods               | Details                                                            |
    | --------------------- | ------------------------------------------------------------------ |
    | `.tshirts()`           | Returns the list of t-shirts with other relevant info              |
    | `.tshirts_by_price_range()`            | Returns the list of t-shirts between a particular price range.     |
    | `.tshirts_by_rating()`        | Returns the list of t-shirts havinga minimum given rating.         |
    | `.tshirts_for_male()`       | Returns the list of t-shirts which are for males.                  |
    | `.tshirts_for_female()`     | Returns the list of t-shirts which are there for females.          |
    | `.tshirt_by_size()`             | Returns the list of tshirts havning a particular size.|
    """

    def __init__(self):
        pass

    def tshirts(
        self,
        url="https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9",
    ):
        """
        It returns the t-shirt data of products from flipkart\n
        Class - `FlipkartClothing()`
        ```python
        clothes = FlipkartClothing()
        clothes.tshirts()
        ```
        """
        obj_keys = ["name", "price", "description", "image", "link"]
        try:
            content = requests.get(url)

            soup = BeautifulSoup(content.content, "html.parser")

            imgs = soup.find_all("img", attrs={"class": "_2r_T1I"})
            names = soup.find_all("div", attrs={"class": "_2WkVRV"})
            prices = soup.find_all("div", attrs={"class": "_30jeq3"})
            desc = soup.find_all("a", attrs={"class": "IRpwTa"})

            res = []
            startlink = "https://www.flipkart.com"

            for i in range(len(imgs)):
                nm = desc[i].attrs["href"]
                name = names[i].text
                img = imgs[i].attrs["src"]
                des = desc[i].text
                price = prices[i].text

                obj_values = [name, price, des, img, startlink + nm]

                res.append(dict(zip(obj_keys, obj_values)))
            return res
        except:
            return None

    def tshirts_by_price_range(self, min, max):
        """
        It returns the t-shirts in a particular price bracket(min-max). The information regarding parameters is as follows:\n
        - min: Bottom range of price\n
        - max: Max range of price\n
        Class - `FlipkartClothing()`
        ```python
        clothes = FlipkartClothing()
        clothes.tshirts_by_price_range(min=500,max=2000)
        ```
        """
        try:
            max = int(max)
            min = int(min)
            if min == max:
                return None
            url = "https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.price_range.from%3D{}&p%5B%5D=facets.price_range.to%3D{}".format(
                min, max
            )
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None

    def tshirts_by_rating(self, rating):
        """
        It returns the t-shirts having the user rating greater than or equal to the minimum passed rating(r)\n
        - range: minimum rating\n
        Class - `FlipkartClothing()`
        ```python
        tees = FlipkartClothing()
        tees.tshirts_by_rating(rating=4.1)
        ```
        """
        r = rating
        try:
            if int(r) < 1 and int(r) >= 5:
                return None
            url = "https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.rating%255B%255D%3D{}%25E2%2598%2585%2B%2526%2Babove".format(
                int(r)
            )
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None

    def tshirts_for_male(self):
        """
        It returns all the t-shirts pertaining to males\n
        Class - `FlipkartClothing()`\n
        ```python
        tees = FlipkartClothing()
        tees.tshirts_for_male()
        ```
        """
        try:
            url = "https://www.flipkart.com/clothing-and-accessories/topwear/tshirts/mens-tshirts/pr?sid=clo,ash,ank,edy&q=tshirt&otracker=categorytree"
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None

    def tshirts_for_female(self):
        """
        It returns all the t-shirts pertaining to females\n
        Class - `FlipkartClothing()`\n
        ```python
        tees = FlipkartClothing()
        tees.tshirts_for_female()
        ```
        """
        try:
            url = "https://www.flipkart.com/clothing-and-accessories/topwear/tshirts/womens-tshirts/pr?sid=clo,ash,ank,loi&q=tshirt&otracker=categorytree"
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None

    def tshirt_by_size(self, m):
        """
        It returns those t-shirts which are of a particular size\n
        Class - `FlipkartClothing()`\n
        ```python
        tees = FlipkartClothing()
        tees.tshirts_for_female()
        ```
        """
        try:
            m = m.upper()
            curavl = ["XS", "S", "M", "L", "XL", "2XL", "3XL"]
            if m not in curavl:
                return None
            url = "https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.size%255B%255D%3D{}".format(
                m
            )
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None
        
    def Formal_shirts_for_male():
        """
        It returns all the t-shirts pertaining to females\n
        Class - `FlipkartClothing()`\n
        ```python
        tees = FlipkartClothing()
        tees.tshirts_for_female()
        ```
        """
        try:
            url = "https://www.flipkart.com/search?q=formal+shirts+for+men&sid=clo%2Cash%2Caxc%2Cmmk%2Cbk1&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=formal+shirts+for+men%7CFormal+Shirts&requestId=2d7ee0f8-6dd3-4857-9a84-6e8b378e7767&as-backfill=on&page=1"
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None

    
a=FlipkartClothing.Formal_shirts_for_male()
print(a)