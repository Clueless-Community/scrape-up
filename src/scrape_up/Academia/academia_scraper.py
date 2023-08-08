from bs4 import BeautifulSoup
import requests

class Academia:
    """
    ... (class documentation) ...
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def get_research_topics(self, topic="None"):
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
                followers = articles.next_sibling.next_sibling  

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