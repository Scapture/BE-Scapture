from rest_framework import serializers
from .models import Video, TestModel

class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()  # 새로운 필드 추가

    class Meta:
        model = Video
        fields = '__all__'

    def get_video_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.video.url)
    
class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'