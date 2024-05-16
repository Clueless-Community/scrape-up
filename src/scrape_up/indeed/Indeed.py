import requests
from bs4 import BeautifulSoup


class Indeed:
    """
    ```python
    indeed = Indeed(search_query, location_query, min_jobs)
    ```

    Attributes:
    | Attribute         | Optional | Details                                        |
    |-------------------|----------|------------------------------------------------|
    | `search_query`    | No       | The search query for job listings              |
    | `location_query`  | Yes      | The location query for job listings            |
    | `min_jobs`        | Yes      | The minimum number of job listings to retrieve |

    Methods:
    | Method                          | Details                                                                  |
    |---------------------------------|--------------------------------------------------------------------------|
    | `.get_jobs()`                   | Returns a list of job listings based on the search and location queries. |
    | `.scrape_job_info(job_card)` | Extracts job details from a given job card HTML element               |
    """

    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    def __init__(
        self, search_query: str, location_query: str = "", min_jobs: int = 100
    ):
        self.search_query = search_query
        self.location_query = location_query
        self.min_jobs = min_jobs

    def get_jobs(self):
        """
        Retrieves job listings based on the search and location queries.

        Returns:
        list: A list of dictionaries, each containing details of a job listing.
        ```js
        [
            {
                'title': 'Principal Validation Engineer',
                'company': 'ARM',
                'location': 'Bengaluru, Karnataka',
                'link': 'https://in.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BgJnowPS_nFa6JvbNw1Ud-JjG_6nenis8YkFjCtkUlxoHXLw2_bm5yl4s91IBplAlbqqJNhhYa7H_jO-GNDfIyg3T_5dJwSCRgZqUKzWGp5QE2wu-KSRKxekLjhWywloA9aU3L_dCvaWl8jKXe9g_b_Ks6RfLln87tpYl9awPbka9MuyygAW6Q4nN6AP84HVVOe2oujXdRTLJNJe9Afeuw89XW3d1Pa8OSvGma3RXh2nn2jzf7GdwJwjoyfjh41eoRLmYwgerS3RcmPG_FtjCj0N3jOjjJ2JxiLmRCiYFsPhqD_RA6LtTKHFPJLl4MhoTq4Sr1nEwEAlleOOso4VeScvumjl627h93IrsZZCIErpJUuHgOe_uG6OYlVode6J4c1AkQa04QsgWf3hgTxRVdDm_hCWj1IOJ4vEWtqcQqzL8JQZrl_7wDdxJdCbLsgzIdhyqeOEtDw6LicE4MpDbsgdOY0IfqDnHurqU7DtVkSGp7M6g3K1LAa9P71Ja5CzLeBENh8PR56Y9A_H3QbTPIETXyOwBAlDy371jZckl2JQQa2ah7foecuDfUq4N5rdJiQazsI_JvSkEykNX2fVpvwXySpFllvCUex1NlER044zfL51qUtWptKee1VCKjK1BloeOdH53P5pnfhiGfLju0RuJh82qBF0vJVytcjOPmjk8IMkOA2M51aTv3BHBfYNsF4WPQgNuPun6VO5o9QIrkI-cGnkM_UqaIFe9-wxPIE1DCVNU7dqWMuJWSVqYq4GA7sQ7uJysLMgj50bUW7JSadrgJBcvZ3IE=&xkcb=SoCn6_M3AAmk1Px83x0KbzkdCdPP&camk=CPChkbYSGj8qrV5440N2ZQ==&p=0&fvj=0&vjs=3',
                'tags': [],
                'description': ['System Validation engineers in this group are responsible for driving validation specifications & methodology and deliver on the validation of subsystems for…'],
                'posted_day': 'Posted 30+ days ago'
            }
            {...},
            {...},
        ]
        ```
        """
        search = self.search_query.strip().replace(" ", "+").lower()
        location = self.location_query.strip().replace(" ", ", ").lower()

        base_url: str = f"https://in.indeed.com/m/jobs?q={search}"
        if location != "":
            base_url = f"{base_url}&l={location}"

        job_listings = []
        start_index = 0
        while len(job_listings) < self.min_jobs:
            url = f"{base_url}&start={start_index}"
            response = requests.get(url, headers=Indeed.headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                job_cards = soup.find_all("div", class_="job_seen_beacon")
                if not job_cards:
                    break
                for job_card in job_cards:
                    job_listings.append(self.scrape_job_info(job_card))
                    if len(job_listings) >= self.min_jobs:
                        break
                start_index += len(job_cards)
            else:
                print(f"Failed to fetch URL: {url}")
                break

        return job_listings

    def scrape_job_info(self, job_card):
        """
        Extracts job details from a given job card HTML element.

        Args:
        job_card: BeautifulSoup HTML element representing a job card.

        Returns:
        dict: A dictionary containing details of the extracted job.
        ```js
        {
            'title': 'Principal Validation Engineer',
            'company': 'ARM',
            'location': 'Bengaluru, Karnataka',
            'link': 'https://in.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BgJnowPS_nFa6JvbNw1Ud-JjG_6nenis8YkFjCtkUlxoHXLw2_bm5yl4s91IBplAlbqqJNhhYa7H_jO-GNDfIyg3T_5dJwSCRgZqUKzWGp5QE2wu-KSRKxekLjhWywloA9aU3L_dCvaWl8jKXe9g_b_Ks6RfLln87tpYl9awPbka9MuyygAW6Q4nN6AP84HVVOe2oujXdRTLJNJe9Afeuw89XW3d1Pa8OSvGma3RXh2nn2jzf7GdwJwjoyfjh41eoRLmYwgerS3RcmPG_FtjCj0N3jOjjJ2JxiLmRCiYFsPhqD_RA6LtTKHFPJLl4MhoTq4Sr1nEwEAlleOOso4VeScvumjl627h93IrsZZCIErpJUuHgOe_uG6OYlVode6J4c1AkQa04QsgWf3hgTxRVdDm_hCWj1IOJ4vEWtqcQqzL8JQZrl_7wDdxJdCbLsgzIdhyqeOEtDw6LicE4MpDbsgdOY0IfqDnHurqU7DtVkSGp7M6g3K1LAa9P71Ja5CzLeBENh8PR56Y9A_H3QbTPIETXyOwBAlDy371jZckl2JQQa2ah7foecuDfUq4N5rdJiQazsI_JvSkEykNX2fVpvwXySpFllvCUex1NlER044zfL51qUtWptKee1VCKjK1BloeOdH53P5pnfhiGfLju0RuJh82qBF0vJVytcjOPmjk8IMkOA2M51aTv3BHBfYNsF4WPQgNuPun6VO5o9QIrkI-cGnkM_UqaIFe9-wxPIE1DCVNU7dqWMuJWSVqYq4GA7sQ7uJysLMgj50bUW7JSadrgJBcvZ3IE=&xkcb=SoCn6_M3AAmk1Px83x0KbzkdCdPP&camk=CPChkbYSGj8qrV5440N2ZQ==&p=0&fvj=0&vjs=3',
            'tags': [],
            'description': ['System Validation engineers in this group are responsible for driving validation specifications & methodology and deliver on the validation of subsystems for…'],
            'posted_day': 'Posted 30+ days ago'
        }
        ```
        """
        job_title_element = job_card.find("h2", class_="jobTitle")
        job_title: str = job_title_element.text.strip() if job_title_element else None

        job_post_state_element = job_card.find("span", class_="css-92r8pb")
        company_name: str = (
            job_post_state_element.text.strip() if job_post_state_element else None
        )

        location_element = job_card.find("div", class_="css-1p0sjhy")
        location: str = location_element.text.strip() if location_element else None

        link_element = job_card.find("a", class_="jcs-JobTitle")
        link: str = (
            "https://in.indeed.com" + link_element["href"] if link_element else None
        )

        meta_data_element = job_card.find("div", class_="jobMetaDataGroup")
        if meta_data_element:
            meta_data_items = meta_data_element.find_all("div", class_="css-1cvo3fd")
            meta_data: list = [item.text.strip() for item in meta_data_items]
        else:
            meta_data: list = []

        job_description_element = job_card.find("div", class_="css-9446fg")
        if job_description_element:
            li_elements = job_description_element.find_all("li")
            job_description: list = [li.text.strip() for li in li_elements]
        else:
            job_description: list = []

        job_post_state_element = job_card.find("span", class_="css-qvloho")
        job_post_state: str = (
            job_post_state_element.contents[-1].text.strip()
            if job_post_state_element
            else None
        )

        job = {
            "title": job_title,
            "company": company_name,
            "location": location,
            "link": link,
            "tags": meta_data,
            "description": job_description,
            "posted_day": job_post_state,
        }
        return job
