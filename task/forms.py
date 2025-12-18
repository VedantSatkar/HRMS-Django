from django import forms
from .models import Task
from employees.models import Employee


class TaskForm(forms.ModelForm):
    assigned_employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'assigned_employee',
            'data-placeholder': 'Select Employee (only for single assignment)'
        })
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'assigned_employee', 'status', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description', 'rows': 4}),
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'id': 'assignment_type'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
