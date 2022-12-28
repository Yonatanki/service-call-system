from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomerCreationForm
from .models import customer

from maintenance.models import call_request


# Create your views here.

def home(request):
    return render(request, 'users/account.html')


def customers(request):
    Customers = customer.objects.all()
    context = {'Customers': Customers}
    return render(request, 'users/customers.html', context)


def userHome(request):
    # print('PK: ', pk)
    # profile = customer.objects.get(id=pk)
    print('REQUEST: ', request)
    # topSkills = profile.skill_set.exclude(description__exact="")
    # otherSkills = profile.skill_set.filter(description="")

    # context = {'profile': profile, 'topSkills': topSkills,
    #            "otherSkills": otherSkills}
    # context = {'profile': profile}
    return render(request, 'users/user-home.html')  # , context)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    # customer_form = CustomerCreationForm()
    if request.method == 'POST':
        # customer_form = CustomerCreationForm(request.POST, request.FILES)

        form = CustomUserCreationForm(request.POST)

        f = request.POST
        print('PHONE: ', form.fields)
        print('PHONE2222: ', request.POST)
        print('PHONE333:\n', f.get('phone'))
        fields = form.fields
        # print('PHONE: ', fields['phone'])
        # customer_form = CustomerCreationForm(request.POST)
        # print('CUSTOMER FORM: ', customer_form)

        if form.is_valid():# and customer_form.is_valid():

            user = form.save(commit=False)  # temporary save to object user but not commit so we can edit the data
            # customer_form.customer_phone = '0545232053'
            # print('CUSTOMER: XXX', customer_form.customer_phone)
            # customer_form.customer_first_name = user.first_name
            # print('CUSTOMER: XXX', customer_form.customer_first_name)
            # customer_form.customer_last_name = user.last_name
            # customer_form.customer_username = user.username.lower
            # phone = customer_form.save(commit=False)
            # customer_form.save()
            user.username = user.username.lower()  # change the username to lower case, to prevent case sensitive

            user.save()  # this save the form
            # customer_form.save()
            a = messages.success(request, 'User account was created!')
            print('MESSAGE: ', a)
            # login(request, user)
            # return redirect('account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}  # , 'customer_form': customer_form}


    return render(request, 'users/login_register.html', context)


def loginUser(request):
    page = 'login'

    # if request.user.is_authenticated:
    #     return redirect('customer')

    if request.method == 'POST':
        print('LOGIN : ', request.POST)
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username,
                            password=password)  # if the username & or password not authenticated return None

        if user is not None:
            print('USER NOT NONE : ', user.id)
            login(request, user)  # create sessions for user in the database get the seesion and add to browser cookies

       
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


@login_required(login_url='login')
def userAccount(request):

    customer = request.user.customer
    print('CUSTOMER: ', customer)
    print('CUSTOMER ID: ', customer.customer_id)
    # skills = profile.skill_set.all()
    print('call req: ', call_request.objects.all())
    # requests = call_request.objects.get(request_customer_id=customer.customer_id)
    context = {'customer': customer}
    # context = {'requests': requests}
    
    # context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)

# @login_required(login_url='login')
# def editAccount(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#
#             return redirect('account')
#
#     context = {'form': form}
#     return render(request, 'users/profile_form.html', context)


# @login_required(login_url='login')
# def inbox(request):
#     profile = request.user.profile
#     messageRequests = profile.messages.all()
#     unreadCount = messageRequests.filter(is_read=False).count()
#     context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
#     return render(request, 'users/inbox.html', context)
# 
# 
# @login_required(login_url='login')
# def viewMessage(request, pk):
#     profile = request.user.profile
#     message = profile.messages.get(id=pk)
#     if message.is_read == False:
#         message.is_read = True
#         message.save()
#     context = {'message': message}
#     return render(request, 'users/message.html', context)


# def createMessage(request, pk):
#     recipient = Profile.objects.get(id=pk)
#     form = MessageForm()
#
#     try:
#         sender = request.user.profile
#     except:
#         sender = None
#
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = sender
#             message.recipient = recipient
#
#             if sender:
#                 message.name = sender.name
#                 message.email = sender.email
#             message.save()
#
#             messages.success(request, 'Your message was successfully sent!')
#             return redirect('user-profile', pk=recipient.id)
#
#     context = {'recipient': recipient, 'form': form}
#     return render(request, 'users/message_form.html', context)
