from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

# Create your views here.
class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoCreateAPIView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
