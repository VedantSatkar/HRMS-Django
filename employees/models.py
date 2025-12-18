from django.db import models
from django.utils.timezone import now

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True
    )

    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_of_joining = models.DateField(default=now)

    def __str__(self):
        return self.name
