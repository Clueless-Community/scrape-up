
```py
from scrape_up import hacker_news
```

Create an instance of `HackerNews` class.

```py
articles = HackerNews()
```

| Methods            | Details                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `.articles_list()` | Returns the latest articles along with their score, author, author url, time, comment count and link in JSON format.     |
| `.new_articles()`  | Returns the latest new articles along with their score, author, author url, time, comment count and link in JSON format. |
| `.past_articles()` | Returns the past articles along with their score, author, author url, time, comment count and link in JSON format.       |
| `.ask_articles()`  | Returns the ask articles along with their score, author, author url, time, comment count and link in JSON format.        |
| `.show_articles()` | Returns the show articles along with their score, author, author url, time, comment count and link in JSON format.       |
| `.jobs()`          | Returns the jobs along with their time and link in JSON format.                                                          |

---