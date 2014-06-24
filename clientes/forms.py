from django import forms
from django.forms import ModelForm
from models import *
from django.forms.models import inlineformset_factory

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

class ClienteContactoForm(forms.ModelForm):
    class Meta:
        model = ClienteContacto
        exclude = ['cliente']
        

#ClienteContactoFormset = inlineformset_factory(Cliente, ClienteContacto)
