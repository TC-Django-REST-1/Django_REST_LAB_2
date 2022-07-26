from django.urls import path
from . import views

app_name = 'date'

urlpatterns = [
    path('date/', views.today_date, name="today_date"),
    path('random/', views.random_num, name="random_num")
]