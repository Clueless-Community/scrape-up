import json
from bs4 import BeautifulSoup as Soup
from scrape_up.config.request_config import RequestConfig, get


class Omdena:
    """
    Class - `Omdena`

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.get_datasets()`           | Returns a dictionary of datasets in Omdena.                                                              |
    | `.get_projects()`           | Returns a dictionary of latest ongoing projects in Omdena.                                                              |
    | `.get_blogs()`              | Returns a dictionary of latest blogs in Omdena.                                                              |

    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config
        self.url = f"https://www.omdena.com/"

    def get_datasets(self) -> dict:
        """
        Class - `Omdena`

        Example:
        ```
        omdena = Omdena()
        omdena.get_datasets()
        ```

        Returns the list of available datasets in Omdena.:
        ```python
        {'datasets': ['https://datasets.omdena.com//dataset/flood-dataset-(malaysia)', 'https://datasets.omdena.com//dataset/2007-2022-homeless-populations-by-state-(usa)', 'https://datasets.omdena.com//dataset/homelessness-in-the-united-states-(2007-2022)', 'https://datasets.omdena.com//dataset/global-wheat-head-detection-(gwhd)', 'https://datasets.omdena.com//dataset/covid-radiology-images', 'https://datasets.omdena.com//dataset/yearly-economics-and-unemployment-(pakistan)', 'https://datasets.omdena.com//dataset/twitter-data-with-pq-scores']}
        ```
        """
        try:
            self.url = f"https://datasets.omdena.com"
            req = get(self.url, self.config)
            page_soup = Soup(req.content, "html.parser")
            
            data = page_soup.find_all("div", attrs={"class": f"dataset-grid"})
            datset_list = []
            
            for card in data:
                for i in card.find_all("a"):
                    datset_list.append(f"{self.url}{i.get('href')}")
            
            return {"datasets": datset_list}

        except Exception:
            return None
        
    def get_blogs(self) -> dict:
        """
        Class - `Omdena`

        Example:
        ```
        omdena = Omdena()
        omdena.get_blogs()
        ```

        Returns the list of latest blogs in Omdena.:
        ```python
            {'blogs': [{
                'title': 'Revolutionizing Short-term Traffic Congestion Prediction with Machine Learning | AI Insights | Omdena Success Story',
                'description': 'Explore how our project leveraged machine learning and computer vision to predict short-term traffic congestion, revolutionizing urban traffic management.',
                'url': 'https://cmsnew.omdena.com/blog/predicting-short-term-traffic-congestion-on-urban-roads-using-machine-learning/',
                'site_name': 'Omdena | Building AI Solutions for Real-World Problems',
                'image': [{'width': 715,
                    'height': 520,
                    'url': 'https://cmsnew.omdena.com/wp-content/uploads/2023/05/Vehicle-and-Vehicle-Direction-Detection.jpeg',
                    'type': 'image/jpeg'}]}
            }]
        ```
        """
        try:
            req = get(f"{self.url}/blog", self.config)
            page_soup = Soup(req.content, "html.parser")
            
            data = page_soup.find("script", attrs={"id": f"__NEXT_DATA__"}).text
            data = json.loads(data)
            
            keys_ = data["props"]["pageProps"]["articles"][0]["yoast_head_json"].keys()
            blogs_data = []
            
            for project in data["props"]["pageProps"]["articles"]:
                project_data_dict = {}
                for key in keys_:
                    if key[:3]=="og_" and key not in ["og_locale", "og_type"]:
                        project_data_dict[key.replace("og_", "")] = project["yoast_head_json"][key]
                blogs_data.append(project_data_dict)
                
            return {"blogs": blogs_data}

        except Exception:
            return None
        
    def get_projects(self) -> dict:
        """
        Class - `Omdena`

        Example:
        ```
        omdena = Omdena()
        omdena.get_projects()
        ```

        Returns the list of latest ongoing projects in Omdena.:
        ```python
            {'projects': [{
                'title': 'Building Real-Time Anomaly Detection for Traveling Agency Transactions',
                'description': 'Join Omdena Top Talent Project to build a real-time anomaly detection system for analyzing transactions on travel agency websites by leveraging data analysis and AI technologies.',
                'url': 'https://cmsnew.omdena.com/projects/building-real-time-anomaly-detection-for-traveling-agency-transactions/',
                'site_name': 'Omdena | Building AI Solutions for Real-World Problems',
                'image': [{'width': 1600,
                    'height': 1066,
                    'url': 'https://cmsnew.omdena.com/wp-content/uploads/2024/06/traveling-agency-transactions.jpeg',
                    'type': 'image/jpeg'}]}
            }]
        ```
        """
        try:
            req = get(f"{self.url}/projects", self.config)
            page_soup = Soup(req.content, "html.parser")
            
            data = page_soup.find("script", attrs={"id": f"__NEXT_DATA__"}).text
            data = json.loads(data)
            
            keys_ = data["props"]["pageProps"]["projects"][0]["yoast_head_json"].keys()
            projects_data = []
            
            for project in data["props"]["pageProps"]["projects"]:
                project_data_dict = {}
                for key in keys_:
                    if key[:3]=="og_" and key not in ["og_locale", "og_type"]:
                        project_data_dict[key.replace("og_", "")] = project["yoast_head_json"][key]
                projects_data.append(project_data_dict)
                
            return {"projects": projects_data}

        except Exception:
            return None