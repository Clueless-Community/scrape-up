from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class HealthGrades:
    """
    Create an instance of `HealthGrades` class

    ```python
    hc = HealthGrades()
    ```

    | Method                      | Details                                                              |
    | --------------------------- | -------------------------------------------------------------------- |
    | `get_best_hospitals(state)` | Fetches and returns information about the best hospitals in a state. |

    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def get_best_hospitals(self, state):
        """
        Fetches and returns information about the best hospitals in a state.\n
        ```python
        hc = HealthGrades()
        hc.get_best_hospitals(state="bihar")
        ```

        Example output:
        ```python
        [
            {
                "Name": "ABC Hospital",
                "Location": "123 Main St, Philadelphia, PA",
                "Link": "https://www.healthgrades.com/hospital/abc-hospital",
                "Awards": ["America's 100 Best Hospitals", "Patient Safety Excellence Award"]
            },
            ...
        ]
        ```
        """
        try:
            state = state.replace(" ", "-")
            url = (
                f"https://www.healthgrades.com/quality/americas-best-hospitals/{state}"
            )
            html_text = get(url, self.config).text
            soup = BeautifulSoup(html_text, "lxml")

            hospitals = []
            container = soup.find("ul", {"class": "quality-results-group"})

            for items in container.find_all("div", {"class": "quality-card"}):
                award = []
                title = items.find("h3")
                location = items.find("div", {"class": "location-info"})
                link = (
                    "https://www.healthgrades.com"
                    + items.find("div", {"class": "hospital-info__hospital-link"}).find(
                        "a", href=True
                    )["href"]
                )
                awards = items.find("ul", {"class": "awards-list__quality-award"})
                for item in awards.find_all("li"):
                    award.append(item.text)
                data = {
                    "Name": title.text,
                    "Location": location.text,
                    "Link": link,
                    "Awards": award[:-2],
                }
                hospitals.append(data)
            return hospitals
        except:
            return None
