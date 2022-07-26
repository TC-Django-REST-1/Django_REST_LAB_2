from django.urls import path
from . import views


app_name = "django_rest"

urlpatterns = [
    path("date/", views.date, name="todayDate"),
    path("random/", views.random, name="random_generation")
] 