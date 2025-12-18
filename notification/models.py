from django.db import models
from django.utils import timezone
from employees.models import Employee


class Notification(models.Model):
    title = models.CharField(max_length=200, default='Notification')
    message = models.TextField(default='')
    recipient = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    notification_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        recipient_name = self.recipient.name if self.recipient else 'Admin'
        return f"{self.title} - {recipient_name}"

    class Meta:
        verbose_name_plural = "Notifications"
