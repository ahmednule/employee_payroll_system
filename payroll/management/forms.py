from django import forms
from .models import Employee, PayrollPeriod

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'department', 'position', 'employment_type', 
                 'date_joined', 'bank_name', 'bank_account', 'tax_id', 'basic_salary']

class PayrollPeriodForm(forms.ModelForm):
    class Meta:
        model = PayrollPeriod
        fields = ['start_date', 'end_date']