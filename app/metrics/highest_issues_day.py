from app.models import CameraStatusLog
from django.db.models import Count
from django.db.models.functions import TruncDate

def get_highest_issues_day():
    highest_issues_day = CameraStatusLog.objects.annotate(day=TruncDate('start_date')).values('day').annotate(issue_count=Count('id')).order_by('-issue_count').first()
    if highest_issues_day:
        return highest_issues_day['day']
    else:
        return None
