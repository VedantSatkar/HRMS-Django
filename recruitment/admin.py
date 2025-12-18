from django.contrib import admin
from .models import Recruitment


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['candidate_name', 'position', 'status', 'applied_date']
    search_fields = ['candidate_name', 'position']
    list_filter = ['status', 'applied_date']
    fields = ['position', 'candidate_name', 'email', 'phone', 'status', 'applied_date']


admin.site.register(Recruitment, RecruitmentAdmin)
