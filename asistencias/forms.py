from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm
from models import *

class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        widgets = {
            'fecha' : DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}),
            'duracion' : DateTimePicker(options={"format": "hh:mm", "pickTime": True,"pickDate":False,"useSeconds":False,"minuteStep":15})
        }
