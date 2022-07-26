from urllib import request, response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import datetime

# Create your views here.




@api_view(['GET'])
def date(request : Request)  -> Response:
   
    return Response({"date": f"Today is {datetime.now().strftime('%Y-%m-%d')} !"})
