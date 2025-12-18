from django.contrib import admin
from .models import Payroll


class PayrollAdmin(admin.ModelAdmin):
    list_display = ['employee', 'salary', 'month', 'year']
    search_fields = ['employee__name']
    list_filter = ['month', 'year']
    fields = ['employee', 'salary', 'bonus', 'deductions', 'month', 'year']


admin.site.register(Payroll, PayrollAdmin)
