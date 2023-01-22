from django import forms
from django.forms import ModelForm, DateField, widgets

from .models import call_request, message


# from .utils import DatePickerInput


class RequestForm(ModelForm):
    class Meta:
        model = call_request

        # widgets = {
        #     'Date': widgets.DateInput(attrs={'type': 'date'})
        # }

        # fields = '__all__'

        fields = ['request_customer_id', 'request_category_id', 'request_sub_category_id', 'request_location_id',
                  'request_description', 'request_img', 'request_video']
        labels = {
            'request_customer_id': 'Customer', 'request_category_id': 'Category',
            'request_sub_category_id': 'Sub Category', 'request_location_id': 'Location',
            'request_description': 'Description', 'request_img': 'Image', 'request_video': 'Video'
        }

        # fields = ['MAC', 'Platform', 'Rack', 'RAM']
        # widgets = {
        #     'tags':forms.CheckboxSelectMultiple(),
        # }
        # {'date_time': DatePickerInput()}
        # fields = ['MAC']#, ....]

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        # self.fields['Owner'].widget.attrs.update(placeholder='Email Address')size="1"
        # self.fields['request_customer_id'].widget.attrs['readonly'] = True
        #       loop "for" to styling the form fields in html:
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = message

        fields = {'message_request_id', 'sender', 'body', 'is_read'}

        labels = {'message_request_id': 'Request', 'sender': 'Sender', 'body': 'Message', 'is_read': 'Read'}

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        # self.fields['Owner'].widget.attrs.update(placeholder='Email Address')size="1"
        # self.fields['request_customer_id'].widget.attrs['readonly'] = True
        #       loop "for" to styling the form fields in html:
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})