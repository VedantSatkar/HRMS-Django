from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contract
from .forms import ContractForm


@login_required
def contract_list(request):
    contracts = Contract.objects.all()
    context = {'contracts': contracts}
    return render(request, 'contract/contract_list.html', context)


@login_required
def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract:contract_list')
    else:
        form = ContractForm()
    return render(request, 'contract/add_contract.html', {'form': form})


@login_required
def edit_contract(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract:contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contract/edit_contract.html', {'form': form, 'contract': contract})


@login_required
def delete_contract(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    contract.delete()
    return redirect('contract:contract_list')
