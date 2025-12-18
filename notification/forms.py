from django import forms
from .models import Notification
from employees.models import Employee


class NotificationForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'recipient_select',
            'data-placeholder': 'Select Employee'
        })
    )
    
    class Meta:
        model = Notification
        fields = ['title', 'message', 'recipient', 'is_read']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notification Title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 4}),
            'is_read': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
