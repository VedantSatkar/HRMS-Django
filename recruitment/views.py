from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Recruitment
from .forms import RecruitmentForm


@login_required
def recruitment_list(request):
    recruitments = Recruitment.objects.all()
    context = {'recruitments': recruitments}
    return render(request, 'recruitment/recruitment_list.html', context)


@login_required
def add_recruitment(request):
    if request.method == 'POST':
        form = RecruitmentForm(request.POST)
        if form.is_valid():
            recruitment = form.save()
            messages.success(request, f'📋 Recruitment for {recruitment.candidate_name} ({recruitment.position}) created!')
            return redirect('recruitment:recruitment_list')
    else:
        form = RecruitmentForm()
    return render(request, 'recruitment/add_recruitment.html', {'form': form})


@login_required
def edit_recruitment(request, recruitment_id):
    recruitment = get_object_or_404(Recruitment, id=recruitment_id)
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, instance=recruitment)
        if form.is_valid():
            # If status changed to hired, set hired_date
            if recruitment.status != 'hired' and form.cleaned_data.get('status') == 'hired':
                form.instance.hired_date = timezone.now().date()
                messages.success(request, f'✓ {recruitment.candidate_name} hired! Employee record auto-created as emp00XXX')
            form.save()
            return redirect('recruitment:recruitment_list')
    else:
        form = RecruitmentForm(instance=recruitment)
    return render(request, 'recruitment/edit_recruitment.html', {'form': form, 'recruitment': recruitment})


@login_required
def delete_recruitment(request, recruitment_id):
    recruitment = get_object_or_404(Recruitment, id=recruitment_id)
    name = recruitment.candidate_name
    recruitment.delete()
    messages.success(request, f'🗑️ Recruitment for {name} deleted!')
    return redirect('recruitment:recruitment_list')
