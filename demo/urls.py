from django.urls import path
from demo import views
urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('task',views.tasklist,name="getmethod"),
    path('taskcreate',views.taskcreate,name="post"),
]
