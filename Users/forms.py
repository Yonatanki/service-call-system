from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
# from .models import Profile, Skill, Message
from phonenumber_field.formfields import PhoneNumberField

from .models import customer


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # phone = PhoneNumberField()

    class Meta:
        model = User
        model._meta.get_field('email')._unique = True
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'First Name', 'last_name': 'Last Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # self.fields['phone'].widget.attrs['placeholder'] = 'Contact phone number'
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CustomerCreationForm(ModelForm):
    #  placholder='Contact phone number'
    # phone = PhoneNumberField()
    class Meta:
        model = customer
        fields = ['customer_phone']
        labels = {'customer_phone': 'Phone'}

    def __init__(self, *args, **kwargs):
        super(CustomerCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': 'Contact phone number'})
            # self.fields['conf_select'].widget.attrs['placeholder'] = "sdsdsdsd"
