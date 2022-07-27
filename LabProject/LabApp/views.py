from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import datetime
import random

# Create your views here.

today_date = datetime.date.today()

@api_view(['GET'])
def GetTodayDate(request : Request):

    response_data ={
        "today's date": today_date
    }
    return Response(response_data)



@api_view(['POST'])
def random_number(request : Request):
    min_num = request.data["min"]
    max_num = request.data["max"]
    if min_num < 0:
        response_data = { "msg" : "Not Allowed. Please provide a min that is bigger than 0" }
        return Response(response_data)
    
    random_num = random.randint(min_num, max_num)
    response_data = { "random": random_num }

    return Response(response_data)

