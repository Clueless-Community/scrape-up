from bs4 import BeautifulSoup

import requests

'''
    WARNING!!!
    Smaller twitch channels with low stream time results is generic return value: 
    "Twitch is the world's leading video platform and community for gamers."

    Steps for use:

    1. Create "TwitchScraper()" class instance
    2. call the instance's function "scrape_title_description()" providing the channel name as a string
    3. Channel stream title is returned (if live),  Channel Description is returned (if offline)
    
    Example: using KaiCenat's twitch channel

    scraper = TwitchScraper()
    title = scraper.scrape_title_description("kaicenat")
    print(title)

    '''
class TwitchScraper():

    def __init__(self):
        self.status = None

    # this function just gets the text within the quotes for the descrption or title
    def get_in_quotes(self, input_string):
        if input_string is None:
            return None
        start_index = 15
        end_index = input_string.find('"', start_index)
        try:
            result = input_string[start_index:end_index]
            return result
        
        except:
            return "Error: No suitable title/description"

    # This function returns either the title of the stream if the channel is live, or the channel description if it's offline
    def scrape_title_description(self, channel: str):
        url = f"https://www.twitch.tv/{channel}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to retrieve the page. This channel might not exist. Status code: {response.status_code}")
                return None
            # make soup to parse html
            soup = BeautifulSoup(response.content, 'html.parser')
            # find the property contain the title or description
            meta_tag_2 = soup.find('meta', {'property': "og:description"})
            # return just the string text itself
            return self.get_in_quotes(str(meta_tag_2))
            
        except:
            print("Failed to scrape.")
            return None
        
