from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .metrics import most_issues, offline_cameras, highest_issues_day
from .models import Camera, CameraGroup, CameraStatusLog,IsOwnerOrReadOnly
from .serializers import (
    CameraSerializer,
    CameraGroupSerializer,
    CameraStatusLogSerializer,
    UserSerializer,
)

class CameraViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Camera model.
    """
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Add IsOwnerOrReadOnly permission

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Associate the logged-in user with the created camera

class CameraGroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CameraGroup model.
    """
    queryset = CameraGroup.objects.all()
    serializer_class = CameraGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CameraStatusLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CameraStatusLog model.
    """
    queryset = CameraStatusLog.objects.all()
    serializer_class = CameraStatusLogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateUserAPIView(APIView):
    """
    API View for creating a new user.
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CameraMostIssuesView(APIView):
    """
    API View to get the camera with the most issues.
    """

    def get(self, request):
        camera_id = most_issues.get_camera_with_most_issues()
        camera = Camera.objects.get(pk=camera_id)
        serializer = CameraSerializer(camera)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OfflineCamerasView(APIView):
    """
    API View to get offline cameras.
    """
    def get(self, request):
        # Get the threshold from query parameters, default to 30 minutes if not provided
        minutes_threshold = request.query_params.get('threshold', 30)

        # Call the updated function to get the offline cameras
        offline_cameras_x_minutes = offline_cameras.get_offline_cameras(int(minutes_threshold))
        # Serialize the offline cameras if needed
        offline_cameras_serialized = CameraSerializer(offline_cameras_x_minutes, many=True).data

        # Return the response with offline cameras data
        return Response({'offline_cameras': offline_cameras_serialized}, status=status.HTTP_200_OK)

class HighestIssuesDayView(APIView):
    """
    API View to get the day with the highest number of issues.
    """
    def get(self, request):
        highest_issues_day_result = highest_issues_day.get_highest_issues_day()
        return Response({'highest_issues_day': highest_issues_day_result}, status=status.HTTP_200_OK)
