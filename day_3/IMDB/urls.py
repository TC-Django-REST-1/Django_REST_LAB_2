
from django.urls import path
from . import views

app_name = 'IMDB'


urlpatterns = [
    path("list/", views.moive_list, name=""),
    path("add/", views.add_movie, name=""),
    path("update/<index>", views.update_movie, name=""),
    path("delete/<index>", views.remove_movie, name=""),
    
]
