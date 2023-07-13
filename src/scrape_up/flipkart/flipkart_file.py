import bs4
from bs4 import BeautifulSoup as bs
import requests


class Flipkart:
    """
    Create an instance of `Flipkart` class\n
    ```python
    item = Flipkart()
    ```
    | Methods               | Details                                                            |
    | --------------------- | ------------------------------------------------------------------ |
    | `.TVs()`              | Returns the list of TV sets on flipkart                            |
    | `.bestseller_books()` | Returns the list of bestselling books data listed on Flipkart.     |
    | `.mobiles()`          | Returns the list of mobile phones under 50K along with their data. |
    | `.sport_shoes()`      | Returns the list of trendong sport shoes data.                     |
    | `.laptops()`          | Returns the list of laptop from flipkart.                          |
    | `.headphones()`          | Returns the list of headphones from flipkart.|
    """

    def __init__(self):
        pass

    def tvs(self):
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.tvs()
            """

            link = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_3pLy-c row"):
                names = data.find("div", attrs={"class": "_4rR01T"})
                price = data.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
                rating = data.find("div", attrs={"class": "_3LWZlK"})
                specification = data.find("div", attrs={"class": "fMghEO"})

                specs = []
                for spec in specification.find_all("li", attrs={"class": "rgWa7D"}):
                    specs.append(spec.text)

                item_details = {
                    "Item_Name": names.text,
                    "Price": price.text,
                    "Rating": rating.text,
                    "Specifications": ", ".join(specs),
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None

    def bestseller_books(self):
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.bestseller_books()
            """

            link = "https://www.flipkart.com/search?q=bestsellers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_4ddWXP"):
                names = data.find("a", attrs={"class": "s1Q9rs"})
                price = data.find("div", attrs={"class": "_30jeq3"})
                rating = data.find("div", attrs={"class": "_3LWZlK"})
                specification = data.find("div", attrs={"class": "_3Djpdu"})

                item_details = {
                    "Item_Name": names.text,
                    "Price": price.text,
                    "Rating": rating.text if rating else None,
                    "Specifications": specification.text if specification else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None

    def mobiles(self):
        try:
            """
            Get the list of mobiles under 50K\n
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.mobiles()
            """

            link = "https://www.flipkart.com/search?q=MOBILE+PHONE+UNDER+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=3"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE"):
                names = data.find("a", class_="_1fQZEK")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="_3LWZlK")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None

    def sport_shoes(self):
        try:
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.BestsellersBooks()
            item.sport_shoes()
            """
            all_items = []
            url = "https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp,cil,1cu&otracker=nmenu_sub_Men_0_Sports%20Shoes"
            response = requests.get(url)
            html_content = response.content
            soup = bs(html_content, "html.parser")

            all_items = []

            div_elements = soup.find_all("div", class_="_1xHGtK _373qXS")

            for div in div_elements:
                name_element = div.find("a", class_="IRpwTa")
                name = name_element.text.strip() if name_element else ""

                image_element = div.find("img", class_="_2r_T1I")
                image_url = image_element["src"] if image_element else ""

                details_element = div.find("a", class_="_3bPFwb")
                details = details_element.text.strip() if details_element else ""

                item_details = {
                    "Name": name,
                    "Image URL": image_url,
                    "Details": details,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            print("Error:", str(e))
            return None

    def laptops(self):
        try:
            """
            Get the list of mobiles under 50K\n
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.mobiles()
            """

            link = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("div", class_="_4rR01T")
                price = data.find("div", class_="_30jeq3 _1_WHN1")
                description = data.find("ul", class_="_1xgFaf")
                review = data.find("div", class_="_3LWZlK")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None

    def headphones():
        """
        Class - `Flipkart`\n
        ```python
        item = Flipkart()
        item.headphones()
        """
        try:
            link = "https://www.flipkart.com/search?q=headphones+bluetooth&sid=0pm%2Cfcn%2Cgc3%2Cka8&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=headphones+bluetooth%7CWireless+Headphones&requestId=beefc9a9-55a8-4b64-b510-b9bc44ae6680&as-backfill=on&page=1"
            page = requests.get(link)
            soup = bs(page.content, "html.parser")

            all_items = []

            for data in soup.findAll("div", class_="_1AtVbE col-12-12"):
                names = data.find("a", class_="s1Q9rs")
                price = data.find("div", class_="_30jeq3")
                description = data.find("div", class_="_3xFhiH")
                review = data.find("div", class_="_3LWZlK")

                item_details = {
                    "Item_Name": names.text if names else None,
                    "Price": price.text if price else None,
                    "Description": description.text if description else None,
                    "Review": review.text if review else None,
                }

                all_items.append(item_details)

            return all_items

        except Exception as e:
            return None



"""
        Create an instance of `FlipkartTees` class.

    ```python
    cloth = FlipkartTees()
    ```

    | Methods               | Details                                                            |
    | --------------------- | ------------------------------------------------------------------ |
    | `.scrape()`           | Returns the list of t-shirts with other relevant info              |
    | `.range()`            | Returns the list of t-shirts between a particular price range.     |
    | `.minrating()`        | Returns the list of t-shirts havinga minimum given rating.         |
    | `.gendermale()`       | Returns the list of t-shirts which are for males.                  |
    | `.genderfemale()`     | Returns the list of t-shirts which are there for females.          |
    | `.size()`             | Returns the list of tshirts havning a particular size.             |

    """



class FlipkartTees:
  """This class returns the t-shirt query elements from flipkart web"""

  def __init__(self):
        print(self)


  def scrape(self, url = 'https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9'):
    
    """It returns the t-shirt data of products from flipkart"""
    try:

      content = requests.get(url)

      soup = BeautifulSoup(content.content, 'html.parser')

      titl = soup.title

      imgs = soup.find_all('img', attrs={'class':'_2r_T1I'})
      names = soup.find_all('div',attrs={'class':'_2WkVRV'})
      prices = soup.find_all('div',attrs={'class':'_30jeq3'})
      desc = soup.find_all('a',attrs={'class':'IRpwTa'})

      res = []
      startlink = 'https://www.flipkart.com'

      for i in range(len(imgs)):

        nm = desc[i].attrs['href']
        name = names[i].text
        img = imgs[i].attrs['src']
        des = desc[i].text
        price = prices[i].text

        res.append([name,price,des,img,startlink+nm])
      return res
    except:
      return None  


  def range(self, min, max):

    """It returns the t-shirts in a particular price bracket(min-max). The information regarding parameters is as follows:\n
    - min: Bottom range of price\n
    - max: Max range of price """ 
    try:

      max = int(max)
      min = int(min)
      if min == max:
        return None
      url = 'https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.price_range.from%3D{}&p%5B%5D=facets.price_range.to%3D{}'.format(min,max)
      k = FlipkartTees().scrape(url)
      return k
    except:
      return None  

  def minrating(self,r):

    """It returns the t-shirts having the user rating greater than or equal to the minimum passed rating(r)"""
    try:

      if int(r)<1 and int(r)>=5:
        return None
      url = 'https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.rating%255B%255D%3D{}%25E2%2598%2585%2B%2526%2Babove'.format(int(r))
      k = FlipkartTees().scrape(url)
      return k
    except:
      return None  

  def gendermale(self):
    
    """It returns all the t-shirts pertaining to males"""
    try:

      url = 'https://www.flipkart.com/clothing-and-accessories/topwear/tshirts/mens-tshirts/pr?sid=clo,ash,ank,edy&q=tshirt&otracker=categorytree'
      k = FlipkartTees().scrape(url)
      return k
    except:
      return None  


  def genderfemale(self):
    """It returns all the t-shirts pertaining to females"""
    try:

      url = 'https://www.flipkart.com/clothing-and-accessories/topwear/tshirts/womens-tshirts/pr?sid=clo,ash,ank,loi&q=tshirt&otracker=categorytree'
      k = FlipkartTees().scrape(url)
      return k
    except:
      return None

  def size(self, m):
    """It returns those t-shirts which are of a particular size"""
    try:

      m = m.upper()
      curavl = ['XS,S,M,L,XL,2XL,3XL']
      if m not in curval:
        return None
      url = 'https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.size%255B%255D%3D{}'.format(m)
      k = FlipkartTees().scrape(url)
      return k
    except:
        return None
            
