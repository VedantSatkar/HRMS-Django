from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Employee
from .forms import EmployeeForm

# READ - List Employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


# CREATE - Add Employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})


# UPDATE - Edit Employee
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/edit_employee.html', {'form': form})


# DELETE - Delete Employee
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')


# DOWNLOAD - Download Single Employee
@login_required
def download_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="employee_{employee.name}.csv"'
    
    writer = csv.writer(response)
    # Headers - Basic employee information only (no sensitive data)
    writer.writerow(['Employee ID', 'Name', 'Email', 'Department', 'Role', 'Phone', 'Status'])
    writer.writerow([
        employee.employee_id,
        employee.name,
        employee.email,
        employee.department.name if employee.department else 'N/A',
        employee.role.name if employee.role else 'N/A',
        employee.phone if hasattr(employee, 'phone') else 'N/A',
        'Active'
    ])
    
    return response


# DOWNLOAD - Download All Employees
@login_required
def download_all_employees(request):
    employees = Employee.objects.all()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_employees.csv"'
    
    writer = csv.writer(response)
    # Headers - Basic employee information only (no sensitive data)
    writer.writerow(['Employee ID', 'Name', 'Email', 'Department', 'Role', 'Phone', 'Status'])
    
    for employee in employees:
        writer.writerow([
            employee.employee_id,
            employee.name,
            employee.email,
            employee.department.name if employee.department else 'N/A',
            employee.role.name if employee.role else 'N/A',
            employee.phone if hasattr(employee, 'phone') else 'N/A',
            'Active'
        ])
    
    return response
