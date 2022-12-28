from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from .forms import RequestForm
from .models import employee
from Users.models import customer


# Create your views here.

def home(request):
    # alt_list = ADC.objects.all()

    return render(request, 'main.html')


def maintenances(request):
    emp = employee.objects.get(employee_id='00699cbe-934f-489d-ba97-f10b5fcea5d0')
    privileges = emp.employee_privileges.all()
    context = {'emp': emp, 'privileges': privileges}
    print('Employee: ', emp, 'Privileges: ', privileges)
    print('Employee ID:', emp.employee_department_id)
    print('Employee type:', type(emp))
    return render(request, 'maintenance/maintenance_home.html', context)


def maintenance(request, pk):
    return render(request, 'maintenance_home.html')


def create_request(request):
    print('REQUEST2:  ', request.user.customer.customer_id)
    request_form = RequestForm()
    # print(request_form)
    customer_instance = request.user.customer
    # default_employee = customer.objects.get(customer_username='administrator')
    # print('DEFAULT EMPLOYEE ', default_employee)
    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)
        print('REQ: ', request.POST)
        if request_form.is_valid():
            print('Valid')
            service_request = request_form.save(commit=False)
            default_employee = customer.objects.get(customer_username='administrator')
            print('DEFAULT EMPLOYEE ', default_employee)
            service_request.request_customer_id = request.user.customer
            request_form.save()
            print('#####: ', default_employee)
            choices = employee.objects.all()
            for choice in choices:
                name = str(choice.employee_user_name)
                print('CHOICE: ', choice, 'USERNAME: ', type(name))
                print('#$@$%@$#%:', choice.employee_user_name == 'administrator')
                if name == 'administrator':
                    service_request.request_employee_id.add(choice)
            service_request.save()
            messages.info(request, 'Alteon successfully added')
            # print(service_request)

            return redirect('request')

        else:
            errors = request_form._errors
            messages.info(request, errors)

    context = {'form': request_form, 'customer': customer_instance}

    return render(request, "maintenance/request.html", context)


def helpDesk(request):
    page = 'IT'
    context = {'page': page}
    return render(request, 'IT/help_desk_home.html', context)
