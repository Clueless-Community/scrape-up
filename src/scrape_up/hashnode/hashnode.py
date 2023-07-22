import requests
from bs4 import BeautifulSoup


class Hashnode:
    """
    Create an instance of `Hashnode` class.
    ```python
    blogs = Hashnode()
    ```
    | Methods          | Details                                                                                              |
    | ---------------- | ---------------------------------------------------------------------------------------------------- |
    | `.get_feed()`     | Returns the blogs with title, descriptions, author, read time, like and comment count, date and link |
    | `.get_featured()` | Returns the featured blogs with title, descriptions, author, like and comment count, date and link   |
    | `.get_recent()`   | Returns the recent blogs with title, descriptions, author, like and comment count, date and link     |
    """

    def get_feed(self):
        """
        Class - `Hashnode`
        Example:
        ```pyton
        blogs = Hashnode()
        blogs.get_feed()
        ```
        Returns:
        ```js
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
        ```
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

    def get_featured(self):
        """
        Class - `Hashnode`
        Example:
        ```python
        blogs = Hashnode()
        blogs.get_featured()
        ```
        Returns:
        ```js
        [
            {
                "title": Title of the blog
                "description": Description of the blog
                "author": Author of the blog
                "like_count": No. of likes of the blog
                "comment_count": No. of comments of the blog
                "date": Date the blog was posted
                "link": Link to the blog
            }
            ...
        ]
        ```js
        """
        url = "https://hashnode.com/featured"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            blogs_data = {"blogs": []}

            blogs = soup.find_all(
                "div",
                class_="w-full first-of-type:border-t-0 border-t lg:!border border-slate-200 dark:border-slate-800 rounded-none lg:rounded-2xl pt-5 md:pt-8 lg:p-6 lg:pb-5 bg-white dark:bg-slate-950 flex flex-col gap-2 sm:gap-4",
            )

            for b in blogs:
                title = (
                    b.find("div", class_="flex flex-col gap-1")
                    .find("div")
                    .find("a")
                    .getText()
                )
                author = b.find(
                    "span",
                    class_="font-semibold text-slate-700 dark:text-slate-200 cursor-pointer",
                ).getText()
                date = b.find(
                    "p", class_="text-sm text-slate-500 dark:text-slate-400 font-normal"
                ).getText()

                try:
                    try:
                        desc = b.find(
                            "span",
                            class_="text-base hidden font-normal text-slate-500 dark:text-slate-400 hn-break-words cursor-pointer md:line-clamp-2",
                        ).getText()
                    except:
                        desc = b.find(
                            "span",
                            class_="text-base hidden font-normal text-slate-500 dark:text-slate-400 hn-break-words cursor-pointer md:line-clamp-3",
                        ).getText()
                except:
                    desc = ""

                link = (
                    b.find("div", class_="flex flex-col gap-1")
                    .find("div")
                    .find("a")["href"]
                )

                try:
                    like_count = b.find(
                        "button", attrs={"aria-label": "Like reaction"}
                    ).getText()
                except:
                    like_count = 0

                try:
                    comment_count = b.find(
                        "button", attrs={"aria-label": "Comment"}
                    ).getText()
                except:
                    comment_count = 0

                blogs_data["blogs"].append(
                    {
                        "title": title,
                        "description": desc,
                        "author": author,
                        "like_count": like_count,
                        "comment_count": comment_count,
                        "date": date,
                        "link": link,
                    }
                )
            return blogs_data["blogs"]
        except:
            return None

    def get_recent(self):
        """
        Class - `Hashnode`
        Example:
        ```python
        blogs = Hashnode()
        blogs.get_recent()
        ```
        Returns:
        ```js
        [
            {
                "title": Title of the blog
                "description": Description of the blog
                "author": Author of the blog
                "like_count": No. of likes of the blog
                "comment_count": No. of comments of the blog
                "date": Date the blog was posted
                "link": Link to the blog
            }
            ...
        ]
        """
        url = "https://hashnode.com/recent"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            blogs_data = {"blogs": []}

            blogs = soup.find_all(
                "div",
                class_="w-full first-of-type:border-t-0 border-t lg:!border border-slate-200 dark:border-slate-800 rounded-none lg:rounded-2xl pt-5 md:pt-8 lg:p-6 lg:pb-5 bg-white dark:bg-slate-950 flex flex-col gap-2 sm:gap-4",
            )

            for b in blogs:
                title = (
                    b.find("div", class_="flex flex-col gap-1")
                    .find("div")
                    .find("a")
                    .getText()
                )
                author = b.find(
                    "span",
                    class_="font-semibold text-slate-700 dark:text-slate-200 cursor-pointer",
                ).getText()
                date = b.find(
                    "p", class_="text-sm text-slate-500 dark:text-slate-400 font-normal"
                ).getText()

                try:
                    try:
                        desc = b.find(
                            "span",
                            class_="text-base hidden font-normal text-slate-500 dark:text-slate-400 hn-break-words cursor-pointer md:line-clamp-2",
                        ).getText()
                    except:
                        desc = b.find(
                            "span",
                            class_="text-base hidden font-normal text-slate-500 dark:text-slate-400 hn-break-words cursor-pointer md:line-clamp-3",
                        ).getText()
                except:
                    desc = ""

                link = (
                    b.find("div", class_="flex flex-col gap-1")
                    .find("div")
                    .find("a")["href"]
                )

                try:
                    like_count = b.find(
                        "button", attrs={"aria-label": "Like reaction"}
                    ).getText()
                except:
                    like_count = 0

                try:
                    comment_count = b.find(
                        "button", attrs={"aria-label": "Comment"}
                    ).getText()
                except:
                    comment_count = 0

                blogs_data["blogs"].append(
                    {
                        "title": title,
                        "description": desc,
                        "author": author,
                        "like_count": like_count,
                        "comment_count": comment_count,
                        "date": date,
                        "link": link,
                    }
                )
            return blogs_data["blogs"]
        except:
            return None
