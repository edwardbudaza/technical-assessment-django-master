from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from app.views import CreateUserAPIView  # Import CreateUserAPIView from app views

schema_view = get_schema_view(
    openapi.Info(
        title="VisioMetric Technical Test",
        default_version="v1",
        description="Web application designed for surveillance officers to log the status of the surveillance cameras under their responsibility. The application serves a broad user base of officers.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.urls")),  # Include app-specific URLs
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/users/", CreateUserAPIView.as_view(), name="create-user"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]