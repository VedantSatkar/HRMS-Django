from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from employees.models import Employee
from attendance.models import Attendance
from notification.models import Notification
from datetime import date

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()
    today = date.today()
    present_today = Attendance.objects.filter(date=today, status='Present').count()
    absent_today = max(0, total_employees - present_today)
    #absent_today = max(total_employees - present_today, 0)

    
    # Get recent notifications
    recent_notifications = Notification.objects.all().order_by('-notification_date')[:5]
    unread_notifications = Notification.objects.filter(is_read=False).count()

    return render(request, 'dashboard/dashboard.html', {
        'total_employees': total_employees,
        'present_today': present_today,
        'absent_today': absent_today,
        'recent_notifications': recent_notifications,
        'unread_notifications': unread_notifications,
    })
