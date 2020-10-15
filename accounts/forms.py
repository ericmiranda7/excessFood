from django.db.models.fields import CharField
from .models import Donator
from django.forms.models import ModelForm
from django.db import models
from django import forms

class DonatorForm(ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Donator
        fields = '__all__'
    