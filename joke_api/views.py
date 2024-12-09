from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JokeSerializer
from rest_framework import status
from .models import Joke

@api_view(['GET', 'POST'])
def joke_list(request):
    if request.method == 'GET':
        jokes = Joke.objects.all()
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def joke_detail(request, pk):
    try:
        joke = Joke.objects.get(pk=pk)
    except Joke.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JokeSerializer(joke)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = JokeSerializer(joke, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        serializer = JokeSerializer(joke, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        joke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)