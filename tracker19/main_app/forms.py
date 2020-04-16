from django import forms
from .models import Entry, Health 
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'date', 'time', 'location', 'address', 'partner', 'comments']
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