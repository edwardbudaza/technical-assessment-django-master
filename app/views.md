# Views Documentation

In this document, we will explore the `views.py` file in detail. This file contains view classes responsible for handling incoming HTTP requests, processing data, and returning appropriate HTTP responses.

## CameraViewSet

- Purpose: Handles CRUD operations for the Camera model.
- Methods:
  - `perform_create`: Overrides the default create method to associate the logged-in user with the created camera.
- Usage:
  - Provides endpoints for creating, retrieving, updating, and deleting Camera objects.

## CameraGroupViewSet

- Purpose: Handles CRUD operations for the CameraGroup model.
- Usage:
  - Provides endpoints for creating, retrieving, updating, and deleting CameraGroup objects.

## CameraStatusLogViewSet

- Purpose: Handles CRUD operations for the CameraStatusLog model.
- Usage:
  - Provides endpoints for creating, retrieving, updating, and deleting CameraStatusLog objects.

## CreateUserAPIView

- Purpose: Provides an endpoint for creating a new user.
- Usage:
  - Used for registering new users in the system.

## CameraMostIssuesView

- Purpose: Provides an endpoint to retrieve the camera with the most issues.
- Usage:
  - Used to fetch the camera with the highest number of issues.

## OfflineCamerasView

- Purpose: Provides an endpoint to retrieve offline cameras.
- Usage:
  - Used to get cameras that have been offline for a specified threshold of time.

## HighestIssuesDayView

- Purpose: Provides an endpoint to retrieve the day with the highest number of issues.
- Usage:
  - Used to determine the day with the most reported issues.
