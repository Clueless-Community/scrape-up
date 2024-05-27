Create an instance of `Letterboxd` class.

```python
letterboxd_user = Letterboxd(user="arpy8")
```

| Methods                     | Details                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| `.films_watched()`          | Returns the numbers of films watched by the user.                                                    |
| `.recent_activity(n)`       | Returns a list of length `n` of the latest activity by the user.                                     |
| `.recent_reviews(n)`        | Returns a list of dictionaries of length `n` with the latest reviews by the user.                    |
| `.get_watchlist(n)`         | Returns a list of length `n` including movies and series watchlisted by the user.                    |
| `.get_followers_count()`    | Returns the number of followers of the user.                                                         |  
| `.get_following_count()`    | Returns the number of following of the user.                                                         |

Note: `n` is an integer value which is optional and can be used to limit the number of results returned by the methods.

---