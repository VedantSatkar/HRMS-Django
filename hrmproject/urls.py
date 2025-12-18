
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dashboard.urls')),
    path('employees/', include('employees.urls')),
    path('attendance/', include('attendance.urls')),
    path('payroll/', include('payroll.urls')),
    path('leave/', include('leave.urls')),
    path('performance/', include('performance.urls')),
    path('recruitment/', include('recruitment.urls')),
    path('reporting/', include('reporting.urls')),
    path('notification/', include('notification.urls')),
    path('task/', include('task.urls')),
    path('contract/', include('contract.urls')),
]