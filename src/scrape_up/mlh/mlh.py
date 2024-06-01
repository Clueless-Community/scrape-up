from bs4 import BeautifulSoup
from scrape_up.config.request_config import RequestConfig, get
import json
class MLH:
    """
    Create an instance of the class `GeeksforGeeks`
    ```py
    mlh = MLH(year="2024")
    mlh.get_events()
    ```

    | Methods           | Details                                                                            |
    | ----------------- | ---------------------------------------------------------------------------------- |
    | `.get_events()`  | Returns the upcoming event ,past event,ongoing event.                                              |

    """
    def __init__(self, year: str, *, config: RequestConfig = RequestConfig()):
        headers = {"User-Agent": "scrapeup"}
        self.config = config
        self.year= year
        if self.config.headers == {}:
            self.config.set_headers(headers)
    def get_events(self):
        try:
            url = f"https://mlh.io/seasons/{self.year}/events"
            response = get(url, self.config)
            soup = BeautifulSoup(response.text, "html.parser")
            main_info=soup.find_all('div',class_="container feature")
            events=main_info[1]
            types=events.find_all('div',class_='row')
            e=[]
            for t in types:
                h=t.find('h3',class_='text-center mb-3')
                
                if(h):
                    d=[]
                    evs=t.find_all('div',class_='event')
                    for ev in evs:
                        name=ev.find('h3',class_='event-name').text.strip()
                        date=ev.find('p',class_='event-date').text.strip()
                        location=ev.find('div',class_='event-location').text.strip().replace('\n'," ").replace('           '," ")
                        mode=ev.find('div',class_='event-hybrid-notes').text.strip()
                        d.append({'name':name,'location':location,'date':date,'mode':mode})
                    e.append({h.text.strip():d})

            return (json.dumps(e))
        except Exception as e:
            return None


"""
    response example:

    [
  {
    "Upcoming Events": [
      {
        "name": "Global Hack Week: Web3",
        "location": "Everywhere, Online",
        "date": "Jun 7th - 13th",
        "mode": "Digital Only"
      },
      {
        "name": "JAMHacks 8",
        "location": "Waterloo, Ontario",
        "date": "Jun 7th - 9th",
        "mode": "In-Person Only"
      },
      {
        "name": "Hack Your Portfolio",
        "location": "Everywhere, Worldwide",
        "date": "Jun 14th - 16th",
        "mode": "Digital Only"
      }
    ]
  },
  {
    "Past Events": [
      {
        "name": "TechTogether Online",
        "location": "Everywhere, Worldwide",
        "date": "Jul 14th - 16th",
        "mode": "Digital Only"
      },
      {
        "name": "Hacks for Hackers",
        "location": "Everywhere, Worldwide",
        "date": "Jul 21st - 23rd",
        "mode": "Digital Only"
      },
      {
        "name": "HackBattle: React vs Angular",
        "location": "Everywhere, Worldwide",
        "date": "Jul 28th - 30th",
        "mode": "Digital Only"
      },
      {
        "name": "Global Hack Week: Data",
        "location": "Everywhere, Worldwide",
        "date": "Jul 31st - Aug 7th",
        "mode": "Digital Only"
      },
      {
        "name": "TechTogether Online",
        "location": "Everywhere, Worldwide",
        "date": "Aug 4th - 6th",
        "mode": "Digital Only"
      }
    ]
  }
]
"""
            