from django.urls import URLPattern
from django.urls import path
from . import views


app_name="second_lab"

urlpatterns = [
path("sysdate/", views.today_date, name="path"),
path("random/", views.get_random_num, name="random_num")
]
