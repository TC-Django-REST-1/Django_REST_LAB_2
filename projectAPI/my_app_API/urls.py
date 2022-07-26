from django.urls import path
from . import views

app_name = "my_app_API"

urlpatterns = [
    path("date/", views.date, name="date"),
    path("random/", views.add_random, name="add_random")
    
]