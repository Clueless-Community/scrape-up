import json
import requests

class RequestConfig:
    def __init__(self):
        self.headers = {}

    def set_headers(self, headers):
        self.headers = headers

class LeetCode:
    """
    ```python
    LeetCode = LeetCode(username="Agastya3636")
    ```
    **username** might not require in a few methods
    | Methods                                | Details                                                                      |
    | ---------------------------------------| -----------------------------------------------------------------------------|
    | `.userContestRanking()`                | Returns rating, global ranking, top percentage, contest count, etc.          |
    | `.activeBadge()`                       | Returns the active badge of the user.                                        |
    | `.languageProblemCount()`              | Returns the problems solved by language.                                     |
    | `.practiceProblemRanking()`            | Returns rank of practice problem by percentage.                              |
    | `.problemsSolvedByDifficultyNo()`      | Returns problems solved by difficulty count.                                 |
    """

    def __init__(self, user: str, *, config: RequestConfig = RequestConfig()):
        self.user = user
        self.config = config
        headers = {"User-Agent": "scrapeup"}
        if self.config.headers == {}:
            self.config.set_headers(headers)
        self.user_profile = self.__scrape_user_profile()

    def __scrape_user_profile(self):
        try:
            query = f"""
            query {{
              matchedUser(username: "{self.user}") {{
                username
                languageProblemCount {{
                  languageName
                  problemsSolved
                }}
                problemsSolvedBeatsStats {{
                  difficulty
                  percentage
                }}
                submitStatsGlobal {{
                  acSubmissionNum {{
                    difficulty
                    count
                  }}
                }}
                activeBadge {{
                  displayName
                  icon
                }}
              }}
              userContestRanking(username: "{self.user}") {{
                attendedContestsCount
                rating
                globalRanking
                totalParticipants
                topPercentage
                badge {{
                  name
                }}
              }}
            }}
            """
            url = 'https://leetcode.com/graphql'

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
                "Content-Type": "application/json"
            }

            payload = {
                "query": query
            }

            response = requests.post(url, headers=headers, data=json.dumps(payload))

      
            response_json = response.json()
            return response_json
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def userContestRanking(self):
        try:
            rank = self.user_profile['data']['userContestRanking']
            return json.dumps(rank, indent=2)
        except Exception as e:
            # print(f"An error occurred: {e}")
            return None

    def activeBadge(self):
        try:
            badge = self.user_profile['data']['matchedUser']['activeBadge']
            return json.dumps(badge, indent=2)
        except Exception as e:
            # print(f"An error occurred: {e}")
            return None

    def languageProblemCount(self):
        try:
            languages = self.user_profile['data']['matchedUser']['languageProblemCount']
            return json.dumps(languages, indent=2)
        except Exception as e:
            # print(f"An error occurred: {e}")
            return None

    def practiceProblemRanking(self):
        try:
            stats = self.user_profile['data']['matchedUser']['problemsSolvedBeatsStats']
            return json.dumps(stats, indent=2)
        except Exception as e:
            # print(f"An error occurred: {e}")
            return None

    def problemsSolvedByDifficultyNo(self):
        try:
            stats = self.user_profile['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum']
            return json.dumps(stats, indent=2)
        except Exception as e:
            # print(f"An error occurred: {e}")
            return None


# Usage example
# leetcode = LeetCode(user="Agastya3636")
# print(leetcode.userContestRanking())
# print(leetcode.activeBadge())
# print(leetcode.languageProblemCount())
# print(leetcode.practiceProblemRanking())
# print(leetcode.problemsSolvedByDifficultyNo())
"""
{
  "attendedContestsCount": 11,
  "rating": 1722.8666788439257,
  "globalRanking": 58499,
  "totalParticipants": 535861,
  "topPercentage": 11.28,
  "badge": null
}
{
  "displayName": "50 Days Badge 2023",
  "icon": "https://assets.leetcode.com/static_assets/marketing/lg50.png"
}
[
  {
    "languageName": "C++",
    "problemsSolved": 152
  },
  {
    "languageName": "JavaScript",
    "problemsSolved": 1
  },
  {
    "languageName": "Python3",
    "problemsSolved": 3
  },
  {
    "languageName": "Pandas",
    "problemsSolved": 13
  }
]
[
  {
    "difficulty": "Easy",
    "percentage": 91.45
  },
  {
    "difficulty": "Medium",
    "percentage": 76.16
  },
  {
    "difficulty": "Hard",
    "percentage": 65.49
  }
]
[
  {
    "difficulty": "All",
    "count": 169
  },
  {
    "difficulty": "Easy",
    "count": 104
  },
  {
    "difficulty": "Medium",
    "count": 54
  },
  {
    "difficulty": "Hard",
    "count": 11
  }
]

"""