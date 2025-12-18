from django.db import models
from django.utils import timezone
from employees.models import Employee


class Performance(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Below Average'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    review = models.TextField(default='')
    review_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        emp_name = self.employee.name if self.employee else 'N/A'
        return f"{emp_name} - Rating: {self.rating}"

    class Meta:
        verbose_name_plural = "Performances"
