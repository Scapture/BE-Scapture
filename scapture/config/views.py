from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import status

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

class VideoDestroyAPIView(generics.DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # 특정 ID에 해당하는 객체 가져오기
        self.perform_destroy(instance)  # 객체 삭제
        return Response(status=status.HTTP_204_NO_CONTENT)


# class GameListAPIView(generics.ListAPIView):
#     serializer_class = VideoSerializer
#     def get_queryset(self):
#         game_id = self.kwargs['game']
#         queryset = Video.objects.filter(game=game_id).order_by(-id)
#         return queryset