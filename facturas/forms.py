from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm, Select
from django.forms.models import modelformset_factory
from django.forms import widgets
from models import *

from django.forms.models import inlineformset_factory

FacturaFormset = inlineformset_factory(Factura, Concepto)

class FacturaCreateForm(ModelForm):
    class Meta:
        model = Factura
        widgets = {
            'fecha' : DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}),
            'owner' : forms.HiddenInput(),
        }
        exclude = ['pagada','borrador','iva','retencion','descuento','forma_pago','total','subtotal']

class FacturaUpdateForm(ModelForm):
    class Meta:
        model = Factura
        widgets = {
            'fecha' : DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}),
        }
        exclude = ['owner','pagada','borrador']

class ConceptoForm(ModelForm):
    class Meta:
        model = Concepto
        exclude = ['factura']

ConceptoFormset = modelformset_factory(Concepto,form=ConceptoForm)
