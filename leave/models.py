from django.db import models
from django.utils import timezone
from employees.models import Employee


class Leave(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    reason = models.TextField(default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        emp_name = self.employee.name if self.employee else 'N/A'
        return f"{emp_name} - {self.start_date}"

    class Meta:
        verbose_name_plural = "Leaves"
