from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from .forms import ReportForm


@login_required
def report_list(request):
    reports = Report.objects.all()
    context = {'reports': reports}
    return render(request, 'reporting/report_list.html', context)


@login_required
def add_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reporting:report_list')
    else:
        form = ReportForm()
    return render(request, 'reporting/add_report.html', {'form': form})


@login_required
def edit_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('reporting:report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'reporting/edit_report.html', {'form': form, 'report': report})


@login_required
def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    report.delete()
    return redirect('reporting:report_list')
