from django import forms
from .models import Entry, Partner, Location, Health 
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'date', 'time', 'comments' ]
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }


class HealthForm(ModelForm):
    class Meta:
        model = Health 
        fields = ['date', 'health', 'feeling', 'symptoms', 'comments']
        widgets = {
            'date': DateInput(),
        }

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['name']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address']