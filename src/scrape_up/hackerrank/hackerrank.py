import requests
from bs4 import BeautifulSoup as bs


class HackerRank:
    """
    First, create an object of class `HackerRank`

    ```python
    hackerank = HackerRank()
    ```

    | Methods                      | Details                                                                                   |
    | ---------------------------- | ----------------------------------------------------------------------------------------- |
    | `get_profile(id="username")` | Returns name, username, country, user_type, details, badges, verified_skills, social etc. |
    | `active_contests()`          | Returns information on active contests like title, status, and link                       |
    | `archived_contests()`        | Returns information regarding archived contests                                           |
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def get_profile(self, id):
        """
         Create an object of the 'HackerRank' class\n
         ```python
         user1 = HackerRank()
         user1.get_profile(id="helloguys289")
         ```
         Response
         ```js
        {
            'name': 'Karri Srinivasa Rao',
            'username': 'helloguys289',
            'country': 'India',
            'user_type': 'Student',
            'details': [ .. ]
        }
         ```
        """
        try:
            url = f"https://www.hackerrank.com/{id}"
            response = requests.get(url, headers=self.headers).text
            soup = bs(response, "lxml")

            user_details_box = soup.find("div", {"class": "profile-summary-card"})
            extra_details_box = soup.find("div", {"class": "profile-details-extra"})
            # Name
            try:
                profile_name = user_details_box.find(
                    "h1", {"class": "profile-heading"}
                ).text.strip()
            except:
                profile_name = ""
            # Username
            try:
                profile_username = user_details_box.find(
                    "p", {"class": "profile-username-heading"}
                ).text.strip()[1:]
            except:
                profile_username = ""
            # Country
            try:
                country_name = user_details_box.find(
                    "p", {"class": "profile-country"}
                ).text.strip()
            except:
                country_name = ""
            # User Type
            try:
                user_type = user_details_box.find(
                    "p", {"class": "profile-subheading"}
                ).text.strip()
            except:
                user_type = ""

            # Social Links
            try:
                social_box = user_details_box.find(
                    "ul", {"class": "profile-social-links-list"}
                )
                social_box_li = social_box.find_all("li")
                socials = []
                for li in social_box_li:
                    social_a = li.find("a")
                    social_heading = social_a["aria-label"]
                    social_link = social_a["href"]
                    social_details = {social_heading: social_link}
                    socials.append(social_details)
            except:
                socials = []

            # Extra Details
            try:
                extra_detail_div = extra_details_box.find_all("div")
                extra_details = []
                for div in extra_detail_div:
                    div_heading = div.find(
                        "p", {"class": "profile-details-label"}
                    ).text.strip()
                    div_content = div.find(
                        "p", {"class": "profile-details-value"}
                    ).text.strip()
                    details = {div_heading: div_content}
                    extra_details.append(details)
            except:
                extra_details = []

            # Right Pane
            user_details_box_right = soup.find("div", {"class": "profile-right-pane"})
            user_details_sections = user_details_box_right.find_all("section")

            # Badges
            try:
                badges_list = user_details_sections[0].find_all(
                    "div", {"class": "hacker-badge"}
                )
                badges = []
                for badge in badges_list:
                    badge_heading = badge.find(
                        "text", {"class": "badge-title"}
                    ).text.strip()
                    star_count = len(badge.find_all("svg", {"class": "badge-star"}))
                    badge_details = {"badge": badge_heading, "stars": star_count}
                    badges.append(badge_details)
            except:
                badges = []

            # Verified Skills
            try:
                verified_certificates = user_details_sections[1].find_all("a")
                verified_skills = []
                for cert in verified_certificates:
                    cert_heading = (
                        cert.text.replace("Verified", "")
                        .replace("Certificate: ", "")
                        .strip()
                    )
                    cert_link = "https://www.hackerrank.com" + cert["href"]
                    cert_details = {
                        "certificate": cert_heading,
                        "certificate_link": cert_link,
                    }
                    verified_skills.append(cert_details)
            except:
                verified_skills = []

            profile_data = {
                "name": profile_name,
                "username": profile_username,
                "country": country_name,
                "user_type": user_type,
                "details": extra_details,
                "badges": badges,
                "verified_skills": verified_skills,
                "social": socials,
            }
            return profile_data
        except:
            return None

    def active_contests(self):
        """
        Get the details of active contests on HackerRank.\n
        First, create an object of class `HackerRank`\n
        ```python
        hrank = HackerRank()
        hrank.active_contests()
        ```
        Returns:
        ```js
        [
            {
                "Title":"ProjectEuler+",
                "Status":"Open Indefinitely",
                "Link":"https://www.hackerrank.com/contests/projecteuler"
            }
        ]
        ```
        """
        try:
            url = "https://www.hackerrank.com/contests"
            html_text = requests.get(url, headers=self.headers).text
            soup = bs(html_text, "lxml")
            container = soup.find("div", {"class": "theme-m contest-list left-pane"})
            actives = []
            active_contest = container.find(
                "div", {"class": "active_contests active-contest-container"}
            )
            for items in active_contest.find_all("li"):
                title = items.find("h4").text
                status = items.find("span", {"class": "contest-status"}).text
                link = (
                    "https://www.hackerrank.com"
                    + items.find("a", {"class": "text-link"}, href=True)["href"]
                )
                data = {"Title": title, "Status": status, "Link": link}
                actives.append(data)
            return actives
        except:
            return None

    def archived_contests(self):
        """
        Get the details of active contests on HackerRank.\n
        First, create an object of class `HackerRank`\n
        ```python
        hrank = HackerRank()
        hrank.archived_contests()
        ```
        Returns:
        ```js
        [
            {
                "title":"Cisco Hack to Secure Challenge 2023"
            }
            ...
        ]
        ```
        """
        try:
            url = "https://www.hackerrank.com/contests"
            html_text = requests.get(url, headers=self.headers).text
            soup = bs(html_text, "lxml")
            container = soup.find("div", {"class": "theme-m contest-list left-pane"})
            archives = []
            archived_contest = container.find(
                "div", {"class": "active_contests archived-contest-container"}
            )
            for items in archived_contest.find_all("li"):
                title = items.find("h4").text
                data = {"title": title}
                archives.append(data)
            return archives
        except Exception:
            return None

