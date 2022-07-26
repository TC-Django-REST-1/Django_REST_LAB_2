from django.urls import URLPattern, path
from . import views

app_name = "randomnum"
urlpatterns = [

    path("random/", views.randomnum,name="random"),
    
]