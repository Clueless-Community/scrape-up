import requests
from bs4 import BeautifulSoup

class Devpost:
    """
    Create an instance of `Devpost` class.
    ```py
    posts = Devpost()
    ```
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.get_projects()` | Returns the latest projects along with their decription, like and commment count, image and member details. |
    """

    def get_projects(self):
        
        url = "https://devpost.com/software"
        projects_data = {"projects": []}
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            heads = soup.find_all("div", class_="large-3 small-12 columns gallery-item")
            for h in heads:
                members_list = []
                title = (
                    h.find("h5")
                    .getText()
                    .strip()
                )
                desc = (
                    h.find("p", class_="small tagline")
                    .getText()
                    .strip()
                )
                like = (
                    h.find("span", class_="count like-count")
                    .getText()
                    .strip()
                )
                comment_count = (
                    h.find("span", class_="count comment-count")
                    .getText()
                    .strip()
                )
                try:
                    img = h.find("img", alt=title)["src"]
                except:
                    img = ""
                members = h.find_all("span", class_="user-profile-link")
                for m in members:
                    name = m.find("img")["alt"]
                    avatar = m.find("img")["src"]
                    link = m["data-url"]
                    members_list.append({
                        "name": name,
                        "avatar_url": avatar,
                        "link": link
                    })
                projects_data["projects"].append(
                    {
                        "title": title,
                        "description": desc,
                        "like_count": like,
                        "comment_count": comment_count,
                        "img_url": img,
                        "members": members_list
                    }
                )
            return projects_data["projects"]
        except:
            return None
