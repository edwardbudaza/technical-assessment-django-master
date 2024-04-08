from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CameraViewSet,
    CameraGroupViewSet,
    CameraStatusLogViewSet,
    CreateUserAPIView,
    CameraMostIssuesView,
    OfflineCamerasView,
    HighestIssuesDayView,
)

router = DefaultRouter()
router.register(r"cameras", CameraViewSet)
router.register(r"camera-groups", CameraGroupViewSet)
router.register(r"camera-status-logs", CameraStatusLogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("create-user/", CreateUserAPIView.as_view(), name="create-user"),
    path("metrics/most-issues/", CameraMostIssuesView.as_view(), name="camera-most-issues"),
    path("metrics/offline-cameras/", OfflineCamerasView.as_view(), name="offline-cameras"),
    path("metrics/highest-issues-day/", HighestIssuesDayView.as_view(), name="highest-issues-day"),
]
