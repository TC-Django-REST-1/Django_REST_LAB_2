from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import date
from random import randint

@api_view(['GET'])
def get_date(request: Request):
    today = "Today is " + date.today().strftime("%x") + " !"
    res = { "date" : today }
    return Response(res)


@api_view(['POST'])
def get_random(request: Request):

    if(request.data["min"]<0):
        res = {"msg", "Not Allowed. Please provide a min that is bigger than 0"}
        return Response(res)
        
    res = { "random": randint(request.data["min"], request.data["max"]) }
    return Response(res)

