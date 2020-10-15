from django.db.models.fields import CharField
from .models import Donator
from django.forms.models import ModelForm
from django.db import models
from django import forms




# class DonatorForm(ModelForm):
#     user = forms.IntegerField(widget=forms.HiddenInput())
#     class Meta:
#         model = Donator
#         fields = '__all__'
    



class DonatorForm(ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Donator
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'phone', 'addresses')

        widgets = {
        			'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
        			'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
        			'email': forms.TextInput(attrs = {'class': 'form-control'}),
        			'phone': forms.TextInput(attrs = {'class': 'form-control'}),
        			'addresses': forms.Select(attrs = {'class': 'form-control'}),
        }
