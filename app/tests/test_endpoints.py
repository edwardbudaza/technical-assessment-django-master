from django.contrib.auth.models import User
from django.urls import reverse
from django_dynamic_fixture import G
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from app.models import Camera

class ViewsetAuthenticationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.authorize()  # Store the authorized user

    def tearDown(self):
        self.client.logout()

    def authorize(self, user=None):
        user = user or G(User)
        token, _ = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        return user

    def deauthorize(self):
        self.client.credentials()

    def test_camera_viewset_authentication_required(self):
        unauthorized_client = APIClient()
        url = reverse("camera-list")

        # Send a POST request to check authentication requirement
        response = unauthorized_client.post(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_camera_group_viewset_authentication_required(self):
        unauthorized_client = APIClient()
        url = reverse("cameragroup-list")

        # Send a PUT request to check authentication requirement
        response = unauthorized_client.put(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_camera_status_log_viewset_authentication_required(self):
        unauthorized_client = APIClient()
        url = reverse("camerastatuslog-list")

        # Send a DELETE request to check authentication requirement
        response = unauthorized_client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_camera_viewset_authentication(self):
        url = reverse("camera-list")

        # Send a GET request to check authentication
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_camera_list(self):
        G(Camera, name="Test", user=self.user)  # Associate the user with the created camera
        url = reverse("camera-list")

        # Send a GET request to check camera list
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test")
