from django.db import models

# Create your models here.
class Video(models.Model):
    video = models.FileField()

class TestModel(models.Model):
    text = models.CharField(max_length=100)