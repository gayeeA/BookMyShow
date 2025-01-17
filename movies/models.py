from django.db import models
from django.contrib.auth.models import User 



class Movie(models.Model):
    name= models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image= models.ImageField(upload_to="movies/" ,blank=True, null=True, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFusGlkNinqf4y11Ibzvi2o6bWMXVM5dHXiA&s")
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    cast= models.TextField()
    description= models.TextField(blank=True,null=True) # optional
    show_timings = models.JSONField(default=list) 
    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='theaters')
    time= models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.movie.name} at {self.time}'

class Seat(models.Model):
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.seat_number} in {self.theater.name}'

class Booking(models.Model):
    seat=models.OneToOneField(Seat,on_delete=models.CASCADE)
    theater=models.ForeignKey(Theater,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies_bookings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_bookings')
    booked_at = models.DateTimeField(auto_now_add=True)
    # booking_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Booking by{self.user.username} for {self.seat.seat_number} at {self.theater.name}'

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    date = models.DateField()
    time = models.TimeField()