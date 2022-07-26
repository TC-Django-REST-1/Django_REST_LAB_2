from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import random as rn
import datetime

# Create your views here.


@api_view(['GET'])
def date(request: Request):
    # return current date
    current_date = datetime.date.today()
    response_body = {
        "date": f'Today is {current_date}!'
    }
    return Response(response_body)


@api_view(['POST'])
def random(request: Request):
    # return random number between $min and $max
    min = request.data['min']
    max = request.data['max']

    if min < 0:
        #{"msg", "Not Allowed. Please provide a min that is bigger than 0"}
        response_body = {
            "msg": "Not Allowed. Please provide a min that is bigger than 0"
        }
        return Response(response_body)

    response_body = {
        "random": rn.randint(min, max)
    }
    return Response(response_body)
