from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date
from random import randint
# Create your views here.

@api_view(['GET'])
def date_today(request: Request):
    date_today = f"Today is {date.today()} !"
    response_data = {"date":date_today}
    return Response(response_data)

@api_view(['POST'])
def random(request: Request):
    min= int(request.data['min'])
    max= int(request.data['max'])
    if min < 0:
        response_data =  {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
    else:
        response_data =  {"random" : randint(min, max)}
    return Response(response_data)