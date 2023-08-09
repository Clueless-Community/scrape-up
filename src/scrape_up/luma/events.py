import requests
from bs4 import BeautifulSoup


class Events:
    

    def get_events(self):
        """
        Class - `Events`
        Example -
        ```python
        luma = Events()
        events = luma.get_events()
        ```
        Return
        ```js
        [
            {
                'title': 'Brexfast Club',
                'organizer': 'By Shai Goldman & Alexandra Settlemyer',
                'location': 'Register to See Location',
                'img_url': 'https://images.lumacdn.com/cdn-cgi/image/format=auto,fit=cover,dpr=2,quality=75,width=200,height=100/event-covers/gd/45c21ae7-67f6-40c7-8820-1cb57ea14705',
                'price': 'Sold Out',
                'link': 'https://lu.ma//nycaug9'
            }
            ...
        ]
        ```
        """
        url = "https://lu.ma/nyc"
        events_data = {"events": []}
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.content, "html.parser")
            cards = soup.find_all("div", class_="jsx-3249095655 card-wrapper")

            for c in cards:
                title = c.find("a")["aria-label"]
                base = c.find_all("div", class_="jsx-3575689807 min-width-0")
                organizer = base[0].getText()
                loc = base[1].getText()
                try:
                    price = c.find("div", class_="jsx-146954525 pill-label").getText()
                except:
                    price = ""
                img = c.find("div", class_="jsx-4068354093 img-aspect-ratio rounded").find("img")["src"]
                link = c.find("a")["href"]
                events_data["events"].append(
                    {
                        "title": title,
                        "organizer": organizer,
                        "location": loc,
                        "img_url": img,
                        "price": price,
                        "link": "https://lu.ma/" + link
                    }
                )
            return events_data["events"]
        except:
            return None

luma = Events()
print(luma.get_events())