from django.urls import URLPattern, path
from . import views

app_name = 'date'
urlpatterns = [

    path("date/", views.date,name="date"),
]