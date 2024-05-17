from bs4 import BeautifulSoup
from pprint import pprint
import json

from scrape_up.config.request_config import RequestConfig, get


class DevCommunity:
    """
    Class - `DevCommunity`

    Creates a scraper for latest articles from https://www.dev.to.
    Creates a scraper for latest articles from https://www.dev.to/t/{tag} with a given tag.
    Creates a scraper for  user details, pinned articles written by a user, and all articles
    written by a user from https://www.dev.to/{username}.

    Example -
    ```python
    dev = DevCommunity('francescoxx')
    """

    def __init__(self, username: str, *, config: RequestConfig = RequestConfig()):
        self.help = "This scrapes articles from the DevCommunity website."
        self.username = username
        self.config = config

    def __scrape_page(self):
        try:
            data = get("https://www.dev.to", self.config)
            data.raise_for_status()
            data = BeautifulSoup(data.text, "html.parser")
            return data
        except:
            message = "An Error Occurred!"
            return message

    def all_articles(self):
        """
                Class - `DevCommunity`
        Example -
        ```python
        articles = dev.all_articles()
        pprint(articles)
        ```
        Return
        ```python
        return
        {
            "{'data': '{'
         '  "articles": ['
         '    {'
         '      "Title": "With GitHub apparently down right now...",'
         '      "Author": "Ben Halpern",'
         '      "Date": "Jun 29",'
         '      "Tags": "#watercooler\#github",'
         '      "Reactions": "22u00a0reactions",'
         '      "Comments": "Comments 6u00a0comments",'
         '      "Read Time": "2 min read"'
         '    },'
         '    {'
         '      "Title": "Sloan\'s Inbox: What is the Secret to a Truly Great '
         'Portfolio?",'
         '      "Author": "Sloan the DEV Moderator",'
         '      "Date": "Jun 29",'
         '      "Tags": '
         '"#discuss\#beginners\#career\#careerdevelopment",'
         '      "Reactions": "10u00a0reactions",'
         '      "Comments": "Comments              1u00a0comment",'
         '      "Read Time": "1 min read"'
         '    },'
         '    {'
         '      "Title": "Sticky sessions with Apache APISIX",'
         '      "Author": "Nicolas Frankel",'
         '      "Date": "Jun 29",'
         '      "Tags": '
         '"#stickysessions\#sessionaffinity\#apacheapisix\#devops",'
         '      "Reactions": "44u00a0reactions",'
         '      "Comments": "Comments\Addu00a0Comment",'
         '      "Read Time": "4 min read"'
         '    }
         '  ]'
         '}',
                'message': 'Successfully fetched all articles.'}

        ```
        """
        page = self.__scrape_page()
        articles_list = {"articles": []}
        try:
            articles = page.find_all(class_="substories")
            for x in articles:
                title = x.find_all(class_="crayons-story__title")
                author = x.find_all(
                    "a", class_="crayons-story__secondary fw-medium m:hidden"
                )
                date = x.find_all("a", class_="crayons-story__tertiary fs-xs")
                tags = x.find_all(class_="crayons-story__tags")
                reactions = x.find_all("span", class_="aggregate_reactions_counter")
                comments = x.find_all(
                    "a",
                    class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center",
                )
                readTime = x.find_all(class_="crayons-story__save")

            for (
                ti,
                a,
                d,
                ta,
                r,
                c,
                re,
            ) in zip(title, author, date, tags, reactions, comments, readTime):
                articles_list["articles"].append(
                    {
                        "Title": ti.text.strip(),
                        "Author": a.text.strip(),
                        "Date": d.text.strip(),
                        "Tags": ta.text.strip(),
                        "Reactions": r.text.strip(),
                        "Comments": c.text.strip(),
                        "Read Time": re.text.strip(),
                    }
                )
            json_data = json.dumps(articles_list, indent=2)
            return {"data": json_data, "message": "Successfully fetched all articles."}
        except:
            message = "An Error Occurred!"
            return message

    def __strTag__(self, tag: str):
        """
                Class - `DevCommunity`
        Example -
        ```python
        tag_name = dev.__strTag__(tag='python')
        print(tag_name)
        ```
        Return
        ```python
                The list of articles we want to scrape have the tag: python
        """
        self.tag = tag
        return f" The list of articles we want to scrape have the tag: {self.tag}"

    def __scrape_tag(self, tag: str):
        try:
            self.tag = tag
            data = get(f"https://www.dev.to/t/{self.tag}", self.config)
            data.raise_for_status()
            data = BeautifulSoup(data.text, "html.parser")
            return data
        except:
            message = "An Error Occurred!"
            return message

    def tag_articles(self, tag: str):
        """
                Class - `DevCommunity`
        Example -
        ```python
        tagged_articles = dev.tag_articles(tag='python')
        pprint(tagged_articles)
        ```
        Return
        ```python
                return
                {
                {'data': '{'
                '  "articles": ['
                '    {'
                '      "Title": "Introducing The Spatial Cypher Cheat Sheet",'
                '      "nAuthor": "William Lyon",'
                '      "Date": "Jun 28",'
                '      "Tags": "#neo4j\#python\#datascience\#gis",'
                '      "Reactions": "5u00a0reactions",'
                '      "Comments": "Comments\Addu00a0Comment",'
                '      "Read Time": "10 min read"'
                '    },'
                '    {'
                '      "Title": "Redis",'
                '      "nAuthor": "Phan Tu1ea5n Thu1eafng",'
                '      "Date": "Jun 28",'
                '      "Tags": "#devops\#python\#javascript\#tutorial",'
                '      "Reactions": "2u00a0reactions",'
                '      "Comments": "Comments\Addu00a0Comment",'
                '      "Read Time": "1 min read"'
                '    },'
                '    {'
                '      "Title": "Making a Cloud Resume",'
                '      "nAuthor": "Tristan Armbrister",'
                '      "Date": "Jun 27",'
                '      "Tags": "#cloud\#azure\#python\#webdev",'
                '      "Reactions": "5u00a0reactions",'
                '      "Comments": "Comments\Addu00a0Comment",'
                '      "Read Time": "7 min read"'
                '    },'
                ]'
                '}',
                'message': 'Successfully fetched all articles with the given tag.'
                }
        """
        self.tag = tag
        page = self.__scrape_tag(self.tag)
        articles_list = {"articles": []}
        try:
            articles = page.find_all(class_="substories")
            for x in articles:
                title = x.find_all(class_="crayons-story__title")
                author = x.find_all(
                    "a", class_="crayons-story__secondary fw-medium m:hidden"
                )
                date = x.find_all("a", class_="crayons-story__tertiary fs-xs")
                tags_ = x.find_all(class_="crayons-story__tags")
                reactions = x.find_all("span", class_="aggregate_reactions_counter")
                comments = x.find_all(
                    "a",
                    class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center",
                )
                readTime = x.find_all(class_="crayons-story__save")

            for (
                ti,
                a,
                d,
                ta,
                r,
                c,
                re,
            ) in zip(title, author, date, tags_, reactions, comments, readTime):
                articles_list["articles"].append(
                    {
                        "Title": ti.text.strip(),
                        "nAuthor": a.text.strip(),
                        "Date": d.text.strip(),
                        "Tags": ta.text.strip(),
                        "Reactions": r.text.strip(),
                        "Comments": c.text.strip(),
                        "Read Time": re.text.strip(),
                    }
                )
            json_data = json.dumps(articles_list, indent=2)
            return {
                "data": json_data,
                "message": "Successfully fetched all articles with the given tag.",
            }
        except:
            message = "An Error Occurred!"
            return message

    def __strUser__(self):
        """
                Class - `DevCommunity`
        Example -
        ```python
        user = dev.__strUser__()
                print(user)
        ```
        Return
        ```python
                The username is: francescoxx
        """
        return f" The username is: {self.username}"

    def __scrape_User(self):
        try:
            username = self.username
            data = get(f"https://www.dev.to/{username}", self.config)
            data.raise_for_status()
            data = BeautifulSoup(data.text, "html.parser")
            return data
        except:
            message = "An Error Occurred!"
            return message

    def user_details(self):
        """
                Class - `User`
        Example -
        ```python
        user_detail = dev.user_details()
        print(user_detail)
        ```
        Return
        ```python
                return
                {'data': [{'Name': 'Francesco Ciulla', 'Bio': 'Check YouTube: https://www.youtube.com/@francescociulla',
                'Address': ['Location', 'Rome,', 'Italy']}], 'message': 'Successfully fetched user details.'}
        """
        page = self.__scrape_User()
        user_details = []
        try:
            user = page.find(class_="profile-header__details")
            name = user.find(class_="crayons-title fw-heavy mb-2").text
            bio = user.find(
                class_="fs-base m:fs-l color-base-90 mb-4 mx-auto max-w-100 m:max-w-75"
            ).text
            address = user.find(class_="profile-header__meta__item").text.split()
            user_details.append({"Name": name, "Bio": bio, "Address": address})
            return {
                "data": user_details,
                "message": "Successfully fetched user details.",
            }
        except:
            message = "An Error Occurred!"
            return {"data": user_details, "message": message}

    def pinned_articles(self):
        """
                Class - `User`
        Example -
        ```python
        pin_articles = dev.pinned_articles()
                pprint(pin_articles)
        ```
        Return
        ```python
                return
                {'data': '{'
                '  "articles": ['
                '    {'
                '      "Title": "Rust ud83eudd80 CRUD Rest API with Docker '
                'ud83dudc33",'
                '      "Date": "May 4",'
                '      "Tags": "#rust\#webdev\#beginners\#devops",'
                '      "Reactions": "129u00a0reactions",'
                '      "Comments": "Comments              37u00a0comments",'
                '      "Read Time": "15 min read"'
                '    },'
                '    {'
                '      "Title": "TypeScript CRUD Rest API, using Nest.js, TypeORM, '
                'Postgres, Docker and Docker Compose",'
                '      "Date": "Mar 26",'
                '      "Tags": "#typescript\#webdev\#beginners\#programming",'
                '      "Reactions": "231u00a0reactions",'
                '      "Comments": "Comments              16u00a0comments",'
                '      "Read Time": "11 min read"'
                '    },'
                '    {'
                '      "Title": "How to Learn Web3",'
                '      "Date": "Sep 1 \'22",'
                '      "Tags": "#web3\#blockchain\#beginners\#programming",'
                '      "Reactions": "494u00a0reactions",'
                '      "Comments": "Comments              49u00a0comments",'
                '      "Read Time": "10 min read"'
                '    }'
                '  ]'
                '}',
                'message': 'Successfully fetched pinned articles.'}
        """
        try:
            page = self.__scrape_User()
            articles_list = {"articles": []}
            articles = page.find_all(
                class_="crayons-card mb-2 border-2 border-solid border-accent-brand"
            )

            for article in articles:
                title = article.find_all(class_="crayons-story__title")
                date = article.find_all("a", class_="crayons-story__tertiary fs-xs")
                tags = article.find_all(class_="crayons-story__tags")
                reactions = article.find_all(
                    "span", class_="aggregate_reactions_counter"
                )
                comments = article.find_all(
                    "a",
                    class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center",
                )
                readTime = article.find_all(class_="crayons-story__save")

            for (
                ti,
                d,
                ta,
                r,
                c,
                re,
            ) in zip(title, date, tags, reactions, comments, readTime):
                articles_list["articles"].append(
                    {
                        "Title": ti.text.strip(),
                        "Date": d.text.strip(),
                        "Tags": ta.text.strip(),
                        "Reactions": r.text.strip(),
                        "Comments": c.text.strip(),
                        "Read Time": re.text.strip(),
                    }
                )
            json_data = json.dumps(articles_list, indent=2)
            return {
                "data": json_data,
                "message": "Successfully fetched pinned articles.",
            }

        except:
            message = "An Error Occurred!"
            return {"data": json_data, "message": message}

    def user_articles(self):
        """
                Class - `User`
        Example -
        ```python
        user_article = dev.user_articles()
                pprint(user_article)
        ```
        Return
        ```python
                return
                {'data': '{'
                '  "articles": ['
                '    {'
                '      "Title": "Rust ud83eudd80 CRUD Rest API with Docker '
                'ud83dudc33",'
                '      "Date": "May 4",'
                '      "Tags": "#rust",'
                '      "Reactions": "129u00a0reactions",'
                '      "Comments": "Comments              37u00a0comments",'
                '      "Read Time": "15 min read"'
                '    },'
                '    {'
                '      "Title": "Kubernetes quick tutorial",'
                '      "Date": "Apr 18",'
                '      "Tags": "#webdev",'
                '      "Reactions": "55u00a0reactions",'
                '      "Comments": "Comments              11u00a0comments",'
                '      "Read Time": "5 min read"'
                '    },'
                '    {'
                '      "Title": "TypeScript CRUD Rest API, using Nest.js, TypeORM, '
                'Postgres, Docker and Docker Compose",'
                '      "Date": "Mar 26",'
                '      "Tags": "#beginners",'
                '      "Reactions": "231u00a0reactions",'
                '      "Comments": "Comments              16u00a0comments",'
                '      "Read Time": "11 min read"'
                '    },'
                '  ]'
                '}',
                'message': 'Successfully fetched all articles.'}
        """
        page = self.__scrape_User()
        articles_list = {"articles": []}
        try:
            articles = page.find_all(class_="substories")
            for article in articles:
                date = article.find_all(class_="crayons-story__tertiary fs-xs")
                title = article.find_all(class_="crayons-story__title")
                tags = article.find_all(class_="crayons-tag crayons-tag--monochrome")
                reactions = article.find_all(class_="aggregate_reactions_counter")
                comments = article.find_all(
                    "a",
                    class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center",
                )
                readTime = article.find_all(class_="crayons-story__tertiary fs-xs mr-2")

            for (
                ti,
                d,
                ta,
                r,
                c,
                re,
            ) in zip(title, date, tags, reactions, comments, readTime):
                articles_list["articles"].append(
                    {
                        "Title": ti.text.strip(),
                        "Date": d.text.strip(),
                        "Tags": ta.text.strip(),
                        "Reactions": r.text.strip(),
                        "Comments": c.text.strip(),
                        "Read Time": re.text.strip(),
                    }
                )
            json_data = json.dumps(articles_list, indent=2)

            return {"data": json_data, "message": "Successfully fetched all articles."}

        except:
            message = "An Error Occurred!"
            return {"data": json_data, "message": message}


dev = DevCommunity("francescoxx")
articles = dev.all_articles()
pprint(articles)

tag_name = dev.__strTag__(tag="python")
tagged_articles = dev.tag_articles(tag="python")
print(tag_name)
pprint(tagged_articles)

user = dev.__strUser__()
user_detail = dev.user_details()
pin_articles = dev.pinned_articles()
user_article = dev.user_articles()
print(user)
print(user_detail)
pprint(pin_articles)
pprint(user_article)
