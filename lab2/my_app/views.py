from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from datetime import date
from random  import randint

# Create your views here.


@api_view(["GET"])
def today_date(request : Request):
    now = datetime.now()
    today_date = now.strftime("%Y-%m-%d")

    response_date = {
        "date":"Today is " + today_date + " !"
    }

    return Response(response_date)



@api_view(["POST"])
def random_number(request : Request):
   
   if request.data['min'] > 0:
        response_rnd = {"random": randint(request.data['min'], request.data['max'])}
   else:
        response_rnd =  {"msg": "Not Allowed. Please provide a min that is biggler than 0"}

   return Response(response_rnd)