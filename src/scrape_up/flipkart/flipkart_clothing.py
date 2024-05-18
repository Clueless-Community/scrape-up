from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class FlipkartClothing:
    """
    Create an instance of `FlipkartTees` class.
    ```python
    cloth = FlipkartTees()
    ```
    | Methods                    | Details                                                        |
    | -------------------------- | -------------------------------------------------------------- |
    | `.scrape()`                | Returns the list of t-shirts with other relevant info          |
    | `.range()`                 | Returns the list of t-shirts between a particular price range. |
    | `.minrating()`             | Returns the list of t-shirts havinga minimum given rating.     |
    | `.gendermale()`            | Returns the list of t-shirts which are for males.              |
    | `.genderfemale()`          | Returns the list of t-shirts which are there for females.      |
    | `.size()`                  | Returns the list of tshirts havning a particular size.         |
    | `formal_shirts_for_male()` | It returns those t-shirts which are of a particular size       |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

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
            content = get(url, self.config)

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

    def tshirts_by_price_range(self, min_price, max_price):
        """
        Class - `FlipkartClothing()`
        ```python
        tees = FlipkartClothing()
        tees.tshirts_by_price_range(min_price, max_price)
        ```
        """
        try:
            min_price = int(min_price)
            max_price = int(max_price)
            if min_price == max_price:
                return "Min and max prices are the same."
            url = f"https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.price_range.from%3D{min_price}&p%5B%5D=facets.price_range.to%3D{max_price}"
            tshirts_list = self.tshirts(url)  # Assuming tshirts method is defined
            return tshirts_list
        except ValueError:
            return "Invalid price values. Please provide valid integers for min and max prices."

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

    def tshirt_by_size(self, size="M"):
        """
        It returns those t-shirts which are of a particular size\n
        Required parameter = `size` - `["XS", "S", "M", "L", "XL", "2XL", "3XL"]`\n
        Class - `FlipkartClothing()`
        ```python
        tees = FlipkartClothing()
        tees.tshirt_by_size()
        ```
        """
        try:
            m = size.upper()
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

    def formal_shirts_for_male():
        """
        It returns all the t-shirts pertaining to females\n
        Class - `FlipkartClothing()`\n
        ```python
        tees = FlipkartClothing()
        tees.formal_shirts_for_male()
        ```
        Return\n
        ```js
        [
            {
                "name":"FIBERMILL",
                "price":"₹389",
                "description":"Men Regular Fit Solid Spread Collar Formal Shirt",
                "image":"https://rukminim2.flixcart.com/image/612/612/xif0q/shirt/k/g/1/l-fbrml-r-fibermill-original-imagjfk6ytwytyg3.jpeg?q=70",
                "link":"..."
            }
            ...
        ]
        ```
        """
        try:
            url = "https://www.flipkart.com/search?q=formal+shirts+for+men&sid=clo%2Cash%2Caxc%2Cmmk%2Cbk1&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=formal+shirts+for+men%7CFormal+Shirts&requestId=2d7ee0f8-6dd3-4857-9a84-6e8b378e7767&as-backfill=on&page=1"
            k = FlipkartClothing().tshirts(url)
            return k
        except:
            return None
