from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import customer

from maintenance.models import call_request, status_request


from django.core.mail import send_mail
from django.conf import settings


# @receiver(post_save, sender=Profile)

# @receiver(post_save, sender=customer)


def updateCustomer(sender, instance, created, **kwargs):
    print('Customer Saved!')
    print('Instance: ', instance)
    print('CREATED: ', created)
    customer = instance
    user = customer.user

    if created == False:

        user.first_name = customer.customer_first_name
        user.last_name = customer.customer_last_name
        user.username = customer.customer_username
        user.email = customer.customer_email
        user.phone = customer.customer_phone
        user.save()


def createCustomer(sender, instance, created, **kwargs):
    print('Customer signal triggered')
    print('INSTANCE: ', instance)
    print('CREATED: ', created)
    print('Sender: ', sender)
    if created:  # checks if instance (customer) created
        user = instance
        print('USER INSTANCE: ', user)
        print('USER INSTANCE EMAIL: ', user.email)
        print('USER INSTANCE USERNAME: ', user.username)
        print('USER INSTANCE FIRST NAME: ', user.first_name)
        # print('USER INSTANCE PHONE: ', user.phone)
        Customer = customer.objects.create(
            user=user,
            customer_username=user.username,
            customer_email=user.email,
            customer_first_name=user.first_name,
            customer_last_name=user.last_name,
            # customer_phone=user.phone
        )

        subject = 'Welcome to Service Call System'
        message = 'We are glad you are here!'

        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [Customer.customer_email],
        #     fail_silently=False,
        # )


def deleteCustomer(sender, instance, **kwargs):
    try:
        user = instance.user
        print('Deleting user...')
        user.delete()
    except:
        pass



def createStatusRequest(sender, instance, created, **kwargs):
    print('Customer signal triggered')
    print('INSTANCE: ', instance)
    print('CREATED: ', created)
    print('Sender: ', sender)
    if created:  # checks if instance (customer) created
        req = instance
        print('USER INSTANCE: ', req)
        # print('USER INSTANCE EMAIL: ', user.email)
        # print('USER INSTANCE USERNAME: ', user.username)
        # print('USER INSTANCE FIRST NAME: ', user.first_name)
        # print('USER INSTANCE PHONE: ', user.phone)
        req = status_request.objects.create(

            # request_employee_id= user
            # user=user,
            # customer_username=user.username,
            # customer_email=user.email,
            # customer_first_name=user.first_name,
            # customer_last_name=user.last_name,
            # customer_phone=user.phone
        )

        subject = 'Welcome to Service Call System'
        message = 'We are glad you are here!'

        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [Customer.customer_email],
        #     fail_silently=False,
        # )


post_save.connect(createCustomer, sender=User)
post_save.connect(updateCustomer, sender=customer)
# post_save.connect(createStatusRequest, sender=call_request)
post_delete.connect(deleteCustomer, sender=customer)
