from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date
import random



# get request
@api_view(['GET'])
def get_date(request : Request):
    
    today_date = "Today is {0}!".format(date.today())

    response_data = { 
        "date" : today_date
        }

    return Response(response_data)

# post request
@api_view(['POST'])
def random_numbers(request : Request):

    numbers = {
        "min" : request.data["min"],
        "max" : request.data["max"]
    }
    if numbers["min"] < 0:
        
        response_data = { 
            "msg" : "Not Allowed. Please provide a min that is bigger than 0"
            }
    else:
         response_data = { 
            "random" : random.randint(numbers["min"], numbers["max"])
            }

    return Response(response_data)

