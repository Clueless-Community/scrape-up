from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup

# Edge
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

# Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

# Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


class AlternativeTo:
    """
    Class - `AlternativeTo`\n
    Parameters - `available_browser` -> Provide The Available Browser from (Edge, Chrome and Firefox)\n
    Description - `Scrape data from AlternativeTo and Provide with Alternatives to the app.`\n
    Methods -\n
        `new_apps()` - `Returns a list of new apps from AlternativeTo`\n
        `most_viewed()` - `Returns a list of most viewed apps from AlternativeTo`\n
        `trending()` - `Returns a list of trending apps from AlternativeTo`\n
        `crew_picked()` - `Returns a list of crew picked apps from AlternativeTo`\n
        `discontinued()` - `Returns a list of discontinued apps from AlternativeTo`\n
        `get_alternatives(app_id, feature=None, platform=None, sort=None, app_license=None, hide_legal_warning=True, page=1)` - `Returns a dictionary of the app and its alternatives`\n
        `search_app(name, page=1)` - `Returns a list of apps matching the name`\n
    """

    LICENSES = {
        "free": "free",
        "open source": "opensource",
        "paid": "commercial",
    }
    SORTS = {
        "rank": "altrank",
        "likes": "likes",
        "popular": "popular",
        "added": "addeddate",
        "views": "views",
    }
    PLATFORMS = {
        "windows": "windows",
        "mac": "mac",
        "online": "online",
        "android": "android",
        "linux": "linux",
        "iphone": "iphone",
        "ipad": "ipad",
    }
    BASE_URL = "https://alternativeto.net/"

    def __init__(self, available_browser=None) -> None:
        self.home_page_data = None
        if available_browser is not None:
            self.available_browser = available_browser.lower()
        else:
            # Check if Edge is installed
            try:
                self.edge_options = Options()
                self.edge_options.add_experimental_option(
                    "excludeSwitches", ["enable-logging"]
                )
                self.edge_options.add_experimental_option("detach", True)
                self.edge_service = Service(EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(
                    service=self.edge_service, options=self.edge_options
                )
                self.driver.quit()
                self.available_browser = "edge"
            except Exception as e:
                # Check if Chrome is installed
                try:
                    self.chrome_options = ChromeOptions()
                    self.chrome_options.add_experimental_option(
                        "excludeSwitches", ["enable-logging"]
                    )
                    self.chrome_options.add_experimental_option("detach", True)
                    self.chrome_service = ChromeService(ChromeDriverManager().install())
                    self.driver = webdriver.Chrome(
                        service=self.chrome_service, options=self.chrome_options
                    )
                    self.driver.quit()
                    self.available_browser = "chrome"
                except Exception as e:
                    try:
                        # Check if Firefox is installed
                        self.firefox_service = FirefoxService(
                            GeckoDriverManager().install()
                        )
                        self.driver = webdriver.Firefox(service=self.firefox_service)
                        self.driver.quit()
                        self.available_browser = "firefox"
                    except Exception as e:
                        self.available_browser = None

    def __set_driver(self) -> None:
        if self.available_browser == "edge":
            self.driver = webdriver.Edge(
                service=self.edge_service, options=self.edge_options
            )
        elif self.available_browser == "chrome":
            self.driver = webdriver.Chrome(
                service=self.chrome_service, options=self.chrome_options
            )
        elif self.available_browser == "firefox":
            self.driver = webdriver.Firefox(service=self.firefox_service)
        else:
            print("No browser found.")
            raise Exception("No browser found.")

    def __scrape_home(self, index) -> list | None:
        try:
            if self.home_page_data is None:
                self.__set_driver()
                self.driver.minimize_window()
                self.wait = WebDriverWait(self.driver, 100)
                self.driver.get(self.BASE_URL)
                self.driver.implicitly_wait(100)
                self.home_page_data = self.driver.page_source
            apps_list = []
            soup = BeautifulSoup(self.home_page_data, "html.parser")
            divs = soup.find_all("div", class_="ItemsInColumnsFlex_colGrid__krhSK")
            new_apps_div = divs[index]
            sub_divs = new_apps_div.find_all("div", class_="")
            for sub_div in sub_divs:
                title = sub_div.find("h3")
                id_list = title.find("a")["href"].split("/")
                id_index = id_list.index("software") + 1
                if index == 1 or index == 3:
                    apps_list.append(
                        {
                            "name": title.text,
                            "id": id_list[id_index],
                            "description": sub_div.find("p").text.strip(),
                        }
                    )
                else:
                    apps_list.append(
                        {
                            "name": title.text,
                            "id": id_list[id_index],
                        }
                    )
            return apps_list
        except Exception as e:
            return None
        finally:
            self.driver.quit()

    def new_apps(self) -> list | None:
        """
        Class - `AlternativeTo`\n
        Parameters - `None`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            new_apps = scraper.new_apps()
            if new_apps is not None:
                for app in new_apps:
                    print("Name:", app["name"])
                    print("ID:", app["id"])
                    print("Description:", app["description"])
            else:
                print("Failed to retrieve new apps.")
        ```
        Output -\n
        ```text
            Name: {app_name}
            ID: {app_id}
            Description: {app_description}
            Name: {app_name}
            ID: {app_id}
            Description: {app_description}
        ```
        """
        return self.__scrape_home(1)

    def most_viewed(self) -> list | None:
        """
        Class - `AlternativeTo`\n
        Parameters - `None`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            most_viewed_apps = scraper.most_viewed()
            if most_viewed_apps is not None:
                for app in most_viewed_apps:
                    print("Name:", app["name"])
                    print("ID:", app["id"])
            else:
                print("Failed to retrieve most viewed apps.")
        ```
        Output -\n
        ```text
            Name: {app_name}
            ID: {app_id}
            Name: {app_name}
            ID: {app_id}
        ```
        """
        return self.__scrape_home(2)

    def trending(self) -> list | None:
        """
        Class - `AlternativeTo`\n
        Parameters - `None`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            trending_apps = scraper.trending()
            if trending_apps is not None:
                for app in trending_apps:
                    print("Name:", app["name"])
                    print("ID:", app["id"])
            else:
                print("Failed to retrieve trending apps.")
        ```
        Output -\n
        ```text
            Name: {app_name}
            ID: {app_id}
            Name: {app_name}
            ID: {app_id}
        ```
        """
        return self.__scrape_home(0)

    def crew_picked(self) -> list | None:
        """
        Class - `AlternativeTo`\n
        Parameters - `None`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            crew_picked_apps = scraper.crew_picked()
            if crew_picked_apps is not None:
                for app in crew_picked_apps:
                    print("Name:", app["name"])
                    print("ID:", app["id"])
                    print("Description:", app["description"])
            else:
                print("Failed to retrieve crew picked apps.")
        ```
        Output -\n
        ```text
            Name: {app_name}
            ID: {app_id}
            Description: {app_description}
            Name: {app_name}
            ID: {app_id}
            Description: {app_description}
        ```
        """
        return self.__scrape_home(3)

    def discontinued(self) -> list | None:
        """
        Class - `AlternativeTo`\n
        Parameters - `None`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            discontinued_apps = scraper.discontinued()
            if discontinued_apps is not None:
                for app in discontinued_apps:
                    print("Name:", app["name"])
                    print("ID:", app["id"])
            else:
                print("Failed to retrieve discontinued apps.")
        ```
        Output -\n
        ```text
            Name: {app_name}
            ID: {app_id}
            Name: {app_name}
            ID: {app_id}
        ```
        """
        return self.__scrape_home(4)

    def get_alternatives(
        self,
        app_id: str,
        feature: str = None,
        platform: str = None,
        sort: str = None,
        app_license: str = None,
        hide_legal_warning: bool = True,
        page: int = 1,
    ) -> dict | None:
        """
        Class - `AlternativeTo`\n
        Parameters -\n
            app_id - `ID of the app`\n
            sort - `Rank`, `Likes`, `Popular`, `Added`, `Views`\n
            app_license - `Free`, `Open Source`, `Paid`\n
            platform - `Windows`, `Mac`, `Online`, `Android`, `Linux`, `iPhone`, `iPad` and more\n
            feature - `Video Download`, `File Sharing`, `Image Sharing`, `Video Streaming` and more\n
            hide_legal_warning - `True` or `False`    (Used to hide apps with legal warning)\n
            page - `Page number`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            data = scraper.get_alternatives(
                "youtube",
                page=1,
                sort="rank",
                app_license="free",
            )
            if data is not None:
                print("Name:", data["name"])
                print("Alternative Apps")
                for alt_app in data["alternative_apps"]:
                    print("Name:", alt_app["name"])
                    print("ID:", alt_app["id"])
            else:
                print("Failed to retrieve alternative apps.")
        ```
        Output-\n
        ```text
            Name: {app_name}
            Alternative Apps
            Name: {alternative_app_name}
            ID: {alternative_app_id}
        ```
        """
        try:
            self.__set_driver()
            self.driver.minimize_window()
            self.wait = WebDriverWait(self.driver, 100)
            URL = self.BASE_URL + "software/" + app_id + f"/?p={page}"
            if feature is not None:
                URL += f"&feature={feature}"
            if platform is not None and platform.lower() in self.PLATFORMS:
                URL += f"&platform={self.PLATFORMS[platform.lower()]}"
            if sort is not None and sort.lower() in self.SORTS:
                URL += f"&sort={self.SORTS[sort.lower()]}"
            if app_license is not None and app_license.lower() in self.LICENSES:
                URL += f"&license={self.LICENSES[app_license.lower()]}"
            if not hide_legal_warning:
                URL += "&lw=1"
            self.driver.get(URL)
            self.driver.implicitly_wait(100)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            app_data = soup.find("div", class_="AppItemBox_miniApp__VokvR appItemBox")
            app_name = app_data.find("a", class_="AppItemBox_appName__kP6bz").text
            app_badges = app_data.find("div", class_="BadgeRow_content__zGqeR")
            app_licenses = app_badges.find("span").text.strip().split("\u2022")
            app_licenses = [app_license.strip() for app_license in app_licenses]
            app_features = app_badges.find_all("a")
            app_features_list = [feature.text.strip() for feature in app_features]
            app_platforms = app_data.find_all("div", class_="BadgeRow_content__zGqeR")[
                1
            ].find_all("span")
            app_platforms_list = [platform.text.strip() for platform in app_platforms]
            app_description = app_data.find(
                "div", class_="meta AppItemBox_desc___ZCVu"
            ).text.strip()
            total_alternatives = soup.find(
                "em", class_="AppFilterPopularBar_simpleEffect__q64k6"
            ).text.strip()

            alternatives_container = soup.find(
                "div", attrs={"data-testid": "alternative-list"}
            ).find("ol")
            alternative_apps = alternatives_container.find_all(
                "li", class_="AppListItem_appListItem__TY1nG"
            )
            alternative_apps_list = []
            for alt_app in alternative_apps:
                alt_app_name = alt_app.find(
                    "h2", class_="Heading_h2__7oYDQ"
                ).text.strip()
                alt_app_url = (
                    alt_app.find("h2", class_="Heading_h2__7oYDQ")
                    .find("a")["href"]
                    .split("/")
                )
                alt_app_id = alt_app_url[alt_app_url.index("software") + 1]
                alt_app_badges = alt_app.find("div", class_="BadgeRow_content__zGqeR")
                alt_app_licenses = (
                    alt_app_badges.find("span").text.strip().split("\u2022")
                )
                alt_app_licenses = [
                    alt_app_license.strip() for alt_app_license in alt_app_licenses
                ]
                alt_app_features = alt_app_badges.find_all("a")
                alt_app_features_list = [
                    feature.text.strip() for feature in alt_app_features
                ]
                alt_app_platforms = alt_app.find_all(
                    "div", class_="BadgeRow_content__zGqeR"
                )[1].find_all("span")
                alt_app_platforms_list = [
                    platform.text.strip() for platform in alt_app_platforms
                ]
                alt_app_description = alt_app.find(
                    "span", class_="AppListItem_description__IVJ2j"
                ).text.strip()
                alternative_apps_list.append(
                    {
                        "name": alt_app_name,
                        "id": alt_app_id,
                        "licenses": alt_app_licenses,
                        "features": alt_app_features_list,
                        "platforms": alt_app_platforms_list,
                        "description": alt_app_description,
                    }
                )

            app_data = {
                "name": app_name,
                "id": app_id,
                "licenses": app_licenses,
                "features": app_features_list,
                "platforms": app_platforms_list,
                "description": app_description,
                "total_alternatives": total_alternatives,
                "alternative_apps": alternative_apps_list,
            }

            if len(app_data["alternative_apps"]) == 0:
                return None

            return app_data

        except Exception as e:
            return None

        finally:
            self.driver.quit()

    def search_app(
        self,
        name: str,
        page: int = 1,
    ) -> list | None:
        """
        Class - `AlternativeTo`\n
        Parameters -\n
            name - `Name of the app`\n
            page - `Page number`\n
        Example -\n
        ```python
            scraper = AlternativeTo("chrome")
            data = scraper.search_app("photoshop")
            if data is not None:
                print("Search Results")
                for app in data:
                    print("Name:", app["name"])
                    print("ID:", app["id"])
            else:
                print("Failed to retrieve alternative apps.")
        ```
        Output-\n
        ```text
            Search Results
            Name: {app_name}
            ID: {app_id}
        ```
        """
        try:
            self.__set_driver()
            self.driver.minimize_window()
            self.wait = WebDriverWait(self.driver, 100)
            URL = self.BASE_URL + "browse/search/?q=" + name + f"&p={page}"
            self.driver.get(URL)
            self.driver.implicitly_wait(100)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            search_list = soup.find_all("li", class_="AppListItem_appListItem__TY1nG")
            search_list_data = []
            for elem in search_list:
                app_name = elem.find("h2", class_="Heading_h2__7oYDQ").text.strip()
                app_url = elem.find("h2", class_="Heading_h2__7oYDQ").find("a")["href"]
                app_id = app_url.split("/")[
                    app_url.split("/").index("software") + 1
                ].strip()
                app_badges = elem.find("div", class_="BadgeRow_content__zGqeR")
                app_licenses = app_badges.find("span").text.strip().split("\u2022")
                app_licenses = [app_license.strip() for app_license in app_licenses]
                app_features = app_badges.find_all("a")
                app_features_list = [feature.text.strip() for feature in app_features]
                badge_divs = elem.find_all("div", class_="BadgeRow_content__zGqeR")
                if len(badge_divs) > 1:
                    app_platforms = badge_divs[1].find_all("span")
                    app_platforms_list = [
                        platform.text.strip() for platform in app_platforms
                    ]
                else:
                    app_platforms_list = []

                app_description = elem.find(
                    "span", class_="AppListItem_description__IVJ2j"
                ).text.strip()
                search_list_data.append(
                    {
                        "name": app_name,
                        "id": app_id,
                        "licenses": app_licenses,
                        "features": app_features_list,
                        "platforms": app_platforms_list,
                        "description": app_description,
                    }
                )
            return search_list_data
        except Exception as e:
            return None
        finally:
            self.driver.quit()
