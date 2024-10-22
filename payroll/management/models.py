from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('PERMANENT', 'Permanent'),
        ('CONTRACT', 'Contract'),
        ('CASUAL', 'Casual'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    date_joined = models.DateField()
    bank_name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=30)
    tax_id = models.CharField(max_length=20)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    
    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"

class Allowance(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Deduction(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fixed_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class PayrollPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    is_processed = models.BooleanField(default=False)
    processed_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    period = models.ForeignKey(PayrollPeriod, on_delete=models.PROTECT)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    total_allowances = models.DecimalField(max_digits=10, decimal_places=2)
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    generated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['employee', 'period']
    
    def __str__(self):
        return f"Payslip - {self.employee} - {self.period}"
