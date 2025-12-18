from django import forms
from .models import Performance
from employees.models import Employee


class PerformanceForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'employee_select',
            'data-placeholder': 'Select Employee'
        })
    )
    
    class Meta:
        model = Performance
        fields = ['employee', 'rating', 'review', 'review_date']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Performance Review', 'rows': 4}),
            'review_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
