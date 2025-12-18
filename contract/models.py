from django.db import models
from django.utils import timezone


class Contract(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('terminated', 'Terminated'),
    ]
    
    employee_name = models.CharField(max_length=100, default='N/A')
    contract_type = models.CharField(max_length=100, default='Full-Time')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    terms = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_name} - {self.contract_type}"

    class Meta:
        verbose_name_plural = "Contracts"
