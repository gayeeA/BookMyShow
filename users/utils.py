# users/utils.py
from collections import Counter

from movies.models import Booking, Movie

def recommend_movies(user):
    bookings = Booking.objects.filter(user=user)
    movie_counts = Counter(booking.movie.title for booking in bookings)
    most_common = movie_counts.most_common(1)
    if most_common:
        return Movie.objects.exclude(title=most_common[0][0])  # Suggest different movies
    return Movie.objects.all()  # Default to all movies if no history
