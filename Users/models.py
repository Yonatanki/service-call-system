from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import User
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
import uuid


# Create your models here.

# from django.db.models.signals import post_save, post_delete
# # from django.dispatch import receiver

class customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    customer_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                   primary_key=True, editable=False)
    customer_first_name = models.CharField(max_length=200, blank=True, null=True)
    customer_last_name = models.CharField(max_length=200, blank=True, null=True)
    customer_email = models.EmailField(max_length=500, blank=True, null=False)
    customer_username = models.CharField(max_length=200, unique=True, blank=True, null=True)
    customer_phone = PhoneNumberField(blank=True, null=True)
    # customer_location = models.CharField(max_length=200, blank=True, null=True)
    customer_image = models.ImageField(null=True, blank=True, upload_to='static/images/customers',
                                       default='static/images/customers/user-default.png')
    customer_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return str(self.customer_username), str(self.customer_email),str(self.customer_id)
        return str(self.customer_username)

    class Meta:
        ordering = ['customer_created']

# class message(models.Model):
#     message_id = models.UUIDField(default=uuid.uuid4, unique=True,
#                                   primary_key=True, editable=False)
#     sender = models.ForeignKey(
#         customer, on_delete=models.SET_NULL, null=True, blank=True)
#     recipient = models.ForeignKey(
#         customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
#     name = models.CharField(max_length=200, null=True, blank=True)
#     email = models.EmailField(max_length=200, null=True, blank=True)
#     subject = models.CharField(max_length=200, null=True, blank=True)
#     body = models.TextField()
#     is_read = models.BooleanField(default=False, null=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.subject

#     class Meta:
#         ordering = ['is_read', '-created']

# @receiver(post_save, sender=customer)
# def customerUpdated(sender, instance, created, **kwargs):
#     print('Customer Saved!')
#     print('Instance: ', instance)
#     print('CREATED: ', created)
#     customer = instance
#     user = customer.user
#
#     if created == False:
#         user.first_name = customer.customer_name
#         user.username = customer.customer_username
#         user.email = customer.customer_email
#         user.save()


# def createCustomer(sender, instance, created, **kwargs):
#     print('CREATED: ', created)
#     if created:  # checks if instance (customer) created
#         user = instance
#         print('USER INSTANCE: ', user)
#         print('USER INSTANCE EMAIL: ', user.email)
#         print('USER INSTANCE USERNAME: ', user.username)
#         print('USER INSTANCE FIRST NAME: ', user.first_name)
#         Customer = customer.objects.create(
#             user=user,
#             customer_username=user.username,
#             customer_email=user.email,
#             customer_name=user.first_name,
#         )
#
#         subject = 'Welcome to Service Call System'
#         message = 'We are glad you are here!'
#
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             [Customer.customer_email],
#             fail_silently=False,
#         )


# def deleteCustomer(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()
#     print('Deleting user...')
#     print('Deleting user...')
#
#
# # post_save.connect(customerUpdated, sender=customer)
# post_save.connect(createCustomer, sender=User)
# post_delete.connect(deleteCustomer, sender=customer)
