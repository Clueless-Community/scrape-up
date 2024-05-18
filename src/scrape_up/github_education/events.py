from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class Events:
    """
    Create an instance of `Events` class.
    ```py
    events = Events()
    ```
    | Methods            | Details                                                                                                              |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------- |
    | `.get_events()` | Returns the latest events along with their title, image_url, description, date, location, language, tags and link. |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def get_events(self):
        """
        Class - `Events`
        Example -
        ```python
        git = Events()
        events = git.get_events()
        ```
        Return
        ```js
        [
            {
                'title': 'GirlScript Summer of Code 2023',
                'image_url': '/assets/global_campus/global-campus-event-3-38fbf275c678987e40b27daf5f00f2c70ab984fc34da98a93b351e13df77eeac.jpg',
                'description': 'GirlScript Summer Of Code is a three-month-long Open-Source Program conducted every summer by the Girlscript...\n        See more',
                'date': 'Aug 10, 2023',
                'location': 'India',
                'language': 'English',
                'tags': ['Online', 'Coding Competition'],
                'link': 'https://gssoc.girlscript.tech/'
            }
            ...
        ]
        ```
        """
        url = "https://education.github.com/events"
        events_data = {"events": []}
        try:
            res = get(url, self.config)

            soup = BeautifulSoup(res.text, "html.parser")

            events = soup.find_all("a", class_="d-flex js-landing-page-link event-card")

            for e in events:
                tags_list = []
                title = e.find("h3", class_="h5").getText().strip()
                img = e.find("img")["src"]
                try:
                    desc = (
                        e.find("p", class_="my-3 short-event color-fg-muted")
                        .getText()
                        .strip()
                    )
                except:
                    desc = ""
                base = e.find_all("p", class_="color-fg-muted text-small")
                date = base[0].getText().strip()
                loc = base[1].getText().strip()
                lang = (
                    e.find("p", class_="color-fg-muted text-small mb-3")
                    .getText()
                    .strip()
                )
                labels = e.find_all(
                    "span", class_="Label--small Label--blue-standard mr-2"
                )
                for l in labels:
                    tags_list.append(l.getText().strip())
                link = e["href"]

                events_data["events"].append(
                    {
                        "title": title,
                        "image_url": img,
                        "description": desc,
                        "date": date,
                        "location": loc,
                        "language": lang,
                        "tags": tags_list,
                        "link": link,
                    }
                )
            return events_data["events"]
        except:
            return None
