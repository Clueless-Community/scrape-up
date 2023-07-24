import requests
from bs4 import BeautifulSoup as bs


class HackerRank:
    """
    First, create an object of class `HackerRank`
    ```python
    user1 = HackerRank(id="helloguys289")
    ```
    | Methods         | Details                                                                                   |
    | --------------- | ----------------------------------------------------------------------------------------- |
    | `get_profile()` | Returns name, username, country, user_type, details, badges, verified_skills, social etc. |
    """

    def __init__(self, id):
        self.id = id

    def get_profile(self):
        """
        Create an object of the 'HackerRank' class\n
        ```python
        user1 = HackerRank(id="helloguys289")
        user1.get_profile()
        ```
        Response
        ```js
       {
        'name': 'Karri Srinivasa Rao', 
        'username': 'helloguys289', 
        'country': 'India', 
        'user_type': 'Student', 
        'details': 
        [
            {
                'Education': 'IIITM, Gwalior (ABV Indian Institute of Information Technology and Management)'
            }
        ], 
        'badges': 
        [
            {
                'badge': 'Problem Solving', 
                'stars': 4
            }, 
            {
                'badge': 'CPP', 
                'stars': 3
            }, 
            {
                'badge': 'Days of Code', 
                'stars': 1
            }, 
            {
                'badge': 'Days of JS', 
                'stars': 1
            }, 
            {
                'badge': 'C language', 
                'stars': 2
            }
        ], 
        'verified_skills': 
        [
            {
                'certificate': 'Problem Solving (Basic)', 
                'certificate_link': 'https://www.hackerrank.com/certificates/d8c5c5dcd307'
            }, 
            {
                'certificate': 'Problem Solving (Intermediate)', 
                'certificate_link': 'https://www.hackerrank.com/certificates/4b16deda4e6a'
            }, 
            {
                'certificate': 'Python (Basic)', 
                'certificate_link': 'https://www.hackerrank.com/certificates/026a64ec0c87'
            }, 
            {
                'certificate': 'Rest API (Intermediate)', 
                'certificate_link': 'https://www.hackerrank.com/certificates/227540142706'
            }
        ], 
        'social': 
        [
            {
                'Github': 'https://github.com/srinivaskarri1999'
            }, 
            {
                'Linkedin': 'https://www.linkedin.com/in/srinivas1999'
            }
        ]
        }
        ```
        """
        try:
            url = f"https://www.hackerrank.com/{self.id}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            response = requests.get(url, headers=headers).text
            soup = bs(response, "lxml")
            
            user_details_box = soup.find("div", {"class": "profile-summary-card"})
            extra_details_box = soup.find("div", {"class": "profile-details-extra"})
            # Name
            try:
                profile_name = user_details_box.find("h1", {"class": "profile-heading"}).text.strip()
            except:
                profile_name = ""
            # Username
            try:
                profile_username = user_details_box.find("p",{"class": "profile-username-heading"}).text.strip()[1:]
            except:
                profile_username = ""
            # Country
            try:
                country_name = user_details_box.find("p",{"class": "profile-country"}).text.strip()
            except:
                country_name = ""
            # User Type
            try:
                user_type = user_details_box.find("p", {"class": "profile-subheading"}).text.strip()
            except:
                user_type = ""

            # Social Links
            try:
                social_box = user_details_box.find("ul", {"class": "profile-social-links-list"})
                social_box_li = social_box.find_all("li")
                socials = []
                for li in social_box_li:
                    social_a = li.find("a")
                    social_heading = social_a["aria-label"]
                    social_link = social_a["href"]
                    social_details = {
                        social_heading : social_link
                    }
                    socials.append(social_details)
            except:
                socials = []

            # Extra Details
            try:
                extra_detail_div = extra_details_box.find_all("div")
                extra_details = []
                for div in extra_detail_div:
                    div_heading = div.find("p", {"class": "profile-details-label"}).text.strip()
                    div_content = div.find("p", {"class": "profile-details-value"}).text.strip()
                    details = {
                        div_heading : div_content
                    }
                    extra_details.append(details)
            except:
                extra_details = []
            
            # Right Pane
            user_details_box_right = soup.find("div", {"class": "profile-right-pane"})
            user_details_sections = user_details_box_right.find_all("section")

            # Badges
            try:
                badges_section_heading = user_details_sections[0].find("header").text.strip()
                badges_list = user_details_sections[0].find_all("div", {"class": "hacker-badge"})
                badges = []
                for badge in badges_list:
                    badge_heading = badge.find("text", {"class": "badge-title"}).text.strip()
                    star_count = len(badge.find_all("svg", {"class": "badge-star"}))
                    badge_details = {
                        "badge" : badge_heading,
                        "stars" : star_count
                    }
                    badges.append(badge_details)
            except:
                badges = []

            # Verified Skills
            try:
                verified_skill_section_heading = user_details_sections[1].find("header").text.strip()
                verified_certificates = user_details_sections[1].find_all("a")
                verified_skills = []
                for cert in verified_certificates:
                    cert_heading = cert.text.replace("Verified","").replace("Certificate: ", "").strip()
                    cert_link =  "https://www.hackerrank.com" + cert["href"]
                    cert_details = {
                        "certificate" : cert_heading,
                        "certificate_link" : cert_link
                    }
                    verified_skills.append(cert_details)
            except:
                verified_skills = []

            profile_data = {
                'name': profile_name,
                'username': profile_username,
                'country': country_name,
                'user_type': user_type,
                'details': extra_details,
                'badges': badges, 
                'verified_skills': verified_skills,
                'social': socials
            }
            return profile_data
        except:
            return None
