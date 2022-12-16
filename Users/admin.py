from django import forms
from django.contrib import admin

# Register your models here.
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import customer

admin.site.register(customer)


# admin.site.register(message)
# @admin.register(customer)

# class ContactForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'phone': PhoneNumberPrefixWidget(),
#         }
#         'phone': PhoneNumberPrefixWidget(initial='US'),


# class ContactAdmin(admin.ModelAdmin):
#     form = ContactForm
