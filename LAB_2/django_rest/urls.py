from django.urls import path
from . import views


app_name = "django_rest"

urlpatterns = [
    path("date/", views.today_date, name="todayDate"),
    path("random/", views.random_num, name="random_generation")
]