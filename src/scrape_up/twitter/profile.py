from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class Profile:
    

    def __init__(self, login_username, login_password, profile_username):
        self.login_username = login_username
        self.login_password = login_password
        self.profile_username = profile_username

    def getInfo(self):
        
        driver = Chrome(ChromeDriverManager().install())
        try:
            driver.get('https://twitter.com/login')
            sleep(3)
            profile_data = {"profile_data": []}
            username = driver.find_element("xpath", '//input[@autocomplete="username"]')
            username.send_keys(self.login_username)
            username.send_keys(Keys.RETURN)
            sleep(1)
            password = driver.find_element("xpath", '//input[@name="password"]')
            sleep(1)
            password.send_keys(self.login_password)
            password.send_keys(Keys.RETURN)
            sleep(2)
            driver.get('https://twitter.com/' + self.profile_username)
            sleep(5)

            name = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/span/span[1]').text
            try:
                desc = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span').text
            except:
                desc = ""
            try:
                industry = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span').text
            except:
                industry = ""
            try:
                location = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[2]/span/span').text
            except:
                location = ""
            try:
                subscriber_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[3]/a/span[1]/span').text
            except:
                subscriber_count = ""
            try:
                try:
                    join_date = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[2]/span').text
                except:
                    join_date = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/span[2]/span').text
            except:
                join_date = ""
            try:
                try:
                    following_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
                except:
                    following_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div[1]/a/span[1]/span').text
            except:
                following_count = ""
            try:
                try:
                    follower_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
                except:
                    follower_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/a/span[1]/span').text
            except:
                follower_count = ""
            user_name = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/span').text
            tweet_count = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div').text
            

            profile_data["profile_data"].append(
                {
                    "name": name,
                    "description": desc,
                    "user_name": user_name,
                    "industry": industry,
                    "location": location,
                    "join_date": join_date,
                    "following_count": following_count,
                    "follower_count": follower_count,
                    "subscriber_count": subscriber_count,
                    "tweet_count": tweet_count
                }
            )
            return profile_data["profile_data"]
        except:
            return None
