from django.contrib import admin
from .models import Camera, CameraGroup, CameraStatusLog

@admin.register(CameraGroup)
class CameraGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'group']
    list_filter = ['group']
    search_fields = ['name', 'location']

@admin.register(CameraStatusLog)
class CameraStatusLogAdmin(admin.ModelAdmin):
    list_display = ['camera', 'status', 'start_date', 'end_date', 'user']
    list_filter = ['status', 'user']
    search_fields = ['camera__name']
