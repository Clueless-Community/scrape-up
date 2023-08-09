from bs4 import BeautifulSoup
import requests

class Academia:
    """
    A class to interact with the Academia website for research topics and papers.

    ...

    Attributes:
    -----------
    headers : dict
        A dictionary containing User-Agent header for making HTTP requests.

    Methods:
    --------
    get_research_topics(topic="None"):
        Fetches and returns research topics starting with the given letter.

    get_research_papers(search):
        Fetches and returns research papers related to the given search term.
    """

    def __init__(self):
        """Initialize the Academia class with the necessary attributes."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def _get_soup(self, url):
        """
        Send an HTTP request to the provided URL and parse the response as BeautifulSoup.

        Parameters:
        -----------
        url : str
            The URL to send the request to.

        Returns:
        --------
        BeautifulSoup
            A BeautifulSoup object representing the parsed HTML content.
        None
            If an error occurs during the request or parsing.
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, "lxml")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def get_research_topics(self, topic="None"):
        """
        Fetches and returns research topics starting with the given letter.

        Parameters:
        -----------
        topic : str, optional
            The letter to filter research topics (default is "None" to get all topics).

        Returns:
        --------
        list of dict
            A list of dictionaries containing information about research topics.
        None
            If an error occurs during fetching or parsing.
        """
        try:
            letter = topic.capitalize()
            url = f"https://www.academia.edu/topics/{letter}"
            soup = self._get_soup(url)
            if not soup:
                return None

            topics = []
            container = soup.find("div", {"class": "topic-list-container"})
            if container:
                for item in container.find_all("div", {"class": "topic-list-item"}):
                    link = item.find("a", href=True)["href"]
                    title = item.find("a").text
                    articles = item.find("p")
                    followers = articles.find_next_sibling("p")

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
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        return topics

    def get_research_papers(self, search):
        """
        Fetches and returns research papers related to the given search term.

        Parameters:
        -----------
        search : str
            The search term to find research papers.

        Returns:
        --------
        list of dict
            A list of dictionaries containing information about research papers.
        None
            If an error occurs during fetching or parsing.
        """
        try:
            search = search.title().replace(" ", "_")
            url = f"https://www.academia.edu/Documents/in/{search}"
            soup = self._get_soup(url)
            if not soup:
                return None

            papers = []
            container = soup.find("div", {"class": "works"})
            if container:
                for item in container.find_all("div", {"class": "item"}):
                    title = item.find("div", {"class": "header"}).text
                    summary = item.find("div", {"class": "description"})
                    summary = summary.text if summary else None
                    link = item.find("a", href=True)["href"]
                    data = {"Title": title, "Summary": summary, "Link": link}
                    papers.append(data)
            return papers
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

