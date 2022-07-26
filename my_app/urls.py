from django.urls import path
from . import views

urlpatterns = [
    path('date/', views.get_date, name="date"),
    path('random/', views.generate_num, name="random")
]