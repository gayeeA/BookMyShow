from django.urls import path
from . import views
from .views import showtimes
urlpatterns=[
    path('',views.movie_list,name='movie_list'),
    path('showtimes/', showtimes, name='showtimes'),
    path('<int:movie_id>/theaters',views.theater_list,name='theater_list'),
    path('theater/<int:theater_id>/seats/book/',views.book_seats,name='book_seats'),
]