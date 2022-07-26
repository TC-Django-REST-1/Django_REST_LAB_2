from django.urls import path
from . import views
app_name = 'my_app'

urlpatterns = [
    path('date/', views.get_date, name='todays_date'),
    path('random/', views.add_random, name='random_number'),
]