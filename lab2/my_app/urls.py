from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('date/',views.date, name='today_date'),
    path('random/',views.random, name='random')
    ]