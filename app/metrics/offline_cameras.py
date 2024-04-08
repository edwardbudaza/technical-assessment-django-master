from app.models import CameraStatusLog
from django.utils import timezone

def get_offline_cameras(minutes_threshold):
    current_time = timezone.now()
    threshold_time = current_time - timezone.timedelta(minutes=minutes_threshold)
    
    # Query offline status logs with start date within the threshold time
    offline_logs = CameraStatusLog.objects.filter(
        status='OFF',
        start_date__lte=current_time,
        #start_date__gte=threshold_time
    )

    offline_cameras = set()  # Use a set to store unique camera instances
    print("------------offline---------")
    print(offline_logs)
    print("------------offline---------")
    # Extract unique cameras from offline logs
    for log in offline_logs:
        print("------------offline-below---------")
        print(log.camera_id)
        print("------------offline-above---------")
    # Extract unique cameras from offline 

        offline_cameras.add(log.camera)

    return list(offline_cameras)
