from bs4 import BeautifulSoup

from scrape_up.config.request_config import RequestConfig, get


class AmazonKindle:
    """
    Create an instance of `Book` class.
    ```python
    books = AmazonKindle()
    ```
    | Methods          | Details                                                |
    | ---------------- | ------------------------------------------------------ |
    | `.bestsellers()` | Returns the list of best-selling books on AmazonKindle |
    | `.topbooks()`    | Returns the list of top books on AmazonKindle          |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def bestsellers(self):
        """
        Class - `Book`\n
        Example -\n
        ```python
        books = AmazonKindle()
        book.bestsellers()
        ```
        Return\n
        ```js
        [
            {
                "Book_Title":"101 Brain Booster Activity Book: Fun Activity Book For Children",
                "Author_Name":"Wonder House Books",
                "Stars":"N/A",
                "Price":"₹149.00",
                "URL":"https://www.amazon.in/101-Brain-Booster-ActivityBook/dp/9388369793/ref=zg_bs_g_books_sccl_20/000-0000000-0000000?psc=1"
            }
        ]
        ```
        """
        try:
            url = "https://www.amazon.in/gp/bestsellers/books/"
            response = get(url, self.config)
            page_contents = response.text
            doc = BeautifulSoup(page_contents, "html.parser")

            book_title_tags = doc.find_all("div", {"class": "zg-grid-general-faceout"})
            author_name_tags = doc.find_all("div", {"class": "zg-grid-general-faceout"})
            rating = "a-icon a-icon-star-small a-star-small-4-5 aok-align-top"
            rating_tags = doc.find_all("i", {"class": rating})
            book_price_tags = doc.find_all("div", {"class": "zg-grid-general-faceout"})
            book_url_tag = doc.find_all("div", {"class": "zg-grid-general-faceout"})

            all_books = []

            for i in range(len(book_title_tags)):
                book_title = book_title_tags[i].find("span").text
                author_name = (
                    author_name_tags[i]
                    .find("div", {"class": "a-row a-size-small"})
                    .text
                )

                # Check if the index is within the range of rating_tags
                if i < len(rating_tags):
                    star_rating = rating_tags[i].find("span").text
                else:
                    star_rating = (
                        "N/A"  # Assign a default value if rating is not available
                    )

                book_price = (
                    book_price_tags[i].find("span", {"class": "p13n-sc-price"}).text
                )
                book_url = (
                    "https://www.amazon.in"
                    + book_url_tag[i].find("a", {"class": "a-link-normal"})["href"]
                )

                book_details = {
                    "Book_Title": book_title,
                    "Author_Name": author_name,
                    "Stars": star_rating,
                    "Price": book_price,
                    "URL": book_url,
                }

                all_books.append(book_details)

            return all_books

        except Exception as e:
            return None

    def topbooks(self):
        """
        Class - `Book`\n
        Example -\n
        ```python
        books = AmazonKindle()
        book.topbooks()
        ```
        Return\n
        ```js
        [
            {
                "Title":"Master Your Emotions: A Practical Guide to Overcome Negativity and Better Manage Your Feelings (Mastery Series Book 1)",
                "Rating(out of 5)":"4.5",
                "Price(in rupees)":"₹199.00",
                "Link":"https://www.amazon.in//Master-Your-Emotions-Practical-Negativity-ebook/dp/B07CX8H6YH/ref=zg_bs_g_digital-text_sccl_1/260-0078955-4830376?psc=1"
            }
            ...
        ]
        ```
        """
        try:
            all_books = []
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
            }
            for page_link in [
                "https://www.amazon.in/gp/bestsellers/digital-text/ref=zg_bs_nav_0",
                "https://www.amazon.in/gp/bestsellers/digital-text/ref=zg_bs_pg_2_digital-text?ie=UTF8&pg=2",
            ]:
                webpage = get(page_link, self.config).text
                soup = BeautifulSoup(webpage, "lxml")
                books_container = soup.find(
                    "div", {"class": "p13n-gridRow _cDEzb_grid-row_3Cywl"}
                )
                for items in books_container.find_all("div", {"id": "gridItemRoot"}):
                    title = items.find(
                        "div", {"class": "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"}
                    ).text
                    stars = items.find("span", {"class": "a-icon-alt"})
                    if stars is None:
                        stars = "Rating not available"

                    else:
                        stars = stars.text.split()[0]
                    price = items.find("span", {"class": "a-size-base"}).text
                    link = items.find("a", {"class": "a-link-normal"}, href=True)
                    url = "https://www.amazon.in/" + link["href"]
                    books = {
                        "Title": title,
                        "Rating(out of 5)": stars,
                        "Price(in rupees)": price,
                        "Link": url,
                    }
                    all_books.append(books)
            return all_books

        except Exception as e:
            return None
