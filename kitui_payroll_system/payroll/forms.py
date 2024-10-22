from django import forms
from .models import Employee, Payroll

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'address', 'bank_account', 'tax_id', 'role', 'date_joined']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'month', 'basic_salary', 'bonuses', 'deductions']
