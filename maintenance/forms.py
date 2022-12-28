from django import forms
from django.forms import ModelForm, DateField, widgets
<<<<<<< HEAD
from .models import call_request

=======
from .models import request
>>>>>>> bde0420 (initial commit)

# from .utils import DatePickerInput


class RequestForm(ModelForm):
    class Meta:

        model = call_request


        # widgets = {
        #     'Date': widgets.DateInput(attrs={'type': 'date'})
        # }

        # fields = '__all__'

        fields = ['request_customer_id', 'request_category_id', 'request_sub_category_id', 'request_location_id',
                  'request_description', 'request_img', 'request_video', 'request_message']
        labels = {
            'request_customer_id': 'Customer', 'request_category_id': 'Category',
            'request_sub_category_id': 'Sub Category', 'request_location_id': 'Location',
            'request_description': 'Description', 'request_img': 'Image', 'request_video': 'Video', 'request_message': 'Message'
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


