# How to use this package? 👀
+ Install the package from `pip`
```powershell
pip install scrape-up
```

+ Scrape the required information, for example one want to extract number of followers of a user.
```python
# Import the required module
from scrape_up import github

# Instantiate an object with username provided.
user = github.User(username="nikhil25803")

# Cal the followers function
print(user.followers())

# Output - '59'
```

---

# The platforms and methods we cover 💫

## GitHub
```python
from scrape_up import github
```

### Scrape User details

First create an object of class `User`
```python
user = github.Users(username="nikhil25803")
```

| Methods |  Details |
|---|---|
|  `.followers()` | Returns the number of followers of a user. |
|  `.get_avatar()` | Returns the avatar url of a user. |


|  `.repo_count()` | Returns the number of Repositories of a user. |
|  `.star_count()` | Returns the number of stars of a user. |

| `.following()` | Returns the number of followings of a user. |

|  `.get_bio()`  | Returns the bio of a user. |
|  `.get_repo()` | Returns the list of pinned repositories for a user. |
|  `.repo_count()` | Returns the number of Repositories of a user. |
|  `.star_count()` | Returns the number of stars of a user. |
|  `.get_yearly_contributions()` |Returns the number of contributions made in 365 days frame. |
|  `.get_repositories()` | Returns the list of repositories of a user. |

