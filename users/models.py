from django.db import models

from movies.models import Movie

from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_bookings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='users_movie_bookings')
    booked_at = models.DateTimeField(auto_now_add=True)