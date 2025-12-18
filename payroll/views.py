from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payroll
from .forms import PayrollForm


@login_required
def payroll_list(request):
    """
    View to display list of payroll records
    """
    payrolls = Payroll.objects.all()
    context = {'payrolls': payrolls}
    return render(request, 'payroll/payroll_list.html', context)


@login_required
def add_payroll(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'payroll/add_payroll.html', {'form': form})


@login_required
def edit_payroll(request, payroll_id):
    payroll = get_object_or_404(Payroll, id=payroll_id)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll:payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'payroll/edit_payroll.html', {'form': form, 'payroll': payroll})


@login_required
def delete_payroll(request, payroll_id):
    payroll = get_object_or_404(Payroll, id=payroll_id)
    payroll.delete()
    return redirect('payroll:payroll_list')
