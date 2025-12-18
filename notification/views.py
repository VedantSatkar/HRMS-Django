from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notification
from .forms import NotificationForm


@login_required
def notification_list(request):
    notifications = Notification.objects.all().order_by('-notification_date')
    context = {'notifications': notifications}
    return render(request, 'notification/notification_list.html', context)


@login_required
def add_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save()
            messages.success(request, f'✉️ Notification "{notification.title}" sent to {notification.recipient.name if notification.recipient else "System"}!')
            return redirect('notification:notification_list')
    else:
        form = NotificationForm()
    return render(request, 'notification/add_notification.html', {'form': form})


@login_required
def edit_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            messages.success(request, f'📝 Notification "{notification.title}" updated successfully!')
            return redirect('notification:notification_list')
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'notification/edit_notification.html', {'form': form, 'notification': notification})


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    title = notification.title
    notification.delete()
    messages.success(request, f'🗑️ Notification "{title}" deleted successfully!')
    return redirect('notification:notification_list')
