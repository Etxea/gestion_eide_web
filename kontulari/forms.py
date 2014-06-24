from django import forms 

from models import *

class ContactoForm(forms.ModelForm):
    cliente = forms.IntegerField(label="", widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Contacto
