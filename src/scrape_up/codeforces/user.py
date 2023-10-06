import requests
from bs4 import BeautifulSoup

class USER:
    """
    Fetches user data from CodeForces Competitive Platform

    lastName → Qi
    country → United States
    lastOnlineTimeSeconds → 1686275190
    city → Princeton
    rating → 3783
    friendOfCount → 12513
    titlePhoto → https://userpic.codeforces.org/312472/title/7cf0a442d4071e87.jpg
    handle → Benq
    avatar → https://userpic.codeforces.org/312472/avatar/5716ac69aea8159a.jpg
    firstName → Benjamin
    contribution → 50
    organization → MIT
    rank → legendary grandmaster
    maxRating → 3813
    registrationTimeSeconds → 1435099979
    maxRank → legendary grandmaster

    """

    user_url = "https://codeforces.com/profile/{}"

    def __init__(self, username):
        self.username = username
        self.userdata = self.user_get_data()

    def extract_text_or_empty(self, element):
        """
        Extract text from an element or return an empty string if the element is None.
        """
        return element.text.strip() if element else ''

    def user_get_data(self):
        """
        Gets all information of a username from CodeForces.
        """
        try:
            url = self.user_url.format(self.username)
            headers = {
                "User-Agent": "scrapeup"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors

            soup = BeautifulSoup(response.text, "html.parser")

            # Extracting user information
            user_info = {}

            # Find the main-info div
            main_info = soup.find("div", class_="main-info")

            # Extract user's rank
            user_info['rank'] = self.extract_text_or_empty(main_info.find("div", class_="user-rank"))

            # Extract user's name and handle
            user_name = main_info.find("h1")
            user_info['handle'] = user_name.find("a").text.strip()

            # Find the div with user information
            user_info_string =  self.extract_text_or_empty(main_info.find("div", style="margin-top: 0.5em;"))
            info_list = user_info_string.split(",")

            user_info["firstName"],  user_info["lastName"] = info_list[0].split()
            user_info["city"] = info_list[1]

            location_info = info_list[2].split("From")
            user_info["country"] = location_info[0].strip()
            user_info["organization"] = location_info[1]

            # Extract user's rating and max rating
            user_rating = soup.find("div", class_="info").find_all("li")
            for item in user_rating:
                if "Contest rating:" in item.text:
                    rating_span = item.find("span", class_="user-legendary")
                    user_info['rating'] = self.extract_text_or_empty(rating_span) if rating_span else ''
                elif "max. legendary grandmaster" in item.text:
                    max_rating_span = item.find("span", class_="user-legendary")
                    user_info['maxRating'] = self.extract_text_or_empty(max_rating_span) if max_rating_span else ''

            # Find the <div> element with class "info"
            info_div = soup.find('div', class_='info')

            # Initialize an empty string to store the contest rating and other such info text
            extracted_text = ''

            # Check if the <div> element exists
            if info_div:
                # Find the <ul> element within the <div>
                ul_element = info_div.find('ul')

                # Check if the <ul> element exists
                if ul_element:
                    # Find all <li> elements within the <ul>
                    li_elements = ul_element.find_all('li')

                    # Loop through each <li> element and extract its text
                    for li in li_elements:
                        text = li.get_text(strip=True)
                        extracted_text += text + ' '

            temp = extracted_text.split(":")

            user_info["contribution"] = temp[2].split()[0]
            user_info["friendsOfCount"] = temp[3].split()[0]
            user_info["lastVisit"] = int(temp[4].split()[0]) * 3600 
            user_info["registered"] = int(temp[5].split()[0]) * 365.25 * 24 * 60 * 60 
            

            # Extract title photo and avatar
            title_photo_div = soup.find("div", class_="title-photo")
            user_info['titlePhoto'] = title_photo_div.find("img")["src"] if title_photo_div else ''
            user_info['avatar'] = title_photo_div.find("img")["src"] if title_photo_div else ''

            # Print the extracted user information
            for key, value in user_info.items():
                print(f"{key} → {value}")

            return "Data Fetching Successful"

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request Error: {str(e)}")

if __name__ == "__main__":
    user = USER("tourist")
    print(user.userdata)
