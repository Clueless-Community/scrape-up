import bs4
from bs4 import BeautifulSoup
import requests

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
      curavl = ['XS','S','M','L','XL','2XL','3XL']
      if m not in curavl:
        return None
      url = 'https://www.flipkart.com/search?q=tshirt&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fbbac901-d12f-4dc5-9a8c-b034cde11af9&p%5B%5D=facets.size%255B%255D%3D{}'.format(m)
      k = FlipkartTees().scrape(url)
      return k
    except:
        return None
