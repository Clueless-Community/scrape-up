### Install the package using `pip`:

```bash
pip install scrape-up --upgrade
```

### Import the required module

> For example - `GitHub`

```py
# Import the required module
from scrape_up import github
```

### Instantiate an object with required parameters

> Also mentioned in the docstring

```
user = github.Users(username="nikhil25803")
```

### Call the required method.

> For example, to extract the number of followers of a user:

```python
# Call the followers method
followers_count = user.followers()
```
