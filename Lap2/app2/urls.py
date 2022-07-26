from django.urls import path
from . import views

app_name = "app2"




urlpatterns = [
    path("date/", views.current_day,name="current day"),
    path("random/", views.random_number, name="random number")
]
