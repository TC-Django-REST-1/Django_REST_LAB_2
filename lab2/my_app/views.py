from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime
from random import randint
# Create your views here.
@api_view(['Get'])
def date(request : Request):
    today_date= {"date": f"Today is {datetime.now().strftime('%Y-%m-%d')} !"}
    return Response(today_date)

@api_view(['POST'])
def random(request : Request):

    min = int(request.data["min"])
    max = int(request.data["max"])

    # rand = choice(range(min, max))
    random = randint(min,max)
    
    if (min<0):    
         return Response({"msg": "Not Allowed. Please provide a min that is bigger than 0"})
    return Response({"generate random number ": random})
