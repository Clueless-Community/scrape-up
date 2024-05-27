Create an object of the 'Courses' class:

```python
scraper = Courses(topic="topic")
```

| Methods                                | Details                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| `.get_courses()`                       | Returns the courses with title, teached by, skills, rating, review count, img url and link |
| `.fetch_modules(course='Course Name')` | Returns the modules associated with the Coursera.                                          |
