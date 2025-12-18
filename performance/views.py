from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Performance
from .forms import PerformanceForm


@login_required
def performance_list(request):
    performances = Performance.objects.all()
    context = {'performances': performances}
    return render(request, 'performance/performance_list.html', context)


@login_required
def add_performance(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance:performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'performance/add_performance.html', {'form': form})


@login_required
def edit_performance(request, performance_id):
    performance = get_object_or_404(Performance, id=performance_id)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance:performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'performance/edit_performance.html', {'form': form, 'performance': performance})


@login_required
def delete_performance(request, performance_id):
    performance = get_object_or_404(Performance, id=performance_id)
    performance.delete()
    return redirect('performance:performance_list')
