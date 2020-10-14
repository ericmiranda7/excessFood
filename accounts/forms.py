from django.db.models.fields import CharField
from .models import Donator
from django.forms.models import ModelForm
from django.db import models
from django import forms

class DonateForm(ModelForm):
    user = forms.IntegerField()
    
    class Meta:
        model = Donator
        fields = ['user', 'first_name', 'last_name', 'email', 'phone']