from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Payroll
from .forms import EmployeeForm, PayrollForm

def dashboard(request):
    total_employees = Employee.objects.count()
    total_payrolls = Payroll.objects.count()
    return render(request, 'dashboard.html', {'total_employees': total_employees, 'total_payrolls': total_payrolls})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def payroll_view(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PayrollForm()
    return render(request, 'payroll_view.html', {'form': form})
