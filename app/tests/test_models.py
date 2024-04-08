from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django_dynamic_fixture import G
from ..models import Camera, CameraStatusLog, CameraGroup  # Import CameraGroup model
from django.contrib.auth.models import User

class CameraModelTest(TestCase):
    def test_initial_status_log_creation(self):
        camera = G(Camera)

        status_logs = CameraStatusLog.objects.filter(camera=camera)

        self.assertEqual(status_logs.count(), 1)
        self.assertEqual(status_logs.first().status, CameraStatusLog.WORKING)

    def test_camera_group_representation(self):
        camera_group = CameraGroup.objects.create(name="Test Group", description="Test Description")
        self.assertEqual(str(camera_group), "Test Group")  # Test string representation

class CameraStatusLogModelTest(TestCase):
    def test_duration_with_end_date(self):
        start_date = timezone.now() - timedelta(days=2)
        end_date = timezone.now() - timedelta(days=1)
        camera_log = G(CameraStatusLog, start_date=start_date, end_date=end_date)

        expected_duration = end_date - start_date

        self.assertEqual(camera_log.duration(), expected_duration)

    # method to verify status log creation
    def test_status_log_creation(self):
        camera = G(Camera)
        user = G(User)  
        status_log = CameraStatusLog.objects.create(
            camera=camera,
            status=CameraStatusLog.WORKING,
            start_date=timezone.now(),
            user=user
        )
        self.assertEqual(CameraStatusLog.objects.count(), 2)
        self.assertEqual(status_log.status, CameraStatusLog.WORKING)
        self.assertEqual(status_log.user, user)