from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import datetime
from random import randint
# Create your views here.

today_date = datetime.date.today()

@api_view(['GET'])

def current_day(recuest: Request):

     
    response_data ={
        "today's date": today_date
    }
    return Response(response_data)





# post


@api_view(["POST"])
def random_number(request : Request):

   if request.data['min'] > 0:
        response_rnd = {"random": randint(request.data['min'], request.data['max'])}
   else:
        response_rnd =  {"msg": "Not Allowed. Please provide a min that is bigger than 0"}

   return Response(response_rnd) 