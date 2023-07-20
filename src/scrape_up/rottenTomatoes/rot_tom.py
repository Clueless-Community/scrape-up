from bs4 import BeautifulSoup
import requests 

#scrape the rotten tomatoes website 

class RottenTomatoes:
    def __init__(self):
        self.url = "https://www.rottentomatoes.com/"
        self.headers =  {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }
    def top_rated(self):
        url=self.url+"top/bestofrt/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract movie titles
        movie_titles = []
        title_elements = soup.find_all('span', class_='p--small', attrs={'data-qa': 'discovery-media-list-item-title'})
        for title_element in title_elements:
            movie_titles.append(title_element.text.strip())

        # Extract streaming dates
        streaming_dates = []
        streaming_elements = soup.find_all('span', class_='smaller', attrs={'data-qa': 'discovery-media-list-item-start-date'})
        for streaming_element in streaming_elements:
            streaming_dates.append(streaming_element.text.strip())

        return movie_titles, streaming_dates
    
    def movie_details(self,movie_name):
        """_summary_

        Args:
            movie_name (barbie): movie name
            
            Returns:
            movie_details (dict):   
                {'rating'(str): 'PG-13(SuggestiveReferences|BriefLanguage)', 
                'genre'(str): 'Comedy', 
                'director'(str): 'English', 
                'producers'(str): ['David Heyman', 'Margot Robbie', 'Tom Ackerley', 'Robbie Brenner'], 
                'writers'(str): ['Greta Gerwig', 'Noah Baumbach'], 'release_date': 'Jul 21, 2023\n\xa0wide', 
                'runtime'(str): '1h 54m', 'distributor': 'WarnerBros.Pictures', 
                'production_co'(str): 'NB/GGPictures,HeydayFilms,LuckyChapEntertainment,Mattel'}
        """
        url=self.url+"m/"+movie_name
        response = requests.get(url)
        soup=BeautifulSoup(response.content,'html.parser')
        movie_details = {}
        # Extract the movie details from the <ul> element with id="info"
        ul_element = soup.find('ul', id='info')
        producers=[]
        writers=[]
        movie_details = ul_element.find_all('span', class_='info-item-value', attrs={'data-qa': 'movie-info-item-value'})
        rating = movie_details[0].text.strip().replace('\n','').replace(' ','')
        genre=movie_details[1].text.strip().replace('\n','').replace(' ','')
        director=movie_details[2].text.strip()
        producers_name=movie_details[4].find_all('a')
        writers_name=movie_details[5].find_all('a')
        release_date=movie_details[6].text.strip()
        runtime=movie_details[7].text.strip()
        distributor=movie_details[8].text.strip().replace('\n','').replace(' ','')
        production_co=movie_details[9].text.strip().replace('\n','').replace(' ','')

        for writer in writers_name:
            writer=writer.text.strip()
            writers.append(writer)
        for producer in producers_name:
            producer=producer.text.strip()
            producers.append(producer)
        
        movie_details = { 'rating': rating, 'genre': genre, 'director': director, 'producers': producers, 'writers': writers, 'release_date': release_date, 'runtime': runtime, 'distributor': distributor, 'production_co': production_co }
        
        return movie_details