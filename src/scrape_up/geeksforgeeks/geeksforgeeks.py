import requests
from bs4 import BeautifulSoup

class Geeksforgeeks:

    def __init__(self,user):
        self.user = user

    def get_profile(self):
        try:
            url = f"https://www.geeksforgeeks.org/user/{self.user}/"
            headers = {"User-Agent": "scrapeup"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            main_info=soup.find('div',class_="AuthLayout_head_content__ql3r2")
            user_data=[]

            username=main_info.find('div',class_="profilePicSection_head_userHandleAndFollowBtnContainer_userHandle__p7sDO").text
            collage_rank=main_info.find('span',class_="profilePicSection_head_userRankContainer_rank__abngM").text
            collage=main_info.find('div',class_="educationDetails_head_left--text__tgi9I").text
            languages=main_info.find('div',class_="educationDetails_head_right--text__lLOHI").text
            campus_ambaasder=soup.find('a',class_="basicUserDetails_head_CA--text__IoHEU").text
            current_potd_streak=main_info.find('div',class_="circularProgressBar_head_mid_streakCnt__MFOF1 tooltipped").text
            score=main_info.find_all('div',class_="scoreCard_head_card_left--score__pC6ZA")
            overall_coding_score=score[0].text
            total_problem_solved=score[1].text
            monthly_coding_score=score[2].text

            user_data={
                'username':username,
                'collage_name':collage,
                'collage_rank':collage_rank,
                'score':{
                    'overall_coding_score':overall_coding_score,
                    'monthly_coding_score':monthly_coding_score,
                },
                'languages_used':languages,
                'current_potd_streak':current_potd_streak,
                'total_problem_solved':total_problem_solved,
                'campus_ambassader':campus_ambaasder,
            }

            return user_data
        except:
            return None

