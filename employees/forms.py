from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    """
    Employee creation form
    """
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'department', 'role', 'email']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'employee_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'EMP001'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@company.com'
            }),
        }
