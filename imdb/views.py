from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


movies_list = [
    {"name": "Spider Man", "rating": 4},
    {"name": "Top Gun", "rating": 5}
]

data = {
    'msg': 'list of movies',
    'movies': movies_list
}

@api_view(['GET'])
def list_movies(request: Request):
    return Response(data)


@api_view(['POST'])
def add_movie(request: Request):
    new_movie = {
        'name': 'Lost',
        'rating': 10
    }

    movies_list.append(new_movie)

    return Response(data)


@api_view(['PUT'])
def update_movie(request: Request, index):
    movie = {
        'name': request.data['name'],
        'rating': request.data['rating']
    }

    movies_list[int(index)] = movie

    return Response(data)


@api_view(['DELETE'])
def delete_movie(request: Request, index):
    del movies_list[int(index)]
    return Response(data)