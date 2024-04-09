# Metrics Module Documentation

This document provides detailed explanations of the functions within the "metrics" module, which consists of several Python files aimed at providing analytics metrics based on camera status logs.

## Overview

The "metrics" module contains modularized Python files that perform specific analytics tasks on camera status logs stored in the database. These tasks include determining the day with the highest number of issues, identifying the camera with the most issues, and retrieving offline cameras within a specified time threshold.

## Benefits of Modular Code

Modular code, such as that found in the "metrics" module, offers several advantages:

- **Reusability**: Each function serves a specific purpose and can be easily reused in different parts of the application or even in other projects.
- **Scalability**: As the application grows, new metrics or analytics functions can be added without impacting existing code, promoting scalability and maintainability.
- **Organization**: Modular code promotes better organization by separating concerns and keeping related functionalities grouped together in separate files.

## Architecture

The choice of architecture for the "metrics" module emphasizes maintainability, flexibility, and scalability:

- **Separation of Concerns**: Each Python file within the "metrics" module focuses on a specific analytics task, such as identifying the camera with the most issues or retrieving offline cameras. This separation of concerns ensures that each file is responsible for a single, well-defined functionality.
- **Modularity**: The modular design allows developers to work on different analytics tasks independently, facilitating collaboration and code management.
- **Reusable Components**: Functions within each file are designed to be reusable, enabling them to be easily integrated into other parts of the application or used in future projects.

## Functionality

### highest_issues_day.py

This file contains a function `get_highest_issues_day()` that determines the day with the highest number of issues recorded in the camera status logs. It performs the following steps:

1. Annotates the camera status logs with the day of the issue.
2. Counts the number of issues for each day.
3. Orders the results by the issue count in descending order.
4. Returns the date of the day with the highest number of issues.

### most_issues.py

The `get_camera_with_most_issues()` function in this file identifies the camera with the most recorded issues. It achieves this by:

1. Grouping camera status logs by camera ID.
2. Counting the number of issues for each camera.
3. Ordering the results by the issue count in descending order.
4. Returning the ID of the camera with the most issues.

### offline_cameras.py

This file contains the `get_offline_cameras(minutes_threshold)` function, which retrieves the cameras that have been offline for a specified time threshold. It performs the following steps:

1. Calculates the threshold time based on the current time and the specified threshold in minutes.
2. Queries the camera status logs for logs with an offline status and a start date within the threshold time.
3. Extracts unique offline cameras from the logs.
4. Returns a list of offline camera instances.
