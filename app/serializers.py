from rest_framework import serializers
from .models import Camera, CameraGroup, CameraStatusLog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class CameraGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraGroup
        fields = ["id", "name", "description"]

class CameraSerializer(serializers.ModelSerializer):
    group = CameraGroupSerializer(read_only=True)

    class Meta:
        model = Camera
        fields = ["id", "name", "location", "group"]
    
    # Override create method to associate group with camera if provided in request data
    def create(self, validated_data):
        group_data = validated_data.pop('group', None)
        if group_data:
            group_instance, _ = CameraGroup.objects.get_or_create(**group_data)
            validated_data['group'] = group_instance
        return super().create(validated_data)

class CameraStatusLogSerializer(serializers.ModelSerializer):
    camera_id = serializers.PrimaryKeyRelatedField(queryset=Camera.objects.all(), source='camera')
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CameraStatusLog
        fields = ["id", "camera_id", "status", "start_date", "end_date", "user"]

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user  # Set user to the logged-in user
        camera_id = validated_data.pop('camera_id', None)
        if camera_id:
            camera_instance = Camera.objects.get(pk=camera_id)
            validated_data['camera'] = camera_instance
        return super().create(validated_data)
    
    def get_user(self, obj):
        return UserSerializer(obj.user).data
