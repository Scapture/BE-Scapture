from django.db import models

# def generate_video_filename(instance, filename):
#     # filename에서 확장자 추출
#     extension = filename.split('.')[-1]
    
#     # 동영상 파일 이름 생성 (예: video1.mov, video2.mov, ...)
#     new_filename = f'video{instance.id}.{extension}'
    
#     # 저장 경로 설정 (S3 또는 다른 스토리지에 따라 설정이 달라질 수 있음)
#     return f'videos/{new_filename}'

# Create your models here.
class Video(models.Model):
    game = models.PositiveBigIntegerField(null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)
    video = models.FileField(upload_to='videos/')
