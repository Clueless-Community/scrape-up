import requests
from bs4 import BeautifulSoup


class Reddit:
    """
    Create an instance of `Reddit` class.
    ```python
    posts = Reddit()
    ```

    | Methods      | Details                                                                                                                         |
    | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
    | `.getFeed()` | Returns the posts with title, descriptions, subreddit, subreddit avatar, time, vote and comment count, image, category and link |
    | `.get_best()` | Returns the best posts with title, descriptions, subreddit, subreddit avatar, time, vote and comment count, image, category and link |
    | `.get_hot()` | Returns the hot posts with title, descriptions, subreddit, subreddit avatar, time, vote and comment count, image, category and link |
    | `.get_top()` | Returns the top posts with title, descriptions, subreddit, subreddit avatar, time, vote and comment count, image, category and link |
    """

    def getFeed(self):
        """
        Class - `Reddit`
        Example:
        ```python
        posts = Reddit()
        posts.getFeed()
        ```
        Returns:
        ```js
        {
            "title": Title of the post
            "description": Description of the post
            "subreddit": subreddit name,
            "subreddit_avatar": subreddit avatar,
            "time": Time the post was posted,
            "vote_count": No. of votes of the post,
            "comment_count": No. of comments of the post,
            "img_url": URL of any image provided in the post,
            "category": Category of the post,
        }
        ```
        """
        url = "https://www.reddit.com/"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            posts_data = {"posts": []}

            posts = soup.find_all("div", attrs={"data-testid": "post-container"})

            for p in posts:
                base = p.find("a", attrs={"data-click-id": "subreddit"})
                subreddit = base["href"]
                subreddit_avatar = base.find("img")["src"]
                title = p.find("h3", class_="_eYtD2XCVieq6emjKBH3m").getText()
                try:
                    desc = p.find("p").getText()
                except:
                    desc = ""
                votes = p.find(
                    "div", class_="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"
                ).getText()
                time = p.find("span", class_="_2VF2J19pUIMSLJFky-7PEI").getText()
                comment_count = p.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").getText()
                try:
                    img = p.find("img", alt="Post image")["src"]
                except:
                    img = ""
                try:
                    category = p.find(
                        "span",
                        class_="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N",
                    ).getText()
                except:
                    category = ""
                link = p.find(
                    "a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"
                )["href"]

                posts_data["posts"].append(
                    {
                        "title": title,
                        "description": desc,
                        "subreddit": subreddit,
                        "subreddit_avatar": subreddit_avatar,
                        "time": time,
                        "vote_count": votes,
                        "comment_count": comment_count,
                        "img_url": img,
                        "category": category,
                        "link": link,
                    }
                )
            return posts_data
        except:
            return None

    def get_best(self):
        """
        Class - `Reddit`
        Example:
        ```python
        posts = Reddit()
        posts.get_best()
        ```
        Returns:
        ```js
        [
            {
                "title":"This is Child abuse. Who gave them permission to procreate?",
                "description":"",
                "subreddit":"/r/facepalm/",
                "subreddit_avatar":"https://styles.redditmedia.com/t5_2r5rp/styles/communityIcon_2c4ms7mggreb1.png",
                "time":"13 hours ago",
                "vote_count":"28.0k",
                "comment_count":"2.5k comments",
                "img_url":"https://preview.redd.it/75z7yw2hlyeb1.png?width=640&crop=smart&auto=webp&s=70556d4e2753676d9d4d23207321235ab1c0c28e",
                "category":"",
                "link":"/r/facepalm/comments/15d18ak/this_is_child_abuse_who_gave_them_permission_to/"
            }
            ...
        ]
        ```
        """
        url = "https://www.reddit.com/r/popular/best/?feedViewType=classicView"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            posts_data = {"posts": []}

            posts = soup.find_all("div", attrs={"data-testid": "post-container"})

            for p in posts:
                base = p.find("a", attrs={"data-click-id": "subreddit"})
                subreddit = base["href"]
                subreddit_avatar = base.find("img")["src"]
                title = p.find("h3", class_="_eYtD2XCVieq6emjKBH3m").getText()
                try:
                    desc = p.find("p").getText()
                except:
                    desc = ""
                votes = p.find(
                    "div", class_="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"
                ).getText()
                time = p.find("span", class_="_2VF2J19pUIMSLJFky-7PEI").getText()
                comment_count = p.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").getText()
                try:
                    img = p.find("img", alt="Post image")["src"]
                except:
                    img = ""
                try:
                    category = p.find(
                        "span",
                        class_="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N",
                    ).getText()
                except:
                    category = ""
                link = p.find(
                    "a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"
                )["href"]

                posts_data["posts"].append(
                    {
                        "title": title,
                        "description": desc,
                        "subreddit": subreddit,
                        "subreddit_avatar": subreddit_avatar,
                        "time": time,
                        "vote_count": votes,
                        "comment_count": comment_count,
                        "img_url": img,
                        "category": category,
                        "link": link,
                    }
                )
            return posts_data["posts"]
        except:
            return None

    def get_hot(self):
        """
        Class - `Reddit`
        Example:
        ```python
        posts = Reddit()
        posts.get_hot()
        ```
        Returns:
        ```js
        [
            {
                "title":"Catching a ball while smoking and looking cool",
                "description":"",
                "subreddit":"/r/nextfuckinglevel/",
                "subreddit_avatar":"https://styles.redditmedia.com/t5_m0bnr/styles/communityIcon_qanlm185crr71.png",
                "time":"7 hours ago",
                "vote_count":"2.4k",
                "comment_count":"80 comments",
                "img_url":"",
                "category":"",
                "link":"/r/nextfuckinglevel/comments/15d9yg7/catching_a_ball_while_smoking_and_looking_cool/"
            }
            ...
        ]
        ```
        """
        url = "https://www.reddit.com/r/popular/hot/?feedViewType=cardView"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            posts_data = {"posts": []}

            posts = soup.find_all("div", attrs={"data-testid": "post-container"})

            for p in posts:
                base = p.find("a", attrs={"data-click-id": "subreddit"})
                subreddit = base["href"]
                subreddit_avatar = base.find("img")["src"]
                title = p.find("h3", class_="_eYtD2XCVieq6emjKBH3m").getText()
                try:
                    desc = p.find("p").getText()
                except:
                    desc = ""
                votes = p.find(
                    "div", class_="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"
                ).getText()
                time = p.find("span", class_="_2VF2J19pUIMSLJFky-7PEI").getText()
                comment_count = p.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").getText()
                try:
                    img = p.find("img", alt="Post image")["src"]
                except:
                    img = ""
                try:
                    category = p.find(
                        "span",
                        class_="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N",
                    ).getText()
                except:
                    category = ""
                link = p.find(
                    "a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"
                )["href"]

                posts_data["posts"].append(
                    {
                        "title": title,
                        "description": desc,
                        "subreddit": subreddit,
                        "subreddit_avatar": subreddit_avatar,
                        "time": time,
                        "vote_count": votes,
                        "comment_count": comment_count,
                        "img_url": img,
                        "category": category,
                        "link": link,
                    }
                )
            return posts_data["posts"]
        except:
            return None

    def get_top(self):
        """
        Class - `Reddit`
        Example:
        ```python
        posts = Reddit()
        posts.get_top()
        ```
        Returns:
        ```js
        {
            "title": Title of the post
            "description": Description of the post
            "subreddit": subreddit name,
            "subreddit_avatar": subreddit avatar,
            "time": Time the post was posted,
            "vote_count": No. of votes of the post,
            "comment_count": No. of comments of the post,
            "img_url": URL of any image provided in the post,
            "category": Category of the post,
        }
        ```
        """
        url = "https://www.reddit.com/r/popular/top/"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            posts_data = {"posts": []}

            posts = soup.find_all("div", attrs={"data-testid": "post-container"})
            for p in posts:
                base = p.find("a", attrs={"data-click-id": "subreddit"})
                subreddit = base["href"]
                subreddit_avatar = base.find("img")["src"]
                title = p.find("h3", class_="_eYtD2XCVieq6emjKBH3m").getText()
                try:
                    desc = p.find("p").getText()
                except:
                    desc = ""
                votes = p.find(
                    "div", class_="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"
                ).getText()
                time = p.find("span", class_="_2VF2J19pUIMSLJFky-7PEI").getText()
                comment_count = p.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").getText()
                try:
                    img = p.find("img", alt="Post image")["src"]
                except:
                    img = ""
                try:
                    category = p.find(
                        "span",
                        class_="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N",
                    ).getText()
                except:
                    category = ""
                link = p.find(
                    "a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"
                )["href"]
                posts_data["posts"].append(
                    {
                        "title": title,
                        "description": desc,
                        "subreddit": subreddit,
                        "subreddit_avatar": subreddit_avatar,
                        "time": time,
                        "vote_count": votes,
                        "comment_count": comment_count,
                        "img_url": img,
                        "category": category,
                        "link": link,
                    }
                )
            return posts_data["posts"]
        except:
            return None