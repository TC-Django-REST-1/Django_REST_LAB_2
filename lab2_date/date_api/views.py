from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from datetime import date
from random import randint


# Create your views here.


@api_view(['GET'])
def today_date(request : Request):

    today = date.today()
    todayDate = today.strftime("%d/%m/%Y")
    
    res = { "date" : f"Today is {todayDate} !" }
    
    return Response(res)


@api_view(['POST'])
def random_num(request : Request):
    data = request.data
    if data["min"] < 0:
        res = {"msg": "Not Allowed. Please provide a min that is bigger than 0"}
        return Response(res)
    else:
        n = randint(data['min'],data['max'])
        res = {"random" : n}
        return Response(res)

