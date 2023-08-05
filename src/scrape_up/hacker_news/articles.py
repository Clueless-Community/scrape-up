import requests
from bs4 import BeautifulSoup


class HackerNews:
    """
    Create an instance of `HackerNews` class.
    ```py
    articles = HackerNews()
    ```
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.articles_list()` | Returns the latest articles along with their score, author, author url, time, comment count and link in JSON format. |
    | `.new_articles()` | Returns the latest new articles along with their score, author, author url, time, comment count and link in JSON format. |
    | `.past_articles()` | Returns the past articles along with their score, author, author url, time, comment count and link in JSON format. |
    | `.ask_articles()` | Returns the ask articles along with their score, author, author url, time, comment count and link in JSON format. |
    | `.show_articles()` | Returns the show articles along with their score, author, author url, time, comment count and link in JSON format. |
    | `.jobs()` | Returns the jobs along with their time and link in JSON format. |
    """

    def articles_list(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.articles_list()
        ```
        Return
        ```js
        [
            {
                "title":"I have written a JVM in Rust",
                "score":"507 points",
                "author":"lukastyrychtr",
                "author_url":"user?id=lukastyrychtr",
                "time":"9 hours ago",
                "comment_count":"79",
                "link":"https://andreabergia.com/blog/2023/07/i-have-written-a-jvm-in-rust/"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = (
                    "0" if not comments_link else comments_link.text.split()[0]
                )
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "score": score,
                        "author": author,
                        "author_url": author_url,
                        "time": time,
                        "comment_count": comment_count,
                        "link": link,
                    }
                )
            return articles_data["articles"]

        except:
            return None

    def new_articles(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.new_articles()
        ```
        Return
        ```js
        [
            {
                "title":"I have written a JVM in Rust",
                "score":"507 points",
                "author":"lukastyrychtr",
                "author_url":"user?id=lukastyrychtr",
                "time":"9 hours ago",
                "comment_count":"79",
                "link":"https://andreabergia.com/blog/2023/07/i-have-written-a-jvm-in-rust/"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/newest"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = (
                    "0" if not comments_link else comments_link.text.split()[0]
                )
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "score": score,
                        "author": author,
                        "author_url": "https://news.ycombinator.com/" + author_url,
                        "time": time,
                        "comment_count": comment_count,
                        "link": link,
                    }
                )
            return articles_data["articles"]

        except:
            return None

    def past_articles(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.past_articles()
        ```
        Return
        ```js
        [
            {
                "title":"I have written a JVM in Rust",
                "score":"507 points",
                "author":"lukastyrychtr",
                "author_url":"user?id=lukastyrychtr",
                "time":"9 hours ago",
                "comment_count":"79",
                "link":"https://andreabergia.com/blog/2023/07/i-have-written-a-jvm-in-rust/"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/front"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = (
                    "0" if not comments_link else comments_link.text.split()[0]
                )
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "score": score,
                        "author": author,
                        "author_url": "https://news.ycombinator.com/" + author_url,
                        "time": time,
                        "comment_count": comment_count,
                        "link": link,
                    }
                )
            return articles_data["articles"]

        except:
            return None

    def ask_articles(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.ask_articles()
        ```
        Return
        ```js
        [
            {
                "title":"I have written a JVM in Rust",
                "score":"507 points",
                "author":"lukastyrychtr",
                "author_url":"user?id=lukastyrychtr",
                "time":"9 hours ago",
                "comment_count":"79",
                "link":"https://andreabergia.com/blog/2023/07/i-have-written-a-jvm-in-rust/"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/ask"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = (
                    "0" if not comments_link else comments_link.text.split()[0]
                )
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "score": score,
                        "author": author,
                        "author_url": "https://news.ycombinator.com/" + author_url,
                        "time": time,
                        "comment_count": comment_count,
                        "link": "https://news.ycombinator.com/" + link,
                    }
                )
            return articles_data["articles"]

        except:
            return None

    def show_articles(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.show_articles()
        ```
        Return
        ```js
        [
            {
                "title":"I have written a JVM in Rust",
                "score":"507 points",
                "author":"lukastyrychtr",
                "author_url":"user?id=lukastyrychtr",
                "time":"9 hours ago",
                "comment_count":"79",
                "link":"https://andreabergia.com/blog/2023/07/i-have-written-a-jvm-in-rust/"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/show"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("span", class_="subline")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                score = j.find("span", class_="score").getText()
                author = j.find("a", class_="hnuser").getText()
                author_url = j.find("a", class_="hnuser")["href"]
                time = j.find("span", class_="age").find("a").getText()
                comments_link = j.find_all("a")[-1]
                comment_count = (
                    "0" if not comments_link else comments_link.text.split()[0]
                )
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "score": score,
                        "author": author,
                        "author_url": "https://news.ycombinator.com/" + author_url,
                        "time": time,
                        "comment_count": comment_count,
                        "link": link,
                    }
                )
            return articles_data["articles"]

        except:
            return None

    def jobs(self):
        """
        Class - `HackerNews`
        Example -
        ```python
        hacker_news = HackerNews()
        articles = hacker_news.jobs()
        ```
        Return
        ```js
        [
            {
                "title":"PropelAuth (YC W22) Is Hiring Engineers",
                "time":"37 minutes ago",
                "link":"https://www.ycombinator.com/companies/propelauth/jobs"
            }
            ...
        ]
        ```
        """
        url = "https://news.ycombinator.com/jobs"

        articles_data = {"articles": []}

        try:
            res = requests.get(url)

            soup = BeautifulSoup(res.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")
            subs = soup.find_all("td", class_="subtext")

            for i, j in zip(titles, subs):
                title = i.find("a").getText()
                time = j.find("span", class_="age").find("a").getText()
                link = i.find("a")["href"]

                articles_data["articles"].append(
                    {
                        "title": title,
                        "time": time,
                        "link": link,
                    }
                )
            return articles_data["articles"]

        except:
            return None
