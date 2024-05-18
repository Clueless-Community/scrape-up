from bs4 import BeautifulSoup
import json

from scrape_up.config.request_config import RequestConfig, get


class Questions:
    """
    Create an instance of `Questions` class.

    ```python
    questions = Questions("topic")
    ```

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.getNewQuestions()`        | Returns the new questions, views, votes, answer counts, and descriptions in JSON format              |
    | `.getActiveQuestions()`     | Returns the active questions, views, votes, answer counts, and descriptions in JSON format           |
    | `.getUnansweredQuestions()` | Returns the unanswered questions, views, votes, answer counts, and descriptions in JSON format       |
    | `.getBountiedQuestions()`   | Returns the bountied questions, views, votes, answer counts, and descriptions in JSON format         |
    | `.getFrequentQuestions()`   | Returns the frequently asked questions, views, votes, answer counts, and descriptions in JSON format |
    | `.getHighScoredQuestions()` | Returns the most voted questions, views, votes, answer counts, and descriptions in JSON format       |
    """

    def __init__(self, topic: str, *, config: RequestConfig = RequestConfig()):
        self.topic = topic
        self.config = config

    def getNewQuestions(self):
        """

        Class - `Questions`
        Example:
        ```
        que = Questions("github")
        scrape = que.getNewQuestions()
        ```
        Returns:
        ```js
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        ```
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic + "?tab=Newest"
        try:
            res = get(url, self.config)
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
        Class - `Questions`
        Example:
        ```
        que = Questions("github")
        scrape = que.getActiveQuestions()
        ```
        Returns:
        ```js
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        ```
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic + "?tab=Active"
        try:
            res = get(url, self.config)
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
        Class - `Questions`
        Example:
        ```
        que = Questions("github")
        scrape = que.getUnansweredQuestions()
        ```
        Returns:
        ```js
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        ```
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic + "?tab=Unanswered"
        try:
            res = get(url, self.config)
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
        Class - `Questions`
        Example:
        ```
        que = Questions("github")
        scrape = que.getBountiedQuestions()
        ```
        Returns:
        ```js
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        ```
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic + "?tab=Bountied"
        try:
            res = get(url, self.config)
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
        Class - `Questions`
        Example:
        ```
        que = Questions("github")
        scrape = que.getFrequentQuestions()
        ```
        Returns:
        ```js
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        ```
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic + "?tab=Frequent"
        try:
            res = get(url, self.config)
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
        Class - `Questions`
        Example:
        ```
        que = Questions("github")
        scrape = que.getHighScoredQuestions()
        ```
        Returns:
        ```js
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        ```
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic + "?tab=Votes"
        try:
            res = get(url, self.config)
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
