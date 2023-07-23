import requests
from bs4 import BeautifulSoup as bs


class Codechef:
    """
    First, create an object of class `Codechef`
    ```python
    user1 = Codechef(id="heltion")
    ```
    | Methods         | Details                                                                  |
    | --------------- | ---------------------------------------------------------------- |
    | `get_profile()` | Returns name, username, profile_image_link, rating, details etc. |
    """

    def __init__(self, id):
        self.id = id

    def get_profile(self):
        """
        Create an object of the 'Swiggy' class\n
        ```python
        user1 = Codechef(id="heltion")
        user1.get_profile()
        ```
        Response
        ```js
       {
        'name': 'Yaowei Lyu',
        'username': 'heltion', 
        'profile_image_link': 'https://cdn.codechef.com/sites/all/themes/abessive/images/user_default_thumb.jpg', 
        'rating': {
            'star': '7★', 
            'current_rating': '2555', 
            'division': '1', 
            'highest_rating': '2555', 
            'global_rank': '72', 
            'country_rank': '8'
            }, 
        'details': {
            'country_flag_link': 'https://cdn.codechef.com/download/flags/24/cn.png', 
            'country_name': 'China', 
            'user_type': 'Student', 
            'institution': 'Zhejiang University China'
            }
        }
        ```
        """
        try:
            url = f"https://www.codechef.com/users/{self.id}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            response = requests.get(url, headers=headers).text
            soup = bs(response, "lxml")

            user_details_box = soup.find("div", {"class": "user-details-container"})
            header_box = user_details_box.find("header")
            profile_image_link = header_box.find("img")["src"]
            profile_name = header_box.find("h1").text.strip()
            profile_details_box = user_details_box.find("section")
            profile_details_ul = profile_details_box.find("ul")
            profile_details_li = profile_details_ul.find_all("li")
            
            # star
            profile_star = profile_details_li[0].find("span",{"class": "rating"}).text.strip()
            # Username
            profile_username = profile_details_li[0].find("span",{"class": "m-username--link"}).text.strip()
            # Country
            country_flag_link = profile_details_li[1].find("img",{"class": "user-country-flag"})["src"]
            country_name = profile_details_li[1].find("span",{"class": "user-country-name"}).text.strip()
            # User Type
            user_type = profile_details_li[2].find("span").text.strip()
            # Institution
            institution = profile_details_li[3].find("span").text.strip()

            profile_rating_box = soup.find("aside", {"class": "sidebar small-4 columns pr0"})

            # Current Rating
            rating_box = profile_rating_box.find("div", {"class": "rating-header"})
            rating_divs = rating_box.find_all("div")
            current_rating = rating_divs[0].text.strip()
            # Division
            division = rating_divs[1].text.strip().replace("(", "").replace(")", "").replace("Div ", "")
            # Highest Rating
            highest_rating = rating_box.find("small").text.strip().replace("(Highest Rating ", "").replace(")", "")

            # Ranks
            ranks_box = profile_rating_box.find("div", {"class": "rating-ranks"})
            ranks_list = ranks_box.find_all("strong")
            global_rank = ranks_list[0].text.strip()
            country_rank = ranks_list[1].text.strip()
            
            profile_data = {
                'name': profile_name,
                'username': profile_username,
                'profile_image_link': profile_image_link,
                'rating': {
                    'star': profile_star,
                    'current_rating': current_rating,
                    'division': division,
                    'highest_rating': highest_rating,
                    'global_rank': global_rank,
                    'country_rank': country_rank
                },
                'details': {
                    'country_flag_link': country_flag_link,
                    'country_name': country_name,
                    'user_type': user_type,
                    'institution': institution
                }
            }
            return profile_data
        except:
            return None