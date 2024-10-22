from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    bank_account = models.CharField(max_length=50)
    tax_id = models.CharField(max_length=20)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('HR', 'HR'), ('Employee', 'Employee')])
    date_joined = models.DateField()

    def __str__(self):
        return self.name

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_salary = self.basic_salary + self.bonuses - self.deductions
        super().save(*args, **kwargs)
