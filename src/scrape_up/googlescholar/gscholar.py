import requests
from bs4 import BeautifulSoup

def get_scholar_results(query, num_results=10):
    
    base_url = "https://scholar.google.com/scholar"
    params = {
        'q': query,
        'hl': 'en',
        'num': num_results
    }

    
    response = requests.get(base_url, params=params)
    response.raise_for_status()  

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='gs_r gs_or gs_scl')

    
    parsed_results = []
    for result in results:
        title_tag = result.find('h3', class_='gs_rt')
        if title_tag and title_tag.a:
            title = title_tag.a.text
            link = title_tag.a['href']
        else:
            title = title_tag.text if title_tag else 'No title'
            link = None

        snippet = result.find('div', class_='gs_rs').text if result.find('div', class_='gs_rs') else 'No snippet'
        publication_info = result.find('div', class_='gs_a').text if result.find('div', class_='gs_a') else 'No publication info'

        parsed_results.append({
            'title': title,
            'link': link,
            'snippet': snippet,
            'publication_info': publication_info
        })

    return parsed_results

# Main function 
if __name__ == "__main__":
    query = input("Enter your query: ")
    num_results = int(input("Enter the number of results you want: "))
    results = get_scholar_results(query, num_results)
    for idx, result in enumerate(results):
        print(f"Result {idx + 1}:")
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Snippet: {result['snippet']}")
        print(f"Publication Info: {result['publication_info']}")
        print()
