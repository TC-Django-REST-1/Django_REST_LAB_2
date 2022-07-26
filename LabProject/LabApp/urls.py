from django.urls import path
from . import views

app_name = "LabApp"

urlpatterns = [
    path("date/", views.GetTodayDate),
    # path("random/", views.random)
]
