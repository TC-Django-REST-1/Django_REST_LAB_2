from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


@api_view(["GET"])
def date(_request: Request) -> Response:
    """Return current date

    Args:
        _request (Request): The request

    Returns:
        Response: Current date
    """
    return Response({"date": f"Today is {datetime.now().strftime('%Y-%m-%d')} !"})
