from bs4 import BeautifulSoup
from pprint import pprint
import json
import requests

class DevCommunity:
    """
    Class - `DevCommunity` \n

    Creates a scraper for latest articles from https://www.dev.to.
    Creates a scraper for latest articles from https://www.dev.to/t/{tag} with a given tag.
    Creates a scraper for  user details, pinned articles written by a user, and all articles 
    written by a user from https://www.dev.to/{username}.

    Example - \n
    ```python
    dev = DevCommunity('python','francescoxx')
    """
    def __init__(self, tag: str, username: str):
        self.help = "This scrapes articles from the DevCommunity website."
        self.tag = tag
        self.username = username

    
    def __scrape_page(self):
        try:
            data = requests.get('https://www.dev.to')
            data.raise_for_status()
            data = BeautifulSoup(data.text, "html.parser")
            return data
        except:
            message = "An Error Occurred!"
            return message
    
    def all_articles(self):
        """
		Class - `DevCommunity` \n
        Example - \n
        ```python
        articles = dev.all_articles()
        pprint(articles)
        ```
        Return \n
        ```python
        return 
        {
            "{'data': '{\n'
         '  "articles": [\n'
         '    {\n'
         '      "Title": "With GitHub apparently down right now...",\n'       
         '      "Author": "Ben Halpern",\n'
         '      "Date": "Jun 29",\n'
         '      "Tags": "#watercooler\\n#github",\n'
         '      "Reactions": "22\\u00a0reactions",\n'
         '      "Comments": "Comments\\n\\n              6\\u00a0comments",\n'
         '      "Read Time": "2 min read"\n'
         '    },\n'
         '    {\n'
         '      "Title": "Sloan\'s Inbox: What is the Secret to a Truly Great '
         'Portfolio?",\n'
         '      "Author": "Sloan the DEV Moderator",\n'
         '      "Date": "Jun 29",\n'
         '      "Tags": '
         '"#discuss\\n#beginners\\n#career\\n#careerdevelopment",\n'
         '      "Reactions": "10\\u00a0reactions",\n'
         '      "Comments": "Comments\\n\\n              1\\u00a0comment",\n'  
         '      "Read Time": "1 min read"\n'
         '    },\n'
         '    {\n'
         '      "Title": "Sticky sessions with Apache APISIX",\n'
         '      "Author": "Nicolas Frankel",\n'
         '      "Date": "Jun 29",\n'
         '      "Tags": '
         '"#stickysessions\\n#sessionaffinity\\n#apacheapisix\\n#devops",\n'
         '      "Reactions": "44\\u00a0reactions",\n'
         '      "Comments": "Comments\\nAdd\\u00a0Comment",\n'
         '      "Read Time": "4 min read"\n'
         '    }
         '  ]\n'
         '}',
 		'message': 'Successfully fetched all articles.'}
        
        ```
		"""
        page = self.__scrape_page()
        articles_list = {"articles": []}
        try:
            articles = page.find_all( class_="substories")
            for x in articles:
                title = x.find_all(class_="crayons-story__title")        
                author = x.find_all('a', class_="crayons-story__secondary fw-medium m:hidden")
                date = x.find_all('a', class_="crayons-story__tertiary fs-xs")       
                tags = x.find_all(class_="crayons-story__tags")
                reactions = x.find_all('span', class_="aggregate_reactions_counter")        
                comments = x.find_all('a',class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center")        
                readTime = x.find_all(class_="crayons-story__save")
    
            for ti,a,d,ta,r,c,re, in zip(title, author, date, tags, reactions, comments, readTime):
                articles_list["articles"].append({
                "Title": ti.text.strip(),
                "Author": a.text.strip(),
                "Date": d.text.strip(),
                "Tags": ta.text.strip(),
                "Reactions": r.text.strip(),
                "Comments": c.text.strip(),
                "Read Time": re.text.strip(),
            })
            json_data = json.dumps(articles_list, indent=2)
            return {"data": json_data, "message": "Successfully fetched all articles."}
        except:
            message = "An Error Occurred!"
            return message


    def __strTag__(self):
        """
		Class - `DevCommunity` \n
    	Example - \n
    	```python
        tag_name = dev.__strTag__() 
        print(tag_name)
        ```
        Return \n
        ```python
		The list of articles we want to scrape have the tag: python
		"""
        return f" The list of articles we want to scrape have the tag: {self.tag}"
    
    def __scrape_tag(self):
        try:
            tag = self.tag
            data = requests.get(f"https://www.dev.to/t/{tag}")
            data.raise_for_status()
            data = BeautifulSoup(data.text, "html.parser")
            return data
        except:
            message = "An Error Occurred!"
            return message
    
    
    def tag_articles(self):
        """
		Class - `DevCommunity` \n
    	Example - \n
    	```python
        tagged_articles = dev.tag_articles()
        pprint(tagged_articles)
        ```
        Return \n
        ```python
		return
		{
		{'data': '{\n'
		'  "articles": [\n'
		'    {\n'
		'      "Title": "Introducing The Spatial Cypher Cheat Sheet",\n'
		'      "nAuthor": "William Lyon",\n'
		'      "Date": "Jun 28",\n'
		'      "Tags": "#neo4j\\n#python\\n#datascience\\n#gis",\n'
		'      "Reactions": "5\\u00a0reactions",\n'
		'      "Comments": "Comments\\nAdd\\u00a0Comment",\n'
		'      "Read Time": "10 min read"\n'
		'    },\n'
		'    {\n'
		'      "Title": "Redis",\n'
		'      "nAuthor": "Phan T\\u1ea5n Th\\u1eafng",\n'
		'      "Date": "Jun 28",\n'
		'      "Tags": "#devops\\n#python\\n#javascript\\n#tutorial",\n'
		'      "Reactions": "2\\u00a0reactions",\n'
		'      "Comments": "Comments\\nAdd\\u00a0Comment",\n'
		'      "Read Time": "1 min read"\n'
		'    },\n'
		'    {\n'
		'      "Title": "Making a Cloud Resume",\n'
		'      "nAuthor": "Tristan Armbrister",\n'
		'      "Date": "Jun 27",\n'
		'      "Tags": "#cloud\\n#azure\\n#python\\n#webdev",\n'
		'      "Reactions": "5\\u00a0reactions",\n'
		'      "Comments": "Comments\\nAdd\\u00a0Comment",\n'
		'      "Read Time": "7 min read"\n'
		'    },\n'
		]\n'
		'}',
 		'message': 'Successfully fetched all articles with the given tag.'
		}
		"""
        page = self.__scrape_tag()
        articles_list = {"articles": []}
        try:
            articles = page.find_all( class_="substories")
            for x in articles:
                title = x.find_all(class_="crayons-story__title")        
                author = x.find_all('a', class_="crayons-story__secondary fw-medium m:hidden")
                date = x.find_all('a', class_="crayons-story__tertiary fs-xs")       
                tags_ = x.find_all(class_="crayons-story__tags")
                reactions = x.find_all('span', class_="aggregate_reactions_counter")        
                comments = x.find_all('a',class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center")        
                readTime = x.find_all(class_="crayons-story__save")
    
            for ti,a,d,ta,r,c,re, in zip(title, author, date, tags_, reactions, comments, readTime):
                articles_list["articles"].append({
                "Title": ti.text.strip(),
                "nAuthor": a.text.strip(),
                "Date": d.text.strip(),
                "Tags": ta.text.strip(),
                "Reactions": r.text.strip(),
                "Comments": c.text.strip(),
                "Read Time": re.text.strip(),
            })
            json_data = json.dumps(articles_list, indent=2)
            return {"data": json_data, "message": "Successfully fetched all articles with the given tag."}
        except:
            message = "An Error Occurred!"
            return message


    def __strUser__(self):
        """
		Class - `DevCommunity` \n
    	Example - \n
    	```python
        user = dev.__strUser__()
		print(user)
        ```
        Return \n
        ```python
		The username is: francescoxx
		"""
        return f" The username is: {self.username}"

    def __scrape_User(self):
        try:
            username = self.username 
            data = requests.get(f"https://www.dev.to/{username}")
            data.raise_for_status()
            data = BeautifulSoup(data.text, "html.parser")
            return data
        except:
            message = "An Error Occurred!"
            return message

    def user_details(self):
        """
		Class - `User` \n
    	Example - \n
    	```python        
        user_detail = dev.user_details()
        print(user_detail)
        ```
        Return \n
        ```python
		return
		{'data': [{'Name': 'Francesco Ciulla', 'Bio': 'Check YouTube: https://www.youtube.com/@francescociulla\n', 
		'Address': ['Location', 'Rome,', 'Italy']}], 'message': 'Successfully fetched user details.'}
		"""
        page = self.__scrape_User()
        user_details = []
        try:	
            user = page.find(class_="profile-header__details")
            name = user.find(class_="crayons-title fw-heavy mb-2").text
            bio = user.find(class_="fs-base m:fs-l color-base-90 mb-4 mx-auto max-w-100 m:max-w-75").text
            address = user.find(class_="profile-header__meta__item").text.split()
            user_details.append({"Name": name, "Bio": bio, "Address": address})
            return {"data": user_details, "message": "Successfully fetched user details."}		
        except:
            message = "An Error Occurred!"
            return {"data": user_details, "message": message}

    def pinned_articles(self):	
        """
		Class - `User` \n
    	Example - \n
    	```python
        pin_articles = dev.pinned_articles()
		pprint(pin_articles)
        ```
        Return \n
        ```python
		return
		{'data': '{\n'
		'  "articles": [\n'
		'    {\n'
		'      "Title": "Rust \\ud83e\\udd80 CRUD Rest API with Docker '
		'\\ud83d\\udc33",\n'
		'      "Date": "May 4",\n'
		'      "Tags": "#rust\\n#webdev\\n#beginners\\n#devops",\n'
		'      "Reactions": "129\\u00a0reactions",\n'
		'      "Comments": "Comments\\n\\n              37\\u00a0comments",\n'
		'      "Read Time": "15 min read"\n'
		'    },\n'
		'    {\n'
		'      "Title": "TypeScript CRUD Rest API, using Nest.js, TypeORM, '
		'Postgres, Docker and Docker Compose",\n'
		'      "Date": "Mar 26",\n'
		'      "Tags": "#typescript\\n#webdev\\n#beginners\\n#programming",\n'
		'      "Reactions": "231\\u00a0reactions",\n'
		'      "Comments": "Comments\\n\\n              16\\u00a0comments",\n'
		'      "Read Time": "11 min read"\n'
		'    },\n'
		'    {\n'
		'      "Title": "How to Learn Web3",\n'
		'      "Date": "Sep 1 \'22",\n'
		'      "Tags": "#web3\\n#blockchain\\n#beginners\\n#programming",\n'
		'      "Reactions": "494\\u00a0reactions",\n'
		'      "Comments": "Comments\\n\\n              49\\u00a0comments",\n'
		'      "Read Time": "10 min read"\n'
		'    }\n'
		'  ]\n'
		'}',
 		'message': 'Successfully fetched pinned articles.'}
		"""
        try:
            page = self.__scrape_User()
            articles_list = {"articles": []}
            articles = page.find_all(class_="crayons-card mb-2 border-2 border-solid border-accent-brand")
            
            for article in articles:
                title = article.find_all(class_="crayons-story__title")
                date = article.find_all('a', class_="crayons-story__tertiary fs-xs")
                tags = article.find_all(class_="crayons-story__tags")
                reactions = article.find_all('span', class_="aggregate_reactions_counter")
                comments = article.find_all('a',class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center")
                readTime = article.find_all(class_="crayons-story__save")
                
            for ti,d,ta,r,c,re, in zip(title, date, tags, reactions, comments, readTime):
                articles_list["articles"].append({
                "Title": ti.text.strip(),
                "Date": d.text.strip(),
                "Tags": ta.text.strip(),
                "Reactions": r.text.strip(),
                "Comments": c.text.strip(),
                "Read Time": re.text.strip(),
            })
            json_data = json.dumps(articles_list, indent=2)
            return {"data": json_data, "message": "Successfully fetched pinned articles."}

        except:
                message = "An Error Occurred!"
                return {"data": json_data, "message": message}

    def user_articles(self):
        """
		Class - `User` \n
    	Example - \n
    	```python
        user_article = dev.user_articles()
		pprint(user_article)
        ```
        Return \n
        ```python
		return
		{'data': '{\n'
		'  "articles": [\n'
		'    {\n'
		'      "Title": "Rust \\ud83e\\udd80 CRUD Rest API with Docker '
		'\\ud83d\\udc33",\n'
		'      "Date": "May 4",\n'
		'      "Tags": "#rust",\n'
		'      "Reactions": "129\\u00a0reactions",\n'
		'      "Comments": "Comments\\n\\n              37\\u00a0comments",\n'
		'      "Read Time": "15 min read"\n'
		'    },\n'
		'    {\n'
		'      "Title": "Kubernetes quick tutorial",\n'
		'      "Date": "Apr 18",\n'
		'      "Tags": "#webdev",\n'
		'      "Reactions": "55\\u00a0reactions",\n'
		'      "Comments": "Comments\\n\\n              11\\u00a0comments",\n'
		'      "Read Time": "5 min read"\n'
		'    },\n'
		'    {\n'
		'      "Title": "TypeScript CRUD Rest API, using Nest.js, TypeORM, '
		'Postgres, Docker and Docker Compose",\n'
		'      "Date": "Mar 26",\n'
		'      "Tags": "#beginners",\n'
		'      "Reactions": "231\\u00a0reactions",\n'
		'      "Comments": "Comments\\n\\n              16\\u00a0comments",\n'
		'      "Read Time": "11 min read"\n'
		'    },\n'
		'  ]\n'
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
                comments = article.find_all('a',class_="crayons-btn crayons-btn--s crayons-btn--ghost crayons-btn--icon-left flex items-center")
                readTime = article.find_all(class_="crayons-story__tertiary fs-xs mr-2")

            for ti,d,ta,r,c,re, in zip(title, date, tags, reactions, comments, readTime):
                articles_list["articles"].append({
                "Title": ti.text.strip(),
                "Date": d.text.strip(),
                "Tags": ta.text.strip(),
                "Reactions": r.text.strip(),
                "Comments": c.text.strip(),
                "Read Time": re.text.strip(),
            })
            json_data = json.dumps(articles_list, indent=2)
            
            return {"data": json_data, "message": "Successfully fetched all articles."}

        except:
                message = "An Error Occurred!"
                return {"data": json_data, "message": message}
            


dev = DevCommunity('python','francescoxx')
articles = dev.all_articles()
pprint(articles)

tag_name = dev.__strTag__()
tagged_articles = dev.tag_articles()
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

    