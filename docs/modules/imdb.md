Create an instance of the `IMDB` class.

```python
scraper = IMDB()
```

| Methods                       | Details                                                        |
| ----------------------------- | -------------------------------------------------------------- |
| `.top_rated()`                | Returns the top-rated movies listed on IMDB.                   |
| `.scrape_genre_movies(genre)` | Returns the list of movies related to the genre you mentioned. |
| `.top_rated_shows()`          | Returns the top-rated shows listed on IMDB.                    |

Create an instance of `Movie` class.

```python
movie = Movie(movie_name)
```

| Methods          | Details                                                  |
| ---------------- | -------------------------------------------------------- |
| `.rating()`      | Returns the IMDB rating of the movie                     |
| `.description()` | Returns the description, cast and director of the movie  |
| `.more_movies()` | Returns similar movies recommended by IMDB               |
| `.box_office()`  | Returns budget, gross worldwide collections of the movie |

Create an instance of `Actor` class.

```python
actor = Actor(actor_name)
```

| Methods             | Details                                                 |
| ------------------- | ------------------------------------------------------- |
| `.popular_movies()` | Returns the popular movies in which the actor has acted |
| `.all_movies()`     | Returns all movies acted in and upcoming movies         |
| `.awards()`         | Returns the number of awards and nominations            |

Create an instance of `Celeb` class.

```python
celeb = Celeb()
```

| Methods         | Details                                            |
| --------------- | -------------------------------------------------- |
| `.top_celebs()` | Returns the name, roles, famous movie of the celeb |

Create an instance of `IndianMovies` class.

```python
indianmovies = IndianMovies()
```

| Methods                | Details                                       |
| ---------------------- | --------------------------------------------- |
| `.top_indian_movies()` | Returns the current list of top Indian movies |

Create an instance of `BoxOffice` class.

```python
boxoffice = BoxOffice()
```

| Methods         | Details                                                                       |
| --------------- | ----------------------------------------------------------------------------- |
| `.top_movies()` | Returns the top box office movies, weekend and total gross and weeks released |

---

<p align="right">(<a href="#top">Back to top</a>)</p>
