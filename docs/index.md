# About

An alternative to APIs, Scrape Up is a Python package for web scraping. It allows you to extract data from platforms like GitHub, Twitter, Instagram, or any other website that contains valuable information. It enables you to gather data through programming.

<div align="center">
  <br>
  <img src="https://img.shields.io/github/repo-size/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-closed-raw/Clueless-Community/scrape-up?style=for-the-badge" />
  <br>
  <img src="https://img.shields.io/github/forks/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr-closed-raw/Clueless-Community/scrape-up?style=for-the-badge" />
  <br>
  <img src="https://img.shields.io/github/stars/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/Clueless-Community/scrape-up?style=for-the-badge" />
</div>

---

## Contribution

Contribute to this project under GSSoC 2024.

![image](https://github.com/Clueless-Community/scrape-up/assets/93156825/0c77de27-cae3-45ec-87fa-2d192450005d)

## What is GSSoC? 🤔

GirlScript Summer Of Code is a three-month-long Open-Source Program conducted every summer by the Girlscript Foundation. With constant efforts, participants contribute to numerous projects under the extreme guidance of skilled mentors over these months. With such exposure, students begin to contribute to real-world projects from the comfort of their homes. GirlScript Summer Of Code has witnessed active participation over the years, and the 2024 edition aims to carry the legacy with a promising impact.

Learn more about it [here](https://gssoc.girlscript.tech/)

---

## Why Scrape Up? 👀

- **Flexible Scraping**: Customize and define the specific data you want to extract from different platforms.
- **Easy-to-Use**: Intuitive Python package interface for both beginners and experienced developers.
- **Multiple Platforms**: Scrape data from various platforms, including GitHub, Twitter, Instagram, and more.
- **Efficient and Fast**: Designed for efficient and reliable scraping of data from multiple sources.

## How to use it? ✨

1. Install the package using `pip`:

```bash
pip install scrape-up --upgrade
```

2. Import the required module and instantiate an object with the necessary parameters:

```python
# Import the required module
from scrape_up import github

# Instantiate an object with the username
user = github.Users(username="nikhil25803")
```

3. Call the desired method to scrape the required information. For example, to extract the number of followers of a user:

```python
# Call the followers method
followers_count = user.followers()

# Print the output
print(followers_count)
```

Output:

```
83
```

4. Explore all the available methods provided by Scrape Up on different platforms [here](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md).

Happy scrapping! 🕸️

## The goal 🎯

In our project journey, we encountered several challenges, including requesting timeouts and rate limits. To overcome these limitations, we developed a powerful Python tool based on web scraping. Our goal is to provide an alternative to APIs for extracting data from various platforms, including GitHub, Twitter, Instagram, and any other website that contains valuable information. Here's what our project aims to achieve:

With our web-scraping-based Python tool, you can unlock a world of data and overcome the limitations often encountered when relying solely on APIs.

🌟 We value the time and effort you put into contributing, and we look forward to reviewing and merging your contributions. Together, let's make web scraping a powerful and accessible tool for extracting data from various platforms.

✨ Thank you for your contribution!

---

<p align="right">(<a href="#top">Back to top</a>)</p>
