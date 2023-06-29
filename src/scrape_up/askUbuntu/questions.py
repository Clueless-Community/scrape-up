from bs4 import BeautifulSoup
import requests
import json


class AskUbuntu:
    def __init__(self, topic):
        self.topic = topic

    def getNewQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getNewQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic+"?tab=Newest"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except:
            error_message = {"message": "No questions related to the topic found"}

            ejson = json.dumps(error_message)
            return ejson
    
    def getActiveQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getActiveQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic+"?tab=Active"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except:
            error_message = {"message": "No questions related to the topic found"}

            ejson = json.dumps(error_message)
            return ejson
        
    def getUnansweredQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getUnansweredQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic+"?tab=Unanswered"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except:
            error_message = {"message": "No questions related to the topic found"}

            ejson = json.dumps(error_message)
            return ejson
         
    def getBountiedQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getBountiedQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic+"?tab=Bountied"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except:
            error_message = {"message": "No questions related to the topic found"}

            ejson = json.dumps(error_message)
            return ejson
        
    def getFrequentQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getFrequentQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic+"?tab=Frequent"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except:
            error_message = {"message": "No questions related to the topic found"}

            ejson = json.dumps(error_message)
            return ejson
    
    def getHighScoredQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getHighScoredQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic+"?tab=Votes"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            json_data = json.dumps(questions_data)
            return json_data
        except:
            error_message = {"message": "No questions related to the topic found"}

            ejson = json.dumps(error_message)
            return ejson
