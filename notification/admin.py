from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'recipient', 'is_read', 'notification_date']
    search_fields = ['recipient__name', 'title']
    list_filter = ['is_read', 'notification_date']
    fields = ['title', 'message', 'recipient', 'is_read', 'notification_date']


admin.site.register(Notification, NotificationAdmin)
