from itertools import product
from django.shortcuts import render
import re
from django.shortcuts import get_object_or_404
from logging import raiseExceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from musiclibrary import serializers
from rest_framework import status



@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer= SongSerializer(songs, many=True)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response(serializer.errors, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
