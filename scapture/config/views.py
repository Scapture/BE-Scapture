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

class TestListAPIView(generics.ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer