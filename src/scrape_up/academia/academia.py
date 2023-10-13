from bs4 import BeautifulSoup
import requests


class Academia:
    """
    Create an instance of `Academia` class

    ```python
    academia = Academia()
    ```

    | Method                        | Details                                                               |
    | ----------------------------- | --------------------------------------------------------------------- |
    | `get_research_topics(letter)` | Fetches and returns research topics starting with the given letter.   |
    | `get_research_papers(search)` | Fetches and returns research papers related to the given search term. |

    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def get_research_topics(self, topic="None"):
        """
        Fetches and returns research topics starting with the given letter.\n
        Param `letter`: The letter to filter research topics (default is "None" to get all topics).\n
        Class - `Academia`\n
        ```python
        ac = Academia()
        ac.get_research_topics(topic="machine learning")
        ```
        Example output:
        ```python
        [
            {
                "Title": "Artificial Intelligence",
                "Link": "https://www.academia.edu/topics/artificial_intelligence",
                "Number of Articles": "20,000",
                "Followers": "5,000"
            },
            ...
        ]
        ```
        """
        try:
            letter = topic.capitalize()
            url = f"https://www.academia.edu/topics/{letter}"
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            topics = []
            container = soup.find("div", {"class": "topic-list-container"})
            for items in container:
                link = items.find("a", href=True)["href"]
                title = items.find("a").text
                articles = items.find("p")
                followers = articles.next_sibling.next_sibling
                data = {
                    "Title": title,
                    "Link": link,
                    "Number of Articles": articles.text,
                    "Followers": followers.text,
                }
                topics.append(data)
            return topics
        except:
            return None

    def get_research_papers(self, search):
        """
        Fetches and returns research papers related to the given search term.\n
        Param `search`: The search term to find research papers.\n
        Class - `Academia`\n
        ```python
        ac = Academia()
        ac.get_research_papers(search="machine learning")
        ```
        Example output:
        ```python
        [
            {
                "Title": "Artificial Neural Networks: A Comprehensive Guide",
                "Summary": "This paper provides an overview of artificial neural networks...",
                "Link": "https://www.academia.edu/Documents/in/Artifical_Neural_Network"
            },
            ...
        ]
        ```
        """
        try:
            search = search.title()
            search = search.replace(" ", "_")
            url = f"https://www.academia.edu/Documents/in/{search}"
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            papers = []
            container = soup.find("div", {"class": "works"})
            for items in container:
                title = items.find("div", {"class": "header"}).text
                summary = items.find("div", {"class": "complete hidden"})
                if summary:
                    summary = summary.text
                else:
                    summary = None
                link = items.find("a", href=True)["href"]
                data = {"Title": title, "Summary": summary, "Link": link}
                papers.append(data)
            return papers
        except:
            return None
