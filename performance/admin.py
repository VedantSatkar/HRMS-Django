from django.contrib import admin
from .models import Performance


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'rating', 'review_date', 'created_at']
    search_fields = ['employee__name']
    list_filter = ['rating', 'review_date']
    fields = ['employee', 'rating', 'review', 'review_date']


admin.site.register(Performance, PerformanceAdmin)
