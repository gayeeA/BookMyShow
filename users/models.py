from django.db import models

from movies.models import Movie
import users

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)