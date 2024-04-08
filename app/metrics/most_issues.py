from app.models import CameraStatusLog
from django.db.models import Count

def get_camera_with_most_issues():
    camera_issues = CameraStatusLog.objects.values('camera_id').annotate(issue_count=Count('id')).order_by('-issue_count')
    if camera_issues:
        most_issues_camera_id = camera_issues[0]['camera_id']
        return most_issues_camera_id
    else:
        return None
