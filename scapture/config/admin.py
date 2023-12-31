from asyncio import format_helpers
from django.contrib import admin
from .models import Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'video',)

admin.site.register(Video, VideoAdmin)
