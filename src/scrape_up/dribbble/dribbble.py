from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Dribbble:
    """
    Create an instance of `Dribbble` class.
    ```py
    shots = Dribbble()
    ```
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.get_shots()` | Returns the latest shots along with their title, designer and designer url like and view count and link. |
    | `.search(topic)` | Returns the latest shots along with their title, designer and designer url like and view count and link for the searched topic. |
    | `.get_animation()` | Returns the latest animation along with their title, designer and designer url like and view count and link. |
    | `.get_branding()` | Returns the latest branding along with their title, designer and designer url like and view count and link. |
    | `.get_illustration()` | Returns the latest illustration along with their title, designer and designer url like and view count and link. |
    | `.get_mobile()` | Returns the latest mobile shots along with their title, designer and designer url like and view count and link. |
    | `.get_webdesign()` | Returns the latest web-design shots along with their title, designer and designer url like and view count and link. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def get_shots(self):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.get_shots()
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/shots"
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                link = s.find(
                    "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                )["href"]

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None

    def search(self, topic):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.search(topic)
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/search/" + topic
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                try:
                    link = s.find(
                        "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                    )["href"]
                except:
                    link = ""

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None

    def get_animations(self):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.get_animations()
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/shots/popular/animation"
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                try:
                    link = s.find(
                        "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                    )["href"]
                except:
                    link = ""

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None

    def get_branding(self):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.get_branding()
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/shots/popular/branding"
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                try:
                    link = s.find(
                        "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                    )["href"]
                except:
                    link = ""

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None

    def get_illustration(self):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.get_illustration()
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/shots/popular/illustration"
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                try:
                    link = s.find(
                        "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                    )["href"]
                except:
                    link = ""

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None

    def get_mobile(self):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.get_mobile()
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/shots/popular/mobile"
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                try:
                    link = s.find(
                        "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                    )["href"]
                except:
                    link = ""

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None

    def get_webdesign(self):
        """
        Class - `Dribbble`
        Example -
        ```python
        dribbble = Dribbble()
        shots = dribbble.get_web-design()
        ```
        Return
        ```js
        [
            {
                'title': 'The full case study of Zelt project',
                'image_url': 'https://cdn.dribbble.com/userupload/9134517/file/still-85ff8d3aba6c58f20730e158a2afdd34.png?resize=400x0',
                'designer': 'Cuberto',
                'designer_url': 'https://www.dribbble.com//cuberto',
                'like_count': '152',
                'views_count': '10.2k',
                'link': 'https://www.dribbble.com//shots/22210785-The-full-case-study-of-Zelt-project'
            }
            ...
        ]
        ```
        """
        url = "https://dribbble.com/shots/popular/web-design"
        shots_data = {"shots": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            shots = soup.find_all(
                "li", class_="shot-thumbnail js-thumbnail shot-thumbnail-container"
            )

            for s in shots:
                title = s.find("div", class_="shot-title").getText().strip()
                img = s.find("img")["src"]
                designer = s.find("span", class_="display-name").getText()
                designer_url = s.find("a", rel="contact")["href"]
                try:
                    like = (
                        s.find(
                            "span",
                            class_="js-shot-likes-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    like = "0"
                try:
                    views = (
                        s.find(
                            "span",
                            class_="js-shot-views-count color-deep-blue-sea-light-20 font-weight-500",
                        )
                        .getText()
                        .strip()
                    )
                except:
                    views = "0"
                try:
                    link = s.find(
                        "a", class_="shot-thumbnail-link dribbble-link js-shot-link"
                    )["href"]
                except:
                    link = ""

                shots_data["shots"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "designer": designer,
                        "designer_url": "https://www.dribbble.com/" + designer_url,
                        "like_count": like,
                        "views_count": views,
                        "link": "https://www.dribbble.com/" + link,
                    }
                )
            return shots_data["shots"]
        except:
            return None
