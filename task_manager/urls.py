from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('task-list')),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('tasks.api_urls')),
]
