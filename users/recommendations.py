from django.db.models import Count
from users.models import Booking

def get_recommendations(user):
    """
    Generate movie recommendations for a given user based on other users' bookings.
    """
    # Get movie IDs the user has already booked
    user_movies = Booking.objects.filter(user=user).values_list('movie_id', flat=True)

    # Recommend movies booked by other users who booked similar movies
    recommendations = (
        Booking.objects.exclude(movie_id__in=user_movies)
        .values('movie_id', 'movie__title')  # Use movie__title if "title" is the field name in the Movie model
        .annotate(count=Count('movie'))
        .order_by('-count')[:5]  # Limit to top 5 recommendations
    )

    return recommendations
