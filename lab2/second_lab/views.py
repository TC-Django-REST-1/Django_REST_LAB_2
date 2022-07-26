from ast import Return
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.
from datetime import datetime
from random  import randint

# Create your views here.

## this function will return sysdate
@api_view(['GET'])
def today_date (request: Request):
    today =  {datetime.now().strftime('%Y-%m-%d')}
    response_date = { "date" : today }
    return Response(response_date)
## this function will return random number between min and max
@api_view(['POST'])
def get_random_num(request: Request):
   min_max_values = {
        "min" : request.data["min"],
        "max" : request.data["max"] 
        }
   if (min_max_values.get("min") < 0): 
     res_data = {
        "msg": "Not Allowed. Please provide a min that is bigger than 0"
        }
     
     return Response(res_data)
   else:
     res_data = { "random": randint(min_max_values.get("min"), min_max_values.get("max")) }
     return Response(res_data)

