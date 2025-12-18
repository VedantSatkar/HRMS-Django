from django import forms
from .models import Payroll
from employees.models import Employee


class PayrollForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'employee_select',
            'data-placeholder': 'Select Employee'
        })
    )
    
    class Meta:
        model = Payroll
        fields = ['employee', 'salary', 'bonus', 'deductions', 'month', 'year']
        widgets = {
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary', 'step': '0.01'}),
            'bonus': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bonus', 'step': '0.01'}),
            'deductions': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Deductions', 'step': '0.01'}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
        }
