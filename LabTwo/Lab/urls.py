from django.urls import path
from . import views
app_name = "Lab"

urlpatterns = [
    path("date/", views.get_date, name="get_date"),
    path("random/", views.random_number, name="random_number")
]