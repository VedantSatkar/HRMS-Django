from django.db import models
from datetime import datetime
from employees.models import Employee


class Payroll(models.Model):
    """
    Model for managing payroll information
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    month = models.IntegerField(choices=[(i, i) for i in range(1, 13)], default=1)
    year = models.IntegerField(default=datetime.now().year)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        emp_name = self.employee.name if self.employee else 'N/A'
        return f"{emp_name} - {self.month}/{self.year}"

    class Meta:
        verbose_name_plural = "Payrolls"
