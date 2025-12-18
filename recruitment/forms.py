from django import forms
from .models import Recruitment


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ['position', 'candidate_name', 'email', 'phone', 'status', 'applied_date', 'hired_date']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'candidate_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Candidate Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'applied_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hired_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        help_texts = {
            'hired_date': 'Set this date when changing status to "Hired"',
        }
