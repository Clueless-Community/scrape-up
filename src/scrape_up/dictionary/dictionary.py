from bs4 import BeautifulSoup
from urllib.request import urlopen

class Dictionary:
    def get_word_of_the_day_url(self):
        with urlopen("https://www.dictionary.com/") as response:
            soup = BeautifulSoup(response, 'html.parser')

            for anchor in soup('button'):
                url = anchor.get('data-linkurl', '/')

                if "word-of-the-day" in url:
                    return url
                
        return None
    
    def get_word_of_the_day(self):
        return self.get_word_of_the_day_url().split("/")[-2].split("-")[0]
    
    def word_of_the_day_definition(self):
        with urlopen(self.get_word_of_the_day_url()) as response:
            soup = BeautifulSoup(response, 'html.parser')

            for para in soup('p'):
                if para.string and para.string[0] not in "EG":
                    return para.string

        return None
            
if __name__ == "__main__":
    d = Dictionary()
    print("Word of the day:", d.get_word_of_the_day())
    print("Definition:", d.word_of_the_day_definition())

            






