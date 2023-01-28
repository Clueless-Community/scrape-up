<h1 align=center> Scrape UP </h1>

<h3 align=center> An alternative to API, this project is a web-scraping-based python package that enables you to scrape data from various platforms like GitHub, Twitter, Instagram, or any useful website.</h3>

----
<br>
<p align="center">
  <a href="https://github.com/Clueless-Community/fintech-api/issues"><img src="https://img.shields.io/github/issues/Clueless-Community/scrape-up.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
  <a href="https://github.com/Clueless-Community/fintech-api/fork"><img src="https://img.shields.io/github/forks/Clueless-Community/scrape-up.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
  <a href="#"><img src="https://img.shields.io/github/stars/Clueless-Community/scrape-up.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
  <a href="https://github.com/Clueless-Community/fintech-api/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Clueless-Community/scrape-up.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
</p>

---

## How to use?
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

You can check all the methods that we provide [here]()

## The goal 🎯
While working on a project, we often ran into a situation where we faced issues like request timeout, rate limit, etc. But leveraging the power of web scrapping, we are here with a solution. This project is a web-scraping-based Python tool that you may use as an alternative to APIs to scrape data from a variety of sites, including GitHub, Twitter, Instagram, and any helpful website.

## Wants to contribute? 👀
We happily welcome any meaningful change or modification to this project.
Before start contributing, we recommend you go through the [CONTRIBUTING.md](https://github.com/Clueless-Community/fintech-api/blob/main/CONTRIBUTING.md) file, where all the guidelines have been mentioned that will guide you to make your contribution.


---
