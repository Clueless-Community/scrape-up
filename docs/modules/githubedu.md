
```python
from scrape_up import github_education
```

### Scrape user details

Create an instance of the `Events` class.

```py
events = github_education.Events()
```

| Methods         | Details                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| `.get_events()` | Returns the latest events along with their title, image_url, description, date, location, language, tags, and link. |

---