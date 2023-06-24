from bs4 import BeautifulSoup
import requests
import json

class Questions:
    def __init__(self, topic):
        self.topic = topic

    def scrape(self):
        url = "https://askubuntu.com/search?q="+self.topic
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        questions_data = {
            "questions": []
        }

        questions = soup.select(".s-post-summary")
        for que in questions:
            name = que.select_one(".s-link").getText()
            stats = que.select(".s-post-summary--stats-item-number")
            vote = stats[0].getText()
            ans = stats[1].getText()
            views = stats[2].getText()
            desc = que.select_one(".s-post-summary--content-excerpt").getText().strip().encode('ascii', 'ignore').decode()
            questions_data['questions'].append({
                "question": name,
                "views": views,
                "vote_count": vote,
                "answer_count": ans,
                "description": desc,
            })
        json_data = json.dumps(questions_data)
        return json_data