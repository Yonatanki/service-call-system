from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RequestForm
from .models import employee


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
    request_form = RequestForm()
    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)

        if request_form.is_valid():
            print('Valid')
            request_form.save()
            service_request = request_form.save(commit=False)

            messages.info(request, 'Alteon successfully added')
            print(service_request)

            return redirect('request')
        else:
            errors = request_form._errors
            messages.info(request, errors)

    context = {'form': request_form}
    return render(request, "maintenance/request.html", context)


def helpDesk(request):
    page = 'IT'
    context = {'page': page}
    return render(request, 'IT/help_desk_home.html', context)
