from asyncio import format_helpers
from django.contrib import admin
from .models import Video, TestModel

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'video',)

class TestModelAdmin(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(Video, VideoAdmin)
admin.site.register(TestModel, TestModelAdmin)
