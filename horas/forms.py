from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm
from models import *

class ParteForm(ModelForm):
    class Meta:
        model = Parte
        widgets = {
            'fecha' : DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False})
        }
