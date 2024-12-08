from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import JokeSerializer
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404_NOT_FOUND)