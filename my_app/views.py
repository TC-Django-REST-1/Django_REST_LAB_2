from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime
from random import choice

@api_view(['GET'])
def get_date(request: Request):
  return Response({"date" : f"Today is {datetime.now().strftime('%Y-%m-%d')} !"})

@api_view(['POST'])
def generate_num(request: Request):
  try:
    min, max = int(request.data["min"]), int(request.data["max"])
    if min < 0:
      return Response({"msg" : "Not Allowed. Please provide a min that is bigger than 0"}, status=400)
    elif min < max:
      return Response({"random" : choice(range(min, max))})
  except Exception as e:
    print(e)
    return Response({"msg" : "Invalid request!"}, status=400)