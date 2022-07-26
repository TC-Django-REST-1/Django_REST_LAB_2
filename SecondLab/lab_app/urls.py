from django.urls import path
from . import views

app_name = "lab_app"

urlpatterns = [
    path("date/", views.today_date, name="today date"),
    path("random/", views.random_number, name="random number")
]
