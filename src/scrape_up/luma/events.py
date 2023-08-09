import requests
from bs4 import BeautifulSoup


class Events:
    

    def get_events(self):
        
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