from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'report_type', 'report_date', 'generated_by']
    search_fields = ['title', 'generated_by']
    list_filter = ['report_type', 'report_date']
    fields = ['title', 'report_type', 'description', 'report_date', 'generated_by']


admin.site.register(Report, ReportAdmin)
