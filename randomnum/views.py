from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import choice

@api_view(["POST"])
def random_num(request: Request) -> Response:
    """ Returns random number between two nmumbers

    Args:
        request (Request): The request

    Returns:
        Response: Random number between two nmumbers
    """    
    if type(request.data) is dict and sorted(list(request.data)) == ["max", "min"]:
        if all(map(lambda num: type(num) is int, request.data.values())):
            if all(map(lambda num: num > 0, request.data.values())):
                return Response({"Random": choice(range(request.data["min"], request.data["max"]))})
            else:
                return Response({"msg", "Not Allowed. Please provide a min and max that is bigger than 0"}, status=400)
    return Response({"msg": "Invalid request data"}, status=400)