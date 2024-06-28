## Chrome Web Store

```python
from scrape_up import chromewebstore.ChromeWebStore
```
### Scraping Details about Chrome extensions

First create a object for class `ChromeWebStore`

```python
store = ChromeWebStore()
```
### Methods Details
| Methods | Details |
|----|----|
| `.search(keywords,filter(optional))` | returns a list of dictionaries containing extension details based on keyword and optional search filter and statues message |
| `.get_details(id,overview(optional))` | returns a dict containing details about given extension id |

### Notes
### **.search()**<br>
`.search()` returns message "success" if scraping is successful. 
`.search()` uses an optional argument `filter` to filter the extension results
```python
filter = {
    'itemTypes': 'EXTENSION' | 'THEME',
    'filterBy': 'featured' | 'establishedPublisher' | 'featured,establishedPublisher',
    'minimalRating':  rating out of 5
}
```
the list of dictionaries returned by `.search()` has the following structure
```python
{
    "title": "Elephantastic Theme",
    "id": "abcdefg1234567890",
    "link": "https://chromewebstore.google.com/webstore/detail/elephantastic-theme/abcdefg1234567890",
    "thumbnail": "https://...",
    "rating": "4.5",
    "no_of_rating": "1000",
    "description": "A delightful theme featuring playful elephant illustrations.",
    "featured": True,
    "verified_publisher": False
}
```

### **.get_details()**
`.get_details()` returns message "success" if scraping is sucessfull. 
`.get_details()` uses optional argument `overview` which if `True` returns the overview or descripton of the extension along with the details.
the dicionary returned by `.get_details()` has following structure
```python
{
    "title": "Video Speed Controller",
    "thumbnail": "https:/...",
    "rating": "4.6",
    "featured": True,
    "verified_publisher": False,
    "tags": ["Extension", "Functionality & UI"],
    "no_of_users": "3,000,000",
    "overview": "Speed up, slow down, advance and rewind HTML5 audio/video with shortcuts",
    "Updated": "May 24, 2024",
    "Offered by": "igrigorik",
    "Size": "72.43KiB",
    "Languages": [""],
    "Developer": "N/A708 Long Bridge Street\nSan Francisco, CA 94158-2512\nUS Email igrigorik@gmail.com",
    "Non-trader": True,
}

```
## Example Usage
`.search()` without `filter`
```python
from scrape_up import chromewebstore.ChromeWebStore
store = ChromeWebStore()
extensions,message=store.search("video downloader")
```
`.search()` with `filter`
```python
from scrape_up import chromewebstore.ChromeWebStore
store = ChromeWebStore()
filter = { 'itemTypes': 'THEME','filterBy': 'featured','minimalRating': 3 }
extensions,message=store.search( "elephant", filter)
```
`.get_details()`
```python
store = ChromeWebStore()
extensions,message=store.get_details("nffaoalbilbmmfgbnbgppjihopabppdk", overview=True)
```