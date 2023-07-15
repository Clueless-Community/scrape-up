import requests
from bs4 import BeautifulSoup


class Hashnode:
    """
    Class - `Hashnode`
    Example:
    ```
    blogs = Hashnode()
    ```\n
    Methods :\n
    1. ``.getFeed() | Response - Blogs with title, descriptions, author, read time, like and comment count, date and link.
    """

    def getFeed(self):
        """
        Class - `Hashnode`
        Example:
        ```
        blogs = Hashnode()
        blogs.getFeed()
        ```
        Returns:
        {
            "title": Title of the blog
            "description": Description of the blog
            "author": Author of the blog
            "read_time": Time required to read the blog
            "like_count": No. of likes of the blog
            "comment_count": No. of comments of the blog
            "date": Date the blog was posted
            "link": Link to the blog
        }
        """
        url = "https://hashnode.com/community"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            blogs_data = {"blogs": []}

            blogs = soup.find_all("div", class_="css-1s8wn94")

            for b in blogs:
                title = b.find("a", class_="css-4zleql").getText()
                desc = (
                    b.find("p", class_="css-1m4ptby")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                author = b.find("a", class_="css-9ssaz8").getText()
                read_time = b.find("span", class_="css-1r5gb7q").getText()
                try:
                    like_section = b.find("button", class_="css-a0cwys")
                    like_count = like_section.find("span").getText()
                except:
                    like_count = "0"
                try:
                    comment_section = b.find("a", class_="css-q5e5vl")
                    comment_count = comment_section.find("span").getText()
                except:
                    comment_count = "0"
                date = b.find("a", class_="css-15gyiyx").getText()
                link = b.find("a", class_="css-4zleql", href=True)["href"]

                blogs_data["blogs"].append(
                    {
                        "title": title,
                        "description": desc,
                        "author": author,
                        "read_time": read_time,
                        "like_count": like_count,
                        "comment_count": comment_count,
                        "date": date,
                        "link": link,
                    }
                )
            return blogs_data
        except:
            return None
