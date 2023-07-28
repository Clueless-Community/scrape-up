from bs4 import BeautifulSoup
import requests

class WHO():
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"}

    def get_disease_outbreak(self,number):
        """
        Get Disease Outbreak News from WHO website.

        Parameters:
        - number (int): The number of pages (each page contains 10 items).

        Returns:
        A dictionary containing a list of Disease Outbreak News:
        {
            "Data": [
                {
                    "Title": str (Title of the outbreak),
                    "Date": str (Date of the outbreak),
                    "Link": str (Link to the full report of the outbreak)
                },
            ]
        }
        """

        try:
            number = number//10
            DON = []
            for i in range(1,number+1):
                url = f"https://www.who.int/emergencies/disease-outbreak-news/{i}"
                html_text = requests.get(url, headers=self.headers).text
                soup = BeautifulSoup(html_text, "lxml")

                container = soup.find("div",{"class":"sf-list-vertical"})

                for items in container.find_all("a",{"class":"sf-list-vertical__item"},href=True):
                    title = items.find("span",{"class":"full-title"})
                    date = title.findNext()
                    date = date.text.split("|")[0]
                    link = items['href']
                    data = {
                        "Title":title.text,
                        "Date":date,
                        "Link":link
                    }
                    DON.append(data)
            return {"Data":DON}
        except:
            return None

