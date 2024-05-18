# import requests
# from bs4 import BeautifulSoup


# class Comapiens:
#     def __init__(self, num_pages: int = 1):
#         self.num_pages = num_pages

#     def write_sorted_list(self, file, company_list):
#         company_list.sort(key=lambda x: x[1], reverse=True)
#         for company_name, rating in company_list:
#             file.write(f"{company_name.strip()} {rating}\n")

#     def scrape_companies(self):
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
#         }

#         for page in range(1, self.num_pages + 1):
#             print(f"Scraping webpage number: {page} of {self.num_pages}")

#             url = f"https://www.ambitionbox.com/list-of-companies?page={page}"
#             response = requests.get(url, headers=headers)

#             if response.status_code == 200:
#                 soup = BeautifulSoup(response.text, "lxml")

#                 companies = soup.find_all("div", class_="companyCardWrapper")

#                 company_ratings = []

#                 for company in companies:
#                     company_name = company.find(
#                         "h2", class_="companyCardWrapper__companyName"
#                     ).text.strip()
#                     company_star = company.find(
#                         "span", class_="companyCardWrapper__companyRatingValue"
#                     )

#                     if company_name and company_star:
#                         try:
#                             rating = float(company_star.text)
#                             company_ratings.append((company_name, rating))
#                         except ValueError:
#                             print(f"Error parsing rating for company: {company_name}")

#                 with open("src/scrape_up/ambitionBox/company_ratings.txt", "a") as f:
#                     f.write(f"\nPAGE: {url}\n")
#                     f.write("COMPANY UNDER 5 STAR\n")
#                     self.write_sorted_list(
#                         f, [r for r in company_ratings if 4 < r[1] <= 5]
#                     )

#                     f.write("\nCOMPANY UNDER 4 STAR\n")
#                     self.write_sorted_list(
#                         f, [r for r in company_ratings if 3 < r[1] <= 4]
#                     )

#                     # Corrected indentation for following lines
#                     f.write("\nCOMPANY UNDER 3 STAR\n")
#                     self.write_sorted_list(
#                         f, [r for r in company_ratings if 2 < r[1] <= 3]
#                     )

#                     f.write("\nCOMPANY UNDER 2 STAR\n")
#                     self.write_sorted_list(
#                         f, [r for r in company_ratings if 1 < r[1] <= 2]
#                     )

#                     f.write("\nCOMPANY UNDER 1 STAR\n")
#                     self.write_sorted_list(
#                         f, [r for r in company_ratings if 0 < r[1] <= 1]
#                     )
#             else:
#                 print(f"Error scraping page {page}: {response.status_code}")


# if __name__ == "__main__":
#     c = Comapiens(10)
#     c.scrape_companies()
