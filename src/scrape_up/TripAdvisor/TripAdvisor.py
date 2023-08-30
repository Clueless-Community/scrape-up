from bs4 import BeautifulSoup
import requests
USER_AGENT = "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"

class TripAdvisor:
    """
    First, create an object of class `TripAdvisor`
    
    ```python
    hotel = TripAdvisor()
    ```
    
    | Methods                  | Details                                              |
    | ------------------------ | ---------------------------------------------------- |
    | `get_details(hotel_url)` | Get the details of a hotel from its TripAdvisor URL. |
    """

    def __init__(self):
        self.headers = {
            "User-Agent": USER_AGENT
        }

    def get_details(self, hotel_url):
        """
        Get the details of a hotel from its TripAdvisor URL.\n
        Parameters:- `hotel_url (str)`: The URL of the hotel on TripAdvisor.
        ```python
        hotel = TripAdvisor()
        hotel.get_details()
        ```
        Returns:
        ```js
        {
            "Rating": "The hotel's rating",
            "Experience": "The hotel's experience summary",
            "Reviews": "The number of reviews for the hotel",
            "Award": "The award received by the hotel, or None if not available",
            "Description": "The description of the hotel as a BeautifulSoup Tag",
            "Amenities": "List of amenities offered by the hotel"
        }
        ```
        """
        try:
            url = hotel_url
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            container = soup.find("div", {"class": "ppuFV _T Z BB"})

            rating = container.find("span", {"class": "uwJeR P"}).text
            experience = container.find("div", {"class": "kkzVG"}).text
            reviews = container.find("span", {"class": "hkxYU q Wi z Wc"}).text
            award = container.find("div", {"class": "bhYSr P"})
            if award:
                award = award.text
            else:
                award = None
            description = container.find("div", {"class": "fIrGe _T"}).text
            pa = container.find("div", {"class": "OsCbb K"})
            amineties = []
            for items in pa.find_all("div", {"class": "yplav f ME H3 _c"}):
                amineties.append(items.text)

            data = {
                "Rating": rating,
                "Experience": experience,
                "Reviews": reviews,
                "Award": award,
                "Description": description,
                "Amenities": amineties,
            }
            return data
        except:
            return None
