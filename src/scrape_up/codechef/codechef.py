import requests
from bs4 import BeautifulSoup as bs


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

    def __init__(self, id):
        self.id = id

    def get_profile(self):
        """
         Create an object of the 'User' class\n
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

    def get_contests():
        '''
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
                {
                "contest_code": "START135B",
                "contest_name": "Starters 135",
                "contest_start_date": "22 May 2024  20:00:00",
                "contest_end_date": "22 May 2024  22:00:00",
                "contest_start_date_iso": "2024-05-22T20:00:00+05:30",
                "contest_end_date_iso": "2024-05-22T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 0
                }
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
                {
                "contest_code": "START132",
                "contest_name": "Starters 132 (Rated till 6 Stars)",
                "contest_start_date": "01 May 2024  20:00:00",
                "contest_end_date": "01 May 2024  22:00:00",
                "contest_start_date_iso": "2024-05-01T20:00:00+05:30",
                "contest_end_date_iso": "2024-05-01T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 22930
                },
                {
                "contest_code": "START131",
                "contest_name": "Starters 131 (Rated till 5 Stars)",
                "contest_start_date": "24 Apr 2024  20:00:00",
                "contest_end_date": "24 Apr 2024  22:00:00",
                "contest_start_date_iso": "2024-04-24T20:00:00+05:30",
                "contest_end_date_iso": "2024-04-24T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 27566
                },
                {
                "contest_code": "START130",
                "contest_name": "Starters 130 (Rated till 6-Stars)",
                "contest_start_date": "17 Apr 2024  20:00:00",
                "contest_end_date": "17 Apr 2024  22:00:00",
                "contest_start_date_iso": "2024-04-17T20:00:00+05:30",
                "contest_end_date_iso": "2024-04-17T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 28434
                },
                {
                "contest_code": "START129",
                "contest_name": "Starters 129 (Rated till 5-Stars)",
                "contest_start_date": "10 Apr 2024  20:00:00",
                "contest_end_date": "10 Apr 2024  22:00:00",
                "contest_start_date_iso": "2024-04-10T20:00:00+05:30",
                "contest_end_date_iso": "2024-04-10T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 32181
                },
                {
                "contest_code": "START128",
                "contest_name": "Starters 128 (Rated till 6-Stars)",
                "contest_start_date": "03 Apr 2024  20:00:00",
                "contest_end_date": "03 Apr 2024  22:00:00",
                "contest_start_date_iso": "2024-04-03T20:00:00+05:30",
                "contest_end_date_iso": "2024-04-03T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 34876
                },
                {
                "contest_code": "START127",
                "contest_name": "Starters 127 (Rated till 5 Stars)",
                "contest_start_date": "27 Mar 2024  20:00:00",
                "contest_end_date": "27 Mar 2024  22:00:00",
                "contest_start_date_iso": "2024-03-27T20:00:00+05:30",
                "contest_end_date_iso": "2024-03-27T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 37656
                },
                {
                "contest_code": "START126",
                "contest_name": "Starters 126 (Rated till 6 Stars)",
                "contest_start_date": "20 Mar 2024  20:00:00",
                "contest_end_date": "20 Mar 2024  22:00:00",
                "contest_start_date_iso": "2024-03-20T20:00:00+05:30",
                "contest_end_date_iso": "2024-03-20T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 39861
                },
                {
                "contest_code": "START125",
                "contest_name": "Starters 125 (Rated till 6-Stars)",
                "contest_start_date": "13 Mar 2024  20:00:00",
                "contest_end_date": "13 Mar 2024  22:00:00",
                "contest_start_date_iso": "2024-03-13T20:00:00+05:30",
                "contest_end_date_iso": "2024-03-13T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 40646
                },
                {
                "contest_code": "START124",
                "contest_name": "Starters 124 (Rated till 5-Stars)",
                "contest_start_date": "06 Mar 2024  20:00:00",
                "contest_end_date": "06 Mar 2024  22:00:00",
                "contest_start_date_iso": "2024-03-06T20:00:00+05:30",
                "contest_end_date_iso": "2024-03-06T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 42655
                },
                {
                "contest_code": "START123",
                "contest_name": "Starters 123 (Rated till 6-Stars)",
                "contest_start_date": "28 Feb 2024  20:00:00",
                "contest_end_date": "28 Feb 2024  22:30:00",
                "contest_start_date_iso": "2024-02-28T20:00:00+05:30",
                "contest_end_date_iso": "2024-02-28T22:30:00+05:30",
                "contest_duration": "150",
                "distinct_users": 42005
                },
                {
                "contest_code": "START122",
                "contest_name": "Starters 122 (Rated till 6-Stars)",
                "contest_start_date": "21 Feb 2024  20:00:00",
                "contest_end_date": "21 Feb 2024  22:00:00",
                "contest_start_date_iso": "2024-02-21T20:00:00+05:30",
                "contest_end_date_iso": "2024-02-21T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 39677
                },
                {
                "contest_code": "START121",
                "contest_name": "Starters 121 (Rated till 6-Stars)",
                "contest_start_date": "14 Feb 2024  20:00:00",
                "contest_end_date": "14 Feb 2024  22:00:00",
                "contest_start_date_iso": "2024-02-14T20:00:00+05:30",
                "contest_end_date_iso": "2024-02-14T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 34442
                },
                {
                "contest_code": "START120",
                "contest_name": "Starters 120 (Rated till 6-Stars)",
                "contest_start_date": "07 Feb 2024  20:00:00",
                "contest_end_date": "07 Feb 2024  22:00:00",
                "contest_start_date_iso": "2024-02-07T20:00:00+05:30",
                "contest_end_date_iso": "2024-02-07T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 37332
                },
                {
                "contest_code": "START119",
                "contest_name": "Starters 119 (Rated till 6-Stars)",
                "contest_start_date": "31 Jan 2024  20:00:00",
                "contest_end_date": "31 Jan 2024  22:00:00",
                "contest_start_date_iso": "2024-01-31T20:00:00+05:30",
                "contest_end_date_iso": "2024-01-31T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 33112
                },
                {
                "contest_code": "START118",
                "contest_name": "Starters 118 (Rated till 5-Stars)",
                "contest_start_date": "24 Jan 2024  20:00:00",
                "contest_end_date": "24 Jan 2024  22:00:00",
                "contest_start_date_iso": "2024-01-24T20:00:00+05:30",
                "contest_end_date_iso": "2024-01-24T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 27683
                },
                {
                "contest_code": "START117",
                "contest_name": "Starters 117 (Rated till 5-Stars)",
                "contest_start_date": "17 Jan 2024  20:00:00",
                "contest_end_date": "17 Jan 2024  22:00:00",
                "contest_start_date_iso": "2024-01-17T20:00:00+05:30",
                "contest_end_date_iso": "2024-01-17T22:00:00+05:30",
                "contest_duration": "120",
                "distinct_users": 22710
                },
                {
                "contest_code": "START116",
                "contest_name": "Starters 116  (Rated till 6-Stars)",
                "contest_start_date": "10 Jan 2024  20:00:00",
                "contest_end_date": "10 Jan 2024  22:15:00",
                "contest_start_date_iso": "2024-01-10T20:00:00+05:30",
                "contest_end_date_iso": "2024-01-10T22:15:00+05:30",
                "contest_duration": "135",
                "distinct_users": 26898
                },
                {
                "contest_code": "START115",
                "contest_name": "Starters 115 (Rated for All)",
                "contest_start_date": "03 Jan 2024  20:00:00",
                "contest_end_date": "03 Jan 2024  22:30:00",
                "contest_start_date_iso": "2024-01-03T20:00:00+05:30",
                "contest_end_date_iso": "2024-01-03T22:30:00+05:30",
                "contest_duration": "150",
                "distinct_users": 26446
                },
                {
                "contest_code": "START114",
                "contest_name": "Starters 114  (Rated till 6 Stars)",
                "contest_start_date": "27 Dec 2023  20:00:00",
                "contest_end_date": "27 Dec 2023  22:15:00",
                "contest_start_date_iso": "2023-12-27T20:00:00+05:30",
                "contest_end_date_iso": "2023-12-27T22:15:00+05:30",
                "contest_duration": "135",
                "distinct_users": 23396
                }
            ],
            "skill_tests": [
                {
                "contest_code": "LPYAS",
                "contest_name": "Python Skill test",
                "contest_start_date": "27 Mar 2024  15:00:00",
                "contest_end_date": "01 Jan 2027  01:30:00",
                "contest_start_date_iso": "2024-03-27T15:00:00+05:30",
                "contest_end_date_iso": "2027-01-01T01:30:00+05:30",
                "contest_duration": "90",
                "problem_count": 30,
                "distinct_users": 0
                },
                {
                "contest_code": "LCPPAS",
                "contest_name": "C++ Skill test",
                "contest_start_date": "28 Mar 2024  00:00:00",
                "contest_end_date": "01 Jan 2027  01:30:00",
                "contest_start_date_iso": "2024-03-28T00:00:00+05:30",
                "contest_end_date_iso": "2027-01-01T01:30:00+05:30",
                "contest_duration": "90",
                "problem_count": 30,
                "distinct_users": 0
                },
                {
                "contest_code": "LCAS",
                "contest_name": "C language skill test",
                "contest_start_date": "28 Mar 2024  00:00:00",
                "contest_end_date": "01 Jan 2027  01:30:00",
                "contest_start_date_iso": "2024-03-28T00:00:00+05:30",
                "contest_end_date_iso": "2027-01-01T01:30:00+05:30",
                "contest_duration": "90",
                "problem_count": 30,
                "distinct_users": 0
                },
                {
                "contest_code": "LJJAAS",
                "contest_name": "Java Skill test",
                "contest_start_date": "28 Mar 2024  00:00:00",
                "contest_end_date": "01 Jan 2027  01:30:00",
                "contest_start_date_iso": "2024-03-28T00:00:00+05:30",
                "contest_end_date_iso": "2027-01-01T01:30:00+05:30",
                "contest_duration": "90",
                "problem_count": 30,
                "distinct_users": 0
                },
                {
                "contest_code": "BDSAJAS01",
                "contest_name": "Data structures and Algorithms in Java test",
                "contest_start_date": "17 Apr 2024  17:00:00",
                "contest_end_date": "01 Jan 2027  02:00:00",
                "contest_start_date_iso": "2024-04-17T17:00:00+05:30",
                "contest_end_date_iso": "2027-01-01T02:00:00+05:30",
                "contest_duration": "120",
                "problem_count": 28,
                "distinct_users": 0
                }
            ],
            "banners": [
                {
                "image": "1715586444.png",
                "link": "https://www.codechef.com/START134"
                },
                {
                "image": "1704448967.png",
                "link": "https://www.codechef.com/roadmap/become-5-star"
                }
            ]
            }
        '''
        try:
            url = "https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            response = requests.get(url, headers=headers).text
            return response
        except:
            return None