from django.urls import path
from . import views

app_name = "secondlab_app"

urlpatterns = [
    path("date/", views.get_date, name="get_date"),
    path("random/", views.random_numbers, name="random_numbers")
]