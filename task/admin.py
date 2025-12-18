from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'status', 'due_date']
    search_fields = ['title', 'assigned_to']
    list_filter = ['status', 'due_date']
    fields = ['title', 'description', 'assigned_to', 'status', 'due_date']


admin.site.register(Task, TaskAdmin)
