from django import forms
from .models import Entry
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'date', 'location', 'address', 'partner', 'comments' ]
        widgets = {
            'date': DateInput()
        }