from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from localflavor.es.forms import *
from models import *

class ProfesorCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ( "username", "email","first_name", "last_name" )
        widgets = {
            'telefono': ESPhoneNumberField(),
        }

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(ProfesorCreateForm, self).save(commit=True)
        user_profile = Profesor(user=user)
        user_profile.save()
        return user, user_profile


class ProfesorChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ( "username", "email","first_name", "last_name" )
        widgets = {
            'telefono': ESPhoneNumberField(),
        }

