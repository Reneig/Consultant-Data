from film_apii import MovieClient, MovieConfig
# %%
# Initialisation du client avec l'URL de l'API
config = MovieConfig(movie_base_url="https://consultant-data3.onrender.com")
client = MovieClient(config=config)

# 1. Health check
print("Health check:")
print(client.health_check())

# 2. Récupérer un film par ID
print("\nMovie ID 1:")
movie = client.get_movie(1)
print(movie)
print(type(movie))

# 3. Lister les films (premiers 5)
print("\nList of movies:")
movies = client.list_movies(limit=5)
print(type(movies))
for m in movies:
    print(m)
    print(type(m))

# 4. Récupérer un rating spécifique
print("\nRating for user 1 and movie 1:")
rating = client.get_rating(user_id=1, movie_id=1)
print(rating)
print(type(rating))

# 5. Lien du film
print("\nLink for movie ID 1:")
link = client.get_link(movie_id=1)
print(link)
print(type(link))

# 6. Analytics
print("\nAnalytics:")
analytics = client.get_analytics()
print(analytics)
print(type(analytics))

# %%
