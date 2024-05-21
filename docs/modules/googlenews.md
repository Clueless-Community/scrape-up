
### Scrape articles with title, descriptions, news source, date and link regarding a topic

Create an instance of `GoogleNews` class.

```python
articles = GoogleNews()
```

| Methods                        | Details                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| `.getArticles(topic="github")` | Returns the list of articles with title, descriptions, news source, date and link in JSON format |
| `.top_stories()`               | Returns the list of top stories listed regarding the mentioned topic                             |
| `.timed_aticles(time)`         | Returns the list of top stories listed regarding the mentioned topic and within that time frame  |
| `.bylanguage(lang)`            | Returns the list of top stories listed regarding the mentioned topic in the specified language   |
| `.bynumerofdaysback(number)`   | Returns the list of stories listed by given number of days back from the current day             |
| `.bylocation(countryname)`     | Returns the list of top stories listed of the specified country or geolocation                   |

---