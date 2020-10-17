from django.db.models.fields import CharField
from .models import Donator, Volunteer
from django.forms.models import ModelForm
from django.db import models
from django import forms
from django.contrib.gis import forms





# class DonatorForm(ModelForm):
#     user = forms.IntegerField(widget=forms.HiddenInput())
#     class Meta:
#         model = Donator
#         fields = '__all__'
    



class DonatorForm(ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput())
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    class Meta:
        model = Donator
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'phone', 'user', 'location')
        widgets = {
        			'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
        			'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
        			'email': forms.TextInput(attrs = {'class': 'form-control'}),
        			'phone': forms.TextInput(attrs = {'class': 'form-control'}),
        }




class VolunteerForm(ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Volunteer
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'phone', 'profession', 'skill_set', 'user')
        # 'subscribe', 'terms_condition', 

        widgets = {
        			'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
        			'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
        			'email': forms.TextInput(attrs = {'class': 'form-control'}),
        			'phone': forms.TextInput(attrs = {'class': 'form-control'}),
        			'profession': forms.TextInput(attrs = {'class': 'form-control'}),
        			'skill_set': forms.TextInput(attrs = {'class': 'form-control'}),
        			# 'subscribe': forms.BooleanField(),
        			# 'terms_condition': forms.BooleanField(),
        }
