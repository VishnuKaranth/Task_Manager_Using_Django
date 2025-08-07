from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'priority', 'status', 'due_date', 'created_at']
    list_filter = ['priority', 'status', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'user')
        }),
        ('Task Details', {
            'fields': ('priority', 'status', 'due_date')
        }),
    )
