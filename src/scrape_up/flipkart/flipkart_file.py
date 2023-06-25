import bs4
from bs4 import BeautifulSoup as bs
import requests

class Flipkart:
    def __init__(self):
        pass

    def item_TV(self):
        
        try:
            
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.item_TV()
            ```
            Return\n
            ```python
            return {all_items with details in json}
            ```
            """
            
            link = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"
            page = requests.get(link)
            soup = bs(page.content, 'html.parser')
    
            all_items = []
            
            for data in soup.findAll('div', class_='_3pLy-c row'):
                names = data.find('div', attrs={'class': '_4rR01T'})
                price = data.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
                rating = data.find('div', attrs={'class': '_3LWZlK'})
                specification = data.find('div', attrs={'class': 'fMghEO'})
    
                specs = []
                for spec in specification.find_all('li', attrs={'class': 'rgWa7D'}):
                    specs.append(spec.text)
    
                item_details = {
                    "Item_Name": names.text,
                    "Price": price.text,
                    "Rating": rating.text,
                    "Specifications": ', '.join(specs),
                }
    
                all_items.append(item_details)
    
            return all_items
        
        except Exception as e:
            return None
    
    def bestSellers(self):
        
        try: 
            
            """
            Class - `Flipkart`\n
            Example -\n
            ```python
            item = Flipkart()
            item.bestSellers()
            ```
            Return\n
            ```python
            return {all_items with details in json}
            ```
            """
            
            link = "https://www.flipkart.com/search?q=bestsellers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            page = requests.get(link)
            soup = bs(page.content, 'html.parser')
    
            all_items = []
    
            for data in soup.findAll('div', class_='_4ddWXP'):
                names = data.find('a', attrs={'class': 's1Q9rs'})
                price = data.find('div', attrs={'class': '_30jeq3'})
                rating = data.find('div', attrs={'class': '_3LWZlK'})
                specification = data.find('div', attrs={'class': '_3Djpdu'})
    
                item_details = {
                    "Item_Name": names.text,
                    "Price": price.text,
                    "Rating": rating.text if rating else None,
                    "Specifications": specification.text if specification else None,
                }
    
                all_items.append(item_details)
    
            return all_items
        
        except Exception as e:
            return None
    
    