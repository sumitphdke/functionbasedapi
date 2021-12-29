from django.urls import path
from demo import views
urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('task',views.tasklist,name="getmethod"),
    path('taskcreate',views.taskcreate,name="post"),
    path('tasks/<str:pk>',views.tasksid,name="get id"),
    path('taskupdate/<str:pk>',views.taskupdate,name="put"),
    path('tasktitle/<str:title>',views.taskid,name="title"),
]
