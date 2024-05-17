from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


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

    def __init__(self, user: str, *, config: RequestConfig = RequestConfig()):
        self.user = user
        headers = {"User-Agent": "scrapeup"}
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_profile(self):
        try:
            url = f"https://www.geeksforgeeks.org/user/{self.user}/"
            response = get(url, self.config)
            soup = BeautifulSoup(response.text, "html.parser")
            main_info = soup.find("div", class_="AuthLayout_head_content__ql3r2")

            username = main_info.find(
                "div",
                class_="profilePicSection_head_userHandleAndFollowBtnContainer_userHandle__p7sDO",
            ).text.strip()
            collage_rank = main_info.find(
                "span", class_="profilePicSection_head_userRankContainer_rank__abngM"
            ).text.strip()
            collage = main_info.find(
                "div", class_="educationDetails_head_left--text__tgi9I"
            ).text.strip()
            languages = main_info.find(
                "div", class_="educationDetails_head_right--text__lLOHI"
            ).text.strip()
            campus_ambaasder = soup.find(
                "a", class_="basicUserDetails_head_CA--text__IoHEU"
            ).text.strip()
            current_potd_streak = main_info.find(
                "div", class_="circularProgressBar_head_mid_streakCnt__MFOF1 tooltipped"
            ).text.strip()
            score = main_info.find_all(
                "div", class_="scoreCard_head_card_left--score__pC6ZA"
            )
            overall_coding_score = score[0].text.strip()
            total_problem_solved = score[1].text.strip()
            monthly_coding_score = score[2].text.strip()

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

            formatted_output = (
                f"Username: {user_data['username']}\n"
                f"College Name: {user_data['collage_name']}\n"
                f"College Rank: {user_data['collage_rank']}\n"
                f"Overall Coding Score: {user_data['score']['overall_coding_score']}\n"
                f"Monthly Coding Score: {user_data['score']['monthly_coding_score']}\n"
                f"Languages Used: {user_data['languages_used']}\n"
                f"Current POTD Streak: {user_data['current_potd_streak']}\n"
                f"Total Problems Solved: {user_data['total_problem_solved']}\n"
                f"Campus Ambassador: {user_data['campus_ambassader']}"
            )

            return formatted_output
        except Exception as e:
            return None
