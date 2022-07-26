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



# @api_view(['POST'])
# def random(request : Request):
#     response_data = {
        
#     }
#     return Response(response_data)
