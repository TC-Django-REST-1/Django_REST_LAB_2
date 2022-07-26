from datetime import datetime
from types import EllipsisType
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import random

# Create your views here.

@api_view(['GET'])
def today_date(request: Request):

    date = "Today is 2022-06-06!"

    return Response(date)


@api_view(['POST'])
def random_num(request: Request):

   
    values = {
        "min" : request.data["min"],
        "max" : request.data["max"]
    }

    if values.get("min") < 0 :

        response_data = {
            "msg": "Not Allowed. Please provide a min that is bigger than 0"
        }
        return Response(response_data)

    else:
        min_num = values.get("min")
        max_num = values.get("max")
        random_value = random.randint(min_num, max_num)


        response_data = {
            "random" : random_value
        }

        return Response(response_data)
    