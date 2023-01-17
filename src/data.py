from src.movies import action_movies, comedy_movies, thriller_movies, horror_movies, romantic_movies
from src.classes import Movie, Genre


action = Genre()
comedy = Genre()
thriller = Genre()
horror = Genre()
romantic = Genre()

for movie in action_movies:
    action.add_to_head(*movie)

for movie in comedy_movies:
    comedy.add_to_head(*movie)

for movie in thriller_movies:
    thriller.add_to_head(*movie)

for movie in horror_movies:
    horror.add_to_head(*movie)

for movie in romantic_movies:
    romantic.add_to_head(*movie)

movie_library = {
    'action': action,
    'comedy': comedy,
    'thriller': thriller,
    'horror': horror,
    'romantic': romantic
}

