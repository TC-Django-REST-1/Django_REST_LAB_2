from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpResponse

import datetime
import random

# Create your views here.
def hello(request):
    return HttpResponse("Hello There")


@api_view(['GET'])
def date(request: Request):

    # date = "Today is 2022-07-26!"
    current_date = datetime.date.today()
    response_body = {
        "date": f'Today is {current_date}!'
    }


    return Response(response_body)


@api_view(['POST'])
def random(request : Request):

    min = int(request.data["min"])
    max = int(request.data["max"])

    if min < 0 :
        response_body = {
            "msg" : "Not Allowed. Please provide a min that is bigger than 0"
        }
    else:
        
        rand = random(range(min, max))
        

        response_body = {
            "random" : rand,
        }
    return Response(response_body) 