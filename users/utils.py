# users/utils.py
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count

from movies.models import Booking

def send_ticket_email(user_email, booking_details):
    subject = "Your Movie Ticket Confirmation"
    message = f"Thank you for your booking!\n\nDetails:\n{booking_details}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)

def get_recommendations(user):
    # Get movies the user has booked
    user_movies = Booking.objects.filter(user=user).values_list('movie_id', flat=True)

    # Recommend movies booked by other users who booked similar movies
    recommendations = Booking.objects.exclude(movie_id__in=user_movies) \
                                      .values('movie_id', 'movie_title') \
                                      .annotate(count=Count('movie')) \
                                      .order_by('-count')[:5]

    return recommendations