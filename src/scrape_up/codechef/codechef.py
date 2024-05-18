import requests
from bs4 import BeautifulSoup as bs

from scrape_up.config.request_config import RequestConfig, get


class User:
    """
    First, create an object of class `User`
    ```python
    user1 = User(id="heltion")
    ```
    | Methods         | Details                                                                   |
    | --------------- | ------------------------------------------------------------------------- |
    | `get_profile()` | Returns name, username, profile_image_link, rating, details etc.          |
    | `get_contests()`| Returns future_contests , past_contests , skill_tests etc in json format. |

    """

    def __init__(self, id_, *, config: RequestConfig = RequestConfig()):
        self.id = id_
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_profile(self):
        """
        Create an object of the 'User' class
        ```python
        user1 = User(id="heltion")
        user1.get_profile()
        ```
        Response
        ```js
        {
            'name': 'Yaowei Lyu',
            'username': 'heltion',
            'profile_image_link': 'https://cdn.codechef.com/sites/all/themes/abessive/images/user_default_thumb.jpg',
            'rating':
                {
                    'star': '7★',
                    'current_rating': '2555',
                    'division': '1',
                    'highest_rating': '2555',
                    'global_rank': '72',
                    'country_rank': '8'
                },
            'details':
                {
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
            response = get(url, self.config).text
            soup = bs(response, "lxml")

            user_details_box = soup.find("div", {"class": "user-details-container"})
            header_box = user_details_box.find("header")
            profile_image_link = header_box.find("img")["src"]
            profile_name = header_box.find("h1").text.strip()
            profile_details_box = user_details_box.find("section")
            profile_details_ul = profile_details_box.find("ul")
            profile_details_li = profile_details_ul.find_all("li")

            # star
            profile_star = (
                profile_details_li[0].find("span", {"class": "rating"}).text.strip()
            )
            # Username
            profile_username = (
                profile_details_li[0]
                .find("span", {"class": "m-username--link"})
                .text.strip()
            )
            # Country
            country_flag_link = profile_details_li[1].find(
                "img", {"class": "user-country-flag"}
            )["src"]
            country_name = (
                profile_details_li[1]
                .find("span", {"class": "user-country-name"})
                .text.strip()
            )
            # User Type
            user_type = profile_details_li[2].find("span").text.strip()
            # Institution
            institution = profile_details_li[3].find("span").text.strip()

            profile_rating_box = soup.find(
                "aside", {"class": "sidebar small-4 columns pr0"}
            )

            # Current Rating
            rating_box = profile_rating_box.find("div", {"class": "rating-header"})
            rating_divs = rating_box.find_all("div")
            current_rating = rating_divs[0].text.strip()
            # Division
            division = (
                rating_divs[1]
                .text.strip()
                .replace("(", "")
                .replace(")", "")
                .replace("Div ", "")
            )
            # Highest Rating
            highest_rating = (
                rating_box.find("small")
                .text.strip()
                .replace("(Highest Rating ", "")
                .replace(")", "")
            )

            # Ranks
            ranks_box = profile_rating_box.find("div", {"class": "rating-ranks"})
            ranks_list = ranks_box.find_all("strong")
            global_rank = ranks_list[0].text.strip()
            country_rank = ranks_list[1].text.strip()

            profile_data = {
                "name": profile_name,
                "username": profile_username,
                "profile_image_link": profile_image_link,
                "rating": {
                    "star": profile_star,
                    "current_rating": current_rating,
                    "division": division,
                    "highest_rating": highest_rating,
                    "global_rank": global_rank,
                    "country_rank": country_rank,
                },
                "details": {
                    "country_flag_link": country_flag_link,
                    "country_name": country_name,
                    "user_type": user_type,
                    "institution": institution,
                },
            }
            return profile_data
        except:
            return None

    def get_contests(self):
        """
        get_contests output
        {
            "status": "success",
            "message": "All contests list",
            "present_contests": [],
            "future_contests": [
                {
                "contest_code": "START134B",
                "contest_name": "Starters 134",
                "contest_start_date": "15 May 2024  20:00:00",
                "contest_end_date": "15 May 2024  22:00:00",
                "contest_start_date_iso": "2024-05-15T20:00:00+05:30",
                "contest_end_date_iso": "2024-05-15T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 0
                },
                ...
            ],
            "practice_contests": [],
            "past_contests": [
                {
                    "contest_code": "START133",
                    "contest_name": "Starters 133 (Rated till 6-Star)",
                    "contest_start_date": "08 May 2024  20:00:00",
                    "contest_end_date": "08 May 2024  22:00:00",
                    "contest_start_date_iso": "2024-05-08T20:00:00+05:30",
                    "contest_end_date_iso": "2024-05-08T22:00:00+05:30",
                    "contest_duration": "120",
                    "distinct_users": 20041
                    },
                    ...
                ]
            }
        """
        try:
            url = "https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all"
            response = get(url, self.config).text
            return response
        except:
            return None
