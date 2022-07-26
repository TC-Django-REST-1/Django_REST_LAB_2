from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import choice
import  random as rna 
from urllib import request, response



@api_view(['POST'])
def randomnum(request: Request):
    min = request.data['min']
    max = request.data['max']

    if min > 0:
        response_data = {
        "random": rna.randint(min, max)
    }
        return Response(response_data)

    response_data= {
            "message": "Not Allowed. Please provide a min that is bigger than 0"
        }
    return Response(response_data)