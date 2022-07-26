from django.shortcuts import render
from urllib import request, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import datetime
import  random as rn 
# Create your views here.

#date
@api_view(['GET'])
def date(request: Request):
    # return current date
    current_date = datetime.date.today()
    res = {
        "date": f'Today is {current_date}!'
    }
    return Response(res)

#random_num

@api_view(['POST'])
def random_num(request: Request):
    min = request.data['min']
    max = request.data['max']

    if min > 0:
        response_data = {
        "random": rn.randint(min, max)
    }
        return Response(response_data)
        
    response_data= {
            "message": "Not Allowed. Please provide a min that is bigger than 0"
        }
    return Response(response_data)


