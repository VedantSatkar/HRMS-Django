from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Leave
from .forms import LeaveForm


@login_required
def leave_list(request):
    """
    View to display list of leave requests
    """
    leaves = Leave.objects.all()
    context = {'leaves': leaves}
    return render(request, 'leave/leave_list.html', context)


@login_required
def add_leave(request):
    """
    View to add a new leave request
    """
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave:leave_list')
    else:
        form = LeaveForm()
    return render(request, 'leave/add_leave.html', {'form': form})


@login_required
def edit_leave(request, leave_id):
    """
    View to edit a leave request
    """
    leave = get_object_or_404(Leave, id=leave_id)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave:leave_list')
    else:
        form = LeaveForm(instance=leave)
    return render(request, 'leave/edit_leave.html', {'form': form, 'leave': leave})


@login_required
def delete_leave(request, leave_id):
    """
    View to delete a leave request
    """
    leave = get_object_or_404(Leave, id=leave_id)
    leave.delete()
    return redirect('leave:leave_list')
