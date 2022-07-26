from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import datetime
from random import choice


@api_view(['GET'])
def date(request):

    date_now = datetime.datetime.now()

    date = "Today is " + date_now.strftime("%Y-%m-%d") + "!"

    response_data = {
        "date" : date ,
    }
    return Response(response_data)



@api_view(['POST'])
def random(request : Request):

    min_num = int(request.data["min"])
    max_num = int(request.data["max"])

    if min_num < 0 :
        response_data = {
            "msg" : "Not Allowed. Please provide a min that is bigger than 0"
        }
    else:
        rand = choice(range(min_num, max_num))

        response_data = {
            "random" : rand,
        }
    return Response(response_data)