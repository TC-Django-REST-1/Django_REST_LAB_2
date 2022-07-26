from urllib import request, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import datetime
import random as rn 


@api_view(['GET'])
def date(request: Request):
    
    current_date = datetime.date.today()
    response_data = {
        "date": f'Today is {current_date}!'
    }
    return Response(response_data)




@api_view(['POST'])
def add_random(request: Request):
    min = request.data['min']
    max = request.data['max']

    if min > 0:
        response_data = {
        "random": rn.randint(min, max)
    }
        return Response(response_data)
        
    response_data= {
            "message": "Not Allowed. Please provide a min that is bigger than 0"
        }
    return Response(response_data)





