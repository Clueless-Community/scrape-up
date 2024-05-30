class Companies:
    """
    A class to scrape company information and ratings from the AmbitionBox website.

    Attributes:
        num_pages (int): The number of pages to scrape.

    Methods:
        __init__(num_pages=1):
            Initializes the Companies object with the specified number of pages to scrape.
        
        print_sorted_list(company_list):
            Prints a list of companies sorted by their ratings in descending order.

        scrape_companies():
            Scrapes company information and ratings from the specified number of pages on the AmbitionBox website.
            Categorizes and prints the companies based on their ratings.
    """

    def __init__(self, num_pages: int = 1):
        """
        Initializes the Companies object with the specified number of pages to scrape.

        Args:
            num_pages (int): The number of pages to scrape. Defaults to 1.
        """
        self.num_pages = num_pages

    def print_sorted_list(self, company_list):
        """
        Prints a list of companies sorted by their ratings in descending order.

        Args:
            company_list (list): A list of tuples where each tuple contains the company name and its rating.
        """
        company_list.sort(key=lambda x: x[1], reverse=True)
        for company_name, rating in company_list:
            print(f"{company_name.strip()} {rating}")

    def scrape_companies(self):
        """
        Scrapes company information and ratings from the specified number of pages on the AmbitionBox website.
        Categorizes and prints the companies based on their ratings.
        
        The companies are categorized and printed as follows:
        - Companies with 5 stars
        - Companies with 4 stars
        - Companies with 3 stars
        - Companies with 2 stars
        - Companies with 1 star
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }

        for page in range(1, self.num_pages + 1):
            print(f"Scraping webpage number: {page} of {self.num_pages}")

            url = f"https://www.ambitionbox.com/list-of-companies?page={page}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                companies = soup.find_all('div', class_="companyCardWrapper")
                company_ratings = []

                for company in companies:
                    company_name = company.find('h2', class_="companyCardWrapper__companyName").text.strip()
                    company_star = company.find('span', class_="companyCardWrapper__companyRatingValue")

                    if company_name and company_star:
                        try:
                            rating = float(company_star.text)
                            company_ratings.append((company_name, rating))
                        except ValueError:
                            print(f"Error parsing rating for company: {company_name}")

                print(f"\nPAGE: {url}\n")
                print("COMPANIES WITH 5 STARS\n")
                self.print_sorted_list([r for r in company_ratings if 4 < r[1] <= 5])

                print("\nCOMPANIES WITH 4 STARS\n")
                self.print_sorted_list([r for r in company_ratings if 3 < r[1] <= 4])

                print("\nCOMPANIES WITH 3 STARS\n")
                self.print_sorted_list([r for r in company_ratings if 2 < r[1] <= 3])

                print("\nCOMPANIES WITH 2 STARS\n")
                self.print_sorted_list([r for r in company_ratings if 1 < r[1] <= 2])

                print("\nCOMPANIES WITH 1 STAR\n")
                self.print_sorted_list([r for r in company_ratings if 0 < r[1] <= 1])
            else:
                print(f"Error scraping page {page}: {response.status_code}")
