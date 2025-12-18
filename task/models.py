from django.db import models
from django.utils import timezone
from employees.models import Employee


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    ASSIGNMENT_CHOICES = [
        ('single', 'Single Employee'),
        ('team', 'Team'),
        ('admin', 'Admin'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200, default='Task')
    description = models.TextField(default='')
    assigned_to = models.CharField(max_length=20, choices=ASSIGNMENT_CHOICES, default='single')
    assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, help_text="For single assignment")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        assignment = f"- {self.assigned_employee.name}" if self.assigned_employee else f"- {self.assigned_to}"
        return f"{self.title} {assignment}"

    class Meta:
        verbose_name_plural = "Tasks"
