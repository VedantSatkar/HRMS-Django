from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'contract_type', 'status', 'start_date', 'end_date']
    search_fields = ['employee_name', 'contract_type']
    list_filter = ['status', 'start_date']
    fields = ['employee_name', 'contract_type', 'start_date', 'end_date', 'status', 'terms']


admin.site.register(Contract, ContractAdmin)
