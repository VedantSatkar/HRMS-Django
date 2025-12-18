from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    tasks = Task.objects.all().order_by('-due_date')
    context = {'tasks': tasks}
    return render(request, 'task/task_list.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form, 'task': task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task:task_list')
