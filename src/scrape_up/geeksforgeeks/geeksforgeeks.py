import requests
from bs4 import BeautifulSoup


class Geeksforgeeks:
    """
    Create an instance of the class `GeeksforGeeks`
    ```py
    gfg = Geeksforgeeks(user="nikhil25803")
    gfg.get_profile()
    ```

    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_profile()`  | Returns the user data in json format.                                              |


    Response:
    ```js
    {
        "username": "22cs3iehq",
        "collage_name": "Rajiv Gandhi Institute of Petroleum Technology (RGIPT) Rae Bareli",
        "collage_rank": "1",
        "score": {
            "overall_coding_score": "6085",
            "monthly_coding_score": "14"
        },
        "languages_used": "C++, Javascript, Python, Java, C",
        "current_potd_streak": "407/1015",
        "total_problem_solved": "1534",
        "campus_ambassader": "22cs3iehq"
    }
    ```
    """

    def __init__(self, user):
        self.user = user

    def get_profile(self):
        try:
            url = f"https://www.geeksforgeeks.org/user/{self.user}/"
            headers = {"User-Agent": "scrapeup"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            main_info = soup.find("div", class_="AuthLayout_head_content__ql3r2")
            user_data = []

            username = main_info.find(
                "div",
                class_="profilePicSection_head_userHandleAndFollowBtnContainer_userHandle__p7sDO",
            ).text
            collage_rank = main_info.find(
                "span", class_="profilePicSection_head_userRankContainer_rank__abngM"
            ).text
            collage = main_info.find(
                "div", class_="educationDetails_head_left--text__tgi9I"
            ).text
            languages = main_info.find(
                "div", class_="educationDetails_head_right--text__lLOHI"
            ).text
            campus_ambaasder = soup.find(
                "a", class_="basicUserDetails_head_CA--text__IoHEU"
            ).text
            current_potd_streak = main_info.find(
                "div", class_="circularProgressBar_head_mid_streakCnt__MFOF1 tooltipped"
            ).text
            score = main_info.find_all(
                "div", class_="scoreCard_head_card_left--score__pC6ZA"
            )
            overall_coding_score = score[0].text
            total_problem_solved = score[1].text
            monthly_coding_score = score[2].text

            user_data = {
                "username": username,
                "collage_name": collage,
                "collage_rank": collage_rank,
                "score": {
                    "overall_coding_score": overall_coding_score,
                    "monthly_coding_score": monthly_coding_score,
                },
                "languages_used": languages,
                "current_potd_streak": current_potd_streak,
                "total_problem_solved": total_problem_solved,
                "campus_ambassader": campus_ambaasder,
            }

            return user_data
        except:
            return None


gfg = Geeksforgeeks(user="nikhil25803")
print(gfg.get_profile())
