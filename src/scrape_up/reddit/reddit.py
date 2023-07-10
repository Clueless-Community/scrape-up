import requests
from bs4 import BeautifulSoup


class Reddit:
   

    def getFeed(self):
        
        url = "https://www.reddit.com/"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            posts_data = {"posts": []}

            posts = soup.find_all("div", attrs={'data-testid': 'post-container'})

            for p in posts:
                base = p.find("a", attrs={'data-click-id': 'subreddit'})
                subreddit = base["href"]
                subreddit_avatar = base.find("img")["src"]
                title = p.find("h3", class_="_eYtD2XCVieq6emjKBH3m").getText()
                try:
                    desc = p.find("p").getText()
                except:
                    desc = ""
                votes = p.find("div", class_="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo").getText()
                time = p.find("span", class_="_2VF2J19pUIMSLJFky-7PEI").getText()
                comment_count = p.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").getText()
                try:
                    img = p.find("img", alt="Post image")["src"]
                except:
                    img = ""
                try:
                    category = p.find("span", class_="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N").getText()
                except:
                    category = ""
                link = p.find("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")["href"]

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
                        "link": link
                    }
                )
            return posts_data
        except:
            return None
