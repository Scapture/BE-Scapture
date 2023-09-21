from django.shortcuts import render
from rest_framework import generics
from .models import Video, TestModel
from .serializers import VideoSerializer, TestModelSerializer

# Create your views here.
class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoCreateAPIView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class GameListAPIView(generics.ListAPIView):
    serializer_class = VideoSerializer
    def get_queryset(self):
        game_id = self.kwargs['game']
        queryset = Video.objects.filter(game=game_id)
        return queryset