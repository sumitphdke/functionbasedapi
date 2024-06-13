**Django REST API for Task Management**

This project provides a simple RESTful API for managing tasks. It includes endpoints for listing, creating, updating, and retrieving tasks by their ID or title. Additionally, the project features an endpoint for exporting task data to a CSV file upon creation.

**Features**
List Tasks: Retrieve a list of all tasks.
Task Details: Retrieve detailed information about a specific task by its ID.
Create Task: Create new tasks and automatically export the task list to a CSV file.
Update Task: Update details of an existing task by its ID.
Retrieve by Title: Retrieve task details based on the task title.
Endpoints

**The API provides the following endpoints:**
GET /task-list/ : List all tasks.
GET /task-detail/<str:pk>/ : Get details of a specific task by its ID.
POST /task-create/ : Create a new task.
POST /task-update/<str:pk>/ : Update an existing task by its ID.
GET /task-title/<str:title>/ : Get details of a task by its title.
