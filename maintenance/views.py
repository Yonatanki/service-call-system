import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from .forms import RequestForm, MessageForm
from .models import employee, call_request, status_request, status
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
    choices = employee.objects.all()
    # for choice in choices:
    #     name = str(choice.employee_user_name)
    #     print('CHOICE1: ', choice, 'USERNAME1: ', type(name), name)
    #     print('#$@$%@$#%1:', choice.employee_user_name == 'administrator', choice.employee_user_name,
    #           type(choice.employee_user_name))

    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)
        print('REQ: ', request.POST)
        if request_form.is_valid():
            print('Valid')
            service_request = request_form.save(commit=False)
            default_employee = customer.objects.get(customer_username='administrator')
            print('DEFAULT EMPLOYEE ', default_employee)
            service_request.request_customer_id = request.user.customer
            status_open = status.objects.get(status_state='open')
            service_request.request_status = status_open
            print('STATUS:  @@@@@: ', status_open)
            # service_request.request_status = handle_uploaded_file(request, new_name_for_file)

            request_form.save()
            print('#####: ', default_employee)
            choices = employee.objects.all()
            for choice in choices:
                name = str(choice.employee_user_name)
                print('CHOICE: ', choice, 'USERNAME: ', type(name), name)
                print('#$@$%@$#%:', choice.employee_user_name == 'administrator', choice.employee_user_name,
                      type(choice.employee_user_name))
                if name == 'administrator':
                    service_request.request_employee_id.add(choice)
            service_request.save()
            messages.info(request, 'Alteon successfully added')
            return redirect('request')

        else:
            errors = request_form._errors
            messages.info(request, errors)

    context = {'form': request_form, 'customer': customer_instance}
    return render(request, "maintenance/request.html", context)


def request_details(request, pk):
    req_details = call_request.objects.get(request_id=pk)
    request_form = RequestForm(instance=req_details)
    today = datetime.date.today()
    message_form = MessageForm()
    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES, instance=req_details)
        print('REQUEST FORM: ', request.POST, '\n', 'REQ@#@#@#: ', request_form)
        message_form = MessageForm(request.POST, request.FILES)
        if message_form.is_valid():
            # req_details.request_message += f'\n[{today}]:\n{request.POST["request_message"]}')

            # f = f'{b}\n[{today}]:\n {request.POST["request_message"]}\n'
            # request_form.request_message = f
            request_form.save()
            service_request = message_form.save(commit=False)
            # print('TODAYE MESSAGE: 2 ', service_request.request_message)
            service_request.message_request_id = req_details
            service_request.sender = request.user.customer  # request.user.customer, this is the user loged in and submit the message

            print('TODAYE MESSAGE: 3 ', service_request.message_request_id)
            service_request.save()
            return redirect('request_details', pk=pk)
        else:
            errors = request_form._errors
            messages.info(request, errors)
    # details = call_request(instance=req_details)
    print('req details: ', req_details.request_employee_id)
    context = {'details': req_details, 'form': message_form}
    return render(request, "maintenance/request_details.html", context)


def helpDesk(request):
    page = 'IT'
    context = {'page': page}
    return render(request, 'IT/help_desk_home.html', context)
