from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['employee_name', 'contract_type', 'start_date', 'end_date', 'status', 'terms']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}),
            'contract_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Type'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'terms': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contract Terms', 'rows': 4}),
        }
