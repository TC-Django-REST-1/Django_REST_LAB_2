from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path("date", views.date, name="date"),
    path("random", views.random_number, name="random"),
]