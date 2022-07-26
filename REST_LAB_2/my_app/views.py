from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import datetime

today = datetime.today().strftime("Today is %Y-%m-%d !")


@api_view(['GET'])
def date(request: Request):

    response_data = {
        "date": today
    }

    return Response(response_data)


@api_view(['POST'])
def random(request: Request):
    try:
        min = request.data["min"]
        max = request.data["max"]

        if int(min) >= 0:
            if int(min) <= int(max):
                response_data = {
                    "random": getRandomNum(min, max)
                }
            else:
               response_data = {
                   "msg": "Not Allowed.  max must be bigger than min"
               }
        else:
            response_data = {
                "msg": "Not Allowed. Please provide a min that is bigger than 0"
            }
    except(Exception):
        response_data = {
            "Error": f"min and max expect to be integer but you but you gave {type(min)=} {type(max)=} "
        }

    return Response(response_data)


def getRandomNum(min: int, max: int):
    import random

    return random.randint(min, max)
