from django import forms
from .models import Entry
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'date', 'time', 'location', 'address', 'partner', 'comments' ]
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }