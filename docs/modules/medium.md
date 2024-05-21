## Medium

```python
from scrape_up import medium
```

### Scrape user details

First, create an object of class `User`

```python
user = medium.Users(username="nikhil25803")
```

| Methods           | Details                                  |
| ----------------- | ---------------------------------------- |
| `.get_articles()` | Returns the article titles of the users. |

### Scrape trending articles

| Methods           | Details                                    |
| ----------------- | ------------------------------------------ |
| `.get_trending()` | Returns the trending titles of the medium. |

### Scrape publication details

First, create an object of class `Publication`

```python
publication = medium.Publication(link="https://....")
```

| Methods           | Details                                              |
| ----------------- | ---------------------------------------------------- |
| `.get_articles()` | Returns a list of articles of the given publication. |

---