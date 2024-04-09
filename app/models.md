# Models Documentation

In this document, we will explore the `models.py` file in detail. This file contains the definition of Django models that represent the data structure of the application.

## CameraGroup

- Purpose: Represents a group of cameras.
- Fields:
  - `name`: CharField, max length 100 characters, representing the name of the group.
  - `description`: TextField, optional, representing the description of the group.
- Usage:
  - Used to categorize cameras into different groups.

## Camera

- Purpose: Represents a camera device.
- Fields:
  - `name`: CharField, max length 100 characters, representing the name of the camera.
  - `location`: TextField, representing the location of the camera.
  - `group`: ForeignKey to CameraGroup, specifying the group to which the camera belongs.
  - `user`: ForeignKey to User, representing the user associated with the camera (nullable).
- Methods:
  - `save`: Overrides the save method to create a CameraStatusLog entry when saving the camera.
- Usage:
  - Used to store information about individual cameras.

## CameraStatusLog

- Purpose: Represents the status log of a camera.
- Fields:
  - `WORKING`, `OFFLINE`, `INCORRECT_POSITION`: Choices for the camera status.
  - `camera`: ForeignKey to Camera, specifying the camera associated with the log.
  - `status`: CharField, max length 3 characters, representing the status of the camera.
  - `start_date`: DateTimeField, representing the start date of the status.
  - `end_date`: DateTimeField, representing the end date of the status (nullable).
  - `user`: ForeignKey to User, representing the user associated with the log (nullable).
- Methods:
  - `duration`: Calculates the duration the camera has been in the current status.
- Usage:
  - Used to track the status changes of cameras over time.

## IsOwnerOrReadOnly

- Purpose: Custom permission to allow only owners of an object to edit it.
- Methods:
  - `has_object_permission`: Determines if the user has permission to modify the object.
- Usage:
  - Used to restrict write access to object owners only.
