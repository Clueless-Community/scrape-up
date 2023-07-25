from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

class IMDB:

    '''
    Create an instance of IMDB class
    ```python
    imdb = IMDB(movie_name)
    ```

    | Methods       | Details                                                 |
    | ------------- | --------------------------------------------------------|
    | `.rating()`   | Returns the IMDB rating of the movie                    |
    | `.desc()`     | Returns the description, cast and director of the movie |
    
    '''

    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.__find_url()
        self.__scrape_page()

    def __find_url(self):
        try:
            movie_search = '+'.join(self.movie_name.split())

            base_url = 'https://www.imdb.com/find/?q='
            url = base_url + movie_search + '&s=all'

            req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

            webpage = urlopen(req).read()
            page_soup = soup(webpage, "html.parser")

            movie_url = page_soup.find('a', {"ipc-metadata-list-summary-item__t"})
            self.url = 'https://www.imdb.com' + str(movie_url['href'])
        except:
            return 'No movie found'

    
    def __scrape_page(self):
        try:
            req = Request(self.url , headers={'User-Agent': 'Mozilla/5.0'})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")
            title = self.page_soup.find("title")
            self.title = title.get_text()
        except:
            return 'No movie found'

    def rating(self):
        try:
            info = self.page_soup.find("span", {'class' : "sc-bde20123-1 iZlgcd"})
            return self.title + '\n' + "IMDB rating: "+ info.get_text()
        except:
            return 'No movie found'

    def desc(self):
        try:
            des = self.page_soup.find("meta", {"name" : "description"})
            return self.title + '\n' + des['content']
        except:
            return 'No movie found'
