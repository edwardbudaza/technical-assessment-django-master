from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import permissions

class CameraGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Camera(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    group = models.ForeignKey(
        CameraGroup, on_delete=models.CASCADE, related_name="cameras"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        CameraStatusLog.objects.create(
            camera=self,
            status=CameraStatusLog.WORKING,
            start_date=timezone.now(),
            user=self.user
        )


class CameraStatusLog(models.Model):
    WORKING = "WRK"
    OFFLINE = "OFF"
    INCORRECT_POSITION = "INC"

    StatusChoices = (
        (WORKING, "Working"),
        (OFFLINE, "Offline"),
        (INCORRECT_POSITION, "Incorrect Position"),
    )

    camera = models.ForeignKey(
        Camera, on_delete=models.CASCADE, related_name="status_logs"
    )
    status = models.CharField(max_length=3, choices=StatusChoices)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.camera.name} - {self.get_status_display()}"

    def duration(self):
        """Calculate the duration the camera has been in the current status."""
        end_time = self.end_date if self.end_date else timezone.now()
        if not self.start_date:
            return None
        duration = end_time - self.start_date
        return duration

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user
