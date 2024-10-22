from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import *
from .forms import *

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'payroll/employee_list.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset

@login_required
def generate_payslip(request, employee_id, period_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        period = PayrollPeriod.objects.get(id=period_id)
        
        # Calculate allowances
        allowances = Allowance.objects.all()
        total_allowances = sum(allowance.amount for allowance in allowances)
        
        # Calculate deductions
        deductions = Deduction.objects.all()
        total_deductions = 0
        for deduction in deductions:
            if deduction.percentage:
                total_deductions += (employee.basic_salary * deduction.percentage / 100)
            elif deduction.fixed_amount:
                total_deductions += deduction.fixed_amount
        
        # Calculate net salary
        net_salary = employee.basic_salary + total_allowances - total_deductions
        
        # Create or update payslip
        payslip, created = Payslip.objects.update_or_create(
            employee=employee,
            period=period,
            defaults={
                'basic_salary': employee.basic_salary,
                'total_allowances': total_allowances,
                'total_deductions': total_deductions,
                'net_salary': net_salary
            }
        )
        
        messages.success(request, 'Payslip generated successfully')
        return redirect('payslip_detail', pk=payslip.id)
    except Exception as e:
        messages.error(request, f'Error generating payslip: {str(e)}')
        return redirect('employee_list')
