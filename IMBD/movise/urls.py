
from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('get_date/', views.today_date, name='get_date'),
    path('get_random/', views.get_random, name='get_random'),
]