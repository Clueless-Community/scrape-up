from bs4 import BeautifulSoup
import requests

class UCI():
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"}

    def datasets(self, number):
        """
        Get UCI datasets information.

        Args:
        number (int): The number of datasets to fetch. The method fetches datasets in batches of 10.

        Example:
        ```python
        uci = UCI()
        datasets_info = uci.datasets(20)
        print(datasets_info)
        ```

        Returns:
        A list of dictionaries containing the information for the requested number of UCI datasets.
        Each dictionary contains the following keys:
        - "Name": The name of the dataset.
        - "Link": The link to the dataset's page on UCI website.
        - "Description": Description of the dataset.
        - "Extra Info": Additional information about the dataset.
        """
        end_loop = number // 10
        number+=1
        dataset = []
        for i in range(0, end_loop+1):
            url = "https://archive.ics.uci.edu/datasets?skip={}&take=10&sort=desc&orderBy=NumHits&search=s".format(i * 10)
            html_text = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html_text, "lxml")

            container = soup.find("div", {"class": "flex flex-col gap-1"})

            for items in container.find_all("div", {"class": "rounded-box bg-base-100"}):
                number -= 1
                if not number:
                    break
                title = items.find("h2").text
                link = "https://archive.ics.uci.edu/" + items.find("a", href=True)['href']
                description = items.find("p").text
                extra_info = ""
                for item in items.find_all("div", {"class": "col-span-3 flex items-center gap-2"}):
                    extra_info = extra_info + item.text + " "
                data = {
                    "Name": title,
                    "Link": link,
                    "Description": description,
                    "Extra Info": extra_info
                }
                dataset.append(data)
        return dataset


