# URLs Documentation

This document describes the URL configuration in the `urls.py` file of the Django application.

## Overview

The `urls.py` file defines the URL patterns for the API endpoints and views of the application. It uses the Django `path` function to map URLs to view functions or classes.

## URL Patterns

- `/`: Root URL pattern that includes the URLs provided by the `DefaultRouter` instance.
- `/create-user/`: URL pattern for creating a new user, linked to the `CreateUserAPIView`.
- `/metrics/most-issues/`: URL pattern for retrieving the camera with the most issues, linked to the `CameraMostIssuesView`.
- `/metrics/offline-cameras/`: URL pattern for retrieving offline cameras, linked to the `OfflineCamerasView`.
- `/metrics/highest-issues-day/`: URL pattern for retrieving the day with the highest number of issues, linked to the `HighestIssuesDayView`.

## ViewSets and Routers

- `DefaultRouter`: Automatically generates URLs for ViewSets, such as `CameraViewSet`, `CameraGroupViewSet`, and `CameraStatusLogViewSet`, and registers them with the appropriate URLs.

## Usage

- The URL patterns defined in this file determine the API endpoints accessible to clients.
- Each URL pattern is associated with a specific view or viewset, providing access to different functionalities of the application.
