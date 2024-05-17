from bs4 import BeautifulSoup as bs

from scrape_up.config.request_config import RequestConfig, get


def link_to_get(link, config: RequestConfig):
    """This function will get the url of the image & book download direct link using the given link for book download"""
    response = get(link, config)
    th_html = bs(response.text, "html.parser")
    td_all = th_html.find_all("td", id="info")
    td_all = td_all[0]
    td_a = td_all.find_all("a")
    link_href = td_a[1].get("href")
    img_link_td = td_all.find("img", alt="cover")
    img_link_src = img_link_td.get("src")
    img_link = f"http://library.lol{img_link_src}"
    return [link_href, img_link]


class LibGen:
    """
    Create an object of the 'LibGen' class\n
    ```python
    scraper = LibGen()
    ```
    | Methods       | Details                       |
    | --------------| ----------------------------- |
    | `.getBooks(book_name=" ")` | Returns the books with name, author, size, format, book link, book cover link, language |
    """

    def __init__(self, *, config: RequestConfig = RequestConfig()):
        self.config = config

    def getBooks(self, book_name: str):
        """
        Class - `LibGen`
        Example:
        ```
        courses = LibGen(book_name="Python")
        courses.getBooks()
        ```
        Returns:
        ```
        [
            {
                "name":"The Silent Patient 9781250301697",
                "author":"Alex Michaelides",
                "size":"411 Kb",
                "format":"epub",
                "link":"https://cloudflare-ipfs.com/ipfs/bafykbzaceanodrmdg7zm2i5yj7v3uv5ep4qnvfv53jj4eydfn53gxsjjkyhgi?filename=Alex%20Michaelides%20-%20The%20Silent%20Patient.epub",
                "language":"http://library.lol/covers/2443000/20ee5ec38fbb07bfe9502007c2a2396f-g.jpg"
            }
        ]
        ```
        """
        try:
            Books = []
            name = book_name
            results = 10
            mainres = 25
            if name == "":
                return "Error: enter name"
            name = name.replace(" ", "+")

            url = f"http://libgen.is/search.php?req={name}&lg_topic=libgen&open=0&view=simple&res={mainres}&phrase=1&column=def"

            response = get(url, self.config)
            bs_html = bs(response.text, "html.parser")

            if "Search string must contain minimum 3 characters.." in bs_html.body:
                return "Error: Title Too Short"

            table = bs_html.find_all("table")
            table = table[2]
            table_rows = table.find_all("tr")
            a = len(table_rows)
            table_rows.pop(0)
            obj_keys = ["name", "author", "size", "format", "link", "language"]
            if a > 1:
                counter = 1
                for i in table_rows:
                    if counter <= results:
                        book_lst = []

                        table_datas = i.find_all("td")

                        book_name = table_datas[2].get_text()

                        author = table_datas[1].get_text()

                        link_row = table_datas[9]
                        a = link_row.find("a", href=True)
                        link = a.get("href")

                        link_all = link_to_get(link, self.config)

                        language_row = table_datas[6]
                        language = language_row.get_text()

                        size_row = table_datas[7]
                        size = size_row.get_text()

                        type_row = table_datas[8]
                        type_ofit = type_row.get_text()

                        if (
                            type_ofit != "pdf" and type_ofit != "epub"
                        ) or language != "English":
                            continue
                        book_lst.append(book_name)
                        book_lst.append(author)
                        book_lst.append(size)
                        book_lst.append(type_ofit)
                        book_lst.append(link_all[0])
                        book_lst.append(link_all[1])
                        book_lst.append(language)

                        Books.append(dict(zip(obj_keys, book_lst)))
                        counter += 1
                if len(Books) >= 1:
                    return Books
                else:
                    return "Error: no results found"
            else:
                return "Error: no results found"
        except:
            return "Error"
