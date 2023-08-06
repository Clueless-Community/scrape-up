from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


class DayInHistory:

    """
    Create an instance of `DayInHistory` class.
    
    ```python
    dayinhistory = DayInHistory()

    ```
    | Methods              | Details                                          |
    | ---------------------|--------------------------------------------------|
    | `.important_events()`| Returns the timezones of cites around the world  |
    | `.holidays()`        | Returns the holidays on the specific day         |
    | `.births()`          | Returns the important birthdays on that day      |
    | `.deaths()`          | Returns the important deaths on that day         |

    """

    def __init__(self):
        self.__scrape_page()

    def __scrape_page(self):
    
        try:
            url = "https://www.timeanddate.com/on-this-day/"
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            webpage = urlopen(req).read()
            self.page_soup = soup(webpage, "html.parser")

        except:
            return None

    def important_events(self):

        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.important_events()
        ```

        Return\n
        ```js
        {
            "2008 Coup in Mauritania": "In the 6th coup in the North African country since 1978,
                            President Sidi Ould Cheikh Abdallahi was overthrown and General Mohamed 
                            Ould Abdel Aziz, a career military officer, was installed in his place.",
            "1965  Voting Rights Act Becomes Law in the United States": " President Lyndon B. Johnson 
                            signed the act, which prohibited any discrimination in voting. The act 
                            enforces the 14th and 15th amendments to the US Constitution. ",
            "1962 Jamaican Independence": "The Caribbean island country was first colonized by the 
                            Spanish in the early 16th century. In 1655, the British invaded Spanish 
                            Jamaica and made it a colony after the Spanish surrendered. Jamaica soon 
                            became one of the most profitable colonies of the British Empire, especially
                            after sugarcane was brought to the island by the English. The Jamaica Independence 
                            Act of July 1962, which was a result of anti-colonial sentiments that were spreading
                            throughout the globe, gave Jamaica full independence by leaving the Federation of the 
                            West Indies.",
            "1945 US Bombs Hiroshima": "In the first of the only two times nuclear weapons have been used in warfare, 
                            the United States dropped a nuclear bomb, nicknamed Little Boy on the industrial city
                            of Hiroshima in Japan. Over 150,000 people were estimated killed by the resulting 
                            explosion. Japan had joined the Second World War in December 1941 on the side of the
                            Axis powers. After the Hiroshima and Nagasaki bombings 3 days later on August 9,
                            Japan surrendered to the Allies and ended the Pacific War.", 
            "1926 First Woman to Swim Across the English Channel": "Gertrude Ederle, an American Olympic
                            swimmer swam across the English channel  a body of water between England and
                            France, in 14 hours and 34 minutes. Only 5 other people, all men, had swum 
                            across the channel before Ederle. "
        }
        ```
        """

        try:

            x = self.page_soup.find("ul", {"class":"list--big"})
            x = x.get_text().split("\n")
            x = x[1:-1]
            history_dic = {}

            for i in range(0, len(x), 3):
                history_dic[x[i]] = x[i + 1]
            
            return history_dic

        except:
            return None
    
    def holidays(self):

        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.holidays()
        ```

        Return\n
        ```js
        {
            "American Family Day": "USA",
            "Celebrations of San Salvador": "El Salvador",
            "Friendship Day": "India",
            "Hiroshima Memorial Day": "Japan",
            "Independence Day": "Bolivia, Jamaica"
        }
        ```
        """

        try:

            x = self.page_soup.find("div", {"class" : "sidebar-holidays"})
            x = x.get_text().split("\n")[5 : -1]
            x = [[z.strip() for z in y.split("-")] for y in x]

            return dict(zip([y[0] for y in x], [y[1] for y in x]))
        
        except:
            return None


    def births(self):

        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.births()
        ```

        Return\n
        ```js
        {
            "1983 Robin van Persie": "Dutch footballer",
            "1928 Andy Warhol": "American artist",
            "1911 Lucille Ball": "American actress",
            "1881 Alexander Fleming": "Scottish scientist, Nobel Prize laureate",
            "1809 Alfred, Lord Tennyson": "English poet"
        }
        ```
        """

        try:
            x = self.page_soup.find("div", {"class" : "otd-life__block"})

            births_dic = {}

            for y in x.find_all("li"):
                z = y.get_text().strip("\n").split("\n")

                if(len(z) == 2):
                    births_dic[z[0]] = z[1]
                else:
                    births_dic[z[0]] = ""

            return births_dic
        
        except:
            return None
        

    def deaths(self):

        """
        Create an instance of `DayInHistory` class.\n

        ```python
        dayinhistory = DayInHistory()
        dayinhistory.deaths()
        ```

        Return\n
        ```js
        {
            "1978 Pope Paul VI": "",
            "1973 Fulgencio Batista": "Cuban army officer, politician, 9th President of Cuba",
            "1969 Theodor W. Adorno": "German sociologist, philosopher",
            "1931 Bix Beiderbecke": "American pianist, composer",
            "1637 Ben Jonson": "English writer"
        }
        ```
        """

        try:
            x = self.page_soup.find_all("div", {"class" : "otd-life__block"})
            x = x[1]

            deaths_dic = {}
            for y in x.find_all("li"):
                z = y.get_text().strip("\n").split("\n")
                if(len(z) == 2):
                    deaths_dic[z[0]] = z[1]
                else:
                    deaths_dic[z[0]] = ""
            
            return deaths_dic

        except:
            return None
