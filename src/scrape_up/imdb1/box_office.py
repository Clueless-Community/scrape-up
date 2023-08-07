from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class BoxOffice:

    """
    Create an instance of `BoxOffice` class.
    ```python
    boxoffice = BoxOffice()
    ```
    | Methods            | Details                                                                       |
    | -------------------|-------------------------------------------------------------------------------|
    | `.top_movies()`    | Returns the top box office movies, weekend and total gross and weeks released |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
        try:
            url = "https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def top_movies(self):

        """
        Create an instance of `BoxOffice` class

        ```python
        boxoffice = BoxOffice()
        boxoffice.top_movies()
        ```

        Return\n
        ```js
        [
            {
                "Movie Name": "Barbie", 
                "Weekend Gross": "$53M", 
                "Total Gross": "$459M", 
                "Weeks released": "3"
            }, 
            {
                "Movie Name": "The Meg 2: The Trench", 
                "Weekend Gross": "$30M", 
                "Total Gross": "$30M", 
                "Weeks released": "1"
            }, 
            {
                "Movie Name": "Oppenheimer", 
                "Weekend Gross": "$29M", 
                "Total Gross": "$229M", 
                "Weeks released": "3"
            }, 
            {
                "Movie Name": "Teenage Mutant Ninja Turtles: Mutant Mayhem", 
                "Weekend Gross": "$28M", 
                "Total Gross": "$43M", 
                "Weeks released": "1"
            }, 
            {
                "Movie Name": "The Haunted Mansion", 
                "Weekend Gross": "$9M", 
                "Total Gross": "$42M", 
                "Weeks released": "2"
            }, 
            {
                "Movie Name": "Sound of Freedom", 
                "Weekend Gross": "$7M", 
                "Total Gross": "$163M", 
                "Weeks released": "5"
            }, 
            {
                "Movie Name": "Mission: Impossible - Dead Reckoning Part One", 
                "Weekend Gross": "$6.5M", "
                Total Gross": "$151M", 
                "Weeks released": "4"
            }, 
            {
                "Movie Name": "Talk to Me", 
                "Weekend Gross": "$6.3M", 
                "Total Gross": "$22M", 
                "Weeks released": "2"
            }, 
            {
                "Movie Name": "Indiana Jones and the Dial of Destiny", 
                "Weekend Gross": "$1.5M", 
                "Total Gross": "$171M", 
                "Weeks released": "6"
            }, 
            {
                "Movie Name": "Elemental", 
                "Weekend Gross": "$1.2M", 
                "Total Gross": "$148M", 
                "Weeks released": "8"
            }
        ]
        
        ```
        """
        try:

            x = self.page_soup.find_all("h3",{"class":"ipc-title__text"})
            x = x[1:11]
            movie_names = []

            for y in x:
                movie_names.append(" ".join(y.get_text().split()[1:]))

            x = self.page_soup.find_all("li", {"class":"sc-ee64acb1-1 lkUVhM"})
            x = [y.get_text() for y in x]

            lis = []

            for y in range(0, len(x), 3):
                dic = {}
                dic["Movie Name"] = movie_names[y//3]
                dic["Weekend Gross"] = x[y].split()[2]
                dic["Total Gross"] = x[y + 1].split()[2]
                dic["Weeks released"] = x[y+ 2].split()[2]
                lis.append(dic)

            return lis
        
        except:
            return None
