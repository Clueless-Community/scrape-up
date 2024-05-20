""" This Python script extracts and saves PubMed article abstracts for a given query using the
BeautifulSoup library. It formats the search query, constructs a URL to access the PubMed API, 
retrieves the search results, and extracts necessary parameters. It then constructs another URL to 
fetch the abstracts, downloads the webpage content, parses it into plain text, and saves the text
to a file named "abstracts.txt". """

# Importing the libraries
import csv
import re
import urllib
from time import sleep
import requests
from bs4 import BeautifulSoup

# Define the search query
query = "Creatine Monohydrate"

# Function to format the search query for URL compatibility
def format_query(search_query):
    if ' ' not in search_query:
        query = search_query
    else:
        query = '"' + '+'.join(search_query.split()) + '"'
    return query

# Format the query
query = format_query(query)
print("Query: " + query)

# Construct the base URL for the PubMed API
base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
db = 'db=pubmed'

# Construct the search URL
search_eutil = 'esearch.fcgi?'
search_term = '&term=' + query
search_usehistory = '&usehistory=y'
search_rettype = '&rettype=json'
search_url = base_url + search_eutil + db + search_term + search_usehistory + search_rettype
print(search_url)

# Execute the search and retrieve the XML response
f = urllib.request.urlopen(search_url)
search_data = f.read().decode('utf-8')

# Parse the XML response to get the total count of abstracts and other parameters
total_abstract_count = int(re.findall("<Count>(\d+?)</Count>", search_data)[0])
print(total_abstract_count)
fetch_webenv = '&WebEnv=' + re.findall("<WebEnv>(\S+)<\/WebEnv>", search_data)[0]
fetch_querykey = '&query_key=' + re.findall("<QueryKey>(\d+?)</QueryKey>", search_data)[0]

# Construct the URL for fetching the abstracts
fetch_eutil = 'efetch.fcgi?'
retmax = 100
retstart = 0
fetch_retstart = "&retstart=" + str(retstart)
fetch_retmax = "&retmax=" + str(retmax)
fetch_retmode = "&retmode=text"
fetch_rettype = "&rettype=abstract"
fetch_url = base_url + fetch_eutil + db + fetch_querykey + fetch_webenv + fetch_retstart + fetch_retmax + fetch_retmode + fetch_rettype

# Function to download the webpage content
def download_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text
    else:
        print("Failed to download.")
        return None

# Function to save text content to a file
def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print("Text saved to", filename)

# Define the fetch URL and the output filename
url = fetch_url
filename = "abstracts.txt"

# Download the webpage content and save it to a file
webpage_text = download_webpage(url)
if webpage_text:
    save_text_to_file(webpage_text, filename)
