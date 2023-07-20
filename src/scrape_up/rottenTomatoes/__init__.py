from rot_tom import RottenTomatoes

__all__ = ["RottenTomatoes"]


movie_name = "barbie"
rt = RottenTomatoes()
movie_details = rt.movie_details(movie_name)
print(movie_details)
