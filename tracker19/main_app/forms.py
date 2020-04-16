from django import forms
from .models import Entry, Partner
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

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['name']