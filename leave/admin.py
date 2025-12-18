from django.contrib import admin
from .models import Leave


class LeaveAdmin(admin.ModelAdmin):
    list_display = ['employee', 'start_date', 'end_date', 'status', 'created_at']
    search_fields = ['employee__name']
    list_filter = ['status', 'created_at']
    fields = ['employee', 'start_date', 'end_date', 'reason', 'status']


admin.site.register(Leave, LeaveAdmin)
