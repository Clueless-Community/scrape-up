```py
from scrape_up import dribbble
```

Create an instance of `Dribbble` class.

```python
shots = dribbble.Dribbble()
```

| Methods               | Details                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `.get_shots()`        | Returns the latest shots along with their title, designer, designer URL, like and view count, and link.                        |
| `.search(topic)`      | Returns the latest shots along with their title, designer, designer URL, like and view count, and link for the searched topic. |
| `.get_animation()`    | Returns the latest animation along with their title, designer, designer URL, like and view count, and link.                    |
| `.get_branding()`     | Returns the latest branding along with their title, designer, designer URL, like and view count, and link.                     |
| `.get_illustration()` | Returns the latest illustration along with their title, designer, designer URL, like and view count, and link.                 |
| `.get_mobile()`       | Returns the latest mobile shots along with their title, designer, designer URL, like and view count, and link.                 |
| `.get_webdesign()`    | Returns the latest web-design shots along with their title, designer, designer URL, like and view count, and link.             |

---
