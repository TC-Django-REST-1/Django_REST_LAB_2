from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date
import random

# Create your views here.

today = date.today()

current_date = [
    {"Date" : today}


]

@api_view(['GET'])
def get_date(request : Request):
    
    response_data = {
        "msg" : "Today is ",
        "date" : current_date
    } 

    return Response(response_data)


@api_view(['POST'])
def random_number(request : Request):
    
    print(request.data)

    response_data = {
        "msg" : "Request has been passed correctly"
    }

    random_num = {
        "min" : request.data["min"],
        "max" : request.data["max"]
    }
    generate_random_number = random.randint(random_num)
    return Response(generate_random_number)