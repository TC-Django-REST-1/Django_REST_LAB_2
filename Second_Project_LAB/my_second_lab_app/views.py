# from django.shortcuts import render
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import datetime
import random
# Create your views here.

@api_view(['GET'])
def getDate(request : Request):
    

    today = datetime.datetime.now()
    today_formated = today.strftime("%Y-%m-%d")

    response_data = {
      "msg": "today date",
      "date": today_formated,
    }

    return Response(response_data)



@api_view(['POST'])
def randomnumber(request : Request):
    

    minumm = request.data['min']
    maximum = request.data['max']

    if minumm < 0 or maximum < 0 :
      
      response_data = {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
      return Response(response_data)

    
    randomNumber = random.randint(minumm, maximum)

    
    response_data = {
      "random" : randomNumber,
    }
    return Response(response_data)


