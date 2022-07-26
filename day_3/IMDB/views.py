from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


movies = [
    {"name": "2 guns","rating": "5"},
    {"name": "last vegas", "rating": "3"}, 
]


@api_view(['GET'])
def moive_list(request):
    return Response(movies)


@api_view(['POST'])
def add_movie(request):

    movie_name = request.data["name"]
    movie_rating = request.data["rating"]

    movies.append({"name": movie_name, "rating": movie_rating},)

    response_data = {
            "msg" : "New movie has been added successfully!"
        }

    return Response(response_data)


@api_view(['PUT'])
def update_movie(request, index):

    movie_name = request.data["name"]
    movie_rating = request.data["rating"]

    # movies[int(index)]["name"]= movie_name
    # movies[int(index)]["rating"]= movie_rating

    movies[int(index)] = {"name":movie_name ,"rating": movie_rating}

    response_data = {
            "msg" : "one movie has been updated successfully!"
        }
    return Response(response_data)


@api_view(['DELETE'])
def remove_movie(request, index):

    movies.pop(int(index))
    response_data = {
            "msg" : "one movie has been deleted successfully!"
        }
    return Response(response_data)

