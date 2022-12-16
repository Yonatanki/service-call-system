from django import forms
from django.forms import ModelForm, DateField, widgets
from .models import request

# from .utils import DatePickerInput


class RequestForm(ModelForm):
    class Meta:
        model = request

        # widgets = {
        #     'Date': widgets.DateInput(attrs={'type': 'date'})
        # }
        fields = '__all__'
        # fields = ['MAC', 'Platform', 'Rack', 'RAM']
        # widgets = {
        #     'tags':forms.CheckboxSelectMultiple(),
        # }
        # {'date_time': DatePickerInput()}
        # fields = ['MAC']#, ....]

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        # self.fields['Owner'].widget.attrs.update(placeholder='Email Address')size="1"
        #       loop "for" to styling the form fields in html:
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})