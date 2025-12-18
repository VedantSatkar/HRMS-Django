from django.db import models
from django.utils import timezone


class Report(models.Model):
    REPORT_TYPES = [
        ('attendance', 'Attendance Report'),
        ('payroll', 'Payroll Report'),
        ('performance', 'Performance Report'),
        ('recruitment', 'Recruitment Report'),
    ]
    
    title = models.CharField(max_length=200, default='Report')
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES, default='attendance')
    description = models.TextField(default='')
    report_date = models.DateField(default=timezone.now)
    generated_by = models.CharField(max_length=100, default='Admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.report_date}"

    class Meta:
        verbose_name_plural = "Reports"
