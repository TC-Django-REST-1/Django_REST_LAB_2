from django.urls import path
from . import views

app_name = "APIEndpoints"
urlpatterns = [
    path('date/', views.CurrentDate, name="date"),
    path('random/', views.randomNumber, name="random")
]
