from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # Ensure xhtml2pdf is installed
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
            payroll = form.save()
            return generate_payroll_pdf(payroll)
    else:
        form = PayrollForm()
    return render(request, 'payroll_view.html', {'form': form})

def generate_payroll_pdf(payroll):
    template = get_template('payroll_report.html')
    html_content = template.render({'payroll': payroll})

    # Create a response object to send the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Payroll_{payroll.employee.name}.pdf"'

    # Use xhtml2pdf to generate PDF
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    # Check for errors in PDF generation
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)

    return response
