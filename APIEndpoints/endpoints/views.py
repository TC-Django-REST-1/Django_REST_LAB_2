from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date
from random import randint
@api_view(['GET'])
def CurrentDate(request:Request):
    currentDate= "Today is " , str(date.today()) , " !"
    res= {'date':currentDate}
    return Response(res)


@api_view(['POST'])
def randomNumber(request : Request):
    min= int(request.data['min'])
    max= int(request.data['max'])
    
    res = {'random': randint(min, max)}
    if min<0 : res=  {"msg": "Not Allowed. Please provide a min that is bigger than 0"}

    return Response(res)
    