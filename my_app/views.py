from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

import datetime
import random

@api_view(['GET'])
def date(request: Request):
    today = 'today is ' + str(datetime.date.today()) +"!"
    response_date = {
        "date": today
    }
    return Response(response_date)

@api_view(['POST'])
def random_number(request: Request):
    if request.data["min"] > 0:
        response_random= {"random": random.randrange(request.data['min'], request.data['max'], 1)}
    else:
        response_random = {"msg": "Not Allowed. Please provide a min that is bigger than 0"}
    return Response(response_random)
