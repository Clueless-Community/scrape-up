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
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
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

            if container:
                for item in container.find_all("div", {"class": "topic-list-item"}):
                    link = item.find("a", href=True)["href"]
                    title = item.find("a").text
                    articles = item.find("p")
                    followers = articles.find_next_sibling("p")  # Use find_next_sibling to get the followers

                    data = {
                        "Title": title,
                        "Link": link,
                        "Number of Articles": articles.text if articles else "N/A",
                        "Followers": followers.text if followers else "N/A",
                    }
                    topics.append(data)
            else:
                print("Container not found")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return topics

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
            for item in container.find_all("div", {"class": "item"}):  # Loop through items
                title = item.find("div", {"class": "header"}).text
                summary = item.find("div", {"class": "description"})
                if summary:
                    summary = summary.text
                else:
                    summary = None
                link = item.find("a", href=True)["href"]
                data = {"Title": title, "Summary": summary, "Link": link}
                papers.append(data)
            return papers
        except:
            return None