from django.urls import path
from . import api_views

urlpatterns = [
    path('tasks/', api_views.TaskListCreateAPIView.as_view(), name='api-task-list'),
    path('tasks/<int:pk>/', api_views.TaskRetrieveUpdateDestroyAPIView.as_view(), name='api-task-detail'),
    path('tasks/stats/', api_views.task_stats, name='api-task-stats'),
]
