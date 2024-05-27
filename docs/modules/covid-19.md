
```py
from scrape_up import covidinfo
```

Create an instance of the `CovidInfo` class.

```python
response = covidinfo.CovidInfo()
```

| Methods              | Details                                                        |
| -------------------- | -------------------------------------------------------------- |
| `.covid_data()`      | Returns the list of all covid data scraped from the website.   |
| `.total_cases()`     | Returns the count of total covid cases all over the world.     |
| `.total_deaths()`    | Returns the count of deaths covid cases all over the world.    |
| `.total_recovered()` | Returns the count of recovered covid cases all over the world. |
| `.latest_news()`     | Return the latest news of the day.                             |

---