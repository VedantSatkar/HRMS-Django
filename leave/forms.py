from django import forms
from .models import Leave
from employees.models import Employee


class LeaveForm(forms.ModelForm):
    """
    Form for leave management
    """
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'employee_select',
            'data-placeholder': 'Select Employee'
        })
    )
    
    class Meta:
        model = Leave
        fields = ['employee', 'start_date', 'end_date', 'reason', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Reason for leave', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
