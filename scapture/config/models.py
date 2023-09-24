from django.db import models

# Create your models here.
class Video(models.Model):
    game = models.PositiveBigIntegerField(null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)
    video = models.FileField()
