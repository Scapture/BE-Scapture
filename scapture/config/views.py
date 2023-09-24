from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

# Create your views here.
class VideoListAPIView(generics.ListAPIView):
    # queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.order_by("-id")
        return queryset

class VideoCreateAPIView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# class GameListAPIView(generics.ListAPIView):
#     serializer_class = VideoSerializer
#     def get_queryset(self):
#         game_id = self.kwargs['game']
#         queryset = Video.objects.filter(game=game_id).order_by(-id)
#         return queryset