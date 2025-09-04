# %%
# Importer les modules nécessaires
from database import SessionLocal
import query_helper

# Créer une session
db = SessionLocal()

# Tester la récupération de films
movies = query_helper.get_movies(db, limit=5, genre="Comedy")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
# Fermer la session
db.close()