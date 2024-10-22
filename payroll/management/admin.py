from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Allowance)
admin.site.register(Deduction)
admin.site.register(PayrollPeriod)
admin.site.register(Payslip)