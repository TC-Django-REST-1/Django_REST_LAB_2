from random import randint
from unicodedata import name
from urllib.request import Request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date

# Create your views here.
today_date =  "Today is " + str(date.today()) + "!" 

@api_view(['GET'])
def get_date(request: Request):
    response_data = {
        'date': today_date
    }
    return Response(response_data)


@api_view(['POST'])
def add_random(request: Request):
    #print(request.data)

    min = int(request.data["min"])
    max = int(request.data["max"])

    response_data = {
        "random:": randint(min, max)
    }
    if min < 0 : response_data = {'msg': 'Not Allowed. Please provide a min that is bigger than 0'}
    return Response(response_data)

