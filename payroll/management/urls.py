from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('generate-payslip/<int:employee_id>/<int:period_id>/', views.generate_payslip, name='generate_payslip'),
    # Add more URL patterns as needed
]
