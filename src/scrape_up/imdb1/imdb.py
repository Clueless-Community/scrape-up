from bs4 import BeautifulSoup
import requests
import openpyxl

class Movie:
    def __init__(self, name=None):
        self.name = name

    def details(self):
        try:
            source = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
            source.raise_for_status()

            """
            to have valid sites- throws error if invalid website
            
            """

            soup = BeautifulSoup(source.text, 'html.parser')
            movies = soup.find('tbody', class_="lister-list").find_all('tr')

            movie_data = []
            for movie in movies:
                movie_name = movie.find('td', class_="titleColumn").a.text
                rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
                year = movie.find('td', class_="titleColumn").span.text.strip('()')
                rating = movie.find('td', class_="ratingColumn imdbRating").strong.text

                movie_data.append([rank, movie_name, year, rating])

                if self.name and movie_name.lower() == self.name.lower():
                    return f"Rank: {rank}\nYear: {year}\nRating: {rating}"

            if self.name:
                return "Movie not found in the top-rated list."

            return movie_data

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def save_to_excel(self):
        movie_data = self.details()
        if not movie_data:
            return "No movie data available."

        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = "Top Rated Movies"

        """
        Sheet will have 4 cols 

        """
        sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

        if isinstance(movie_data, list):
            for movie in movie_data:
                sheet.append(movie)
        else:
            movie = movie_data.split('\n')
            sheet.append([movie[0].split(': ')[1], self.name, movie[1].split(': ')[1], movie[2].split(': ')[1]])

        filename = "IMDB Ratings.xlsx"
        excel.save(filename)
        return f"Movie data saved to {filename}"
    

    def scrape_movies(self):
        try:
            source = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
            source.raise_for_status()

            soup = BeautifulSoup(source.text, 'html.parser')
            movies = soup.find('tbody', class_="lister-list").find_all('tr')

            """
            Extracting the details of the Top 250 movies. 

            """

            movie_data = []
            for movie in movies:
                movie_name = movie.find('td', class_="titleColumn").a.text
                rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
                year = movie.find('td', class_="titleColumn").span.text.strip('()')
                rating = movie.find('td', class_="ratingColumn imdbRating").strong.text

                movie_data.append([rank, movie_name, year, rating])

            return movie_data

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []


    """
    Creating an excel file that has the list of all 250 movies.

    """

    def save_all_movies_to_excel(self):
        movie_data = self.scrape_movies()
        if not movie_data:
            return "No movie data available."

        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = "Top Rated Movies"
        sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

        for movie in movie_data:
            sheet.append(movie)

        filename = "IMDB Ratings.xlsx"
        excel.save(filename)
        return f"Movie data saved to {filename}"

movie_name = input("Enter a movie name (optional): ")
movie = Movie(name=movie_name)
if movie_name:
    print(movie.details())
else:
    print(movie.save_to_excel())
    
movie.save_all_movies_to_excel()
