from django.urls import path
from .views import dashboard, employee_list, add_employee, payroll_view

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', add_employee, name='add_employee'),
    path('payroll/', payroll_view, name='payroll_view'),
]
