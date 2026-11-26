# 🕷️ Scrape Up

Scrape Up is a Python package for extracting publicly available data from websites such as GitHub, Instagram, Twitter, and many others. It provides a straightforward, programmatic alternative when a platform API is unavailable or too limited for your use case.

<p align="center">
  <a href="https://pypi.org/project/scrape-up/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/scrape-up?style=for-the-badge"></a>
  <a href="https://pepy.tech/project/scrape-up"><img alt="Total PyPI downloads" src="https://img.shields.io/pepy/dt/scrape-up?style=for-the-badge"></a>
  <a href="https://github.com/Clueless-Community/scrape-up/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Clueless-Community/scrape-up?style=for-the-badge"></a>
  <a href="https://github.com/Clueless-Community/scrape-up/forks"><img alt="GitHub forks" src="https://img.shields.io/github/forks/Clueless-Community/scrape-up?style=for-the-badge"></a>
  <a href="https://github.com/Clueless-Community/scrape-up/issues"><img alt="GitHub open issues" src="https://img.shields.io/github/issues/Clueless-Community/scrape-up?style=for-the-badge"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-yellow.svg?style=for-the-badge"></a>
</p>

## Why Scrape Up?

- **Flexible:** Choose the platform and data you want to extract.
- **Approachable:** Use a small Python interface suitable for scripts and applications.
- **Broad coverage:** Work with modules for GitHub, social platforms, news sites, marketplaces, and more.
- **API alternative:** Retrieve public information without depending entirely on a platform API.

## Installation

Install or upgrade the package from [PyPI](https://pypi.org/project/scrape-up/):

```bash
python -m pip install --upgrade scrape-up
```

## Quick start

Import a platform module, create the relevant scraper, and call the method for the data you need:

```python
from scrape_up import github

user = github.Users(username="nikhil25803")
followers_count = user.followers()

print(followers_count)
```

Because websites can change their markup or access rules, scraper behavior may change even when your code does not. Use each platform responsibly and follow its applicable terms and policies.

## Documentation

See the [platform and method reference](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md) for the available scrapers and their interfaces.

## Contributing

Contributions are welcome. Read the [contribution guide](https://github.com/Clueless-Community/scrape-up/blob/main/CONTRIBUTING.md), then check the [open issues](https://github.com/Clueless-Community/scrape-up/issues) or propose an improvement.

## License

Scrape Up is distributed under the [MIT License](LICENSE).
