from django.db import models

# Create your models here.
class Video(models.Model):
    game = models.PositiveBigIntegerField(null=True, blank=True)
    video = models.FileField()

class TestModel(models.Model):
    text = models.CharField(max_length=100)