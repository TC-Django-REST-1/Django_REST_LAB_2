from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    #get
    path("date/", views.date, name="date"),
    #post
    path("random/", views.random, name="random")
]
