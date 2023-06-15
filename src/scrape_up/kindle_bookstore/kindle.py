#Import the necessary libraries
#requests for downloading webpage, BeautifulSoup for web scraping, pandas for creating dataframe
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Book:
    
    #Give the necessary url of the kindle site, to scrape information
    url= 'https://www.amazon.in/gp/bestsellers/books/'
    response= requests.get(url)
    page_contents= response.text

    #Parse the information
    doc = BeautifulSoup(page_contents, 'html.parser')

    #Extracting title of the book
    book_title_tags= doc.find_all('div',{"class": "zg-grid-general-faceout"})
    def get_book_title(book_title_tags):
        Book_Titles=[]
        for tag in book_title_tags:
            Book_Titles.append(tag.find('span').text)
        return Book_Titles

    # get_book_title(book_title_tags)[:10]

    #Extracting authors 
    author_name_tags= doc.find_all('div',{'class':'zg-grid-general-faceout'})
    def get_all_authors(author_name_tags):
        Author_Names=[]
        for tag in author_name_tags:
            Author_Names.append(tag.find('div',{'class':'a-row a-size-small'}).text)
        return Author_Names
    # get_all_authors(author_name_tags)[:10] 

    #Extracting ratings
    rating='a-icon a-icon-star-small a-star-small-4-5 aok-align-top'
    rating_tags= doc.find_all('i',{'class': rating})
    def get_all_stars(rating_tags):
        Stars=[]
        for tag in rating_tags:
            Stars.append(tag.find('span').text)
        return Stars
    # get_all_stars(rating_tags)[:10]

    #Extracting price
    book_price_tags= doc.find_all('div',{"class": "zg-grid-general-faceout"})
    def get_all_price(book_price_tags):
        Book_Price=[]
        for tag in book_price_tags:
            Book_Price.append(tag.find('span',{'class':'p13n-sc-price'}).text)
        return Book_Price
    # get_all_price(book_price_tags)[:10]

    #Extracting book url
    book_url_tag=doc.find_all('div',{"class": "zg-grid-general-faceout"})
    def get_all_url(book_url_tag):
        Book_Title_Urls=[]
        base_url="https://www.amazon.in"
        for tag in book_url_tag:
            Book_Title_Urls.append(base_url + tag.find('a',{'class':'a-link-normal'})['href'])
        return Book_Title_Urls
    # get_all_url(book_url_tag)[:10]

    #Scraping multiple pages by providing page url
    def scrape_page(page_number):
        url='https://www.amazon.in/gp/bestsellers/books/' + str(page_number)
        doc=BeautifulSoup(page_contents, 'html.parser')
        title=get_book_title(book_title_tags)
        author=get_all_authors(author_name_tags)
        stars=get_all_stars(rating_tags)
        price=get_all_price(book_price_tags)
        title_url=get_all_url(book_url_tag)
        return title,author,stars,price,title_url

    all_titles,all_authors,all_stars,all_price,all_urls=[],[],[],[],[]
    for page_number in range(1,3):
        title,author,stars,price,title_url= scrape_page(page_number)
        all_titles += title
        all_authors += author
        all_stars += stars
        all_price +=price
        all_urls +=title_url
    
    all_books={
                 'Book_Title': all_titles,
                 'Author_Name':all_authors,
                 'Stars': all_stars ,
                 'Price': all_price ,
                 'URL':all_urls}

    #Creating a dataframe using pandas
    dataframe = pd.DataFrame.from_dict(all_books, orient='index')
    dataframe = dataframe.transpose()
    
#Print dataframe
#dataframe