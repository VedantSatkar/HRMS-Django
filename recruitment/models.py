from django.db import models
from django.utils import timezone


class Recruitment(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
        ('hired', 'Hired'),
    ]
    
    position = models.CharField(max_length=100, default='N/A')
    candidate_name = models.CharField(max_length=100, default='N/A')
    email = models.EmailField(default='example@email.com')
    phone = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    applied_date = models.DateField(default=timezone.now)
    hired_date = models.DateField(null=True, blank=True)
    employee_created = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.candidate_name} - {self.position}"

    class Meta:
        verbose_name_plural = "Recruitments"
