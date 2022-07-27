from django.urls import path
from .views import list_movies, add_movie, update_movie, delete_movie

app_name = 'imdb'
urlpatterns = [
    path('', list_movies, name='list_movies'),
    path('add', add_movie, name='add_movie'),
    path('update/<index>', update_movie, name='update_movie'),
    path('delete/<index>', delete_movie, name='update_movie')
]