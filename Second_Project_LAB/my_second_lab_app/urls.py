from django.urls import path
from . import views

app_name = "my_second_lab_app"


urlpatterns = [
    path("/date", views.getDate, name="date view"),
    path("/random", views.randomnumber, name="random number")
]