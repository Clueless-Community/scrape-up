#Import the necessary libraries
#requests for downloading webpage, BeautifulSoup for web scraping, pandas for creating dataframe
import requests
from bs4 import BeautifulSoup

# scraping kindle product page
class Book:
    
    def __init__(self, url: str):
        self.url = url

    def scrape_page(self):
        """
        Class - `Book`\n
        Example -\n
        ```python
        book= Book(url= "https://www.amazon.in/gp/bestsellers/books/")
        book.scrape_page()
        ```
        Return\n
        ```python
        return {all_books with details in json}
        ```
        """
        try:
            url = self.url
            response = requests.get(url)
            page_contents = response.text
            doc = BeautifulSoup(page_contents, 'html.parser')

            book_title_tags = doc.find_all('div', {"class": "zg-grid-general-faceout"})
            author_name_tags = doc.find_all('div', {'class': 'zg-grid-general-faceout'})
            rating = 'a-icon a-icon-star-small a-star-small-4-5 aok-align-top'
            rating_tags = doc.find_all('i', {'class': rating})
            book_price_tags = doc.find_all('div', {"class": "zg-grid-general-faceout"})
            book_url_tag = doc.find_all('div', {"class": "zg-grid-general-faceout"})

            all_books = []

            for i in range(len(book_title_tags)):
                book_title = book_title_tags[i].find('span').text
                author_name = author_name_tags[i].find('div', {'class': 'a-row a-size-small'}).text
            
                # Check if the index is within the range of rating_tags
                if i < len(rating_tags):
                    star_rating = rating_tags[i].find('span').text
                else:
                    star_rating = "N/A"  # Assign a default value if rating is not available
            
                book_price = book_price_tags[i].find('span', {'class': 'p13n-sc-price'}).text
                book_url = "https://www.amazon.in" + book_url_tag[i].find('a', {'class': 'a-link-normal'})['href']

                book_details = {
                    'Book_Title': book_title,
                    'Author_Name': author_name,
                    'Stars': star_rating,
                    'Price': book_price,
                    'URL': book_url
                }

                all_books.append(book_details)

            return all_books
    
        except Exception as e:
            print("An error occurred:", str(e))
            return []

