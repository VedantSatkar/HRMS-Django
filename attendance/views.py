from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required
@login_required

def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {
        'records': records
    })


def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()

    return render(request, 'attendance/add_attendance.html', {
        'form': form
    })
