```py
from scrape_up import hackerrank
```

### Scrape user details

Create an object of class `User`.

```python
hackerank = hackerrank.User()
```

| Methods                      | Details                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| `get_profile(id="username")` | Returns name, username, country, user_type, details, badges, verified_skills, social etc. |
| `get_skills()`               | Returns a list of verified skills and their links.                                        |

### Scrape contest details

Create an object of class `Contest`.

```python
hackerank = hackerrank.Contest()
```

| Methods               | Details                                                              |
| --------------------- | -------------------------------------------------------------------- |
| `active_contests()`   | Returns information on active contests like title, status, and link. |
| `archived_contests()` | Returns information regarding archived contests.                     |

---