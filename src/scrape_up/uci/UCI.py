from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class UCI:
    """
    Create an instance of UCI class
    ```python
    uci = UCI()
    ```
    | Methods       | Details                               |
    | ------------- | ------------------------------------- |
    | `.datasets()` | Fetches datasets information from UCI |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
        self.config = config
        if self.config.headers == {}:
            self.config.set_headers(headers)

    def datasets(self, number):
        """
        Get UCI datasets information.\n
        Args:
        `number (int)`: The number of datasets to fetch. The method fetches datasets in batches of 10.
        Example:
        ```python
        uci = UCI()
        datasets_info = uci.datasets(20)
        ```
        Returns:
        ```js
        [
            {
                "Name":"Iris",
                "Link":"https://archive.ics.uci.edu//dataset/53/iris",
                "Description":"A small classic dataset from Fisher, 1936. One of the earliest datasets used for evaluation of classification methodologies.\n",
                "Extra Info":" Classification  Multivariate  150 Instances  4 Attributes "
            }
        ]
        ```
        """
        try:
            number = number // 10
            dataset = []
            for i in range(0, number):
                url = "https://archive.ics.uci.edu/datasets?skip={}&take=10&sort=desc&orderBy=NumHits&search=s".format(
                    i * 10
                )
                html_text = get(url, self.config).text
                soup = BeautifulSoup(html_text, "lxml")

                container = soup.find("div", {"class": "flex flex-col gap-1"})

                for items in container.find_all(
                    "div", {"class": "rounded-box bg-base-100"}
                ):
                    title = items.find("h2").text
                    link = (
                        "https://archive.ics.uci.edu/"
                        + items.find("a", href=True)["href"]
                    )
                    description = items.find("p").text
                    extra_info = ""
                    for item in items.find_all(
                        "div", {"class": "col-span-3 flex items-center gap-2"}
                    ):
                        extra_info = extra_info + item.text + " "
                    data = {
                        "Name": title,
                        "Link": link,
                        "Description": description,
                        "Extra Info": extra_info,
                    }
                    dataset.append(data)
            return dataset
        except:
            return None
