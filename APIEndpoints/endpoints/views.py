from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from datetime import date
from random import choice

@api_view(['GET'])
def date(_request: Request) -> Response:
   
    return Response({"date": f"Today is {datetime.now().strftime('%Y-%m-%d')} !"})


@api_view(['POST'])
def random_num(request: Request) -> Response:
    if type(request.data) is dict and sorted(list(request.data)) == ["max", "min"]:
        if all(map(lambda num: type(num) is int, request.data.values())):
            if all(map(lambda num: num > 0, request.data.values())):
                return Response(
                   {"Random": choice(range(request.data["min"], request.data["max"]))}
                )
            else:
                return Response(
                    {
                        "msg",
                        "Not Allowed. Please provide a min and max that is bigger than 0",
                    },
                    status=400,
                )
    return Response({"msg": "Invalid request data"}, status=400)
    
